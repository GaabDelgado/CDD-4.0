#Altere o exercicio anterior e mostre na tela ao final, o nome de cada aluno e sua respectiva posição no array

alunos=int(input("Digite a quantidade de alunos da sala: "))
lista_alunos =[]
for i in range(alunos):
    lista_alunos.append(input("Digite o nome dos alunos: "))
cont=0
for aluno in lista_alunos:
        print(cont,aluno )
        cont+=1