#Numero com o dobro, o triplo e a raiz dele, utilizando modulo de math

import math
num=int(input('Digite numero: '))
dobro=num*2
triplo=num*3
raiz=round(math.sqrt(num),2)
print('o dobro dele é {}, o triplo é {} e a raiz dele é {}'.format(dobro,triplo,raiz))
