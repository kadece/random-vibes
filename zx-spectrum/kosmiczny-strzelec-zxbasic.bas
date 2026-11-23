10 REM KOSMICZNY STRZELEC - ZX BASIC (ZXBC)
20 BORDER 0: PAPER 0: INK 7: CLS
30 DIM w AS Integer
35 DIM z AS Integer
40 DIM px AS Integer
45 DIM ax(6) AS Integer
50 DIM ay(6) AS Integer
55 DIM bx(4) AS Integer
60 DIM by(4) AS Integer
65 DIM bb(4) AS Integer
70 DIM i AS UByte
75 DIM j AS UByte
80 DIM k$ AS String
90 LET w = 0: LET z = 3: LET px = 15
100 FOR i = 1 TO 6: GOSUB 500: NEXT i
110 FOR i = 1 TO 4: LET bb(i) = 0: NEXT i
120 REM PETLA GLOWNA
130 IF z = 0 THEN GOTO 900
140 PRINT AT 0,0;"WYNIK:";w;"     ZYCIA:";z;"     "
150 PRINT AT 21,px;"^"
160 LET k$ = INKEY$
170 IF k$ = "5" AND px > 0 THEN PRINT AT 21,px;" ": LET px = px - 1
180 IF k$ = "8" AND px < 31 THEN PRINT AT 21,px;" ": LET px = px + 1
190 IF k$ = " " THEN GOSUB 600
200 FOR i = 1 TO 4
210 IF bb(i) = 1 THEN PRINT AT by(i),bx(i);" ": LET by(i) = by(i) - 1: IF by(i) < 1 THEN LET bb(i) = 0 ELSE PRINT AT by(i),bx(i);"|"
220 NEXT i
230 FOR i = 1 TO 6
240 IF ay(i) >= 1 THEN PRINT AT ay(i),ax(i);" "
250 LET ay(i) = ay(i) + 1
260 IF ay(i) > 21 THEN GOSUB 500
270 IF ay(i) >= 1 AND ay(i) <= 21 THEN PRINT AT ay(i),ax(i);"O"
280 FOR j = 1 TO 4
290 IF bb(j) = 1 AND bx(j) = ax(i) AND by(j) >= ay(i) - 1 AND by(j) <= ay(i) + 1 THEN LET bb(j) = 0: PRINT AT by(j),bx(j);" ": PRINT AT ay(i),ax(i);" ": GOSUB 500: LET w = w + 10: BEEP 0.2,10
300 NEXT j
310 NEXT i
320 FOR i = 1 TO 6
330 IF ay(i) = 21 AND ax(i) = px THEN LET z = z - 1: PRINT AT 21,px;"*": BEEP 0.5,0: PAUSE 30: GOSUB 500
340 NEXT i
350 PAUSE 2
360 GOTO 130
500 REM NOWY ASTEROIDA
510 LET ax(i) = INT(RND * 32): LET ay(i) = -INT(RND * 8)
520 RETURN
600 REM STRZAL
610 FOR i = 1 TO 4
620 IF bb(i) = 0 THEN LET bb(i) = 1: LET bx(i) = px: LET by(i) = 20: RETURN
630 NEXT i
640 RETURN
900 REM KONIEC GRY
910 CLS
920 PRINT AT 10,6;"KONIEC GRY!"
930 PRINT AT 13,8;"WYNIK:";w
940 PRINT AT 16,3;"NACISNIJ DOWOLNY KLAWISZ"
950 IF INKEY$ = "" THEN GOTO 950
960 CLS
970 GOTO 90
