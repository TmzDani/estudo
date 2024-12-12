#Ideia da aula, Bubble Sort


#Exercicio professor
V = [6,5,3,1,8,7,2,4]
aux = 0
troca = False
tam = len(V) - 1
while not troca:
    troca = True
    for c in range(tam):
        if V[c] > V[c + 1]:
            aux = V[c]
            V[c] = V[c + 1]
            V[c + 1] = aux
            c += 1
            troca = False
print(V)

#Resolucao do professor
V = [6, 5, 3, 1, 8, 7, 2, 4]
Troca = True
Final = len(V) - 1
while Troca:
    Troca = False
    for i in range(0,Final):
        if V[i] > V[i + 1]:
            aux = V[i]
            V[i] = V[i + 1]
            V[i + 1] = aux
            Troca = True
    Final -= 1
print(V)
print(Final)
