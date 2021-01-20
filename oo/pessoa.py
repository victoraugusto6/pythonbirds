class Pessoa:
    def __init__(self, *filhos, nome, idade):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, {id(self)}]'


if __name__ == '__main__':
    victor = Pessoa(nome='Victor', idade='25')
    joao = Pessoa(victor, nome='João', idade=50)

    for filho in joao.filhos:
        print(filho.nome)
        joao.sobrenome = 'Fernandes'
        del joao.filhos
        print(joao.__dict__)
