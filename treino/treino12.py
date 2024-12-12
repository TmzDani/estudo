from random import randint
vet = []
for c in range(600):
    vet.append(randint(1,1000))
print(vet)    
vet2 = []

troca = True
max = 95
min = 2

while troca:
    troca = False
    for c in range(len(vet) - 1):
        if vet[c] > vet[c + 1]:
            aux = vet[c]
            vet[c] = vet[c + 1]
            vet[c + 1] = aux
            troca = True
for i in range(len(vet)):
    if i == 0:
        if vet[i] > min and vet[i] < max and vet[i]:
            vet2.append(vet[i])
    else:
        if vet[i] > min and vet[i] < max and vet[i] != vet[i - 1]:
            vet2.append(vet[i])
print(vet2)
