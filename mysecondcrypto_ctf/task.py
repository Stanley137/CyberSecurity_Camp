from hashlib import sha384
FLAG = ''
hash = lambda c: sha384(c).hexdigest()[:5]
#print(''.join([hash(c.encode()) for c in FLAG ]))

c = "8a5e675d378d18254a5981deaad14a1ad0e1ad0e95ed472df8bcf6e5335f72df8586b017580a87d840f985f9158ac1075823758237582375823000f40b759a4eb0bcf6ec2b14000f41d0ec17580a87d8f99c575d37883c5049e7e7cdc1d0ec000f41f366"
cipher = [c[i:i+5] for i in range(0, len(c), 5)]
# create table
table = dict()
for b in range(256):
    h = hash(bytes([b]))
    table[h] = bytes([b])
flag = b"".join([table[h] for h in cipher])
print(flag)
# BreakAll{H4sH_Enc0d....?Wh47?!En6rypt!?}