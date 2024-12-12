# v = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#Onde está o 17?
#pesquisa de nylon
#A pesquisa binaria tem que estar ordenado.

V = []
for i in range(1, 3000000, 2):
    V.append(i)
#print(V)

n = int(input('Buscar qual valor? '))
achou = False
ini = 0
fim = len(V) - 1
cont = 0
while ini <= fim and not achou:
    meio = (fim + ini) // 2
    cont += 1
    if V[meio] == n:
        achou = True
    elif V[meio] < n:
        ini = meio + 1
    else:
        fim = meio - 1
if achou:
    print(meio)
else:
    print(-1)
print('Foram:',cont,'Tentativas')

#Faca um programa que crie um vetor com 300 valores pares e atraves da busca binaria, procure um valor nela

V = []
for c in range(0,600, 2):
    V.append(c)
    print(c, end=', ')

s = int(input('Digite valor: '))
encon = False
ini = 0
fim = len(V) - 1
cont = 0
while ini <= fim and not encon:
    meio = (fim + ini) // 2
    cont += 1
    if V[meio] == s:
        encon = True
    elif V[meio] < s:
        ini = meio + 1
    else:
        fim = meio - 1
if encon:
    print('Esta na posicao {}'.format(meio))
else:
    print(-1)
print('Foram {} tentativas'.format(cont))


