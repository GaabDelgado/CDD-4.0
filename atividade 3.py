nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
aumento = int(input("Digite a % do aumento anual do salario: "))
salario_final = float(input(salario+salario+(aumento/100))



print("nome: ", nome, "\n idade: ",idade, "\n salário: ", salario )
print("Ano que vem seu salário será: ", aumento, "% mais alto, totalizando: ", salario_final)