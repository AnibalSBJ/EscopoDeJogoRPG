import random
class heroi:
    def __init__(self,raca,classe,level,forca):
        self.raca = raca
        self.classe = classe
        self.level = level
        self.forca = forca

    def ataque(self):
        dano = random.random()*self.forca
        return dano



