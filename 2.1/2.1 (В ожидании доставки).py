h = int(input())
m = int(input())
vd = int(input())

ch = h + (vd // 60)
cm = m + (vd % 60)

ok1 = cm // 60 + (ch % 24)
ok2 = cm % 60

if (ok1 > 9 and ok1 != 24) and ok2 > 9:
    print(f'{ok1}:{ok2}')

elif (ok1 > 9 and ok1 != 24) and ok2 <= 9:
    print(f'{ok1}:0{ok2}')

elif ok1 <= 9 and ok2 > 9:
    print(f'0{ok1}:{ok2}')

elif ok1 == 24 and ok2 > 9:
    print(f'00:{ok2}')

elif ok1 == 24 and ok2 <= 9:
    print(f'00:0{ok2}')

else:
    print(f'0{ok1}:0{ok2}')