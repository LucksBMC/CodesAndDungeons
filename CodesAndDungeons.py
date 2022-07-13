from multiprocessing.connection import wait
import os, time, secrets, keyboard, ced
from datetime import datetime

os.system('cls')
try: #Verifica a existência de um arquivo de um jogo salvo
    save_file = open('save.txt', 'r') 
except:
    save_file = ''
saved = False

file = ''
for i in save_file: #Verifica a existência de um jogo salvo.
    saved = True
    file+=i

print(datetime.today().strftime('%H:%M:%S'))

if saved: #Se um jogo salvo for encontrado, este comando recuperará os arquivos.
    print('Jogo salvo detectado!')
    name = file[file.index('#1')+2:file.index('#2')]
    weapon = file[file.index('#2')+2:file.index('#3')]
    equipment = file[file.index('#3')+2:file.index('#4')]
    cash = int(file[file.index('#4')+2:file.index('#5')])
    level = int(file[file.index('#5')+2:file.index('#6')])
    exp = int(file[file.index('#6')+2:file.index('#7')])
    life = int(file[file.index('#7')+2:file.index('#8')])
    max_life = 20+(level*5)
    print(f'Nome: {name}\nVida: {life}\nArma: {ced.weaponget(weapon)}\nEquipamento: {ced.equipget(equipment)}\nMoedas: {cash}\nNível: {level}\nExp: {exp}')
else:
    name = ced.playtext('Jogo salvo não detectado.\n\nInsira seu nome: ',True)
    weapon = 0
    equipment = 0
    cash = 0
    level = 1
    exp = 0
    life = 25
    max_life = 20+(level*5)
    os.system('cls')
    ced.playtext(f'{name}! Bem-vindo(a) ao Codes & Dungeons')
    time.sleep(3)
    ced.playtext('Use a tecla Z para confirmar e X para cancelar!')
    keyboard.wait('z')
# INICIANDO JOGO --------------------------------------------------------------------------------------------

ced.playtext('carregando...')
time.sleep(2)

timeset = datetime.today().strftime('%H:%M:%S')
ced.playtext(f'[{timeset}] - {name} entrou na masmorra...')

