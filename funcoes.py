import random

def ataque(forca):
    dano = random.random()*forca
    return dano

def cura(vida,item):
    cura_vida = vida + item
    return cura_vida

def fuga():
    chance_de_fuga = random.random()*10
    if chance_de_fuga < 5:
        print("você tropeçou e não conseguiu fugir!")
    else:
        print("você meteu o pé!")

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
