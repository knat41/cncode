w = input()
n = len(w)
p = True
for i in range(n//2):
    if w[i] != w[n - 1]:
        p = False
        break
    n -= 1
if p:
    print("TRUE")
else:
    print("FALSE")
    