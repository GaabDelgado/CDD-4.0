#Escreva um algorito que receba a temperatua em Fahrenheit e calcule para Celcius

temp_F=float(input("Digite a temperatura em Fahrenheit: "))
temp_C= ((temp_F - 32)/9)*5

print(f'A temperatura em graus Celcius é {temp_C:.2f}')