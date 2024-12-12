Vet = [6, 5, 2, 9, 20, 56, 79, 234, 2345, 655, -1]

troca = True
fim = len(Vet) - 1
aux = 0
cont = 0

while troca:
    troca = False
    for i in range(len(Vet) - 1):
        if Vet[i] > Vet[i + 1]:
            aux = Vet[i]
            Vet[i] = Vet[i + 1]
            Vet[i + 1] = aux
            troca = True
    fim -= 1

print(Vet)

num = int(input('Digite numero: '))
encon = False
fim2 = len(Vet) - 1
ini = 0

while ini <= fim2 and not encon:
    meio = (fim2 + ini) // 2
    if Vet[meio] == num:
        encon = True
    elif Vet[meio] < num:
        ini = meio + 1
    else:
        fim = meio - 1
if encon:
    print('Está na posicao {}'.format(meio))
else:
    print(-1)


            
