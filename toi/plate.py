'''toi1_plate'''
nc, ns = [int(x) for x in input().split()]
lines = []
cline = {}
registration = {}
while ns > 0:
    c, s = [int(x) for x in input().split()]
    if s not in registration:
        registration[s] = c
    ns -= 1
cmd = ''
while cmd != 'X':    
    match input().split():
        case ['E', s_id]:
            pass
        case ['D']:
            pass
        case ['X']:
            print(0)
            break
