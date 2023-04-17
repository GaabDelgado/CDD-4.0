while True:

    while True:
        nota1=float(input("Primeira nota: "))
        if nota1 >= 0 and nota1 <= 10:
            break
        else:
            print(f'Digite uma nota de 0 a 10!')
    while True:
        nota2=float(input("Segunda nota: "))
        if nota2 >= 0 and nota2 <= 10:
            break
        else:
            print(f'Digite uma nota de 0 a 10!')
    print(f'=-=' * 15)
    print(f'A média do aluno é {(nota2 + nota1) / 2}')

    continuar = input("Deseja continuar? ").upper()

    if continuar == 'N':
        print("Você saiu.")
        break