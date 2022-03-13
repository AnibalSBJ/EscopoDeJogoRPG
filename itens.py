class itens:
    def __init__(self,pocao_cura,arma,vestimenta):
        self.pocao_cura = pocao_cura
        self.arma = arma
        self.vestimenta = vestimenta
        
    def Cura(self,vida):
        vida_atual = self.pocao_cura + vida
        return vida_atual

    def equiparArma(self,forca_heroi):
        forca_heroi = forca_heroi + 10
        return forca_heroi

    def equiparVestimenta(self,vida_heroi):
        vida_heroi = vida_heroi + 50
        return vida_heroi
