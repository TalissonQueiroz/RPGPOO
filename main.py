from personagem import *
import random

Jogador = Personagem()
Inimigo = Personagem()

def Menu():
    menu = open('menu.txt', 'r')
    print(menu.read())
    menu.close()
def Menu2():
    menu2 = open('menu2.txt','r')
    print(menu2.read())
    menu2.close()
def Atributos():
    atb =open('atributos.txt','r')
    print(atb.read())
    atb.close()
def escolharaca():
    raca = open('raca.txt','r')
    print(raca.read())
    raca.close()

while True:
    Menu()
    selecionar = int(input('Escolha uma Opcao: '))
    if selecionar == 1:
        escolharaca()
        selecionar = int(input('Escolha uma Opcao: '))
        if selecionar == 1:
            Jogador.humano()
            print('Voce Escolheu:')
            Jogador.status()
            break

    elif selecionar == 2:
        Menu2()
        selecionar = int(input('Escolha uma Opcao: '))
        if selecionar == 1:
            Atributos()

print('Prepare-se para a Luta')
print('Iniciando...')

while Jogador.vivo == True or Inimigo.vivo == True:
    if Inimigo.vivo == True and Jogador.vivo == True:
        Inimigo.ataque(Jogador)
    if Jogador.vivo == True and Inimigo.vivo == True:
        Jogador.ataque(Inimigo)

