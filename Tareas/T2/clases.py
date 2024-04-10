def Ejercito():
    pass

def Combatientes(self, nombre, vida_maxima, vida, poder, defensa, agilidad, resistencia):
    def __init__(self):
        self.nombre = nombre
        self.vida_maxima = vida_maxima
        self.vida = vida
        self.poder = poder
        self.defensa = defensa
        self.agilidad = agilidad
        self.defensa = defensa
        self.resistencia = resistencia
        denominador = self.poder + self.agilidad + self.resistencia
        self.ataque = round((denominador*2*self.vida)/self.vida_maxima)


