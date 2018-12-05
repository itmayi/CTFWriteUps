#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 13:51
# @Author  : Heinz
# @Site    : 
# @File    : HighwayHash.py
# @Software: PyCharm

from highwayhash import *
import binascii


"""
signed __int64 __fastcall HighwayHashReset(__int64 key, _QWORD *state)
{
  signed __int64 result; // rax@1

  state[8] = 0x1BE6D5D5FE4CCE2Fi64;
  state[9] = 0x24093822299F31D0i64;
  state[10] = 0x33198A2E03707344i64;
  state[11] = 0x443F6A8885A308D3i64;
  state[12] = 0x5BD39E10CB0EF593i64;
  state[13] = 0x60ACF169B5F18A8Ci64;
  state[14] = 0x7E5466CF34E90C6Ci64;
  state[15] = 0x852821E638D01377i64;
  *state = 0xCF0C0C1ED5EDF3Ei64;
  state[1] = state[9] ^ 0x3F3E3D3C3B3A1918i64;
  state[2] = state[10] ^ 0x1226252423222121i64;
  state[3] = state[11] ^ 0x2F2E2D2C2B2A2928i64;
  state[4] = state[12] ^ 0x1312111117161514i64;
  state[5] = state[13] ^ 0x3B3A19183F3E3D3Ci64;
  state[6] = state[14] ^ 0x2322212112262524i64;
  result = state[15] ^ 0x2B2A29282F2E2D2Ci64;
  state[7] = result;
  return result;
}
"""
key = b'\x00'*32
len_hash = bytes.fromhex('c4e6d88da28015d3')
print(len_hash)
print(highwayhash_64(key,bytes('19','ascii')))
print(highwayhash_64(key,bytes('0019','ascii')))
#爆破长度
# for i in range(260):
#     data =str(i)
#     data = data.rjust(4,'0')
#     print('data:',data,'length:',len(data))
#     data = bytes(data,'ascii')
#     result = highwayhash_64(key,data)
#     print(result)
#     if result == len_hash:
#         print("i:",i)
#         break
