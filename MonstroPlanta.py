import random
class MonstroPlanta:
    def __init__(self,tamanho,cor,raridade,tipo,level,vida):
        self.tamanho = tamanho
        self.cor = cor
        self.raridade = raridade
        self.tipo = tipo
        self.level = level
        self.vida = vida

    def ataque(self):
        dano = random.random()*self.forca
        return dano
