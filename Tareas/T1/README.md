# Tarea 1: DCCiudad 🚈🐈


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

Mi código logra (*se supone*) que casi todas las funciones pedidas *funcionen*. La función asegurar_ruta no funciona completamente bien, ya que sólo logra funcionar completamente si es que el número de túneles intermedios es menor a 4, y la situación no es muy rara o un caso borde.


### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

### Parte 1:
#### Automatización: 40 pts (67,3%)

##### ✅ Información Red: 
Conté las estaciones con el largo de la lista de estaciones y recorrí la lista sumando los indices para cada estación para obtener los túneles individuales.

##### ✅ Agregar túnel: 
Cree una función que definía el índice de la estación comparando el string con la posicion en la lista de estaciones y con eso alteré la posición indicada de la lista, transformando el 0 en un 1 si es que no existía el túnel.

##### ✅ Tapar túnel 
Hice lo mismo que agregar el túnel, pero cambié 1´s a 0´s.

##### ✅ Invertir túnel
Cree una función que me definía si existía un túnel entre dos lugares y a partir de eso, separé en las condiciones pedidas por el enunciado y desarrollé, cambiando de ordenes los indices para dar vuelta los túneles.

##### ✅ Nivel conexiones
Utilicé la función que había creado para ver si existía un túnel, sumado con la función elevar_matriz que se nos entregó para obtener si existían caminos con distintos caminos intermedios. Y con eso separé según las condiciones indicadas en el enunciado y retorné lo necesario.

##### ✅ Rutas posibles
Utilicé la función elevar_matriz y la elevé al valor pedido + 1, ya que así se obtenía el valor pedido de estaciones intermedias. Luego saqué el indice de la red, que me indicaba la cantidad de caminos y lo retorné.

##### ✅ Ciclos más cortos
Pasé por todos los número hasta el máximo pedido, con un ```for```, elevando la matriz cada vez y utilizando la función para ver si existía algun túnel, y si es que se terminaba ese rango, entonces no existía una ruta y se retornaba -1.

##### ✅ Estaciones intermedias
Primero tomé todos los caminos que podían salir de la estación pedida y los metí en una lista, y luego recorrí la lista, analizando cuáles de esas estaciones tenían túneles hacia el destino, y nuevamente los metí en una lista, que es la que la función devuelve.


##### ✅ Estaciones intermedias avanzado
Cree una lista con todas las estaciones a las que se podía llegar desde el inicio, y aparte hice una lista de todas las estaciones que podían llegar al destino. Finalmente crucé las dos listas, y obtuve una lista que tenía todas las conexiones intermedias posibles (ya que por un lado salían del inico, entre ellas estaban conectadas, y por el otro lado llegaban al destino)

##### ✅ Cambiar planos
Después de filtrar si el archivo existía o no, abrí la primera linea considerandola como "n" y tomando ese número las siguientes n, para agregarlas a una lista de las estaciones. Luego la última línea le separé las comas, pasé todos los strings a números y los separé en la n listas de n componentes. (esto fue lo que saqué de internet)

##### 🟠 Asegurar rutas
No supe programar las rutas totales que tenía cada estación por lo que sólo logré programar esta función hasta 4 rutas intermedias :(. A pesar de esto, los casos bordes como que la estación llega a si misma, no los puedo resolver.





### Parte 2:
#### Menú: 13 pts (21,7%)
##### ✅ Consola:
De lo que probé yo, todo funcionaba correctamente

##### ✅ Menú de Acciones:
Mis pruebas funcionaron y mi menú fue a base de prints. Hice una función que imprimía lo que no se alteraba del menú (que está en ```funciones.py```) para que el código en ```main.py``` no estuviese tan engorroso.

##### ✅ Modularización:
Separé en distintos archivos para que los archivos principales no estuviesen tan cargados de códigos, creando algunas funciones que se repetían mucho a lo largo de la tarea, cómo sacar el índice de la estación.

##### ✅ PEP8:
*Creo* que logré seguir todo lo pedido. Traté de escribir variables claras, excepto para algunos ```for i in range``` que el *i* no significaba nada específico, sólo que se recorrían números.



## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```funciones.py``` en ```T1```
2. ```red.py``` en ```T1``` (esto no sabía si era necesario explicitarlo)


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```: ```path.join``` y ```path.exists``` 
2. ```sys```: ```argv``` y  ```exit``` 


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```funciones```: Contiene las funciones ```hay_tunel```, ```indice``` e ```imprimir_menu``` e para simplificar el código en ```red.py``` y en ``main.py`` (están explicadas en el archivo)


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:
 
1. Para el desarrollo de la función **nivel_conexiones** asumí que el hecho que se podía o pedía usar la función alcanzable **no implicaba que no se podían usar las demás funciones** de dcciudad, por lo que **usé la función elevar_matriz**
2. Cómo no se explicitaba qué había que hacer con el archivo ```ejemplos.py```, asumí que no era necesario agregarlo al .gitignore, y lo eliminé.
 


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \https://es.stackoverflow.com/questions/134908/dividir-lista-en-lista-de-listas>: este separa listas en listas de igual tamaño, y está implementado en el archivo ```red.py``` en las líneas **136, 137, 138 y 139** y hace que se dividan equitativamente las listas de las rutas cuando se cambian los planos.
