#Faca um programa(sem utilizar "facilidades" do python que pegue um vetor quer e inverta os seus valores SEM CRIAR UM VETOR NOVO)

#Resolucao Professor
v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
 15, 16, 17, 18, 19, 20]
i = 0
f= 19
aux = 1 
while i < f:
    aux = v[i]
    v[i] = v[f]
    v[f] = aux
    i += 1
    f -= 1
print(v)

V = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

V.reverse()
print(V)




"""Uma escola de samba recebeu como pontos pela alegoria os seguintes 5 valores inclusos no vetor Notas. 
Lembrando que a nota mais alta e a nota mais baixa são descartadas. Faça um programa que calcule a média final do quesito."""
Notas = [9.9, 9.7, 9.8, 10, 10]
 
maior = Notas[0]
menor = Notas[0]
soma = 0
for Nota in Notas:
    if Nota > maior:
        maior = Nota
    if Nota < menor:
        menor = Nota
    soma += Nota
media = (soma - maior - menor)/(len(Notas)-2)
print(media)
print("A maior nota é {}".format(maior))
print('A menor nota é {}'.format(menor))


        







