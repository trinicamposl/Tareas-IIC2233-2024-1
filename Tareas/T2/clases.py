from parametros import oro_inicial, cansancio, prob_cab, red_cab, atq_cab, prob_mag
from parametros import red_mag,atq_mag, prob_pal, aum_pal, prob_mdb, def_mdb, prob_car, aum_car
from abc import ABC, abstractmethod
import random

class Ejercito():
    def __init__(self):
        self.combatientes = []
        self.oro = oro_inicial
        self.ronda = 1
    
    def combatir(self, enemigo):
        while len(enemigo.combatientes) != 0 or len(self.combatientes) != 0:
            for i in range(len(self.combatientes)):
                jugador = self.combatientes(i)
                contrincante = enemigo.combatiente(i)
                mi_vida = jugador.vida
                su_vida = contrincante.vida
                while mi_vida != 0 or su_vida != 0:
                    jugador.atacar(enemigo, self)
                    contrincante.atacar(self, enemigo)
                    mi_vida = jugador.vida
                    su_vida = contrincante.vida
                if mi_vida == 0:
                  self.combatientes.pop(indice(jugador, self.combatientes))
                if su_vida == 0:
                    enemigo.combatientes.pop(indice(contrincante, enemigo.combatientes))  
                break
        if len(enemigo.combatientes) == 0:
            if len(self.combatientes) != 0: 
                return(True, "Ganaste esta ronda! :D")
            else:
                return(False, "Murieron todos tus gatos. Perdiste el juego D:")       
        else:
                return(False, "Murieron todos tus gatos. Perdiste el juego D:")     

    @property
    def presentarse(self):
        self.__str__()

    def __str__(self):
        print("Este es tu ejército actual:")
        if len(self.combatientes) != 0:
            for combatiente in self.combatientes:
                combatiente.presentarse() # revisar!!
            print(f"Te quedan {len(self.combatientes)} combatientes. ¡Éxito en la batalla!")
        else:
            print("No tienes ningún combatiente. Te recomiendo comprar alguno para la batalla!")
    
    def agregar_ejercito (self, gato):
        self.combatientes.append(gato)                 
class Combatientes(ABC):
    def __init__(self,nombre, vida_maxima, poder, defensa, agilidad, resistencia):
        self.nombre = nombre
        self.vida_maxima = int(vida_maxima)
        self._vida = int(vida_maxima) #revisar
        self.poder = int(poder)
        self.defensa = int(defensa)
        self.agilidad = int(agilidad)
        self.defensa = int(defensa)
        self.resistencia = int(resistencia)
        denominador = self.poder + self.agilidad + self.resistencia
        self.ataque = round((denominador*2*self._vida)/self.vida_maxima)
    
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

class Guerrero(Combatientes):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tipo = "Gato Guerrero"  
    
    def __str__(self):
        f1 = f"Hola! Soy {self.nombre}, un {self.tipo} con {self._vida}/{self.vida_maxima} de vida"
        print(f"{f1}, {self.ataque} de ataque y {self.defensa} de defensa")
    
    def presentarse(self):
        self.__str__()
    
    def atacar(enemigo, self):
        self.agilidad -= self.agilidad*(1-cansancio/100)
        enemigo._vida -= round (self.ataque - enemigo.defensa)

    def evolucionar(self, pieza):
        return Items(pieza).evolucionar_gato(self)

class Caballero(Combatientes):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tipo = "Gato Caballero"  
    
    def __str__(self):
        f1 = f"Hola! Soy {self.nombre}, un {self.tipo} con {self._vida}/{self.vida_maxima} de vida"
        print(f"{f1}, {self.ataque} de ataque y {self.defensa} de defensa")
    
    def presentarse(self):
        self.__str__()
    
    def atacar(enemigo, self):
        if random.randint(0,100)<=prob_cab:
            poder_antiguo = enemigo.poder
            enemigo.poder = enemigo.poder(1-red_cab/100)
            enemigo._vida =  round(self.ataque*(atq_cab/100) - enemigo.defensa)
        else:
            self.agilidad -= self.agilidad*(1-cansancio/100)
            enemigo._vida -= round (self.ataque - enemigo.defensa)

    def evolucionar(self, pieza):
        return Items(pieza).evolucionar_gato(self)
    
