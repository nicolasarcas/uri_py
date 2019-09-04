a,b,c = map(float,input().split())

if a<c+b and b<c+a and c<a+b:
    p = a+b+c
    print('Perimetro = %.1f'%p)
else:
    ar = ((a+b)*c)/2
    print('Area = %.1f'%ar)