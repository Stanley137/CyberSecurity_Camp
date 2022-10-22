from Crypto.Util.number import inverse, long_to_bytes, bytes_to_long
from Crypto.PublicKey import RSA # pycrypto an useful package

rsa = RSA.importKey(open('pub.pem').read())
N = rsa.n
e = rsa.e
p = 270613060120468613971049355250995010949
q = 317961772531370599800029965079161987889
phi = (p-1) * (q-1)
d = inverse(e, phi)
cipher = bytes_to_long(open('flag.enc', 'rb').read())
flag = pow(cipher, d, N)
print(long_to_bytes(flag))
print(N, e)
# BreakALLCTF{b@$RSA}