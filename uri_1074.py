a = int(input())

for x in range(a):
    b=int(input())
    if b > 0 and b % 2 == 0:
        print('EVEN POSITIVE')
    elif b > 0 and b % 2 != 0:
        print('ODD POSITIVE')
    elif b < 0 and b % 2 == 0:
        print('EVEN NEGATIVE')
    elif b < 0 and b % 2 != 0:
        print('ODD NEGATIVE')
    else:
        print('NULL')