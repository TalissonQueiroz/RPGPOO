from random import randint, uniform


class Personagem():
    def __init__(self, nome, vida, p_ataque, p_defesa):
        self.nome = nome
        self.vida = vida
        self.p_ataque = p_ataque
        self.p_defesa = p_defesa
        self.vivo = True

    def carac(self):
        print(f'Nome do personagem: {self.nome}')
        print(f'HP: {self.vida:.2f}')
        print(f'PA: {self.p_ataque}')
        print(f'PD: {self.p_defesa}\n')

    def ataque(self, object):
        self.dano = (self.p_ataque / 4) * uniform(0.8, 1.2)
        defesa = (object.p_defesa) * 0.1
        self.dano = self.dano - defesa
        object.vida = (object.vida) - self.dano
        if object.vida <= 0:
            object.vida = 0
            object.vivo = False
            print(f'{self.nome} derrota {object.nome} com um dano de: {self.dano:.2f}.')
        else:
            print(f'{self.nome} ataca {object.nome} e inflige: {self.dano:.2f}.')


esqueleto = Personagem('Esqueleto', 55, 90, 50)
orc = Personagem('Orc', 60, 70, 90)
troll = Personagem('Troll', 70, 65, 65)

orc.carac()  ##Funciona normal, mas após o While não funciona mais

while orc.vivo == True or esqueleto.vivo == True:
    if esqueleto.vivo == True and orc.vivo == True:
        esqueleto.ataque(orc)

    if orc.vivo == True and esqueleto.vivo == True:
        orc.ataque(esqueleto)

orc.carac()  ##Não funciona após o While, como resolver este problema?
esqueleto.carac()  ##Não funciona após o While, como resolver este problema?
troll.carac()  ##Não funciona após o While, como resolver este problema?