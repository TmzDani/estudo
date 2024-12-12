#Pegue o valor max e min de um vetor

vet = [1, 6, 7, 9, 4, 3]

# Inicializando maior e menor com o primeiro elemento do vetor
maior = vet[0]
menor = vet[0]

for c in vet:
    if c > maior:
        maior = c
    if c < menor:
        menor = c

print("Maior:", maior)
print("Menor:", menor)
