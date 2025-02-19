n = int(input())
for i in range(n):
    for j in range(n - i):
        print("*", end = ' ')
    print("")

for i in range(n):
    m = n
    while m - i > 0:        
        print("*", end = ' ')
        m -= 1
    print("")
# while n > 0:
#     for i in range(n):
#         print("*", end = ' ')
#     print("")
#     n -= 1
# 
# while n > 0:
#     m = n
#     while m > 0:
#         print("*", end = ' ')
#         m -= 1
#     n -= 1
#     print("")
    