
# CRIE A CLASSE PRODUTO, ONDE PODEMOS CADASTRAR NOME E O PREÇO. CRIE TAMBÉM UM MÉTODO QUE MOSTRE UMA ETIQUETA DE PREÇO DO PRODUTO
from rich import print
from rich.panel import Panel
class Produto:
    
    def __init__(self, nome = "", preco = 0):
        self._nome = nome 
        self._preco = preco
    
    def etiqueta(self):
        etiqueta = Panel(f"{self._nome}\n----------------------------\n{self._preco}", title="Produto")
        print(etiqueta)

p1 = Produto("Computador", 3000.00)
p1.etiqueta()