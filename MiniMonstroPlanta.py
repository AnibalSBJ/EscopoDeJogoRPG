import random
class MiniMonstroPlanta:
    def __init__(self,tamanho,cor,raridade,tipo,forca,level):
        self.tamanho = tamanho
        self.cor = cor
        self.raridade = raridade
        self.tipo = tipo
        self.forca = forca
        self.level = level

    def ataque(self):
        dano = random.random()*self.forca
        return dano