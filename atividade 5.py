#Faça um código pra ler 5 numeros e guardar numa array e armazenar em um vetor.Após a leitura total dos 5 numeros, o código deve escrever esses 5 numeros lidos na ordem inversa

lista=[]
for x in range(5):
    lista.append(int(input("Digite um número: ")))
for y in range(-1, -6, -1):
    print(lista[y])

#Está percorrendo o indice no negativo ao contrário usando o range negativo (1, 2, 3, 4 // -4,-3, -2,-1)