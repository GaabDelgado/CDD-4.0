#Pergunte ao usuário quantos alunos tem na sala e crie um array, unidimensional (vetor) com o nome de todos os alunos da sala

alunos=int(input("Digite a quantidade de alunos da sala: "))
lista_alunos =[]
for i in range(alunos):
    lista_alunos.append(input("Digite o nome dos alunos: "))
#printar um abaixo do outro fora do array.
for aluno in lista_alunos:
    print(aluno)