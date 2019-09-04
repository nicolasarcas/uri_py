lista = []
cont = 0
s=0
for i in range(6):
    a = float(input())
    lista.append(a)
for i in lista:
    if i > 0:
        cont += 1
        s+=i 
print(cont,'valores positivos')
print('{:.1f}'.format(s/cont))