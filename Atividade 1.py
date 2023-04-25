#Faça um sistema de login, pedindo a senha do usuario e mostrando seu nome e a mensagem, login efetuado com sucesso.
usuario=[]
senha=[]
for x in range(5):
    usuario.append(input("Usuário: "))
    senha.append(input("Senha: "))
    print()

novo_usuario = input("Digite o usúario: ")
nova_senha = input("Digite a senha: ")
confusuario = False

for y in range(5):
    if novo_usuario == usuario[y]:
        if nova_senha == senha[y]:
            confusuario = True
            break

if confusuario:
    print("Usuario e senha corretos.")

else:
    print("Usuário ou senha incorretos! Tente Novamente.")

