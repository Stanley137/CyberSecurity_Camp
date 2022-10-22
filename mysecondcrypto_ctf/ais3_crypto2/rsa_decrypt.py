from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes

p = 800644567978575682363895000391634967
q = 83024947846700869393771322159348359271173
n = p * q
e = 65537
phi = (p-1) * (q-1)
d = inverse(e, phi)

with open('flag.enc', 'rb') as f:
    cipher = f.read()
    cipher = bytes_to_long(cipher) # bytes to decimal
    plain_text = pow(cipher, d, n)
    plain_text = long_to_bytes(plain_text)  # decimal to bytes
    print(plain_text)
    f.close()