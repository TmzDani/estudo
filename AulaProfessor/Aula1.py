#Aula do professor sobre matrizes

# matriz = [[0, 0, 0, 0], [0, 0, 0, 0]]

# for l in range(len(matriz)):
#     for c in range(len(matriz[l])):
#         matriz[l][c] = int(input('Digite numero: '))
# print(matriz)

# M = []

# for i in range(2):
#     M.append([])
#     for j in range(4):
#         M[i].append([])
#         for z in range(3):
#             M[i][j].append(int(input('Digite valor: ')))
# print(M)


#Exercicios do professor

matriz = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

#Exercicio do professor
soma = 0
produto = 1
total = 0
diagonal = 1
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        total += matriz[i][j]
        if j == 0:
            soma += matriz[i][j]
        if i == 0:
            produto *= matriz[i][j]
        if i == j:
            diagonal *= matriz[i][j]

print(f"Soma da primeira coluna: {soma}")
print(f"Produto da primeira linha: {produto}")
print(f"Soma de todos os elementos: {total}")
print(f"Produto diagonal principal: {diagonal}")

#Exercicio do Professor 2
M1 = [[-10, 1, 4, 6],
      [2, 3, 2, 8]]

M2 = [[1, 8, 4, -1],
      [0, 6, 3, -3]]

M3 = []

for i in range(len(M1)):
    M3.append([])
    for c in range(len(M1[i])):
        M3[i].append(M1[i][c] + M2[i][c])
print(M1)
print(M2)
print(M3)
    