while True:
    class enemy: #CRIANDO A BASE PADRÃO DE TODOS OS INIMIGOS
        def __init__(self, name, life, atk, type = None):
            self.name = name
            self.life = life
            self.atk = atk
            self.type = type

    # CRIANDO OS INIMIGOS
    olhudo = enemy('Olhudo', 25, 5)
    vex = enemy('Vex', 20, 10)
    sorks = enemy('Sorks', 30,3)
    enemies = [olhudo,vex,sorks]

    # CRIANDO OS TRADERS (Quando foram roubados)
    alvez = enemy('Alvez', 35, 6)
    ivan = enemy('Ivan', 20, 7)
    zikov = enemy('Zikov', 40, 3)
    traders = [alvez,ivan,zikov]

    action = secrets.choice(['enemy','treasure','store'])


    # CONTROLE DE NÍVEL E REGENERAÇÃO
    if exp >= level*5:
        exp = 0
        level+=1
        max_life = 20+(level*5)
        life = max_life
        timeset = datetime.today().strftime('%H:%M:%S')
        ced.playtext(f'[{timeset}] - {name} subiu para o nível {level}! (Vida maximizada)')
        keyboard.wait('z')
    if life < max_life:
        heal = 0
        for i in range(0,secrets.choice(range(2,10))):
            if life<max_life:
                life+=1
                heal+=1
        timeset = datetime.today().strftime('%H:%M:%S')
        ced.playtext(f'[{timeset}] - {name} curou {heal} pontos de vida.')
        keyboard.wait('z')

    while True:
        ced.playtext(f'[z] - CONTINUAR | [x] - STATUS | [c] - SALVAR')
        while True:
            if keyboard.is_pressed('x'):
                break
            if keyboard.is_pressed('z'):
                break
            if keyboard.is_pressed('c'):
                break
        if keyboard.is_pressed('z'):
            timeset = datetime.today().strftime('%H:%M:%S')
            ced.playtext(f'{name} decidiu continuar explorando a masmorra...')
            break
        if keyboard.is_pressed('x'):
            timeset = datetime.today().strftime('%H:%M:%S')
            ced.playtext(f'Nome: {name}')
            ced.playtext(f'Vida: {life}')
            ced.playtext(f'Arma: {ced.weaponget(weapon)}')
            ced.playtext(f'Equipamento: {ced.equipget(equipment)}')
            ced.playtext(f'Moedas: {cash}')
            ced.playtext(f'Nível: {level}')
            ced.playtext(f'Exp: {exp}')
        elif keyboard.is_pressed('c'):
            save_file = open('save.txt', 'w') 
            save_file.write(f'#1{name}#2{weapon}#3{equipment}#4{cash}#5{level}#6{exp}#7{life}#8')
            ced.playtext(f'jogo salvo!')
            time.sleep(3)

    # PROCEDIMENTO BÁSICO DE BATALHA -----------------------------------------------------------

    if action == 'enemy':
        monster = secrets.choice(enemies)
        timeset = datetime.today().strftime('%H:%M:%S')
        ced.playtext(f'[{timeset}] - {name} encontrou um {monster.name} ({monster.name} possui {monster.life} pontos de vida).')
        while True:
            ced.playtext(f'[z] - LUTAR | [x] - FUGIR')
            while True:
                if keyboard.is_pressed('x'):
                    break
                if keyboard.is_pressed('z'):
                    break
            if keyboard.is_pressed('x'):
                timeset = datetime.today().strftime('%H:%M:%S')
                ced.playtext(f'[{timeset}] - {name} decidiu fugir de {monster.name}!')
                keyboard.wait('z')
                timeset = datetime.today().strftime('%H:%M:%S')
                if ced.percent50():
                    ced.playtext(f'[{timeset}] - {name} conseguiu fugir de {monster.name}!')
                    break
                else:
                    timeset = datetime.today().strftime('%H:%M:%S')
                    ced.playtext(f'[{timeset}] - {name} não conseguiu fugir de {monster.name}!')
                    keyboard.wait('z')
                    timeset = datetime.today().strftime('%H:%M:%S')
                    ced.playtext(f'[{timeset}] - {monster.name} vai atacar...')
                    keyboard.wait('z')
                    timeset = datetime.today().strftime('%H:%M:%S')
                    ced.playtext(f'[{timeset}] - {monster.name} atacou {name} e causou {monster.atk} de dano.')
                    life-=monster.atk
                    keyboard.wait('z')
                    timeset = datetime.today().strftime('%H:%M:%S')
                    if life > 0:
                        ced.playtext(f'[{timeset}] - {name} continua com {life} pontos de vida!')
                    else:
                        ced.playtext(f'[{timeset}] - {name} morreu!')
                        ced.playtext(f'FIM DE JOGO!')
                        keyboard.wait('z')
                        exit()
            elif keyboard.is_pressed('z'):
                timeset = datetime.today().strftime('%H:%M:%S')
                ced.playtext(f'[{timeset}] - {name} decidiu atacar {monster.name}!')
                keyboard.wait('z')
                atk = ced.atk()
                damage = atk*ced.weapondamage(weapon)
                timeset = datetime.today().strftime('%H:%M:%S')
                if atk == 0:
                    ced.playtext(f'[{timeset}] - {name} falhou e não conseguiu atacar.')
                if atk == 1:
                    ced.playtext(f'[{timeset}] - {name} acertou {monster.name} de raspão usando {ced.weaponget(weapon)} e causou {damage} de dano!')
                    monster.life-=damage
                if atk == 2:
                    ced.playtext(f'[{timeset}] - {name} antingiu {monster.name} usando {ced.weaponget(weapon)} e causou {damage} de dano!')
                    monster.life-=damage
                if atk == 3:
                    ced.playtext(f'[{timeset}] - {name} atacou {monster.name} com {ced.weaponget(weapon)} e causou {damage} de dano!')
                    monster.life-=damage
                if atk == 4:
                    ced.playtext(f'[{timeset}] - {name} atingiu {monster.name} em cheio com {ced.weaponget(weapon)} e causou incríveis {damage} de dano!')
                    monster.life-=damage
                keyboard.wait('z')
                if monster.life > 0:
                    timeset = datetime.today().strftime('%H:%M:%S')
                    ced.playtext(f'[{timeset}] - {monster.name} ainda possui {monster.life} pontos de vida!')
                    keyboard.wait('z')
                    timeset = datetime.today().strftime('%H:%M:%S')
                    ced.playtext(f'[{timeset}] - {monster.name} vai atacar...')
                    keyboard.wait('z')
                    timeset = datetime.today().strftime('%H:%M:%S')
                    ced.playtext(f'[{timeset}] - {monster.name} atacou {name} e causou {monster.atk} de dano.')
                    life-=monster.atk
                    keyboard.wait('z')
                    timeset = datetime.today().strftime('%H:%M:%S')
                    if life > 0:
                        ced.playtext(f'[{timeset}] - {name} continua com {life} pontos de vida!')
                    else:
                        ced.playtext(f'[{timeset}] - {name} morreu!')
                        ced.playtext(f'FIM DE JOGO!')
                        keyboard.wait('z')
                        exit()
                else:
                    money = secrets.choice(range(0,75))
                    ced.playtext(f'[{timeset}] - {monster.name} foi derrotado por {name}!')
                    keyboard.wait('z')
                    timeset = datetime.today().strftime('%H:%M:%S')
                    ced.playtext(f'[{timeset}] - {name} recebeu {money}g e 1exp!')
                    exp+=1
                    cash+=money
                    break

    # PROCEDIMENTO BÁSICO DE TESOURO -------------------------------------------------------------------

    if action == 'treasure':
        chest = ced.chest()
        timeset = datetime.today().strftime('%H:%M:%S')
        ced.playtext(f'[{timeset}] - {name} encontou um báu de {chest}!')
        ced.playtext(f'[z] - ABRIR | [x] - IGNORAR')
        while True:
            if keyboard.is_pressed('x'):
                break
            if keyboard.is_pressed('z'):
                break
        if keyboard.is_pressed('x'):
            timeset = datetime.today().strftime('%H:%M:%S')
            ced.playtext(f'[{timeset}] - {name} ignorou o baú de {chest}.')
        elif keyboard.is_pressed('z'):
            timeset = datetime.today().strftime('%H:%M:%S')
            ced.playtext(f'[{timeset}] - {name} decidiu abrir o baú de {chest}.')
            item = ced.chestopen(chest)
            keyboard.wait('z')
            timeset = datetime.today().strftime('%H:%M:%S')
            ced.playtext(f'[{timeset}] - {name} encontrou {item} no baú.')
            if item == 'jaqueta de couro' or item == 'curativo' or item == 'capacete de motoqueiro' \
                or item == 'anel poderoso':
                ced.playtext(f'[z] - EQUIPAR | [x] - JOGAR FORA')
                while True:
                    if keyboard.is_pressed('x'):
                        break
                    if keyboard.is_pressed('z'):
                        break
                if keyboard.is_pressed('z'):
                    timeset = datetime.today().strftime('%H:%M:%S')
                    ced.playtext(f'[{timeset}] - {name} equipou {item}.')
                    equipment = ced.equipindex(item)
                if keyboard.is_pressed('x'):
                    timeset = datetime.today().strftime('%H:%M:%S')
                    ced.playtext(f'[{timeset}] - {name} deixou {item} para trás.')
            elif item == 'caco de vidro' or item == 'faca' or item == 'facão' \
                or item == 'correntes' or item == 'flechas':
                ced.playtext(f'[z] - EQUIPAR | [x] - JOGAR FORA')
                while True:
                    if keyboard.is_pressed('x'):
                        break
                    if keyboard.is_pressed('z'):
                        break
                if keyboard.is_pressed('z'):
                    timeset = datetime.today().strftime('%H:%M:%S')
                    ced.playtext(f'[{timeset}] - {name} equipou {item}.')
                    weapon = ced.weaponindex(item)
                if keyboard.is_pressed('x'):
                    timeset = datetime.today().strftime('%H:%M:%S')
                    ced.playtext(f'[{timeset}] - {name} deixou {item} para trás.')
            elif item == 'vida orgânica':
                timeset = datetime.today().strftime('%H:%M:%S')
                ced.playtext(f'[{timeset}] - {name} maximou os pontos de vida!')
            elif item == '10g' or item == '50g' or item == '100g' or item == '200g' or item == '250g' \
                or item == '500g':
                money = int(item[:item.index('g')])
                timeset = datetime.today().strftime('%H:%M:%S')
                cash+=money
                ced.playtext(f'[{timeset}] - {name} coletou {money} moedas e agora possui {cash} moedas!')

    # PROCEDIMENTO BÁSICO DE LOJA ------------------------------------------------------------------------------

    if action == 'store':
        traderman = secrets.choice(traders)
        timeset = datetime.today().strftime('%H:%M:%S')
        ced.playtext(f'[{timeset}] - {name} se depara com {traderman.name}, um negociante!')
        keyboard.wait('z')
        item = ced.traderitem()
        cost = ced.tradercash()
        timeset = datetime.today().strftime('%H:%M:%S')
        ced.playtext(f'[{timeset}] - {traderman.name} lhe oferece {item} por {cost} moedas. (Você possui {cash} moedas)')
        ced.playtext(f'[z] - COMPRAR | [x] - IGNORAR | [c] - ROUBAR')
        while True:
            if keyboard.is_pressed('x'):
                break
            if keyboard.is_pressed('z'):
                break
            if keyboard.is_pressed('c'):
                break
        if keyboard.is_pressed('z'):
            if cash >= cost:
                cash-=cost
                timeset = datetime.today().strftime('%H:%M:%S')
                ced.playtext(f'[{timeset}] - {name} comprou {item} por {cost} moedas!')
                if item == 'jaqueta de couro' or item == 'curativo' or item == 'capacete de motoqueiro' \
                    or item == 'anel poderoso':
                    equipment = ced.equipindex(item)
                elif item == 'caco de vidro' or item == 'faca' or item == 'facão' \
                    or item == 'correntes' or item == 'flechas':
                    weapon = ced.weaponindex(item)
                exp+=1

            else:
                keyboard.wait('z')
                timeset = datetime.today().strftime('%H:%M:%S')
                ced.playtext(f'[{timeset}] - {name} não tem moedas suficientes para comprar {item}!')
        elif keyboard.is_pressed('x'):
            timeset = datetime.today().strftime('%H:%M:%S')
            ced.playtext(f'[{timeset}] - {name} ignorou a oferta de {traderman.name}!')
        elif keyboard.is_pressed('c'):
            timeset = datetime.today().strftime('%H:%M:%S')
            ced.playtext(f'[{timeset}] - {name} decidiu roubar {item} de {traderman.name}.')
            keyboard.wait('z')
            if ced.percent50():
                timeset = datetime.today().strftime('%H:%M:%S')
                ced.playtext(f'[{timeset}] - {name} furtou {item} com sucesso.')
                if item == 'jaqueta de couro' or item == 'curativo' or item == 'capacete de motoqueiro' \
                    or item == 'anel poderoso':
                    equipment = ced.equipindex(item)
                elif item == 'caco de vidro' or item == 'faca' or item == 'facão' \
                    or item == 'correntes' or item == 'flechas':
                    weapon = ced.weaponindex(item)
            else:
                timeset = datetime.today().strftime('%H:%M:%S')
                ced.playtext(f'[{timeset}] - {traderman.name} flagrou {name} tentando o roubar!')
                keyboard.wait('z')
                timeset = datetime.today().strftime('%H:%M:%S')
                ced.playtext(f'[{timeset}] - {traderman.name} parte para o confronto! ({traderman.name} possui {traderman.life} pontos de vida).')
                while True:
                    ced.playtext(f'[z] - LUTAR | [x] - FUGIR')
                    while True:
                        if keyboard.is_pressed('x'):
                            break
                        if keyboard.is_pressed('z'):
                            break
                    if keyboard.is_pressed('x'):
                        timeset = datetime.today().strftime('%H:%M:%S')
                        ced.playtext(f'[{timeset}] - {name} decidiu fugir de {traderman.name}!')
                        keyboard.wait('z')
                        timeset = datetime.today().strftime('%H:%M:%S')
                        if ced.percent50():
                            ced.playtext(f'[{timeset}] - {name} conseguiu fugir de {traderman.name}!')
                            break
                        else:
                            timeset = datetime.today().strftime('%H:%M:%S')
                            ced.playtext(f'[{timeset}] - {name} não conseguiu fugir de {traderman.name}!')
                            keyboard.wait('z')
                            timeset = datetime.today().strftime('%H:%M:%S')
                            ced.playtext(f'[{timeset}] - {traderman.name} vai atacar...')
                            keyboard.wait('z')
                            timeset = datetime.today().strftime('%H:%M:%S')
                            ced.playtext(f'[{timeset}] - {traderman.name} atacou {name} e causou {traderman.atk} de dano.')
                            life-=traderman.atk
                            keyboard.wait('z')
                            timeset = datetime.today().strftime('%H:%M:%S')
                            if life > 0:
                                ced.playtext(f'[{timeset}] - {name} continua com {life} pontos de vida!')
                            else:
                                ced.playtext(f'[{timeset}] - {name} morreu!')
                                ced.playtext(f'FIM DE JOGO!')
                                keyboard.wait('z')
                                exit()
                    elif keyboard.is_pressed('z'):
                        timeset = datetime.today().strftime('%H:%M:%S')
                        ced.playtext(f'[{timeset}] - {name} decidiu atacar {traderman.name}!')
                        keyboard.wait('z')
                        atk = ced.atk()
                        damage = atk*ced.weapondamage(weapon)
                        timeset = datetime.today().strftime('%H:%M:%S')
                        if atk == 0:
                            ced.playtext(f'[{timeset}] - {name} falhou e não conseguiu atacar.')
                        if atk == 1:
                            ced.playtext(f'[{timeset}] - {name} acertou {traderman.name} de raspão usando {ced.weaponget(weapon)} e causou {damage} de dano!')
                            traderman.life-=damage
                        if atk == 2:
                            ced.playtext(f'[{timeset}] - {name} antingiu {traderman.name} usando {ced.weaponget(weapon)} e causou {damage} de dano!')
                            traderman.life-=damage
                        if atk == 3:
                            ced.playtext(f'[{timeset}] - {name} atacou {traderman.name} com {ced.weaponget(weapon)} e causou {damage} de dano!')
                            traderman.life-=damage
                        if atk == 4:
                            ced.playtext(f'[{timeset}] - {name} atingiu {traderman.name} em cheio com {ced.weaponget(weapon)} e causou incríveis {damage} de dano!')
                            traderman.life-=damage
                        keyboard.wait('z')
                        if traderman.life > 0:
                            timeset = datetime.today().strftime('%H:%M:%S')
                            ced.playtext(f'[{timeset}] - {traderman.name} ainda possui {traderman.life} pontos de vida!')
                            keyboard.wait('z')
                            timeset = datetime.today().strftime('%H:%M:%S')
                            ced.playtext(f'[{timeset}] - {traderman.name} vai atacar...')
                            keyboard.wait('z')
                            timeset = datetime.today().strftime('%H:%M:%S')
                            ced.playtext(f'[{timeset}] - {traderman.name} atacou {name} e causou {traderman.atk} de dano.')
                            life-=traderman.atk
                            keyboard.wait('z')
                            timeset = datetime.today().strftime('%H:%M:%S')
                            if life > 0:
                                ced.playtext(f'[{timeset}] - {name} continua com {life} pontos de vida!')
                            else:
                                ced.playtext(f'[{timeset}] - {name} morreu!')
                                ced.playtext(f'FIM DE JOGO!')
                                keyboard.wait('z')
                                exit()
                        else:
                            ced.playtext(f'[{timeset}] - {traderman.name} foi derrotado por {name}!')
                            timeset = datetime.today().strftime('%H:%M:%S')
                            money = secrets.choice(range(0,75))
                            ced.playtext(f'[{timeset}] - {name} recebeu {money}g e 1exp!')
                            exp+=1
                            cash+=money
                            timeset = datetime.today().strftime('%H:%M:%S')
                            ced.playtext(f'[{timeset}] - {name} furtou {item} com sucesso.')
                            if item == 'jaqueta de couro' or item == 'curativo' or item == 'capacete de motoqueiro' \
                                or item == 'anel poderoso':
                                equipment = ced.equipindex(item)
                            elif item == 'caco de vidro' or item == 'faca' or item == 'facão' \
                                or item == 'correntes' or item == 'flechas':
                                weapon = ced.weaponindex(item)
                            exp+=1
                            break