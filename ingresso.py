class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"O ingresso custa {self.valor},00 R$.")


class VIP(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def imprimeValor(self,adicional):
        total=self.valor + self.valor * adicional/100
        print(f'O ingresso custa {total},00R$.')

normal= Ingresso(100)
normal.imprimeValor()

vip=VIP(200)
vip.imprimeValor(20)