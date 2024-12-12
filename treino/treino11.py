#revele a posicao de um numero

vet = []

for c in range(0,600,2):
    vet.append(c)
print(vet)

ini = 0
fim = len(vet) - 1
cont = 0
achou = False

num = int(input('Digite valor: '))
while ini <= fim and not achou:
    meio = (ini + fim) // 2
    cont += 1
    if vet[meio] == num:
        achou = True
    elif vet[meio] < num:
        ini = meio + 1
    else:
        fim = meio - 1
if achou:
    print('Esta na posicao {}'.format(meio))
else:
    print(-1)
print('foram {} vezes rodadas'.format(cont))

