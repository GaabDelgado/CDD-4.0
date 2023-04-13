senhac = "carcara"
chances=3
senha=input("Digite a senha: ")

while senha != senhac:
    chances-= 1
    print("senha incorreta, digite: ")
    senhac=input()
    print(chances)
    if chances>2 and senha!=senhac
        print ("senha bloqueada")
        break
else:
    print("Acesso liberado")