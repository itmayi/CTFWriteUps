# coding:utf-8
import re

# 替换字符串string中指定位置p的字符为c
def _sub(string,p,c):
    new = []
    for s in string:
        new.append(s)
    if(p < len(string)):
        new[p] = c
    return ''.join(new)
results = ''
with open('ook_1', 'r+') as f:
    for line in f.readlines():

        result = _sub(line,8,'')
        results += result
    print results
    f.write(results)


