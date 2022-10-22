from pwn import *
from hashpumpy import hashpump
from base64 import b64encode,b64decode
context.log_level = 'DEBUG'

def decode_coupon(text):
    text = b64decode(text)
    return text[:32], text[32:]

r = remote('140.110.112.222',4118)
r.recvuntil(b'free coupon for you : ')
coupon = r.recvline().strip(b'\n')
auth, content = decode_coupon(coupon)
add_coupon = b'NjOwRzhBO18X3kU8nKpP'
hash_coupon, send_coupon = hashpump(auth.hex(), content, add_coupon, 20)
coupon = b64encode(bytes.fromhex(hash_coupon) + send_coupon)
r.recvuntil(b'> ')
r.sendline(b'1')
r.recvuntil(b'coupon : ')
r.sendline(coupon)
r.interactive()
# MyFirstCTF{WasRkZjXmkjFbVtjdIDv}