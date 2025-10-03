class livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        return f'Livro "{livro.titulo}" adicionado à biblioteca.'

    def listar_livros(self):
        if not self.livros:
            return "Nenhum livro na biblioteca."
        return [f"{livro.titulo} por {livro.autor} ({livro.ano_publicacao})" for livro in self.livros]
    
    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                return f'Livro "{titulo}" removido da biblioteca.'
        return f'Livro "{titulo}" não encontrado na biblioteca.'
    
livro1 = livro("1984", "George Orwell", 1949)
livro2 = livro("To Kill a Mockingbird", "Harper Lee", 1960)
livro3 = livro("The Great Gatsby", "F. Scott Fitzgerald", 1925) 
livro4 = livro("One Hundred Years of Solitude", "Gabriel Garcia Marquez", 1967)
livro5 = livro("Pride and Prejudice", "Jane Austen", 1813)

biblioteca = Biblioteca()

print(biblioteca.adicionar_livro(livro1))
print(biblioteca.adicionar_livro(livro2))
print(biblioteca.adicionar_livro(livro3))
print(biblioteca.adicionar_livro(livro4))
print(biblioteca.adicionar_livro(livro5))

print(biblioteca.listar_livros())
print(biblioteca.remover_livro("1984"))
print(biblioteca.listar_livros())
print(biblioteca.remover_livro("The Great Gatsby"))
print(biblioteca.listar_livros())