from asyncio.windows_events import NULL
import random
from turtle import clear
from drag import drag
from MiniMonstroPlanta import MiniMonstroPlanta
from ogro import ogro
from MonstroPlanta import MonstroPlanta
from heroi import heroi
import os
import time

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
    time.sleep(0.05)
    print(ch, end='', flush=True)

raca = NULL
classe = NULL
hero = heroi(raca,classe)
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
    time.sleep(0.05)
    print(ch, end='', flush=True)

string = '''
Escolha agora qual a raça
de seu herói dentre as opções a seguir:

[1]humano
[2]elfo
[3]anão
[4]druida

'''
for ch in string:
    time.sleep(0.05)
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
    hero.raca = "druida"

print(f"\n você escolheu a classe {hero.classe} de raça {hero.raca},\n vamos iniciar sua aventura!")

time.sleep(3)

print("Sua aventura começa entrando na floresta maldita aos arredores de midgard")