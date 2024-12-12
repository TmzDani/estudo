vet = ['Ronaldinho', 'Osvaldo', 'Germanio', 'Ariadna']

troca = True
fim = len(vet) - 1
aux = 0

while troca:
    troca = False
    for i in range(len(vet) - 1):
        if vet[i] > vet[i + 1]:
            aux = vet[i]
            vet[i] = vet[i + 1]
            vet[i + 1] = aux
            troca = True
print(vet)