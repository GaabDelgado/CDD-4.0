#MENU COM "DEF"

def menu():
    print(f'''
############ MENU ###########

1-SOMA
2-SUBTRAÇÃO
3-MULTIPLICAÇÃO
4-DIVISÃO
5-SAIR

########### MENU ###########
''')

def soma(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mult(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

while True:
    menu()
    opcao=int(input("Qual sua escolha: "))

    if opcao == 5:
        break

    n1 = float(input("Digite um número:"))
    n2 = float(input("Digite o segundo número: "))
    if opcao == 1:

        print(soma(n1,n2))
    elif opcao == 2:

        print(sub(n1,n2))
    elif opcao == 3:

        print(mult(n1,n2))
    elif opcao == 4:

        print(div(n1,n2))