nota_alunos=[]
soma=0
for x in range (5):
    nota_alunos.append(float(input("Digite as notas dos alunos: ")))
for i in nota_alunos:
    soma+=i
media=soma/5
for nota in nota_alunos:
    if nota >= media:
        print(nota," Acima da media!")
    else:
        print(nota," Abaixo da média!")

#Formato do professor

alunos=[]
somas=0
cont=0
for x in range (5):
    alunos.append("Digite a nota do aluno: ")

for y in range (5):
    soma+=alunos[y]
media=soma/5

for t in range(5):
    if media>=alunos[t]
        cont+=1
print("Aquantidade de alunos acima da média é ",cont)