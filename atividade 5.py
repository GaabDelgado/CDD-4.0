# menu principal
n1=int(input("Digite um número: "))
n2=int(input("Digite outro númmero: "))

print("[1] - SOMA")
print("[2] - SUBTRAÇÃO")
print("[3] - MULTIPLICAÇÃO")
print("[4] - DIVISÃO")
print("[5] - DIGITE OUTRO NÚMERO")
print("[6] - SAIR")
while 1:
    res = int(input("Opcao: "))
    if res == 1:
        print(n1 + n2)
    elif res == 2:
        print(n1-n2)
    elif res == 3:
        print(n1*n2)
    elif res == 4:
        print(n1/n2)
    elif res == 5:
        continue
    elif res == 6:
        break
    else:
        print("ERRO: A opção não se encontra defenida ! tente novamente!")