# Tarea 3 :ballot_box:

## Consideraciones generales :octocat:
Mi tarea define _casi_ todas las funciones pedidas de manera eficiente y rápida. Esta tarea fue hecha con mucho esfuerzo búsquedas en google (stackoverflow mi bestie)

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  _```el nombre del archivo con el que testeen las funciones```_. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```funciones.py``` en ```T3```
2. ```data/``` en ```T3``` con todos los archivos que se desean leer, específicados según su tamaño en carpetas dentro de esta carpeta, siendo sus nombres ```s```, ```m``` y ```l``` para achivos pequeños, medianos o grandes respectivamente.

Además tiene que haber un archivo llamado ```utilidad.py``` que contenga las diferentes namedtuples utilizadas a lo largo de la tarea y distintos archivos dentro de la misma.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://www.geeksforgeeks.org/convert-generator-object-to-list-in-python/ para convertir un generador en una lista, lo que utilicé a lo largo de mi tarea para poder iterar de nuevo sobre el generador.
2. https://www.geeksforgeeks.org/handling-missing-keys-python-dictionaries/ para asignar un valor random al acceder a un diccionario con una llave que no está en ese (línea 251) (igual creo que eso está dentro de los contenidos)
3. https://stackoverflow.com/questions/3594514/how-to-find-most-common-elements-of-a-list para obtener la cantidad de repeticiones del elemento más repetido con el método Counter (usé varias veces counter.most_common()[0][1])