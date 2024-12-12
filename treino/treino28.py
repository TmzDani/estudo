matriz = [[1, 2, 3], [4, 5, 6]]
soma = 0

def contar(matriz):
    for i in range(len(matriz)):
        for e in range(len(matriz[i])):
            soma += 1
    return soma
print(contar(matriz))
