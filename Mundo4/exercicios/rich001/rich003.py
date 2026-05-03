from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Exemplo")

tabela.add_column("Nome")
tabela.add_column("Preço")
tabela.add_row("Coca-cola", "R$ 5,00")

print(tabela)