#ler um vetor A de 10 números. Logo em seguida, ler mais um número e guardar em uma variavel X.
#Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo apos imprimir o vetor M

vetorA=[1,2,3,4,5,6,7,8,9,10]
vetorM=[]
x=int(input("número multiplicador:"))
for n in range (10):
    vetorM.append(vetorA[n]*x)
print(vetorM)

