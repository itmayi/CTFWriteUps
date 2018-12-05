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
"""

