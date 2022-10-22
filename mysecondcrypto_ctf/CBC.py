import logging

from pwn import *
context.log_level = 'DEBUG'
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

r = remote('140.110.112.216',  4120)
cipher = b64decode(r.recvline().strip())
print(len(cipher), type(cipher))
iv, block1, block2, padding = cipher[:16], cipher[16:32], cipher[32:48], cipher[48:]
DEC_c1 = xor(block1, b'A'*16)
C2 = xor(DEC_c1, b'CTFGOGOGO\00\00\00\00\00\00\00')
payload = iv + C2 + block2 + padding # remember base64
r.sendline(b64encode(payload))
r.interactive()
