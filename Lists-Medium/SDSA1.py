s = "4193 with words"  

Operators = ['-']


p = []

for i in range(len(s)):
    if s[i].isdigit() or s[i] in Operators:
        p.append(s[i])


print(''.join(p))


