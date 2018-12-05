#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 10:13
# @Author  : Heinz
# @Site    : 
# @File    : CodeInterpreter.py
# @Software: PyCharm

"""
逆向第一题：CodeInterpreter
解题思路：翻译虚拟机汇编指令为x86汇编指令，观察对输入做的运算和对输出做的处理
if(dword_6024B0 || (unsigned __int8)first !=0x5E || (second & 0XFF0000) != 0X5E0000 || (unsigned __int8)third != 0x5E){
    puts("try again.");
}else{
    ....
}
dword_6024B0为reg[4]，因此r4必须为0，保证if条件不成立。然后根据翻译结果可以得到三个方程式
最后使用z3库求解。

z3库Mac上安装失败，在window64位可以安装成功
"""

from z3 import *
s = Solver()
first = BitVec('first',32)
second = BitVec('second',32)
third = BitVec('third',32)
s.add(((first >> 4) * 0x15 - third - 0x1d7ecc6b) | ((third >> 8) * 3 + second - 0x6079797c) | ((first >> 8) + second - 0x5fbcbdbd) == 0)
s.add((second & 0xff0000) == 0x5e0000)
s.add((first & 0xff) == 0x5e)
s.add((third & 0xff) == 0x5e)
print(s.check())
mod = s.model()
chars = [
          mod[first],
          mod[second],
          mod[third]
        ]
print chars

"""
[1583308382,1600020063,1583243102]
hex(1583308382)=0x5e5f5e5e
hex(1600020063)=0x5f5e5e5f
hex(1583243102)=0x5e5e5f5e
X-NUCA{5e5f5e5e5f5e5e5f5e5e5f5e}
"""