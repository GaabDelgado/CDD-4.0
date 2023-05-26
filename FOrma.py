class Forma:
    def __init__(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro


class Retangulo(Forma):
    def __init__(self, altura, largura):
        area = altura * largura
        perimetro = 2 * (altura + largura)
        super().__init__(area, perimetro)

    def imprimeArea(self):
        print(f"A área do retângulo é: {self.area}")

    def imprimePerimetro(self):
        print(f"O perímetro do retângulo é: {self.perimetro}")


class Triangulo(Forma):
    def __init__(self, lado1, lado2, lado3):
        semiperimetro = (lado1 + lado2 + lado3) / 2
        area = (semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3)) ** 0.5
        perimetro = lado1 + lado2 + lado3
        super().__init__(area, perimetro)

    def imprimeArea(self):
        print(f"A área do triângulo é: {self.area}")

    def imprimePerimetro(self):
        print(f"O perímetro do triângulo é: {self.perimetro}")


retangulo = Retangulo(5, 8)
retangulo.imprimeArea()
retangulo.imprimePerimetro()

triangulo = Triangulo(3, 4, 5)
triangulo.imprimeArea()
triangulo.imprimePerimetro()
