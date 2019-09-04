import math

a,b,c = map(float,input().split())
delta = b**2 - 4*a*c

if delta < 0 or a == 0:
    print('Impossivel calcular')
    exit()
delta = math.sqrt(delta)

x1 = (-b+ delta)/(2*a)
x2 = (-b- delta)/(2*a)
    
print('R1 = %.5f'%x1)
print('R2 = %.5f'%x2)