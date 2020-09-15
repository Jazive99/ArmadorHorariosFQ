# ArmadorHorariosFQ

Autor: José Alberto Cabrera Jaime
Contacto: albertocabja@gmail.com

El código "main.py" tiene como finalidad evaluar todas las posibles combinaciones a partir de una determinada cantidad de asignaturas y grupos. 
Esta serie de instrucciones da por hecho que el usuario sabe cómo correr códigos en lenguaje Python.

=========================
I N S T R U C C I O N E S
=========================

1. Descargar "main.py". El código utiliza las librerías sympy, progress, re, time y logging. Se invita al usuario a verificar que todas las librerías están instaladas antes de hacer uso del código.

2. En la misma carpeta donde se haya guardado "main.py", guardar un archivo llamado "Horarios.txt". Este archivo debe contener:
        2.1 En la primera línea el número de asignaturas que se desea evaluar.
        2.2 En las siguientes líneas, la clave de la i-ésima asignatura y el número de grupos que se evaluar para la misma.
        2.3 En las siguiente líneas, el horario de que tiene el j-ésimo grupo para la i-ésima asignatura. 
        2.4 El horario va en formato de 24 horas sin puntuación, e.g., las 2:30 pm se escribe 1430.
En el repositorio se encuentra un ejemplo de este archivo. Se invita al usuario seguir el ejemplo de "Horario.txt" al pie de la letra para evitar errores. Así mismo, el código podría no funcionar correctamente si el archivo contiene faltas de ortografía o si los días no empiezan en mayúscula.

3. Correr el código "main.py" desde la misma capreta que lo contiene(se recomienda que sea simplemente con el comando "python main.py" o equivalente). El código leerá el archivo "Horarios.txt" y armará un conjunto de posibles combinaciones. En el caso de tener una cantidad gigantesca de combinaciones, podría preguntarse al usuario si desea continuar la operación. Al aceptar, se comenzarán a evaluar las posibles combinaciones, guardando en memoria las que NO tengan ningún traslape. 

4. Cuando el código termine de evaluar, mostrará en pantalla un resumen de la evaluación y preguntará al usuario si desea guardar (en un archivo llamado "Resultados.txt" en la misma carpeta) las combinaciones que no hayan tenido NINGÚN traslape. En el repositorio se encuentra un ejemplo de este archivo.

-------------------
NOTAS Y SUGERENCIAS
-------------------

- El código sólo funciona con asignaturas de 4 dígitos. No leerá 10 ni 00202, en este caso la correción sería 0010 y 0202.

- El código sólo funciona con grupos ordenados. Por ejemplo, si el archivo "Horarios.txt" se guarda con grupos salteados "El grupo 1 tiene [...], El grupo 3 tiene [...], El grupo 5 tiene [...]", el código los lee de manera ordenada como "El grupo 1 tiene [...], El grupo 2 tiene [...], El grupo 3 tiene [...]". Si el usuario quiere utilizar una notación distinta a la de grupos ordenados, se recomienda llevar un control al momento de leer los resultados para evitar confusiones.

- El código solo funciona con horarios que empiezan y terminan en la hora o en la media hora. Por ejemplo, no va a leer la línea "El grupo 1 tiene clases los días Lunes de 1100 a 1245", porque 12:45 no es ni la hora ni media hora. La corrección sería "El grupo 1 tiene clases los días Lunes de 1100 a 1230" o "El grupo 1 tiene clases los días Lunes de 1100 a 1300". 

- Antes de comenzar las evaluaciones, el código preguntará si desea continuar en caso de que el número de combinaciones sea muy grande. En este caso, el tiempo estimado es solamente un ajuste empírico y no está relacionada con la cantidad de operaciones lógicas que conllevan las combinaciones. El tiempo estimado es una guía para que el usuario decida si quiere o no continar la operación.

- El código no funciona con procesamiento en paralelo.

- Se recomienda que el usuario no ejecute la operación si el código estima un tiempo demasiado grande (demasiadas combinaciones posibles). En estos casos, lo que se sugiere es que el usuario modifique la cantidad de grupos para que sean menos las combinaciones posibles.

- Si ya existe un archivo "Resultados.txt" en la misma carpeta de "main.py", el código lo va a sobreescribir. Si el usuario utiliza el código varias veces, se recomienda cambiar el nombre del archivo "Resultados.txt" según convenga.

- En caso de no encontrar ninguna combinación sin tralape, el código simplemente se cerrará sin guardar ningún archivo "Resultados.txt" en la misma carpeta de "main.py".





