#Usando while escreva um algoritmo que preencha um array A com os 10 primeiros números ímpares, iniciando por zero.
a=[]
count=10
numero=1
while count > 0:
    if numero % 2 != 0:
        a.append(numero)
        count-=1
    numero+=1
print(a)