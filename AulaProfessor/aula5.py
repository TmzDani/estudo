# Faça um programa que:

# Leia um vetor A com N elementos já ordenados e um vetor B com M elementos também já ordenados.
# Intercale os dois vetores A e B, formando um vetor C, sendo que ao final do processo de intercalação, 
# o vetor C continue ordenado. Nenhum outro processo de ordenação poderá ser utilizado além da intercalação dos vetores A e B.
# Caso um vetor (A ou B) termine antes do outro, o vetor C deverá ser preenchido com os elementos 
# do vetor que ainda possui informações.

A = [1, 2, 3, 4, 5]
B = [2, 4, 6, 10, 12, 14, 16, 18]
C = []

while A and B:  # Enquanto ambas as listas não estiverem vazias
    if A[0] <= B[0]:
        C.append(A.pop(0))  # Remove o primeiro elemento de A e adiciona a C
    else:
        C.append(B.pop(0))  # Remove o primeiro elemento de B e adiciona a C

# Se sobrar elementos em A ou B, adicione-os a C
C.extend(A)  # Adiciona os elementos restantes de A
C.extend(B)  # Adiciona os elementos restantes de B

print(C)

            


