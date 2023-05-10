#faça uma função que conte a quantia de vogais de um texto
texto="O rato roeu a roupa do rei de roma"

def conta_vogais(str):
    vogais='aeiouAEIOU'
    cont=0

    for x in str.lower():
        if x in vogais:
           cont+=1
    return cont

print(conta_vogais(texto))

#===============================//==================================================//==================================

#modelo do professor:
def contar_vogais(t):
    cont=0
    for x in t:
        if x in 'aeiouAEIOU':
            cont+=1
    print(cont)

texto="O rato roeu a roupa do rei de roma"
contar_vogais(texto)