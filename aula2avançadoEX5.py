class Pessoa:
    def __init__(self,nome):
        self.nome = nome
   
class Estudante(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)
        self.curso = curso
    
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e ando no curso de {self.curso}."

class Professor(Pessoa):
    def __init__(self, nome, disciplina):
        super().__init__(nome)
        self.disciplina = disciplina

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e leciono a disciplina de {self.disciplina}."
        
# Criando objetos
estudante1 = Estudante("Carlos", "Engenharia")
estudante2 = Estudante("João", "Medicina")
professor1 = Professor("Dr. Silva", "Matemática")  
professor2 = Professor("Dra. Costa", "Biologia")

print(estudante1.apresentar())
print(estudante2.apresentar())
print(professor1.apresentar())
print(professor2.apresentar())