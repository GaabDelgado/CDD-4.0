count1 = 0
count2 = 0
for x in range (10):
    n1 = int(input("Digite um numero: "))
    if n1 >= 10 and n1 <= 20:
        count1+=1
    else:
        count2+=1
print("Você tem", count1, "números dentro e ", count2, "Números fora.")
