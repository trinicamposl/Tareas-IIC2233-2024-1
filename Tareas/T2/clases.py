from parametros import oro_inicial, cansancio, prob_cab, red_cab, atq_cab, prob_mag
from parametros import red_mag,atq_mag
from abc import ABC, abstractmethod
import random


def Ejercito():
    def __init__(self):
        self.combatientes = []
        self.oro = oro_inicial
    
    def combatir(enemigo):
        pass

    @property
    def presentarse(self):
        return __str__(self)
 

    def __str__(self):
        print("Este es tu ejército actual:")
        for combatiente in self.combatientes:
            presentarse(combatiente)
            

def Combatientes(ABC):
    def __init__(self,nombre, vida_maxima, vida, poder, defensa, agilidad, resistencia):
        self.nombre = nombre
        self.vida_maxima = vida_maxima
        self._vida = vida
        self.poder = poder
        self.defensa = defensa
        self.agilidad = agilidad
        self.defensa = defensa
        self.resistencia = resistencia
        denominador = self.poder + self.agilidad + self.resistencia
        self.ataque = round((denominador*2*self.vida)/self.vida_maxima)
    
    @property
    def curarse(self):
        return self._vida
    
    @curarse.setter
    def curarse(self, cantidad):
        self._vida = min(self._vida + cantidad, self.vida_maxima)

    @abstractmethod
    def presentarse(self):
        pass
 
    @abstractmethod
    def atacar(enemigo, self):
        pass

    @abstractmethod
    def evolucionar(self):
        pass



def Guerrero(Combatiente):
    def __init__(self, tipo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tipo = "Gato Guerrero"  
    
    def __str__(self):
        print(f"¡Hola! Soy {self.nombre}, un {self.tipo} con
                   {self.vida}/ {self.vida_maxima} de vida, {self.ataque} de
                     ataque y {self.defensa} de defensa")
    
    def presentarse(self):
        return __str__(self)
    
    def atacar(enemigo, self):
        self.agilidad -= self.agilidad*(1-cansancio/100)
        enemigo.vida -= round (self.ataque - enemigo.defensa)


    def evolucionar(self):
        pass

def Caballero(Combatiente):
    def __init__(self, tipo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tipo = "Gato Caballero"  
    
    def __str__(self):
        print(f"¡Hola! Soy {self.nombre}, un {self.tipo} con
                   {self.vida}/ {self.vida_maxima} de vida, {self.ataque} de
                     ataque y {self.defensa} de defensa")
    
    def presentarse(self):
        return __str__(self)
    
    def atacar(enemigo, self):
        if random.randint(0,100)<prob_cab:
            enemigo.poder = enemigo.poder(1-red_cab/100)
            enemigo.vida =  round(self.ataque*(atq_cab/100) - enemigo.defensa)    
        else:
            self.agilidad -= self.agilidad*(1-cansancio/100)
            enemigo.vida -= round (self.ataque - enemigo.defensa)

    def evolucionar(self):
        pass
    
def Mago(Combatiente):
    def __init__(self, tipo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tipo = "Gato Mago"  
    
    def __str__(self):
        print(f"¡Hola! Soy {self.nombre}, un {self.tipo} con
                   {self.vida}/ {self.vida_maxima} de vida, {self.ataque} de
                     ataque y {self.defensa} de defensa")
    
    def presentarse(self):
        return __str__(self)
    
    def atacar(enemigo, self):
        if random.randint(0,100)<prob_mag:
            enemigo.defensa = round(self.ataque*(atq_mag/100) - enemigo.defensa*(100 - red_mag)/100)    
        else:
            self.agilidad -= self.agilidad*(1-cansancio/100)
            enemigo.vida -= round (self.ataque - enemigo.defensa)
        self.resistencia = self.resistencia*(1-cansancio/100)
        self.agilidad = self.agilidad*(1-cansancio/100)


    def evolucionar(self):
        pass

def Paladin(Guerrero, Caballero):
    def __init__(self, tipo, *args, **kwargs): #revisar??
        super().__init__(*args, **kwargs)
        self.tipo = "Gato Paladin"  
    
    def __str__(self):
        print(f"¡Hola! Soy {self.nombre}, un {self.tipo} con
                   {self.vida}/ {self.vida_maxima} de vida, {self.ataque} de
                     ataque y {self.defensa} de defensa")
    
    def presentarse(self):
        return __str__(self)
    
    def atacar(enemigo, self):
        if random.randint(0,100)<prob_mag:
            enemigo.defensa = round(self.ataque*(atq_mag/100) - enemigo.defensa*(100 - red_mag)/100)    
        else:
            self.agilidad -= self.agilidad*(1-cansancio/100)
            enemigo.vida -= round (self.ataque - enemigo.defensa)
        self.resistencia = self.resistencia*(1-cansancio/100)
        self.agilidad = self.agilidad*(1-cansancio/100)


    def evolucionar(self):
        pass


    

        
    
        

