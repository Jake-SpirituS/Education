# put your python code here
alph_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s_forcode = input()
s_decode = ''
n = 0
s_temp = ''
for i in range(len(s_forcode)):
    if s_forcode[i].upper() in alph_eng:
        n += 1
        s_temp += s_forcode[i]
        continue
    if s_forcode[i].upper() not in alph_eng:
        for j in range(n):
            if s_temp[j].upper() == s_temp[j]:
                z = alph_eng.find(s_temp[j])
                s_decode += alph_eng[(z+n) % 26]
            elif s_temp[j].upper() != s_temp[j]:
                z = alph_eng.find(s_temp[j].upper())
                s_decode += alph_eng[(z+n) % 26].lower()
        s_decode += s_forcode[i]
        n = 0
        s_temp = ''

if s_temp != '':
    for j in range(n):
        if s_temp[j].upper() == s_temp[j]:
            z = alph_eng.find(s_temp[j])
            s_decode += alph_eng[(z + n) % 26]
        elif s_temp[j].upper() != s_temp[j]:
            z = alph_eng.find(s_temp[j].upper())
            s_decode += alph_eng[(z + n) % 26].lower()

print(s_decode)
