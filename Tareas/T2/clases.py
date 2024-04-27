from parametros import ORO_INICIAL, CANSANCIO, PROB_CAR, RED_CAB, ATQ_CAB, PROB_MAG
from parametros import RED_MAG,ATQ_MAG, PROB_PAL, AUM_PAL, PROB_MDB, DEF_MDB, PROB_CAR, AUM_CAR
from abc import ABC, abstractmethod
import random

class Ejercito():
    def __init__(self):
        self.combatientes = []
        self.oro = ORO_INICIAL
        self.ronda = 1
    
    def combatir(self, enemigo):
        while len(enemigo.combatientes) != 0 or len(self.combatientes) != 0:
            for i in range(len(self.combatientes)):
                jugador = self.combatientes[i]
                contrincante = enemigo.combatientes[i]
                mi_vida = jugador._vida
                su_vida = contrincante._vida
                while mi_vida != 0 and su_vida != 0:
                    jugador.atacar(contrincante)
                    texto = f"{jugador.nombre} ha atacado a {contrincante.nombre} dejandolo con "
                    texto_2 = f"{contrincante._vida} de vida"
                    print(texto + texto_2)
                    contrincante.atacar(jugador)
                    texto = f"{contrincante.nombre} ha atacado a {jugador.nombre} dejandolo con"
                    print(texto + f"  {jugador._vida} de vida")
                    mi_vida = jugador._vida
                    su_vida = contrincante._vida
                    if mi_vida == 0:
                        self.combatientes.pop(indice(jugador, self.combatientes))
                    if su_vida == 0:
                        enemigo.combatientes.pop(indice(contrincante, enemigo.combatientes))  
                        break
        if len(enemigo.combatientes) == 0:
            if len(self.combatientes) != 0:
                self.ronda+=1 
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
    def __init__(self, nombre, vida_maxima, poder, defensa, agilidad, resistencia):
        self.nombre = nombre
        self._vida_maxima = int(vida_maxima)
        self._vida = int(vida_maxima) #revisar
        self._poder = int(poder)
        self._defensa = int(defensa)
        self._agilidad = int(agilidad)
        self._resistencia = int(resistencia)
        denominador = self._poder + self._agilidad + self._resistencia
        self.ataque = round((denominador*2*self._vida)/self._vida_maxima)
    
    @property
    def curarse(self):
        return self._vida
    
    @curarse.setter
    def curarse(self, cantidad):
        self._vida = min(self._vida + cantidad, self._vida_maxima)
        self._vida = max(self._vida, 0)

    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, cantidad):
        self._vida = min(cantidad, self._vida_maxima)
        self._vida = max(self._vida, 0)

    @property
    def vida_maxima(self):
        return self._vida_maxima
    
    @vida_maxima.setter
    def vida_maxima(self, cantidad):
        self._vida_maxima = min(cantidad, 100)
        self._vida_maxima = max(cantidad, 0)
    
    @property
    def poder(self):
        return self._poder
    
    @poder.setter
    def poder(self, cantidad):
        self._poder = min(cantidad, 10)
        self._poder = max(cantidad, 1)

    @property
    def defensa(self):
        return self._defensa
    
    @defensa.setter
    def defensa(self, cantidad):
        self._defensa = min(cantidad, 20)
        self._defensa = max(cantidad, 1)
    
    @property
    def agilidad(self):
        return self._agilidad
    
    @agilidad.setter
    def agilidad(self, cantidad):
        self._agilidad = min(cantidad, 10)
        self._agilidad = max(cantidad, 1)
    @abstractmethod
    def presentarse(self):
        pass
 
    @abstractmethod
    def atacar(self, enemigo):
        pass

    @abstractmethod
    def evolucionar(self):
        pass

class Guerrero(Combatientes):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tipo = "Gato Guerrero"  
    
    def __str__(self):
        f1 = f"Hola! Soy {self.nombre}, un {self.tipo} con {self._vida}/{self._vida_maxima} de vida"
        print(f"{f1}, {self.ataque} de ataque y {self._defensa} de defensa")
    
    def presentarse(self):
        self.__str__()
    
    def atacar(self, enemigo):
        self._agilidad -= self._agilidad*(1-CANSANCIO/100)
        enemigo._vida -= round(self.ataque - enemigo._defensa)

    def evolucionar(self, pieza):
        return Items(pieza).evolucionar_gato(self)

