from random import randint, uniform

class Personagem:
    def __init__(self):
        self.raca = 'raca'
        self.ataque = 0
        self.defesa = 0
        self.vida = 0
        self.vivo = True

    def status(self):
        print(f'Raça: {self.raca}\n'
              f'Ataque: {self.ataque}\n'
              f'Defesa: {self.defesa}\n'
              f'Vida: {self.vida:.2f}\n'
              f'Vivo: {self.vivo}\n')


    def humano(self):
        self.raca = 'Humano'
        self.ataque = 30
        self.defesa = 20
        self.vida = 45
        self.vivo = True
    def orc(self):
        self.raca = 'Orc'
        self.ataque = 40
        self.defesa = 35
        self.vida = 60
        self.vivo = True
    def mago(self):
        self.raca = 'Mago'
        self.ataque = 50
        self.defesa = 10
        self.vida = 35
        self.vivo = True
    def troll(self):
        self.raca = 'Troll'
        self.ataque = 25
        self.defesa = 65
        self.vida = 80
        self.vivo = True
    def elfo(self):
        self.raca = 'Elfo'
        self.ataque = 50
        self.defesa = 30
        self.vida = 40
        self.vivo = True
    def anao(self):
        self.raca = 'Anao'
        self.ataque = 45
        self.defesa = 20
        self.vida = 40
        self.vivo = True

    def javali(self):
        self.raca = 'Animal'
        self.ataque = 5
        self.defesa = 10
        self.vida = 8
        self.vivo = True

    def ataque(self, object):
        self.dano = (self.ataque / 4) * uniform(0.8, 1.2)
        defesa = (object.defesa) * 0.1
        self.dano = self.dano - defesa
        object.vida = (object.vida) - self.dano
        if object.vida <= 0:
            object.vida = 0
            object.vivo = False
            print(f'{self.raca} derrota {object.raca} com um dano de: {self.dano:.2f}.')
        else:
            print(f'{self.raca} ataca {object.raca} e inflige: {self.dano:.2f}.')







