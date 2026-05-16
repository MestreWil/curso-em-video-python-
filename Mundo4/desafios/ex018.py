from rich import print
from rich.panel import Panel

# Crie uma classe Churrasco, onde seja possível informar quantas pessoas vão participar e mostre quanto de carne deve ser comprado, 
# o custo total do churrasco e o preço por pessoa

#CONSIDERE:
# Consumo padrão: 400g por pessoa
# Preço: R$82,40kg

class Churrasco:
    
    def __init__(self, titulo = '', pessoas = 0):
        self._titulo = titulo
        self._pessoas = pessoas
        self._consumo = 0.4
        self._preco = 82.40
    def analisar(self):
        consumo_por_pessoa = self._consumo * self._pessoas
        preco_total = consumo_por_pessoa * self._preco
        preco_por_pessoa = preco_total / self._pessoas
        kg_total = self._consumo * self._pessoas
        mensagem = f"Analisando [green]{self._titulo}[/] com [blue]{self._pessoas} convidados.[/]\n"
        mensagem += f"Cada participante comerá {self._consumo} e cada Kg custa R${self._preco}\n"
        mensagem += f"Recomendo [blue]comprar {kg_total}[/] de carne\n"
        mensagem += f"O custo total será de [green]{preco_total:.2f}[/]\n"
        mensagem += f"Cada pessoa pagará [yellow]{preco_por_pessoa}[/]\n"
        analise = Panel(mensagem, title=self._titulo)
        print(analise)
c1 = Churrasco("Churras dos amigos", 15)
c1.analisar()