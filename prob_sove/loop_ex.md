## ตัวอย่าง 1
```python
P = float(input())
i = float(input())
n = int(input())
print(P*(1+i)**n)
```
## ตัวอย่าง 2
```python
P = float(input())
i = float(input())
n = int(input())
while n > 0:
    P = P + (P * i) # P * (1 + i)
    n -= 1
print(f"{P:,.2f}") # f""
```
