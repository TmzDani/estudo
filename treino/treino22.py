##O que é função
#O que define a assinatura da função
#O que é varargs
#Qual a diferença entre argumento e parametro
#R: Uma função pode ou não retornar valores 

def mudai(i):
    i = i + 1
    i = 3
    i = i * 2

def mudav(v):
    v[1] = 6
    v = [1, 2, 3]

i = 4
mudai(i)
v = [4, 12, 2024]
mudav(v)

print(i)
print(v)



#Outra forma
def mudav(v):
    v[1] = 6
    v = [1, 2, 3]
    v[0] = 15

v = [4, 12, 2024]
mudav(v)
print(v)

#Nao executar
s = "Olá"
s = s + "turma"
for i in range(50):     #para o seu bem e o da maquina, não execute, vai ocupar a memoria de lixo e foder com força o processamento  
    s = s + str(i)
    print(s)

"""
NUMERO PRIMO É AQUELE QUE SÓ É DIVISIVEL POR ELE MESMO E PELO NUMERO 1. CRIE UMA FUNÇÃO QUE RETORNE
"""

num = int(input('Digite numero: '))

def primo(a, b):
    a = num/1
    b = num/num
    if b == 1 and a == num:
        True
    return True

print('É primo'.format(primo(num)))
