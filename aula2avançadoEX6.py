'''class Animal:
    def __init__(self,falar):
        self.falar = falar

class Cao(Animal):
    def __init__(self, nome):
        super().__init__(falar="Au Au")
        self.nome = nome

    def apresentar(self):
        return f"Eu sou {self.nome} e eu digo {self.falar}." 
    
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(falar="Miau")
        self.nome = nome

    def apresentar(self):
        return f"Eu sou {self.nome} e eu digo {self.falar}."
    
cao1 = Cao("Asdrubal")
gato1 = Gato("Tareco")

print(cao1.apresentar())
print(gato1.apresentar())'''
class Animal:
    def falar(self):
        raise NotImplementedError("Subclasses devem implementar este método.")
    
class Cao(Animal):
    def __init__(self):
        self.nome = "Cão"
    def falar(self):
        return f"{self.nome}: diz Au Au"
    
class Gato(Animal):
    def __init__(self):
        self.nome = "Gato"
    def falar(self):
        return f"{self.nome}: diz Miau"
    
animais = [Cao(), Gato(), Cao(), Gato()]
for animal in animais:
    print(animal.falar())