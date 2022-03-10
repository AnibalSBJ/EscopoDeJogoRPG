from asyncio.windows_events import NULL
import random
from turtle import clear
from drag import drag
from MiniMonstroPlanta import MiniMonstroPlanta
from ogro import ogro
from MonstroPlanta import MonstroPlanta
from heroi import heroi
import os

opcao = 0

print('''
Bem-vindo aventureiro!, 
escolha seu herói para lhe 
representar em suas batalhas

Escolha a classe do seu herói:

[1]guerreiro
[2]mago
[3]arqueiro

''')
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

print(f"\n você escolheu a classe {hero.classe}")

print('''
Escolha agora qual a raça
de seu herói dentre as opções a seguir:

[1]humano
[2]elfo
[3]anão
[4]druida

''')

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
