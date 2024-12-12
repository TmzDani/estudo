#Criar um vetor contendo numeros e strings e preciso separar-los 

vetor = [1,'hello world', 2, 'pika',9, 'python', 4]

numero = []
string = []

for item in vetor:                      #vai listar todos os itens de vetor
    if isinstance(item, str):       #Vai puxar os itens de formato string
        string.append(item)                 #Vai adicionar os valores string de item no vetor string
    elif isinstance(item,(int,float)):          #Vai puxar os itens em formato numerico
        numero.append(item)                     #Vai adicinoar os valores de item, já separados em int ou float neste caso
print(numero)   	   
print(string)
