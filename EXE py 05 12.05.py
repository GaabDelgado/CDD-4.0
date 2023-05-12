def num_primo(num):
    if num == 0 or num ==1:
        print(f'Não é um número primo.')
    elif num == 2 or num == 3:
        print(f'É umm número primo.')
    else:
        if num % 2 != 0 and num % 3 != 0:
            print(f'É número primo.')
        else:
            print(f'Não é um número primo')

num_primo(10)
num_primo(63)
num_primo(90)