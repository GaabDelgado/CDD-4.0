#Escreva um algoritmo para ler dois valores(considere que não serão lidos valores iguais) e escrevel-los em ordem crescente

v1=int(input("Digite o valor 2: "))
v2=int(input("Digiteo valor 2: "))

while v1 == v2:
    v2 = int(input("Digite um valor: "))

if v1 > v2:
    print(f' {v1} > {v2}')
else:
    print(f'{v2} > {v1}')