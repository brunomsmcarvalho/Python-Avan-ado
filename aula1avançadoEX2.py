class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self): #método para calcular a área
        return self.largura * self.altura

    def calcular_perimetro(self): #método para calcular o perímetro
        return 2 * (self.largura + self.altura)

largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
retangulo1 = Retangulo(largura, altura)
area = retangulo1.calcular_area()
perimetro = retangulo1.calcular_perimetro()
print(f"A área do retângulo é: {area}")
print(f"O perímetro do retângulo é: {perimetro}")
