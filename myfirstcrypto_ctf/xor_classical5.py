# compare the header
gif_header = b'\x47\x49\x46\x38\x39\x61'
flag_header = b'\x00\x78\x20\x7f\x08\x07'
# g ^ k = f, k = f ^ g
key = b''.join([bytes([g^f]) for g,f in zip(gif_header, flag_header)])
print(key)
key *= 38000
with open('flag.gif.enc', 'rb') as fp_read:
    with open('flag.gif', 'wb') as fp_write:
        cipher = fp_read.read()
        output = b''.join([bytes([c^f]) for c,f in zip(cipher, key)])
        fp_write.write(output)
        fp_write.close()
    fp_read.close()