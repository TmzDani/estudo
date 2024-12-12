#Desafio guanabara

maior = 0
menor = 0

for i in range(0,3):
    num = int(input('Digite valor: '))
    maior = num
    menor = num
    if num > maior:
        maior = num
    if num > menor:
        menor = num
print(maior)
print(menor)
