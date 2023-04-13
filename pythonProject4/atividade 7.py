N_alunos=int(input ("Digite  o número de alunos: "))
N_div = N_alunos
S_Notas = 0
while N_alunos >0:
    Notas_alunos=float(input("Digite a nota dos alunos:"))
    S_Notas += Notas_alunos
    N_alunos -= 1
print("A média dos alunos é:", S_Notas / N_div)