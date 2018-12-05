# encoding=UTF8

import string

enc = "PVSF{vVckHejqBOVX9C1c13GFfkHJrjIQeMwf}"

grid = "lovekfc" + "abdghijmnpqrstuwxyz"

flag = ''

print (string.ascii_uppercase)
print (string.ascii_lowercase)

for i in enc:
    if i in string.ascii_lowercase:  # abcdefghijklmnopqrstuvwxyz
        index = grid.lower().index(i)
        flag += string.ascii_lowercase[index]
        continue
    if i in string.ascii_uppercase:  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
        index = grid.upper().index(i)
        flag += string.ascii_uppercase[index]
        continue
    flag += i

print (flag)