class veiculo:
    def __init__(self,mover):
        self.mover = mover
class Carro(veiculo):
    def __init__(self):
        super().__init__(mover="sobre rodas")
        self.tipo = "Carro"
class Bicicleta(veiculo):
    def __init__(self):
        super().__init__(mover="sobre pedais")
        self.tipo = "Bicicleta"
class Aviao(veiculo):
    def __init__(self): 
        super().__init__(mover="pelo ar")
        self.tipo = "Avião"

    def mover_veiculo(self):
        return f"O veículo está se movendo {self.mover}."
    
carro1 = Carro()
bicicleta1 = Bicicleta()
aviao1 = Aviao()
print(f"{carro1.tipo} se move {carro1.mover}.")
print(f"{bicicleta1.tipo} se move {bicicleta1.mover}.")
print(f"{aviao1.tipo} se move {aviao1.mover}.")

