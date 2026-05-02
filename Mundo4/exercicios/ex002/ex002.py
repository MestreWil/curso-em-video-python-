# Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade
    
    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "", idade = 0): #Método construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos."
    
    def __str__(self):
        return self.mensagem()
    
    def __getstate__(self):
        return f"Estado do objeto: {self.nome}, {self.idade}"

# Declaração de Objetos
g1 = Gafanhoto("William", 28)

print(g1.mensagem())

g2 = Gafanhoto("MestreWill", 35)

print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())

print(g1.__doc__)
print(g1)
print(g1.__dict__) # Atributo
print(g1.__getstate__())# Metodo