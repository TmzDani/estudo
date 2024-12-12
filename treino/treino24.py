def primo(num):
    if num < 2:
        return False  # Números menores que 2 não são primos
    for i in range(2, int(num ** 0.5) + 1):  # Checa divisores de 2 até a raiz quadrada do número
        if num % i == 0:
            return False
    return True

num = int(input("Digite um número: "))  # Solicita um número ao usuário
if primo(num):
    print(f"O número {num} é primo!")
else:
    print(f"O número {num} não é primo.")
