list1 = [0xED,0x9A,0xEE,0x55,0xC5,0xC0,0xC,0x5E,0xD8,0xE0,0x1E,0xB2,0xED,0x49,0x4F,0x2B,0xD3,0x74,0xD9,0xD5,0xDA,0x6,0x38,0xB8,0x1D,0x0D,0x5D,0x64,0xDF,0x17,0x2A,0xEA]
list2 = [0x8,0x9A,0xB0,0x32,0x46,0xDC,0xB2,0x12,0xF,0x2B,0xFD,0xEB,0x70,0xD5,0xCA,0xA,0xE8,0xF9,0x87,0xE5,0x24,0x6,0x8B,0xB,0x62,0x54,0xD7,0xAF,0x2E,0xF1,0xEF,0x74]

print len(list1)
print len(list2)

res = []
for i in range(len(list1)):
    res.append(chr(list1[i] ^ list2[i]))

print "".join(res)