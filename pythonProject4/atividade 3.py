count = 0
for x in range (10):
    v = int(input("Digite um número: "))
    if v <0:
        count+=1
print("Você Digitou", count, "número(s) negativos.")