class Mago(Combatientes):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tipo = "Gato Mago"  
    
    def __str__(self):
        f1 = f"Hola! Soy {self.nombre}, un {self.tipo} con {self._vida}/{self.vida_maxima} de vida"
        print(f"{f1}, {self.ataque} de ataque y {self.defensa} de defensa")

    def presentarse(self):
        self.__str__()
    
    def atacar(enemigo, self):
        if random.randint(0,100)<=prob_mag:
            enemigo.defensa = round(self.ataque*(atq_mag/100) - enemigo.defensa*(100 - red_mag)/100)    
        else:
            self.agilidad -= self.agilidad*(1-cansancio/100)
            enemigo._vida -= round (self.ataque - enemigo.defensa)
        self.resistencia = self.resistencia*(1-cansancio/100)
        self.agilidad = self.agilidad*(1-cansancio/100)

    def evolucionar(self, pieza):
        return Items(pieza).evolucionar_gato(self)

class Paladin(Guerrero, Caballero):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.tipo = "Gato Paladin"  
    
    def __str__(self):
        f1 = f"Hola! Soy {self.nombre}, un {self.tipo} con {self._vida}/{self.vida_maxima} de vida"
        print(f"{f1}, {self.ataque} de ataque y {self.defensa} de defensa")
    
    def presentarse(self):
        self.__str__()
    
    def atacar(enemigo, self):
        if random.randint(0,100)<=prob_pal:
            Caballero.atacar(enemigo, self)    
        else:
            Guerrero.atacar(enemigo, self)
        self.resistencia = self.resistencia*(1+(aum_pal/100))

    def evolucionar(self):
        print("Yo no puedo evolucionar :(")

class MagoDeBatalla(Guerrero, Mago):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.tipo = "Gato Mago De Batalla"  
    
    def __str__(self):
        f1 = f"Hola! Soy {self.nombre}, un {self.tipo} con {self._vida}/{self.vida_maxima} de vida"
        print(f"{f1}, {self.ataque} de ataque y {self.defensa} de defensa")
    
    def presentarse(self):
        self.__str__()
    
    def atacar(enemigo, self):
        if random.randint(0,100)<=prob_mdb:
            Mago.atacar(enemigo, self)    
        else:
            Guerrero.atacar(enemigo, self)
        self.agilidad = self.agilidad*(1-cansancio/100)
        self.defensa = self.defensa*(1+def_mdb/100)

    def evolucionar(self):
        print("Yo no puedo evolucionar :(")

class CaballeroArcano(Caballero, Mago):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.tipo = "Gato Caballero Arcano"  
    
    def __str__(self):
        f1 = f"Hola! Soy {self.nombre}, un {self.tipo} con {self._vida}/{self.vida_maxima} de vida"
        print(f"{f1}, {self.ataque} de ataque y {self.defensa} de defensa")

    def presentarse(self):
        self.__str__()
    
    def atacar(enemigo, self):
        if random.randint(0,100)<=prob_car:
            Mago.atacar(enemigo, self)
            self.agilidad = self.agilidad*(1-cansancio/100)
            self.defensa = self.defensa*(1+def_mdb/100)    
        else:
            Guerrero.atacar(enemigo, self)
            self.agilidad = self.agilidad*(1-cansancio/100)
            self.defensa = self.defensa*(1+def_mdb/100)

    def evolucionar(self):
        print("Yo no puedo evolucionar :(")

class Items():
    def __init__(self, nombre):
        self.nombre = nombre

    def evolucionar_gato(self, gato):
        if self.nombre == "Pergamino":
            if gato.tipo == "Gato Guerrero":
                nuevo_gato = MagoDeBatalla(*convertir_gato(gato))
                return nuevo_gato            
            elif gato.tipo == "Gato Caballero":
                nuevo_gato = CaballeroArcano(*convertir_gato(gato))
                return nuevo_gato        
        elif self.nombre == "Lanza":
            if gato.tipo == "Gato Mago":
                nuevo_gato = MagoDeBatalla(*convertir_gato(gato))
                return nuevo_gato            
            elif gato.tipo == "Gato Caballero":
                nuevo_gato = Paladin(*convertir_gato(gato))
                return nuevo_gato
            
        elif self.nombre == "Armadura":
            if gato.tipo == "Gato Mago":
                nuevo_gato = CaballeroArcano(*convertir_gato(gato))
                return nuevo_gato            
            elif gato.tipo == "Gato Guerrero":
                nuevo_gato = Paladin(*convertir_gato(gato))
                return nuevo_gato

def convertir_gato(gato):
    """
    Esta funcion me da una lista con datos para poder hacer la clase nueva de manera más eficiente
    """
    nombre = gato.nombre
    vida_maxima = gato.vida_maxima
    poder = gato.poder
    defensa = gato.defensa
    agilidad = gato.agilidad
    resistencia = gato.resistencia
    return [nombre, vida_maxima, poder, defensa, agilidad, resistencia]

def indice(gato, lista):
    for i in range (len(lista)):
        if lista[i].nombre == gato.nombre:
            return i