class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
class cliente:
    def __init__(self, nome,email):
        self.nome = nome
        self.email = email
class carrinho:
    def __init__(self):
        self.listaProdutos = []

    def adicionarProduto(self, produto):
        self.listaProdutos.append(produto)

    def removerProduto(self, produto):
        if produto in self.listaProdutos:
            self.listaProdutos.remove(produto)

    def calcularTotal(self):
        total = sum(produto.preco for produto in self.listaProdutos)
        return total
    
produto1 = produto("Notebook", 3500.00)
produto2 = produto("Mouse", 150.00)
produto3 = produto("Teclado", 250.00)
cliente1 = cliente("Ana", "ana@example.com")
cliente2 = cliente("Bruno", "bruno@example.com")
carrinho1 = carrinho()
carrinho1.adicionarProduto(produto1)    
carrinho1.adicionarProduto(produto2)
carrinho1.adicionarProduto(produto3)
print(f"O total do carrinho é: {carrinho1.calcularTotal()}€")
carrinho1.removerProduto(produto2)  
print(f"O total do carrinho após remover o mouse é: {carrinho1.calcularTotal()}€")
