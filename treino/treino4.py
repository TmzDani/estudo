#Ordene essa lista e dps faca uma busca binaria para revelar a posicao do numero
vetor = [2, 8, 6, 4, 10, 22, 64, 128]

troca = True
fim = len(vetor) - 1
aux = 0

while troca:
    troca = False
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            aux = vetor[i]
            vetor[i] = vetor[i + 1]
            vetor[i + 1] = aux
            troca = True
print(vetor)

num = int(input('Digite valor: '))
encon = False
fim2= len(vetor) - 1
ini = 0
cont = 0

while ini <= fim2 and not encon:
    meio = (ini + fim2) // 2
    cont += 1
    if vetor[meio] == num:
        encon = True
    elif vetor[meio] < num:
        ini = meio + 1
    else:
        ini = meio - 1
if encon:
    print('Está na posicao {}'.format(meio))
else:
    print(-1)
print('Foram {} tentativas'.format(cont))

          