class Caballero(Combatientes):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tipo = "Gato Caballero"  
    
    def __str__(self):
        f1 = f"Hola! Soy {self.nombre}, un {self.tipo} con {self._vida}/{self._vida_maxima} de vida"
        print(f"{f1}, {self.ataque} de ataque y {self._defensa} de defensa")
    
    def presentarse(self):
        self.__str__()
    
    def atacar(self, enemigo):
        if random.randint(0,100)<=PROB_CAR:
            enemigo._poder = enemigo._poder*(1-RED_CAB/100)
            enemigo._vida = round(self.ataque*(ATQ_CAB/100) - enemigo._defensa)
        else:
            self._agilidad -= self._agilidad*(1-CANSANCIO/100)
            enemigo._vida -= round(self.ataque - enemigo._defensa)

    def evolucionar(self, pieza):
        return Items(pieza).evolucionar_gato(self)
    
class Mago(Combatientes):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tipo = "Gato Mago"  
    
    def __str__(self):
        f = f"Hola! Soy {self.nombre}, un {self.tipo} con {self._vida}/{self._vida_maxima} de vida"
        print(f"{f}, {self.ataque} de ataque y {self._defensa} de defensa")

    def presentarse(self):
        self.__str__()
    
    def atacar(self, enemigo):
        if random.randint(0,100)<=PROB_MAG:
            enemigo._defensa = round(self.ataque*(ATQ_MAG/100)-enemigo._defensa*(100 - RED_MAG)/100)    
        else:
            self._agilidad -= self._agilidad*(1-CANSANCIO/100)
            enemigo._vida -= round(self.ataque - enemigo._defensa)
        self._resistencia = self._resistencia*(1-CANSANCIO/100)
        self._agilidad = self._agilidad*(1-CANSANCIO/100)

    def evolucionar(self, pieza):
        return Items(pieza).evolucionar_gato(self)

class Paladin(Guerrero, Caballero):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.tipo = "Gato Paladin"  
    
    def __str__(self):
        f1 = f"Hola! Soy {self.nombre}, un {self.tipo} con {self._vida}/{self._vida_maxima} de vida"
        print(f"{f1}, {self.ataque} de ataque y {self._defensa} de defensa")
    
    def presentarse(self):
        self.__str__()
    
    def atacar(self ,enemigo):
        if random.randint(0,100)<=PROB_PAL:
            Caballero.atacar(self, enemigo)    
        else:
            Guerrero.atacar(self, enemigo)
        self._resistencia = self._resistencia*(1+(AUM_PAL/100))

    def evolucionar(self):
        print("Yo no puedo evolucionar :(")

class MagoDeBatalla(Guerrero, Mago):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.tipo = "Gato Mago De Batalla"  
    
    def __str__(self):
        f1 = f"Hola! Soy {self.nombre}, un {self.tipo} con {self._vida}/{self._vida_maxima} de vida"
        print(f"{f1}, {self.ataque} de ataque y {self._defensa} de defensa")
    
    def presentarse(self):
        self.__str__()
    
    def atacar(enemigo, self):
        if random.randint(0,100)<=PROB_MDB:
            Mago.atacar(enemigo, self)    
        else:
            Guerrero.atacar(enemigo, self)
        self._agilidad = self._agilidad*(1-CANSANCIO/100)
        self._defensa = self._defensa*(1+DEF_MDB/100)

    def evolucionar(self):
        print("Yo no puedo evolucionar :(")

class CaballeroArcano(Caballero, Mago):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.tipo = "Gato Caballero Arcano"  
    
    def __str__(self):
        f1 = f"Hola! Soy {self.nombre}, un {self.tipo} con {self._vida}/{self._vida_maxima} de vida"
        print(f"{f1}, {self.ataque} de ataque y {self._defensa} de defensa")

    def presentarse(self):
        self.__str__()
    
    def atacar(enemigo, self):
        if random.randint(0,100)<=PROB_CAR:
            Mago.atacar(enemigo, self)
            self._agilidad = self._agilidad*(1-CANSANCIO/100)
            self._defensa = self._defensa*(1+DEF_MDB/100)    
        else:
            Guerrero.atacar(enemigo, self)
            self._agilidad = self._agilidad*(1-CANSANCIO/100)
            self._defensa = self._defensa*(1+DEF_MDB/100)

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
    vida_maxima = gato._vida_maxima
    poder = gato._poder
    defensa = gato._defensa
    agilidad = gato._agilidad
    resistencia = gato._resistencia
    return [nombre, vida_maxima, poder, defensa, agilidad, resistencia]

def indice(gato, lista):
    for i in range (len(lista)):
        if lista[i].nombre == gato.nombre:
            return i