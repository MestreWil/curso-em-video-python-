# Declaração de Classe
class Gafanhoto:
    def __init__(self): #Método construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos."

# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "William"
g1.idade = 28
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "MestreWill"
g2.idade = 35
print(g2.mensagem())