a,b = map(int,input().split())
total =0
if a == 1:
    total+= b * 4.0
if a == 2:
    total+= b * 4.50
if a == 3:
    total+= b * 5.0
if a == 4:
    total+= b * 2.0
if a == 5:
    total+= b * 1.50
print('Total: R$ %.2f'%total)