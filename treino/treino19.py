import re           #pesquisei uma biblioteca para melhor uso

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
    maiuscula = sum(1 for c in senha if c.isupper())
    minuscula = sum(1 for c in senha if c.islower())
    numeros = sum(1 for c in senha if c.isdigit())
    simbolos = sum(1 for c in senha if not c.isalnum())

    #Adicionando pontos :D
    pontos += num * 4
    pontos += (num - maiuscula) * 2
    pontos += (num - minuscula) * 2
    pontos += numeros * 4
    pontos += simbolos * 6

    # Numeros e simbolos no meio da senha
    meio = senha[1: -1]                 #Irá excluir o primeiro e último digito
    num_meio = sum(1 for c in meio if c.isdigit() or not c.isalnum())
    pontos += num_meio * 2
    
    #Regras extras(adiciona 2 pontos para cada regra)
    regras = 0
    if num >= 8:
        regras += 1
    if (maiuscula >= 3/4 * num or minuscula >=3/4 * num or
        numeros >= 3/4 * num or simbolos >= 3/4 * num):
        regras += 1
    pontos += regras * 2

    #subtração
    #Deduções
    if numeros == 0 and simbolos == 0:
        pontos -= num
    if maiuscula == 0 and minuscula == 0 and simbolos == 0:
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
