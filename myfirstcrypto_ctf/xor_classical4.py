def decrypt(cipher, key):
    output = b''
    for i,c in enumerate(cipher):
        output += bytes([c ^ key[i % len(key)]])
    return output

with open('flag.enc', 'rb') as f:
    # my
    cipher = f.read()
    key = b'S3cRe7-K3y' * 4
    print(decrypt(cipher, b'S3cRe7-K3y'))
    f.close()
    # teacher
    output = ''.join([chr(c^k) for c,k in zip(cipher,key)]) # list expression
    print(output)
