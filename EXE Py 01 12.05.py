def calcular_estoque(quantidade, valor_unitario, nome):
    return quantidade*valor_unitario,nome

retorno=calcular_estoque(30, 5, "aua")
print(f'Você tem {retorno[1]} em seu estoque, totalizando {retorno[0]},00R$.')