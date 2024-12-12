v = [9, 4, 3, 2, 1, 40, 32, 6]

troca = True
fim = len(v) - 1
aux = 0
cont = 0

while troca:
    troca = False
    for i in range(len(v) - 1):
        if v[i] > v[i + 1]:
            aux = v[i]
            v[i] = v[i + 1]
            v[i + 1] = aux
            troca = True
    cont += 1
print(v)
print(cont)
