# # #Desafio Guanabara
# def area(a, b):
#     total = a * b
#     return total

# largura = float(input('Digite largura: '))
# comprimento = float(input('Digite comprimento: '))
# print(area(largura, comprimento))

# #Desafio Guanabara
# def escreva(txt):
#     print('-=' * len(txt))
#     print(txt)
#     print('-=' * len(txt))
#     return print

# escreva('Ola mundo!')
# escreva('CeV')
# escreva('Curso em video Python')

#Desafio Guanabara
# def contador(inicio, fim, passo):
#     for c in range(inicio, fim, passo):
#         print(c, end = '')
#     print()
#     for i in range(fim, inicio, -passo):
#         print(i, end ='')
#     print()
#     # for j in range(inicio + 1, fim, passo + 1):
#     #     print(j, end = '')

# contador(1, 10, 1)
# contador(10, 0, 2)


#Passagem por referência
# def item(lista):
#     lista.append(4)

# num = [1, 2, 3]
# item(num)
# print(num)  # Saída: [1, 2, 3, 4]

#Checa sua idade atual no ano de 2024, e verifica se o voto é opcional ou obrigatório ou não vota.
# def votação(a):
#     idade = 2024 - a
#     if idade < 16: 
#         return f'Com {idade}, NÃO VOTA!'
#     elif 16 <= idade < 18 or idade > 65:
#         return f'Com {idade}, VOTO OPCIONAL!'
#     else:
#         return f'Com {idade}, VOTO OBRIGATÓRIO'

# num = int(input('Digite seu ano: '))
# print(votação(num))


# #Calcula fatorial
# def fatorial(n):
#     f = 1
#     for i in range(n, 0, -1):
#         f *= i
#     return f

# print(fatorial(5))


# """Faça um programa que tenha a função ficha(), que receba dois parãmetros opcionais: o nome do jogador,
# e quantos gols ele marcou, o programa deverá ser capaz de mostrar a ficha do jogador. mesmo que algum dado
# não tenha sido informado corretamente"""
# def ficha(jog = '<desconhecido>', gol = 0):
#     print(f'o jogador {jog}, fez {gol} gol(s) no torneio ')

# #Programa Inicial
# n = str(input('Nome do jogador: '))
# g = str(input('Número de gols: '))

# if g.isnumeric():
#     g = int(g)

# else:
#     g = 0
# if n.strip() == '':
#     ficha(gol = g)
# else:
#     ficha(n, g)


#Função que só aceita se for um número
# def leiaInt(msg):
#     ok = False
#     valor = 0
#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print('ERRO! Digite um número válido')
#         if ok:
#             break
#     return valor

# n = leiaInt('Digite um número: ')
# print(f'Você acabou de digitar {n}') 


# #Faça um programa que pode receber várias notas
# def notas(*n, sit = False):
#     r = dict()
#     r['total'] = len(n)
#     r['maior'] = max(n)
#     r['menor'] = min(n)
#     r['media'] = sum(n)/len(n)
#     if sit:
#         if r['media'] >= 7:
#             r['situação'] = 'BOA'
#         elif r['media'] >= 5:
#             r['situação'] = 'RAZOÁVEL'
#         else:
#             r['situação'] = 'RUIM'
#     return r

# resp = notas(5.5, 2.5, 1.5, sit = True)
# print(resp)


# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for c in range(0, 3):
#     for l in range(0, 3):
#         matriz[c][l] = int(input('Digite o valor na posicao [{} {}]'.format(c, l)))

# for linha in matriz:
# #     print(linha)

# #Peça um vetor de 5 elementos, e imprima o maior e o menor dele
# vet = []
# maior = 0
# menor = 0
# for c in range(0, 5):
#     vet.append(int(input('Digite valores: ')))
#     if c == 0:
#         maior = menor = vet[c]
#     else:
#         if vet[c] > maior:
#             maior = vet[c]
#         if vet[c] < menor:
#             menor = vet[c]
# print(vet)
# print(maior)
# print(menor)


# """Um programa onde o usuario pode adicionar varios valores, e se caso ele adicione um que já exista
# o codigo não adicionara"""

# numeros = list()
# while True:
#     n = int(input('Digite numero: '))
#     if n not in numeros:
#         numeros.append(n)
#         print('Valor adicionado')
#     else:
#         print('Valor já existe, não será adicionado')
#     r = str(input('Deseja continuar? S/N \n'))
#     if r in 'Nn':
#         break
# print(numeros)

"""Crie um programa onde o usuario possa digitar 5 valores numericos e cadastre-os em uma lista
no final, deve mostrar a lista ordenada"""

# lista = []
# for c in range(0, 5):
#     lista.append(int(input('Digite 5 valores: ')))
# print(lista)

# troca = True
# fim = len(lista) - 1
# while troca:
#     troca = False
#     for i in range(len(lista) - 1):
#         if lista[i] > lista[i + 1]:                 #caso queira em decrescente, use < nessa linha, subsitui
#             aux = lista[i]
#             lista[i] = lista[i + 1]
#             lista[i + 1] = aux
#             troca = True
#     fim -= 1
# print(lista)


#Faça um programa que separe os numeros inseridos em pares e impares

num = list()
pares = list()
impares = list()

while True:
    num.append(int(input('Digite valor: ')))
    resp = str(input('Quer continuar? S/N \n'))
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

#Faça um programa que fale que a expressão do usuario que ele digitou, está errada
expr = str(input('Digite a expressão: '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:   
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')

