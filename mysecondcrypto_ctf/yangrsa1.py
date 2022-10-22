﻿from Crypto.Util.number import inverse
n = 83092583783534841000145280642003842283533340442637642451258941907393275732996256523893438356692786223410880194199043046345864683398238392329295750150314289824255749149834103
p = 2262150367
q = 3006300461
r = 12218233223644524650141958853163065112163255395621655741865064529020634406575730714768264558014607893896434523845321502371618344594488810317052606914954669
e = 11
phi = (p-1) * (q-1) * (r-1) # 從phi定義可以知道，n的質因式分解
d = inverse(e, phi)
c = 32392151763267291269610586564983347951891395196084251182633225594245167922176424232164117237142038355860036871811244158149537196288428230971760474130300660929743492107190512

p = pow(c, d, n)
flag = bytes.fromhex(hex(p)[2:])
print(flag)