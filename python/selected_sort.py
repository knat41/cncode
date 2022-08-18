l = [13, 86, 44, 50, 9, 54, 90, 42, 61, 58]

s = [] # รายการคำตอบ (Answer List)
n = len(l)
i = 0
r = 1
while i < n:
    print(f'round {r}')
    print(f'S {s}')
    print(f'L {l}')
    m = min(l)
    l.remove(m)
    s.append(m)
    i += 1
    r += 1
print(f'round {r}')
print(f'S {s}')
print(f'L {l}')
