# Tarea 2: DCCombatientes 🐈⚔️

Bienvenid@ a mi tarea! :D. La hice con mucho cariño y estrés jajajaj

## Consideraciones generales :octocat:
Mi tarea logra modelar de manera linda los menús, comprar gatos y evolucionarlos. En cuanto al combate en sí, y logra modelar los combates, pero por alguna razón me quedaron los parámetros muy dificiles entonces hay tuve que aumentar el oro inicial para poder ganar.

Cabe destacar que me costó mucho entender la tarea y me tinca que hay cosas que están mal diseñadas en el código porque no entendí bien cómo se hacían como el tema del ataque y el combate en general, y además no sabía como revisar si estaban bien definidas las clases y los métodos asi que puede que por ahí hayan cosas malas.

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

#### Programación Orientada a Objetos: 12 pts (10%)
##### 🟠 Definición de clases, herencia y *properties*
Usé tanto herencia, como clases y properties aunque no sé si logré definir bien algunas properties como la vida, que me creo algunos problemas

#### Preparación del programa: 10 pts (8%)
##### ✅ Inicio de la partida:
Según lo que probé, está a prueba de errores. Eso sí tuve unos problemas con los path asi que no sé si funcionan de manera correcta :/. El usuario tiene que comenzar corriendo el archivo main de la manera que se haga en su pc (py, python, python3) y agregar el parametro de la dificultad, siendo "facil", "intermedio" o "dificil".

#### Entidades: 56 pts (47%)
##### ✅ Ejército:
Definí un ejercito inicialmente vacío, con la capacidad de agregar combatienes al mismo y con una cantidad de oro (que se va gastando/ganando) y la ronda actual del juego. También es capaz de imprimir el ejército actual que tiene, y en caso de no tener, también avisa esto.

##### 🟠 Combatientes:
Desde lo que probé, todo salía bien. Son la clase padre de los tipos de combatientes, y usan properties para controlar los valores que tienen que estar en rangos, y metodos abstractos para aquellos métodos que cambiaban según la clase, como la forma de atacar. No sé si realmente se descuentan los ataques como se debería, pero porque no sabía cómo revisar esto, pero cada clase sí logra presentarse, sobreescribiendo ´__str__´

##### 🟠 Ítems:
No sé si cumple con exactamente con lo que me pedían, pero es una clase hecha y derecha.

#### Flujo del programa: 30 pts (25%)
##### ✅ Menú de Inicio:
Creo que dentro de todo igual me quedó decente, y no logré romper el código asi que creo que es a prueba de fallas del usario.
##### ✅ Menú Tienda:
Incluye los precios, importados desde parametros.py para evitar hardcoding. Y según yo también estaba a prueba de fallas del usuario
##### ✅ Selección de gato:
Se puede comprar un gato, y este se agrega al ejército y además se descuenta su valor. Si es para evolucionarlo, únicamente aparecen los gatos acordes al tipo de objeto usado
##### 🟠 Fin del Juego:
Si es que se gana la ronda 3, se termina el juego y así también se "sale" de la terminal, y si uno pierde, vuelve a comenzar el juego, con la cantidad de oro inicial y un ejercito vacío
##### ✅ Robustez:
Hasta donde yo sé, el juego es capaz de detectar todo tipo de errores y avisa al jugador (de manera un poco pasivo agresiva) que intente de nuevo.

#### Archivos: 12 pts (10%)
##### ✅ Archivos .txt
##### ✅ parametros.py
No tuve problemas para importar ninguno de estos archivos. Eso sí, cuando el archivo de unidades está incorrecto, avisa cuando intenta comprar el gato, es decir, igual muestra el menú de tienda, pero al momento de comprar el gato, tira un error y cierra el programa


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```clases.py``` en ```T2```
2. ```funciones.py``` en ```T2```
3. ```momento_compras.py``` en ```T2```
4. ```juego.py``` en ```T2```
5. ```parametros.py``` en ```T2```
**además tiene que haber un archivo llamado ```unidades.txt``` (de texto) para poder importar los gatos que se pueden comprar dentro de la carpeta data/ y los distintos archivos para las dificultades dentro de esta misma carpeta en el formato ```"dificultad_escogida".txt```**


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```abc```: básicamente para herencia y métodos abstractos (```ABC``` y ```abstractmethod```)
2. ```os```: para el control de los parámetros por consola y para terminar el juego (```exit()``` y ```args```)
3. ```random```: para casos aleatorios y el uso de probabilidades (principalmente ```random.randint()```)

### Librerías propias :pencil2:
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```clases.py```: Contiene todas las clases creadas, incluyendo herencia, polimorfismo (creo), properties y clases abstractas. Contiene clases como  ```Ejercito```, ```Items```, ```Guerrero```, entre otras (contiene una función que no logré ponerla en otro archivo sin crear problemas para importar archivos entre sí.)

2. ```funciones```: Hecha para facilitar y limpiar un poco los códigos, tiene funciones que se tenía que utilizar mucho y ocupaban muchas líneas, como ```revisar_parametros```, ```revisar_unidades```, etc. (Las funciones suelen ser autoexplicativas con el nombre, sino tienen una pequeña descripción)

3. ```momento compras```: Contiene sólo el método para la compra de artículos y combatientes en la función ```comprar()```

4. ```juego```: Contiene la una función que se concentra en el inicio del juego y deriva al módulo ```momento compras``` en el caso de que el jugador quiera comprar cosas.

5. ```parametros```: contiene todos los parámetros necesarios para evitar _Hard Coding_

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Consideré que para la compra de combatientes, **_el stock era ilimitado_**, pero al evolucionar algun gato que esté repetido, sólo se evolucionaría el primero que aparezca en la lista de combatientes con el nombre del que se quiere evolucionar. Esto lo hice tomando como base la **issue #176**, donde se habla un poco de la interpretación de esta situación.

2. Asumí que **_activar un poder_** significaba **_atacar como el poder activado_**, es decir, si activo mi poder como guerrero, ataco como guerrero, incluyendo todas las implicancias que tiene el ataque del guerrero. Se habla de esto en la **issue #171**

3. Asumí que en las clases mixtas como ```Paladín``` y ```Mago De Batalla```, en el caso que no se cumpliera la probabilidad especificada en el enunciado, el combatiente atacaba como la otra clase padre. (por ejemplo en el paladin cuando no se cumplía la probabilidad de paladín para atacar como Caballero, entonces atacaba como Guerrero). Esto también se habla en la **issue #171**

4. Asumí que en el ataque, **_atacaba primero el jugador_**, teniendo cierta ventaja sobre el oponente, debido a que esto no se explicita en la tarea (y así era más fácil). Esto se ahonda en la **issue #243** 

5. Asumí que los **_ataques a los stats del otro jugador eran permanentes_** (así era más fácil), ya que no se explicita en la tarea si es que son para el 1v1 o si son por siempre. Esto se habla en la **issue #248**

6. Asumí que el archivo con las unidades siempre se iba a llamar unidades.txt (no sé si esto salía en el enunciado pero no lo leí en ninguna issue)
PD: Mi computador murió como por 6 días del periodo de la tarea asi que porfa ten piedadddd :pensive:


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>

## Descuentos

La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/main/Tareas/Bases%20Generales%20de%20Tareas%20-%20IIC2233.pdf).