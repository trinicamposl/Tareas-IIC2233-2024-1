# Tarea 3: DCCome Lechuga 🐢🍉🥬


## Consideraciones generales :octocat:

Mi tarea logra presentar un juego fácil de manejar para el usuario, con el mayor esfuerzo que tenga una interfaz _linda_ (no lo logré). Dentro de todo, se modela bien lo pedido, las teclas mueven a Pepa según corresponde y esta no se sale del tablero, sí existen ciertos problemas con _hacer poop_, que si uno presiona G en pleno de un traslado entre celdas, Pepa _hace poop_ en su posición previa al movimiento. Creo que no logré bien la separación de frontend y backend, lo mismo con servidor y cliente y creo que tengo una cantidad absurda e innecesaria de señales, pero mi código funciona (_se supone_). A pesar de que lo intenté, creo que mi tarea no está completamente desacoplada y se podría optimizar mucho más.
Es importante mencionar que le cambié la tipografía de base al juego, a una que mi computador tenía y supongo que viene instalada en pyqt6, en caso de que no funcione por esto, habria que cambiar toda ocurrencia de ```Cascadia Mono SemiBold``` a alguna otra tipografía como comic sans o no sé.


### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores



#### Entidades: 18.5 pts (21%)
##### 🟠 Pepa:
Pepa es modelada pero no tiene una clase individual, sino que se encuentra inmersa dentro del tablero. Esto fue porque cuando intenté crearla fuera, se me habría como una ventana aparte (después caché que podía arreglarlo alterando el _parent_, pero ya era muy tarde para cambiarlo)
##### 🟠 Sandías:
Se genera una sola sandía que se va apareciendo y desapareciendo (esto lo comento en los supuestos); moviendose de manera aleatoria y desapareciendo ya sea porque se acabó el tiempo o porque fue presionada. No supe bien si las sandías estaban apareciendo cada un rango de tiempo constante. Además, no logré escalar las sandías al mismo tamaño de las lechugas en cada partida, por lo que siempre es chiquitita (que creo que hace el juego mejor?)

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
No creo haber entendido perfecto netwirking así que tampoco sé si está perfecto, tampoco sé como comprobar que está bien codificado y decodificado, pero los mensajes se codificaban y decodificaban y llegaban bien. Y creo que ya al final de la tarea, se me empezó a mezclar qué iba en el frontend y qué en el backend.
##### 🟠 Arquitectura
##### 🟠 *Networking*
##### 🟠 Codificación y decodifición

#### Archivos: 11 pts (12%)
##### ✅ *sprites*
##### ✅ *puzzle*
##### 🟠 JSON
En los parámetros del servidor, en el archivo JSON está incluido el path del archivo de puntajes.txt, sin el uso que path.join, que podría generar un problema.
##### ✅ parámetros.py


## Ejecución :computer:
Los módulo principales de la tarea a ejecutar son  ```main.py```, tanto de la carpeta ```servidor``` como la carpeta ```cliente```. Además se debe crear los siguientes archivos y directorios adicionales:

### En ```/servidor```
1. ```puntajes.txt```
2. ```parametros.json```
3. ```funciones_servidor.py```
4. ```main.py```

Además obviamente, de la carpeta ```/assets```, que debe contener la carpeta ```/solucion_puzzles```, y dentro de esta, las soluciones de los puzzles en formato txt.

### En ```/cliente```
1. La carpeta ```\frontend``` que contiene los archivos  ```Tablero.py``` y ```VentanaDeInicio.py```
2. La carpeta ```\backend``` que contiene los archivos  ```backend.py``` y ```parametros.json```
Y los archivos:
3. ```funciones.py```
4. ```parametros.py```
5. ```copia.txt```
6. ```main.py```

Además obviamente, de la carpeta ```/assets```, que debe contener las carpetas ```/sprites```, ```/sonidos``` y ```/base_puzzles```, cada una con sus archivos respectivos.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```json```: ```parametros.json``` para cumplir con lo pedido y tener el host
2. ```pickle```: ```main.py``` del servidor y ```backend.py``` del cliente, para transformar en bytes y destransformar(?)
3. ```os```: ```parametros.py`` para que los paths relativos funcionaran en cualquier dispositivo
4. ```sys```: en varias partes, para manejar el fin del programa
5. ```pyqt6```: principalmente en ```VentanaDeInicio.py```y ```Tablero.py```, para manejar interfaz gráfica, uso de timers, locks, etc. (incluyendo Qt, Qt.Core, Qt.Gui, etc.)

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```VentanaDeInicio```: Contiene a ```VentanaInicio```, ```PopUp```
2. ```Tablero```: Contiene a ```Tablero```, ```Sandia``` y ```Timer```
3. ```funciones``` y ```funciones_servidor``` contienen diversas funciones útiles para simplificar código en los archivos principales

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Asumí que el tiempo de duración de la sandía en pantalla siempre sería menor al de aparición, por lo que nunca habría más de una sola sandía a la vez. Esto no lo vi en ninguna issue, ni se mencionaba en el enunciado
2. Asumí que se podía tener un archivo que guardara los puntajes también en el cliente, que copiaba linea por linea el archivo de puntajes.txt a partir del servidor. Esto tampoco se prohibía en el enunciado.
3. ...

PD: perdón por el desorden del código, fue una semana con muchas pruebas, controles y tareas y no logré ordenarlo.


-------




## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. Tomé el archivo ```servidor.py``` de la experiencia 4 como base para el archivo de mi propio servidor así también el archivo ```frontend.py``` y ```backend.py``` de la actividad como 3 como base de mi archivos presentes en las carpetas de los mismos nombres
2. https://www.pythonguis.com/tutorials/pyqt6-qscrollarea/: este hace crea un área _scrolleable?_ y está implementado en el archivo ```frontend.py``` y hace que funcione como se debe el Salón de la Fama
3. https://python-forum.io/thread-37323.html: este código fue mi base para crear el timer en el juego, igual fue alterado en el proceso pero de este código empecé.
4. https://github.com/tomastrivino/iic2233-2023-1/blob/main/T3/cliente/Scripts/encoding.py: este código, fue base para codificar y decodificar los mensajes que se enviaban entre servidor y cliente, también como guía entre los mismos, más concretamente con las funciones ```codificar``` y ```decodificar``` de ```funciones.py``` y ```funciones_servidor.py```
5. https://www.pythonguis.com/tutorials/pyqt6-dialogs/: este ayuda a la creación de los distintos popups, presentes ```VentanaDeInicio.py``` y ```Tablero.py```

## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/main/Tareas/Bases%20Generales%20de%20Tareas%20-%20IIC2233.pdf).