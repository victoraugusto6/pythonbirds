class Pessoa:
    def __init__(self, nome='Victor', idade=25):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá, {id(self)}]'


if __name__ == '__main__':
    p = Pessoa()
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
