10 N = 2
11 M = 7
20 T = N
21 C = 0
22 S = 0
30 IF T <= M THEN GOTO 40 ELSE GOTO 80 END IF
40 IF (T MOD 2) = 1 THEN GOTO 50 ELSE GOTO 60 END IF
50 S = S + T
51 C = C + 1
60 T = T + 1
70 GOTO 30
80 PRINT C
90 PRINT S
100 END
