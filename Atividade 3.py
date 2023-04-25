#Faça um código para ler um vetor de 10 números. Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.

lista_num=[]
con=0
for x in range (10):
    lista_num.append(int(input("Digite um valor: ")))
print()
num2=int(input("Digite outro valor: "))

for y in range (10):
    if num2 == lista_num[y]:
        con+=1
print()
print(f'O valor foi apresentado {con} vezes.')