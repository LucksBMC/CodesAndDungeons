# Codes And Dungeons functions
import time, os, keyboard, secrets
from datetime import datetime

class enemy:

    def __init__(self, vida, atk, tipo = None):
        self.vida = vida
        self.atk = atk
        self.tipo = tipo

Olhudo = enemy(25, 5)
Vex = enemy(20, 10, 'ice')
Sus = enemy(30,3)

enemies = [Olhudo,Vex,Sus]

def playtext(string, ask = False):
    text = ''
    for i in string:
        text+=i
        time.sleep(0.01)
        print("\r",text, end='')
    if ask:
        return input()
    else:
        print(' ')

def attacktest(atk, fire = False, poison = False, ice = False, energy = False) :
    chance = 0
    high = False
    while True:
        if keyboard.is_pressed('z'):
            break

        time.sleep(0.05)

        if high:
            chance-=1
        else:
            chance+=1
        if chance == 0:
            high = False
        elif chance == 10:
            high = True

        hud = ['╔═╗','║ ║','║ ║','║ ║','║ ║','║ ║','║ ║','║ ║','║ ║','║ ║','║ ║','╚═╝']
        for i in range(chance):
            hud.remove('║ ║')
            hud.insert(10,'║█║')
        os.system('cls')
        for i in hud:
            print(i) 
    attack = chance*atk
    return attack

def actions():
    actions = ['enemy','boss','treasure','friend','store']
    return secrets.choice(actions)

def percent50():
    chance = [True,False]
    return secrets.choice(chance)

def atk():
    atk = [0,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4]
    return secrets.choice(atk)

def weaponget(index): # RECEBE O ID E RETORNA O NOME DA ARMA
    index = int(index)
    if index == 0:
        return 'socos'
    elif index == 1:
        return 'faca'
    elif index == 2:
        return 'caco de vidro'
    elif index == 3:
        return 'facão'
    elif index == 4:
        return 'correntes'
    elif index == 5:
        return 'flechas'

def weaponindex(name): # RECEBE O NOME E RETORNA O ID DA ARMA
    if name == 'socos':
        return 0
    elif name == 'faca':
        return 1
    elif name == 'caco de vidro':
        return 2
    elif name == 'facão':
        return 3
    elif name == 'correntes':
        return 4
    elif name == 'flechas':
        return 5

def equipget(index): # RECEBE O ID E RETORNA O NOME DO EQUIPAMENTO
    index = int(index)
    if index == 0:
        return 'nada'
    elif index == 1:
        return 'curativo'
    elif index == 2:
        return 'jaqueta de couro'
    elif index == 3:
        return 'capacete de motoqueiro'
    elif index == 4:
        return 'anel poderoso'

def equipindex(name): # RECEBE O NOME E RETORNA O ID DO EQUIPAMENTO
    if name == 'nada':
        return 0
    elif name == 'curativo':
        return 1
    elif name == 'jaqueta de couro':
        return 2
    elif name == 'capacete de motoqueiro':
        return 3
    elif name == 'anel poderoso':
        return 4

def weapondamage(index): # RECEBE O ID E RETORNA O DANO DA ARMA
    index = int(index)
    if index == 0:
        return 3
    elif index == 1:
        return 8
    elif index == 2:
        return 6
    elif index == 3:
        return 11
    elif index == 4:
        return 9
    elif index == 5:
        return 8

def chest():
    chance = ['madeira','madeira','madeira','madeira','prata','prata',
        'prata','ouro','ouro','ossos']
    return secrets.choice(chance)
    
def chestopen(type):
    if type == 'madeira':
        chance = ['caco de vidro','faca','curativo','jaqueta de couro','nada','10g']
    elif type == 'prata':
        chance = ['facão','capacete de motoqueiro','anel poderoso','nada','flechas','50g','100g']
    elif type == 'ouro':
        chance = ['correntes','faca','jaqueta de couro','facão','anel poderoso','flechas','nada','100g','200g','100g']
    elif type == 'ossos':
        chance = ['vida orgânica','500g','250g']
    return secrets.choice(chance)

def traderitem():
    chance = ['faca','jaqueta de couro','anel poderoso','correntes','flechas','capacete de motoqueiro']
    return secrets.choice(chance)

def tradercash():
    chance = [50,75,100,200,500]
    return secrets.choice(chance)