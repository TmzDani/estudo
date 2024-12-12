#Representando 5% do valor informado e sendo diminuido para o novo

valor=float(input('Digite valor: '))
desconto=valor*0.05
novo=round(valor-desconto,2)
print(novo)
