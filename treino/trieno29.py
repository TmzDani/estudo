#faça apenas

num = list()
pares = list()
impares = list()

while True:
    num.append(int(input('Digite valor: ')))
    resp = str(input('Continua: S/N \n'))
    if resp in 'Nn':
        break

for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(num)
print(pares)
print(impares)


troca = True
fim = (len(num))

while troca:
    troca = False
    for c in range(len(num) - 1):
        if num[c] > num[c + 1]:
            aux = num[c]
            num[c] = num[c + 1]
            num[c + 1] = aux
            troca = True
    fim -= 1

print(num)
