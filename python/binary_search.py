'''PROGRAM : Binary Search
   WRITER  : NAT KANJANASIRI
   DATE    : AUG 3, 2022
   PURPOSE : Teaching Computational Scicence M.4 '''
A = [8, 9, 13, 35, 42, 44, 50, 54, 58, 60, 61, 62, 77, 84, 86, 90, 92, 96]
n = len(A)
found = False
target = 62
left = 0
right = n - 1
nc = 1
tail = ''
print('target =', target)
while left <= right:
    mid = (left + right) // 2
    x = A[mid]
    print('ROUND', nc, 'LEFT =', left + 1, 'RIGHT =', right + 1, 'MID =', mid +1, '',end='')
    if x == target:
        found = True
        print(f'{x} equal to {target}')
        break
    if x < target:
        left = mid + 1
        print(f'{x} less than {target}')
    if x > target:
        right = mid - 1
        print(f'{x} greater than {target}')
    nc += 1
if found:
    print(f'found {x} at {mid + 1}')
else:
    print('not found')

