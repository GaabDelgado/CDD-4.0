class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False):
        self.nome = nome
        self.peso=peso
        self.idade = idade
        self._comendo = comendo
        self.falando = False
        self.dormindo=False

    def comer(self, comida):

        if self._comendo:
            print(f'Você já está comendo...')
        else:
            self._comendo=True
            print(f'Você começou a comer {comida}!')


    def parar_comer(self):
        if self._comendo:
            self._comendo = False
            print(f'Você parou de comer.')
        else:
            print(f'Você está comendo.')

    def falar(self):
        if not self.falando and not self._comendo:
            self.falando = True
            print(f'Você começou a falar.')
        elif self.falando:
            print(f'Você está falando...')
        else:
            print("Você não deveria falar comendo.")

    def parar_falar(self):
        if self.falando:
            self.falando=False
            print("Você parou de falar.")
        else:
            print("Você nao está falando no momento.")

    def dormir(self):
        if not self.dormindo and not self._comendo and not self.falando:
            self.dormindo = True
            print("Você começou a dormir.")
        elif self.dormindo:
            print("Você ja está dormindo...")
        elif self.falando:
            print("Você nao pode dormir falando...")
        else:
            print("Você não pode dormir estando comendo.")

    def acordar(self):
        if self.dormindo:
            self.dormindo = False
            print("Você acordou!!")
        else:
            print("Você já está acordado...")



p1 = Pessoa("Delgado", 105, 21)
print(f'{p1.nome} tem {p1.idade} e tem também {p1.peso} kg')
p1.comer("Pão")
p1.comer("Pão")
p1.falar()
p1.parar_comer()
p1.falar()
p1.comer("Pão")
p1.dormir()
p1.parar_falar()
p1.dormir()