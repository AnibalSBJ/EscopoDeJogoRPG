from asyncio.windows_events import NULL
import random
from turtle import clear
from drag import drag
from itens import itens
from ogro import ogro
from MonstroPlanta import MonstroPlanta
from heroi import heroi
import os
import time
import funcoes
import math

opcao = 0

os.system('clear')

string = '''

Bem-vindo aventureiro!, 
escolha seu herói para lhe 
representar em suas batalhas

Escolha a classe do seu herói:

[1]guerreiro
[2]mago
[3]arqueiro

'''
for ch in string:
    time.sleep(0.03)
    print(ch, end='', flush=True)

raca = NULL
classe = NULL
potion = 0
weapon = "nenhuma"
vest = "nenhuma"
hero = heroi(raca,classe,1,20,200)
inventario = itens(potion,weapon,vest)

opcao = int(input())

if opcao == 1:
    hero.classe = "guerreiro"
elif opcao == 2:
    hero.classe = "mago"
elif opcao == 3:
    hero.classe = "arqueiro"


os.system('clear')

string = f"\n você escolheu a classe {hero.classe}"

for ch in string:
    time.sleep(0.03)
    print(ch, end='', flush=True)

string = '''
Escolha agora qual a raça
de seu herói dentre as opções a seguir:

[1]humano
[2]elfo
[3]anão
[4]orc

'''
for ch in string:
    time.sleep(0.03)
    print(ch, end='', flush=True)


opcao_raca = int(input())

os.system('clear')

if opcao_raca == 1:
    hero.raca = "humano"
elif opcao_raca == 2:
    hero.raca = "elfo"
elif opcao_raca == 3:
    hero.raca = "anão"
elif opcao_raca == 4:
    hero.raca = "orc"

string = f"\n você escolheu a classe {hero.classe} de raça {hero.raca},\n vamos iniciar sua aventura!"

for ch in string:
    time.sleep(0.03)
    print(ch, end='', flush=True)

time.sleep(3)

os.system('clear')

string = '''
Sua aventura começa entrando na floresta maldita aos arredores de midgard,
sua terra foi devastada por monstros do submundo com afinidades elementais,
diversos monstros de elementos diferentes estão zaralhando a porra toda, e tu
é o escolhido pra limpar a merda toda.
'''

for ch in string:
    time.sleep(0.03)
    print(ch, end='', flush=True)

time.sleep(2)

os.system('clear')

matou_monstro = False

string = '''

Andando tranquilamente pela floresta você encontra um monstro planta!,
ele tem uma aparência meio fraca e você com certeza pode derrotá-lo

'''

for ch in string:
    time.sleep(0.03)
    print(ch, end='', flush=True)

while matou_monstro == False:

    string = '''

    o que você decide fazer?

    [1]batalhar com ele
    [2]ignorá-lo

    '''

    for ch in string:
        time.sleep(0.03)
        print(ch, end='', flush=True)

    opcao_batalha = int(input())

    monstroPlanta1 = MonstroPlanta("pequeno","verde","comum","elemental de planta","1","5",5)



    if opcao_batalha == 1:
        dano = funcoes.ataque(hero.forca)
        vida2 = float(monstroPlanta1.vida) - dano
        string = f'''

        você decidiu atacar o monstro planta!
        e causou um total de {dano} de dano
        
        '''

        for ch in string:
            time.sleep(0.03)
            print(ch, end='', flush=True)

        if vida2 <= 0:
            print("\n você matou o monstro planta!")
            hero.level = hero.level+1
            matou_monstro = True
        else:
            print(f"\n a vida atual do monstor planda é {math.floor(vida2)}")

    elif opcao_batalha == 2:
        fuga = funcoes.fuga()
        if fuga == True:
            print("você meteu o pé")
            matou_monstro = True
        else:
            print("você tropeçou e não conseguiu fugir!")
            time.sleep(1)
            hero.vida = math.floor(hero.vida - funcoes.ataque(monstroPlanta1.forca))
    
print('''

continuando sua viagem aventureiro, gostaria de saber seus status?

[1]sim
[2]não

''')

opcao = int(input())

if opcao == 1:
    print(f'''
    seu herói possui:
    {hero.forca} de força
    {hero.level} de level
    {hero.vida} de vida

    atualmente
    ''')

time.sleep(5)

os.system('clear')

string = '''
Dando continuação à sua aventura, você encontra um baú em seu caminho, deseja abrí-lo ?

[1]sim
[2]não

'''

for ch in string:
    time.sleep(0.03)
    print(ch, end='', flush=True)

opcao = int(input())

if opcao == 1:
    chance = random.random()*10
    if chance < 3:
        chance_pocao = random.random()*10
        print("você encontrou uma poção!, ela lhe garantiu um aumento aleatório em algum status")
        if chance_pocao < 5:
            hero.forca = hero.forca + 5
        elif chance_pocao >= 5:
            hero.vida = hero.vida + 5
    elif chance >= 3 and chance <=6 and hero.classe == "guerreiro":
        print("você encontrou um machado grande!, que lhe garantiu um aumento significativo de poder")
        hero.forca = hero.forca + 5
    elif chance >= 3 and chance <=6 and hero.classe == "arqueiro":
        print("você encontrou um arco grande!, que lhe garantiu um aumento significativo de poder")
        hero.forca = hero.forca + 5
    elif chance >= 3 and chance <=6 and hero.classe == "mago":
        print("você encontrou um cetro grande!, que lhe garantiu um aumento significativo de poder")
        hero.forca = hero.forca + 5
    elif chance > 6:
        print("você encontrou uma couraça demoniaca, que lhe garantiu um aumento significativo de vida")
        hero.vida = hero.vida + 50

time.sleep(2)

print(f'''
    Agora seu herói possui:
    {hero.forca} de força
    {hero.level} de level
    {hero.vida} de vida

    atualmente
    ''')

time.sleep(3)

string = '''

Dando continuação à sua jornada

'''
    





