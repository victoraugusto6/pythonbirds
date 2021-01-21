class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome, idade):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, {id(self)}]'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'Ele tem {cls.olhos} olhos'


class Homem(Pessoa):
    pass


# Sobrescrita de atributo
class Mutante(Pessoa):
    olhos = 0


if __name__ == '__main__':
    victor = Mutante(nome='Victor', idade='25')
    joao = Homem(victor, nome='João', idade=50)

    for filho in joao.filhos:
        print(filho.nome)
        joao.sobrenome = 'Fernandes'
        del joao.filhos
        print(joao.__dict__)
        print(Pessoa.metodo_estatico(), victor.metodo_estatico())
        print(Pessoa.nome_e_atributos_de_classe(), victor.nome_e_atributos_de_classe())
        print(victor.olhos)
