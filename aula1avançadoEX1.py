class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    
aluno1 = Pessoa("Ana", 22)
aluno2 = Pessoa("Bruno", 25)
print(aluno1.apresentar())
print(aluno2.apresentar())