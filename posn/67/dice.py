'''Dice 1006'''
n = int(input())
rolls = [input() for _ in range(n)]
for i in range(n):
    first = True
    for j in range(len(rolls[i])):
        if first:
            ds = {'TOP':1, 'FRONT':2, 'LEFT':3, 'RIGHT':4, 'REAR':5, 'BOTTOM':6}
            first = False
        roll = rolls[i][j]
        match roll:
            case 'F':
                ds['TOP'], ds['FRONT'], ds['REAR'], ds['BOTTOM'] = ds['REAR'], ds['TOP'], ds['BOTTOM'], ds['FRONT']
            case 'B':
                ds['TOP'], ds['FRONT'], ds['REAR'], ds['BOTTOM'] = ds['FRONT'], ds['BOTTOM'],  ds['TOP'], ds['REAR']
            case 'L':
                ds['TOP'], ds['LEFT'], ds['RIGHT'], ds['BOTTOM']= ds['RIGHT'], ds['TOP'], ds['BOTTOM'], ds['LEFT']
            case 'R':
                ds['TOP'], ds['LEFT'], ds['RIGHT'], ds['BOTTOM']= ds['LEFT'], ds['BOTTOM'], ds['TOP'], ds['RIGHT']
            case 'C':
                ds['FRONT'], ds['LEFT'], ds['RIGHT'], ds['REAR'] = ds['RIGHT'], ds['FRONT'], ds['REAR'], ds['LEFT']
            case 'D':
                ds['FRONT'], ds['LEFT'], ds['RIGHT'], ds['REAR'] = ds['LEFT'], ds['REAR'], ds['FRONT'], ds['RIGHT']
    print(ds['FRONT'], end = " ")
