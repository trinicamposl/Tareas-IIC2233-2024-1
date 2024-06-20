# Tarea 3: DCCome Lechuga 🐢🍉🥬


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Entidades: 18.5 pts (21%)
##### ❌✅🟠 Pepa
##### ❌✅🟠 Sandías

#### Interfaz gráfica: 27 pts (30%)
##### ❌✅🟠 Ventana Inicio
##### ❌✅🟠 Ventana Juego
##### ❌✅🟠 Fin del *puzzle*

#### Interacción: 13 pts (14%)
##### ❌✅🟠 *Cheatcodes*
##### ❌✅🟠 Sonidos

#### *Networking*: 20.5 pts (23%)
##### ❌✅🟠 Arquitectura
##### ❌✅🟠 *Networking*
##### ❌✅🟠 Codificación y decodifición

#### Archivos: 11 pts (12%)
##### ❌✅🟠 *sprites*
##### ❌✅🟠 *puzzle*
##### ❌✅🟠 JSON
##### ❌✅🟠 parámetros.py


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```archivo.py```. Además se debe crear los siguientes archivos y directorios adicionales:
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