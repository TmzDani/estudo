#Faca um programa que leia o comprimento do cateto oposto e adjacente e calcule a hipotenusa:

import math
ops=int(input('Digite oposto: '))
adj=int(input('Digite adjacente: '))
hipo=math.sqrt(ops**2 + adj**2)
print(hipo)
