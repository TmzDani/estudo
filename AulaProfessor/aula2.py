# Faca um programa que some o conteudo de dois vetores e armazene o resultado de dois vetores e armazene o resultado
#  em um terceiro vetores

#resolucao do professor
V1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
V2 = [2, 4, 6, 8, 10, 12, 14, 16]
V3 = []
i = 0
while i < len(V1) or i < len(V2):
    if i <len(V1) and i < len(V2):
        V3.append(V1[i] + V2[i])
    elif i < len(V1):
        V3.append(V1[i])
    else:
        V3.append(V2[i])
    i += 1
print(V3)

# O que sao vetores(ou arrays)?
# é uma estrutura de dados que armazena uma colecao de elementos


# #Faca a uniao de A e b, intercessao e diferenca
# A = [2, 4, 7, 13, 14, 15, 16]
# B = [1, 6, 7, 11, 13, 16, 18]
# U = []
# I = []
# D = []
# for e in A:
#     U.append(e)
# for e in B:
#     if e not in U:
#         U.append(e)                 #Uni os valores de A e B
# print(U)

# for e in A:
#     if e in B:
#         I.append(e)                 #Só adiciona os valores que tem em A e B
# print(I)

# for e in A:
#     if e not in B:
#         D.append(e)                 #Só adiciona os valores que tem em A mas nao tem em B=
# print(D)


# Definindo os vetores
V1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
V2 = [2, 4, 6, 8, 10, 12, 14, 16]
V3 = []

# Encontrando o tamanho do vetor menor
tamanho_minimo = min(len(V1), len(V2))

# Somando os elementos dos vetores
for i in range(tamanho_minimo):
    V3.append(V1[i] + V2[i])

# Exibindo os resultados
print("Vetor 1:", V1)
print("Vetor 2:", V2)
print("Resultado (Vetor 3):", V3)






