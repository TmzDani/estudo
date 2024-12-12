#Exemplo de def sendo usado
# def soma(a, b):
#     return a + b

# print(soma(1,2))

#Crie uma função que necessite de três argumentos, e que forneça a soma desses três argumentos

# def soma(a, b):
#     return a + b
# print(soma(1,2))

# def soma2(a, b, c):
#     return a + b + c
# print(soma(1, 2, 3))

# def soma3(a, b, c, d):
#     return a + b + c + d
# print(soma3(1, 2, 3, 4))

#Outra forma
# def soma(*n):     #varargs
#     total = 0
#     for aux in n :
#         total += aux
#     return total

# print(1)
# print(soma(1, 2))
# print(soma(1, 2, 3))
# print(soma(1, 2, 3, 4))


"""
FAÇA UM PROGRAMA COM DUAS FUNÇÕES, UMA RECEBE UMA TEMPERATURA EM FAHRENHEIT E RETORNA
EM CELCIUS E OUTRA QUE FAZ O INVERSO. LEMBRANDO QUE AS FORUMLAS SÃO C = (F - 32) x 5/9
E F = (C x 9/5) + 32.
"""

# def fahrenheit(c):
#     return (c * 9 / 5) + 32

# def celcius(f):
#     return (f - 32) * 5 / 9

# print(fahrenheit(54))
# print(celcius(28))
# print(celcius(fahrenheit(50)))

#2 variaveis
def mudai(i):
    i = i * 2   # 'i' aqui é uma variável local. A mudança só afeta a cópia local de 'i'

i = 3           # 'i' é uma variável global
mudai(i)        # Chamando a função 'mudai' com o valor de 'i' como argumento
print(i)        # Imprime o valor de 'i' global


vet = [1, 2, 3]
def alterar(a, b, c):
    vet = [4, 5, 6]
    return vet

print(vet)



    


























