#Fazer um código para ler um valor N qualquer (que será o tamanho dos vetores).Após, ler dois vetores A e B(de tamanho N cada um) e depois armazenar em um terceiro
#vetor Soma a soma dos elementos do vetor A com os do vetor B(respeitando as mesmas posições) e escrever o vetor Soma.

a=[]
b=[]
c=[]

opc=int(input("Quantos valores temos?: ")) #Código pra ler um vetor qualquer

for x in range(opc): #Ler vetores A e B (com o tamanho do vetor dito anteriormente)

    a.append(int(input("Digite o valor do vetor A: ")))
    b.append(int(input("Digite o valor do vetor B: ")))
    c.append(a[x] + b[x]) #Soma os vetores A e B!
    print()

print(c) #Mostra o resultado da soma.