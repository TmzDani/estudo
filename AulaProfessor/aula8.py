"""
Implemente um programa que exiba um triângulo de Pascal (Tartaglia) de ordem n, sendo n informado pelo usuário. 
Para tal, considere uma matriz quadrada de ordem n, o triângulo de Pascal segue a seguinte regra de formação:

todos os elementos da primeira coluna da matriz são iguais a 1;
todos os elementos da diagonal principal da matriz também são iguais a 1;
para os demais elementos são obtido pela soma do elemento da mesma coluna na linha de cima com o seu vizinho esquerdo;
os elementos acima da diagonal principal não são exibidos.
"""

import math
v1 = []

num = int(input(' Digite numero: '))
for c in range(2, num + 1):
    v1.append(c)

raiz = int(math.sqrt(num))

for i in range(0, raiz):
    if v1[i] != 0:
        for j in range(i + v1[i], len(v1), v1[i]):
            v1[j] = 0
for i in range(len(v1)):
    if v1[i] != 0:
        print(v1[i], end=', ')
        


