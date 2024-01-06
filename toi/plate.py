'''toi1_plate'''
nc, ns = [int(x) for x in input().split()]
lines = []
dline = {}
cline = []
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
            s_id = int(s_id)
            if len(lines) != 0:
                pass
            else:
                lines.append(s_id)
                if registration[s_id] not in dline:
                    dline[registration[s_id]] = 1
                else:
                    dline[registration[s_id]] += 1
        case ['D']:
            if len(lines) == 0:
                print("empty")
        case ['X']:
            print(0)
            break
