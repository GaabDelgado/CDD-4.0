ímpares=[]
pares=[]
positivos=[]
negativos=[]
zeros=[]

for x in range (10):
    num = int(input("Digite um número: "))
    if num == 0:
        zeros.append(num)
    elif num % 2 !=0 and num >0:
        ímpares.append(num)
        positivos.append(num)
    elif num % 2 != 0 and num < 0 :
        ímpares.append(num)
        negativos.append(num)
    elif num % 2 == 0 and num >0:
        pares.append(num)
        positivos.append(num)
    elif num % 2 == 0 and num < 0:
        pares.append(num)
        negativos.append(num)
print(f'{ímpares}, {pares}, {positivos}, {negativos}, {zeros}')