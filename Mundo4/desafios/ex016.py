
from rich import print
#Crie a classe Funcionario, onde podemos cadastrar nome, setor, cargo. Crie também um método que permita ao funcionário se apresentar

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self._nome = nome
        self._setor = setor
        self._cargo = cargo

    def novoNome(self, novoNome):
        self._nome = novoNome

    def novoSetor(self, novoSetor):
        self._Setor = novoSetor
    
    def novoCargo(self, novoCargo):
        self._cargo = novoCargo

    def apresentacao(self):
        return f"Olá, tudo bem? Meu nome é [bold white on red]{self._nome}[/]. \nTrabalho no setor de [bold white on red]{self._setor}[/] no cargo de [bold white on red]{self._cargo}[/]."
    
funcionario1 = Funcionario("William", "Programação", "Desenvolvedor de software")

print(funcionario1.apresentacao())