vin = 0
vout = 0;
x = int(input())
for y in range(x):
    z = int(input())
    if z >= 10 and z <=20:
        vin += 1
    else:
        vout += 1
print(vin,'in')
print(vout,'out')