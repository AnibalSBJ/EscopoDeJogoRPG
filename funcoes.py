import random
from turtle import clear
from drag import drag
from itens import itens
from ogro import ogro
from MonstroPlanta import MonstroPlanta
from heroi import heroi

def ataque(forca):
    dano = random.random()*forca
    return dano

def cura(vida,item):
    cura_vida = vida + item
    return cura_vida

def fuga():
    chance_de_fuga = random.random()*10
    if chance_de_fuga > 5:
        return True
    else:
        return False

def especial(tipo_heroi,forca):
    if tipo_heroi == "guerreiro":
        ataque_especial = "Machadada feroz"
    elif tipo_heroi == "arqueiro":
        ataque_especial = "Rajada de flechas"
    elif tipo_heroi == "mago":
        ataque_especial = "Bola de fogo"

    print(f"você usou {ataque_especial}!")
    
    if tipo_heroi == "guerreiro" or "arqueiro":
        dano_ataque_especial = forca*random.random()*10
    else:
        dano_ataque_especial = forca*random.random()*20
    return dano_ataque_especial

def createMonster():
    chance_monstro = random.random()*10
    monsterLevel = round(random.random()*10)
    if chance_monstro < 6:
        novoMonstro = MonstroPlanta("pequeno","verde","comum","elemental de planta",monsterLevel,monsterLevel*10,monsterLevel)
    elif chance_monstro >= 6 and chance_monstro <= 9:
        novoMonstro = ogro("médio","verde","raro","lutador",monsterLevel*10,monsterLevel*100,monsterLevel*10)
    elif chance_monstro > 9:
        novoMonstro = drag("grande","vermelho","lendário","dragão elemental",monsterLevel*100,monsterLevel*1000,monsterLevel*100)
    return novoMonstro

