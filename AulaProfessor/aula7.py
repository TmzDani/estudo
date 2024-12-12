#Crivo de erastones
#Faca um programa que peca para o usuario ir até algum numero, usando o metodo erastones

import math
v1 = []

num = int(input('Digite numero: '))
for c in range(2, num + 1):
    v1.append(c)

raiz = int(math.sqrt(num))
for i in range(0, raiz):
    if v1[i] != 0:
        for j in range(i+v1[i], len(v1), v1[i]):
            v1[j] = 0
for i in range(len(v1)):
    if v1[i] != 0:
        print(v1[i],end=', ')


#Resolucao do professor

num = int(input('Primos até qual numero: '))
primos = []
for _ in range(num + 1):
    primos.append(True)
primos[0] = False
primos[1] = False 

max = int(num**0.5)
print(max)

for i in range(2, max + 1):  # Começar em 2 e ir até max + 1
    if primos[i]:
        for j in range(i * 2, num + 1, i):  # Começar em i * 2
            primos[j] = False

for i in range(num + 1):
    if primos[i]:
        print(i, end=', ')
