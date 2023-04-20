#Faça um código para ler 5 nomes de usuários e suas respectivas senhas e armazenar cada lista em um array diferente, após completar a digitação, imprimir, nome, senha e posição dos dados no array

lista_usuario=[]
lista_senha=[]
for x in range(5):
    lista_usuario.append(input("Nome de usuário: "))
    lista_senha.append(input("Digite a senha: "))

#6.2 mostrar posição na array
for y in range (5):
    print(y, lista_usuario[y],lista_senha[y])