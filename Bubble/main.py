"""
Usando do algoritmo da bolha, ordene a lista de nomes do vetor nomes.
"""
V = []

arquivo = open('Bubble/nomes.txt')
for linha in arquivo:
    V.append(linha.strip())
arquivo.close()
print(V)

# Bubble Sort

troca = True
fim = len(V) - 1
while troca:
    troca = False
    for i in range(len(V) - 1):
        if V[i] > V[i + 1]:
            aux = V[i]
            V[i] = V[i + 1]
            V[i + 1] = aux
            troca = True
    fim -= 1
print(V)
            
