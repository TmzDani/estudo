"""Desafio
Instruções:
Faça um programa que retorne a pontuação de uma senha, podendo assim ser avaliada se é forte ou não. Utilize a tabela de resultado abaixo para informar ao usuário se a senha escolhida é muito fraca, fraca, boa, forte ou muito forte.

Regras da pontuação:
- Adições (soma pontos):
Número de caracteres * 4
Maiúsculas: (Número de caracteres - maiúsculas) * 2
Minúsculas: (Número de caracteres - minúsculas) * 2
Números: número de dígitos * 4
Símbolos: número de símbolos * 6
Numeros e símbolos no meio da senha: número * 2
Regras extras: número de regras atendidas * 2
Mínimo 8 caracteres
3/4 de maiúsculas ou minúsculas ou números ou símbolos

- Deduções (reduz pontos):
Somente letras: número de letras
Somente números: número de dígitos
Caracteres repetidos (insensível ao case): número de repetidos
Maiúsculas repetidas consecutivamente: maiúsculas repetidas * 2
Minúsculas repetidas consecutivamente: minúsculas repetidas * 2
Números consecutivos: consecutivos * 2
Letras sequenciais (ex: abc) (>3): (caracteres na sequência - 2) * 3
Números sequenciais (ex: 123) (>3): (caracteres na sequências - 2) * 3
Símbolos sequenciais (ex: !@#) (>3): (caracteres na sequências - 2) * 3

- Resultado:
Pontuação < 20): "Muito fraca"
20 <= Pontuação < 40): "Fraca"
40 <= Pontuação < 60): "Boa"
60 <= Pontuação < 80): "Forte"
80 <= Pontuação: "Muito forte"""

#pesquisei uma biblioteca para melhor uso
import re           


#3 funções para auxiliar durante os pontos
def contar_sequencias(s, padrao):               
    #conta as sequencias de caracteres
    return len(re.findall(padrao, s))

def contar_repetidos_consecutivos(s, condicao):
    #conta os caracteres que se repetem de acordo com as regras
    contador = 0
    for i in range(1, len(s)):
        if condicao(s[i]) and condicao(s[i - 1]) and s[i] == s[i - 1]:
            contador += 1
    return contador

def pontuacao_senha(senha):
    #aqui será a contagem de pontos
    pontos = 0

    #adição
    num = len(senha)
    #aqui a função sum trabalha como um gerador, as condições propostas dentro de cada uma, se forem atendidas, ela ira somar com o sum
    maiuscula = sum(1 for c in senha if c.isupper())                #isupper, se tiver maiuscula, retorna verdadeiro
    minuscula = sum(1 for c in senha if c.islower())                #islower, se tiver minuscula, retorna verdadeiro
    numeros = sum(1 for c in senha if c.isdigit())                  #isdigit, se tiver numero, retorna verdadeiro
    simbolos = sum(1 for c in senha if not c.isalnum())                 #isalnum, esse se não tiver numero ou letra, retorna verdadeiro

    #Adicionando pontos :D
    pontos += num * 4
    pontos += (num - maiuscula) * 2
    pontos += (num - minuscula) * 2
    pontos += numeros * 4
    pontos += simbolos * 6

    # Numeros e simbolos no meio da senha
    meio = senha[1: -1]                 #Irá excluir o primeiro e último digito
    num_meio = sum(1 for c in meio if c.isdigit() or not c.isalnum())           #ira percorre o meio da senha, e vai verificar se tem numero ou não tem letra ou numero
    pontos += num_meio * 2                                                                                      #utilizando assim o alfanumérico para métrica
    
    #Regras extras(adiciona 2 pontos para cada regra)
    regras = 0
    if num >= 8:                                                                 #1 regra, a senha deve ser maior ou igual a 8 digitos
        regras += 1

    """2 regra(mais dificil), ela basicamente verifica se os valores maiusculos,
    minusculos, numeros e simbolos, representa pelo menos 3/4 do total da senha
    se pelo menos QUALQUER UMA das condições forem atendidas, ela conta + 1 na regra
    """
    if (maiuscula >= 3/4 * num or minuscula >=3/4 * num or                       
        numeros >= 3/4 * num or simbolos >= 3/4 * num):                              
        regras += 1                                                                         
    pontos += regras * 2

    #subtração
    #Deduções
    if numeros == 0 and simbolos == 0:                                      #Aqui vai verificar se não tiver nenhum numero e nenhum simbolo, se sim, ai é sofre a subtração de pontos
        pontos -= num
    if maiuscula == 0 and minuscula == 0 and simbolos == 0:                 #mesma coisa, só que aqui vai verificar se só tem numeros
        pontos -= numeros

    #repetição
    repetidos = sum(1 for c in senha if senha.count(c) > 1)     #vai contar quantas repeticoes tem na senha
    pontos -= repetidos

    #Casos de repetição
    pontos -= contar_repetidos_consecutivos(senha, str.isupper) * 2                 #maiscula
    pontos -= contar_repetidos_consecutivos(senha, str.islower) * 2                 #minuscula
    pontos -= contar_repetidos_consecutivos(senha, str.isdigit) * 2                   #numeros

    #Casos sequenciais
    pontos -= contar_sequencias(senha, r"[a-zA-Z]{4,}") * 3                         #ele ta indo de a-z tudo minusculo e de A-Z tudo maiusculo, se tiver 4 no minimo ele conta
    pontos -= contar_sequencias(senha, r"\d{4,}") * 3                               #aqui basicamente ta usando uma expressa chamada \d, que é basicamente numeros de 0 a 9, e se tiver uma sequencia de no minimo 4 numeros consecutivos, ele conta
    pontos -= contar_sequencias(senha, r"[!@#\$%\^&\*\(\)_\+\-=\[\]\{\};:'\",<>\./?\\|`~]{4,}") * 3        #nem cristo sabe o que é isso aqui,mas aparentemente ele ta analisando caracter especial por caraceter, enquanto vai andando pela senha, se achar 4, ele conta

    #FINALLY

    #Aqui achei melhor (e mais compacto) dar valor a variavel classificacao, e retornar ela junto com os pontos, tentei com o print e deu errado
    if pontos < 10:
        classificacao ="Muito fraca"
    elif 10 <= pontos < 30:
        classificacao = "Fraca"
    elif 30 <= pontos < 50:
        classificacao = "Boa"
    elif 50 <= pontos < 70:
        classificacao = "Forte"
    else:
        classificacao = "Muito Forte"
    return pontos, classificacao
    
senha = input("Digite sua senha: ")
pontuacao, classificacao = pontuacao_senha(senha)
print('Pontuação {}'.format(pontuacao))
print('Classificação: {}'.format(classificacao))