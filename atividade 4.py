#Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes, e que exiba a lista desses nomes na tela.
#Após exibir essa lista, o programa deve mostrar também os nomes na ordem inversa em que o usuário os digitou, um por linha.

usuario=[]
for x in range (5):
    usuario.append(input("Digite o usuário: "))
print()

for z in range (5):
    print(usuario[z])
print()

for y in range(-1,-6,-1):
    print(usuario[y])