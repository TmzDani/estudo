V = []
for c in range(0,600,2):
    V.append(c)
    print(V, end=', ')

ini = 0
fim = len(V) - 1
cont = 0
busca = False

n = int(input('Digite valor: '))
while ini <= fim and not busca:
    meio = (ini + fim) // 2
    cont += 1
    if V[meio] == n:
        busca = True
    elif V[meio] < n:
        ini = meio + 1
    else:
        fim = meio - 1
if busca:
    print('Esta na posicao {}'.format(meio))
else:
    print(-1)
print('Foram {} tentativas'.format(cont))





        

