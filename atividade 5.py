#Faça um algoritmo que leia 10 vetores do tipo inteiro e armazene-os em um vetor.
#A seguir, o algoritmo deverá informar:

#(1) todos os números pares que existem no vetor;
#(2) o menor e o maior valor existente no vetor;
#(3) quantos dos valores do vetor são maiores que a média desses valores

num=[]
for x in range (5):
    num.append(int(input("Digite um valor:"))) #SOLICITA OS NÚMEROS DO VETOR!
print('=-=' * 20)

for z in range(5):
    if num[z] % 2 == 0: #<- VERIFICAR NÚMEROS PARES!!
        print(f'{num[z]}, \n')
print('=-=' * 20)

acumulador = 0
menornum = 0
maiornum = 0
con_media=0

for y in range(5): #MOSTRA MENOR E O MAIOR NÚMERO DO VETOR!
    acumulador+=num[y]
    if y==0:
        menornum = num[0]
        maiornum = num[0]
        continue
    if num[y] > maiornum:
        maiornum = num[y]
    if num[y] <  menornum:
        menornum = num[y]

print(f'O menor valor é {menornum} e o maior é {maiornum}')
print('=-='*20)

media=acumulador /5

for c in range(5): #MOSTRA VETORES ACIMA DA MÉDIA!
    if num[c] >= media:
        con_media += 1

print(f'{con_media} números foram maior que a média')