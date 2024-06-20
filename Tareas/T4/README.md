# Tarea 3: DCCome Lechuga 🐢🍉🥬


## Consideraciones generales :octocat:

Mi tarea logra presentar un juego fácil de manejar para el usuario, con el mayor esfuerzo que tenga una interfaz _linda_ (no lo logré). Dentro de todo, se modela bien lo pedido, las teclas mueven a Pepa según corresponde y esta no se sale del tablero, sí existen ciertos problemas con _hacer poop_, que si uno presiona G en pleno de un traslado entre celdas, Pepa _hace poop_ en su posición previa al movimiento. Creo que no logré bien la separación de frontend y backend, lo mismo con servidor y cliente y creo que tengo una cantidad absurda e innecesaria de señales, pero mi código funciona (_se supone_). Es importante mencionar que le cambié la tipografía de base al juego, a una que mi computador tenía y supongo que viene instalada en pyqt6, en caso de que no funcione por esto, habria que cambiar toda ocurrencia de ```Cascadia Mono SemiBold``` a alguna otra tipografía como comic sans o no sé. 


### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores



#### Entidades: 18.5 pts (21%)
##### 🟠 Pepa:
Pepa es modelada pero no tiene una clase individual, sino que se encuentra inmersa dentro del tablero. Esto fue porque cuando intenté crearla fuera, se me habría como una ventana aparte (después caché que podía arreglarlo alterando el _parent_, pero ya era muy tarde para cambiarlo)
##### 🟠 Sandías:
Se genera una sola sandía que se va apareciendo y desapareciendo (esto lo comento en los supuestos); moviendose de manera aleatoria y desapareciendo ya sea porque se acabó el tiempo o porque fue presionada. No supe bien si las sandías estaban apareciendo cada un rango de tiempo constante.

#### Interfaz gráfica: 27 pts (30%)
##### ✅ Ventana Inicio
Se genera una ventana de inicio con los requisitos, que se actualiza automáticamente el salón de la fama después de ganar una partida.
##### 🟠 Ventana Juego
Nunca logré que el tablero me quedara exactamente cuadrado pero lo demás debería estar bien.
##### ✅ Fin del *puzzle*
Se avisa en caso de acertar o perder el puzzle, así también el caso en que se acaba el tiempo, y se vuelve a la ventana de inicio actualizada.

#### Interacción: 13 pts (14%)
##### 🟠 *Cheatcodes*
Los cheatcodes se activan pero sólo pueden ser activados cuando está presente el tablero y no la ventana de inicio.

##### ✅ Sonidos
Se debería escuchar todo tipo de sonido, a menos que durante la partida el jugar haya activado el cheatcode _MUTE_

#### *Networking*: 20.5 pts (23%)
##### ❌✅🟠 Arquitectura
##### ❌✅🟠 *Networking*
##### ❌✅🟠 Codificación y decodifición

#### Archivos: 11 pts (12%)
##### ✅ *sprites*
##### ✅ *puzzle*
##### ✅ JSON
##### ✅ parámetros.py


## Ejecución :computer:
Los módulo principales de la tarea a ejecutar son  ```main.py```, tanto de la carpeta ```servidor``` como la carpeta ```cliente```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```archivo.ext``` en ```ubicación```
2. ```directorio``` en ```ubicación```
3. ...


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```librería_1```: ```función() / módulo```
2. ```librería_2```: ```función() / módulo``` (debe instalarse)
3. ...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```librería_1```: Contiene a ```ClaseA```, ```ClaseB```, (ser general, tampoco es necesario especificar cada una)...
2. ```librería_2```: Hecha para <insertar descripción **breve** de lo que hace o qué contiene>
3. ...

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. Tomé el archivo ```servidor.py``` de la experiencia 4 como base para el archivo de mi propio servidor así también el archivo ```frontend.py``` y ```backend.py``` de la actividad como 3 como base de mi archivos del mismo nombre.
2. https://www.pythonguis.com/tutorials/pyqt6-qscrollarea/: este hace crea un área _scrolleable?_ y está implementado en el archivo ```frontend.py``` y hace que funcione como se debe el Salón de la Fama
3. https://python-forum.io/thread-37323.html: este código fue mi base para crear el timer en el juego, igual fue alterado en el proceso pero de este código empecé.
4. https://github.com/tomastrivino/iic2233-2023-1/blob/main/T3/cliente/Scripts/encoding.py: este código, fue base para codificar y decodificar los mensajes que se enviaban entre servidor y cliente, también como guía entre los mismos.
5. https://www.pythonguis.com/tutorials/pyqt6-dialogs/: este ayuda a la creación de los distintos popups

## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/main/Tareas/Bases%20Generales%20de%20Tareas%20-%20IIC2233.pdf).