class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False

    def exibir_informacoes(self):
        return f"{self.marca} {self.modelo}, Ano: {self.ano}"

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            return f"O carro {self.modelo} está agora ligado."
        else:
            return f"O carro {self.modelo} já está ligado."

    def desligar(self):
        if self.ligado:
            self.ligado = False
            return f"O carro {self.modelo} está agora desligado."
        else:
            return f"O carro {self.modelo} já está desligado."

    def acelerar(self):
        if self.ligado:
            return f"O carro {self.modelo} está a acelerar!"
        else:
            return f"Não é possível acelerar. O carro {self.modelo} está desligado."

# Criando objetos
meu_carro1 = Carro("Toyota", "Corolla", 2020)   
meu_carro2 = Carro("Honda", "Civic", 2019)

# Usando os métodos
print(meu_carro1.exibir_informacoes())

print(meu_carro1.acelerar())     # Deve dizer que está desligado
print(meu_carro1.ligar())        # Liga o carro
print(meu_carro1.acelerar())     # Agora pode acelerar
print(meu_carro1.desligar())     # Desliga o carro
print(meu_carro1.acelerar())     # Novamente não pode acelerar