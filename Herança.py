class animal:
    def __int__(self,nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f' O{self.nome} foi comer...')

class Gato(animal):
    def __init__(self,nome, cor):
        super().__init__(nome,cor)

    def miar(self):
        print(f'O{self.nome} foi miando...')

class Cachorro(animal):
    def __int__(self, nome, cor):
        super().__init__(nome,cor)

    def latir(self):
        print(f'O {self.nome} foi latindo...')

class Vaca(animal):
    def __int__(self, nome, cor):
        super().__init__(nome,cor)

    def mugir(self):
        print(f'A {self.nome} foi fazendo muuuuuuuu...')

