"""
Escreva um programa que através da busca binária faça a consulta numa lista telefônica.
O usuário irá informar o nome da pessoa, a busca será feita no vetor nomes, e irá retornar o número no vetor fones.
"""

nomes = []
fones = []

arquivo = open('ListaTelefonica/nomesordenados.txt')
for linha in arquivo:
    nomes.append(linha.strip())
arquivo.close()

arquivo = open('ListaTelefonica/fones.txt')
for linha in arquivo:
    fones.append(linha.strip())
arquivo.close()

for i in range(0, len(nomes)):
    print(f'{nomes[i]:10} {fones[i]:10}')

# Algoritmo da Pesquisa Binária:
nome = input('Informe o nome a ser localizado: ')

find = False
ini = 0
fim = len(fones) - 1
cont = 0

while ini <= fim and not find:
    meio = (fim + ini) // 2
    cont += 1
    if nomes[meio] == nome:
        find = True
    elif nomes[meio] < nome:
        ini = meio + 1
    else:
        fim = meio - 1
if find:
    print('O numero de {} é {}'.format(nome,fones[meio]))
else:
    print(-1)
print('Foram {} tentativas'.format(cont))
