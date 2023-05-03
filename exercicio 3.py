hora_inicio = int(input("Inicio do round de xadrez: "))
hora_final = int(input("Final do round de xadrez: "))
soma= (hora_inicio + hora_final)
if hora_inicio < hora_final :
    print(f'Sua partida durou {hora_final-hora_inicio}horas.')
else:
    print(f'sua partida durou {(24 - hora_inicio)+hora_final} horas')