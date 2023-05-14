print('''
###############################################################
########################## CDD 4.0 ############################
###############################################################
####################### JOGO DA FORCA #########################
###############################################################
################ FEITO POR GABRIEL DELGADO ####################
###############################################################
''')

import random #importa uma biblioteca que tras funções aleatorias.

palavras=["computador", "cachorro", "brasil", "passaro"]

palavra= random.choice(palavras) #escolhe uma palavra.

tentativas=0
chances=2

letras_escolhidas=[] #criei uma lista com as letras que ja foram escolhidas.
estado_atual= ["_"]*len(palavra) #vai ficar no lugar das letras que não foram escolhidas ainda.
#"len" vai colocar a quantia de "_" equivalente a palavra.

print("Bem vindo ao jogo da forca forasteiro!")
print("Você terá 10 chances.")
print("Boa sorte!")

while tentativas < chances and ''.join(estado_atual) != palavra:

    letra=input("\nQual letra você quer tentar?\n ")

    #Caso escolha uma letra repetida
    while letra in letras_escolhidas:
        print("Você ja escolheu essa letra, escolha outra.")
        letra = input("\nQual letra você quer tentar?\n ")

    letras_escolhidas.append(letra)

    if letra in palavra:
        print("Você acertou a letra!\n")
        for i in range(len(palavra)):
            if letra == palavra[i]:
                estado_atual[i] = letra
    else:
        print("Errou!")
        tentativas = tentativas + 1

    #quantas tentativas ele tem:
    print(f'Você ja fez {tentativas} tentativa erradas e ainda tem {chances - tentativas} tentativas.')

    #qual o estado atual da palavra:
    print("Esse é o estado atual:")
    print(estado_atual)

    #quais as letras ele ja tentou:
    print("as letras que você ja tentou são:")
    for item in letras_escolhidas:
        print(item, end=" ")
if tentativas == chances:
    print("Você perdeu!!\n")
    print("Burrão menó.")
else:
    print("Ganhaste, parabuains!")

print(f'A palavra era, {palavra}')