#Classe:é uma estrutura que define um conjunto de atributos e métodos que podem ser utilizados para criar objetos.
# as classes são fundamentais para a programação orientada a objetos, proporcionando organização, reutilização,
# abstração e outras vantagens que contribuem para o desenvolvimento de software eficiente e escalável.
# Os paradigmas de programação são essenciais para o desenvolvimento de software eficiente e escalável,propoecionando organização,reutilização e abstração.
# Sim:a versatilidade do Python como linguagem multiparadigma possibilita a construção de diversos tipos de softwares.

class Carro:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca
    def get_nome(self):
        return self._nome

    def get_marca(self):
        return self._marca
    def set_marca(self, nova_marca):
        self._marca = nova_marca


# Criando uma instância da classe Carro
meu_carro = Carro(nome="Prisma", marca="Chevrolet")

# Acessando os atributos
print(f"Nome do carro: {meu_carro.nome}")
print(f"Marca do carro: {meu_carro.marca}")
