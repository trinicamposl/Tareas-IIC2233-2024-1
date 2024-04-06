from abc import ABC, abstractmethod
import random


class Vehiculo(ABC):
    identificador = 0
    def __init__(self, rendimiento, marca, energia = 120)-> None:
        self.rendimiento = int(rendimiento)
        self.marca = marca
        self._energia = max(0,energia)
        self.identificador = Vehiculo.identificador
        Vehiculo.identificador += 1

    @abstractmethod
    def recorrer (self,kilometros) -> None:
        pass

    @property
    def autonomia(self) -> float:
        return self._energia * self.rendimiento
    
    
    @property
    def energia(self) -> int:
        return self._energia

    @energia.setter
    def energia (self, numero):
        if numero <= 0:
            self._energia = 0
        else:
            self._energia = int(numero)
        

class AutoBencina(Vehiculo):
    def __init__ (self, bencina_favorita, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.bencina_favorita = bencina_favorita

    def recorrer(self, kilometros):
        recorrido = min(self.autonomia, kilometros)
        gasto = recorrido/self.rendimiento
        self._energia -= gasto
        return f"Anduve por {recorrido}Km y gaste {int(gasto)}L de bencina"    
    

class AutoElectrico(Vehiculo):
    def __init__ (self, *args, vida_util_bateria, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.vida_util_bateria = vida_util_bateria

    def recorrer(self, kilometros):
        recorrido = min(self.autonomia, kilometros)
        gasto = recorrido/self.rendimiento
        self._energia -= gasto
        return f"Anduve por {recorrido}Km y gaste {int(gasto)}W de energia electrica"  


class Camioneta(AutoBencina):
    def __init__ (self, *args, capacidad_maleta, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.capacidad_maleta = capacidad_maleta

        
        

class Telsa(AutoElectrico):
    def recorrer(self, kilometros) -> str:
        texto = super().recorrer(kilometros)
        texto_final = texto + " de forma inteligente"
        return texto_final

class FaitHibrido(AutoBencina, AutoElectrico):
    def __init__(self, rendimiento, marca, energia, bencina_favorita, **kwargs):
        super().__init__(rendimiento = rendimiento, marca = marca, energia = energia,
                          bencina_favorita = bencina_favorita,
                          vida_util_bateria = 5, **kwargs)

    def recorrer(self, kilometros) -> str:
        texto_1 = AutoBencina.recorrer(self, (kilometros/2))
        texto_2 = AutoElectrico.recorrer(self, (kilometros/2))
        return texto_1 + " " + texto_2
