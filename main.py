'''
main.py
ArmadordeHorarios

Created by Alberto Cabrera on 06/12/18.
Contact: albertocabja@gmail.com

Calcula las posibles combinaciones de grupos sin
traslapes de horarios.
El input es un archivo de texto llamado Horarios.txt
'''

from sympy import FiniteSet
from progress.bar import ChargingBar
import re
import time
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable()

def Espacio_blanco():
    # Definir el espacio de horarios. Definimos el espacio como
    # un diccionario. Automatizar la escritura de esta función
    # con automateEspacio.py y automateEspacio.txt del directorio Try_2

    Espacio = {'Lunes_700' : '' , 'Martes_700' : '' , 'Miércoles_700' : '' , 'Jueves_700' : '' , 'Viernes_700' : '' , 'Sábado_700' : '' ,
               'Lunes_730' : '' , 'Martes_730' : '' , 'Miércoles_730' : '' , 'Jueves_730' : '' , 'Viernes_730' : '' , 'Sábado_730' : '' ,
               'Lunes_800' : '' , 'Martes_800' : '' , 'Miércoles_800' : '' , 'Jueves_800' : '' , 'Viernes_800' : '' , 'Sábado_800' : '' ,
               'Lunes_830' : '' , 'Martes_830' : '' , 'Miércoles_830' : '' , 'Jueves_830' : '' , 'Viernes_830' : '' , 'Sábado_830' : '' ,
               'Lunes_900' : '' , 'Martes_900' : '' , 'Miércoles_900' : '' , 'Jueves_900' : '' , 'Viernes_900' : '' , 'Sábado_900' : '' ,
               'Lunes_930' : '' , 'Martes_930' : '' , 'Miércoles_930' : '' , 'Jueves_930' : '' , 'Viernes_930' : '' , 'Sábado_930' : '' ,
               'Lunes_1000' : '' , 'Martes_1000' : '' , 'Miércoles_1000' : '' , 'Jueves_1000' : '' , 'Viernes_1000' : '' , 'Sábado_1000' : '' ,
               'Lunes_1030' : '' , 'Martes_1030' : '' , 'Miércoles_1030' : '' , 'Jueves_1030' : '' , 'Viernes_1030' : '' , 'Sábado_1030' : '' ,
               'Lunes_1100' : '' , 'Martes_1100' : '' , 'Miércoles_1100' : '' , 'Jueves_1100' : '' , 'Viernes_1100' : '' , 'Sábado_1100' : '' ,
               'Lunes_1130' : '' , 'Martes_1130' : '' , 'Miércoles_1130' : '' , 'Jueves_1130' : '' , 'Viernes_1130' : '' , 'Sábado_1130' : '' ,
               'Lunes_1200' : '' , 'Martes_1200' : '' , 'Miércoles_1200' : '' , 'Jueves_1200' : '' , 'Viernes_1200' : '' , 'Sábado_1200' : '' ,
               'Lunes_1230' : '' , 'Martes_1230' : '' , 'Miércoles_1230' : '' , 'Jueves_1230' : '' , 'Viernes_1230' : '' , 'Sábado_1230' : '' ,
               'Lunes_1300' : '' , 'Martes_1300' : '' , 'Miércoles_1300' : '' , 'Jueves_1300' : '' , 'Viernes_1300' : '' , 'Sábado_1300' : '' ,
               'Lunes_1330' : '' , 'Martes_1330' : '' , 'Miércoles_1330' : '' , 'Jueves_1330' : '' , 'Viernes_1330' : '' , 'Sábado_1330' : '' ,
               'Lunes_1400' : '' , 'Martes_1400' : '' , 'Miércoles_1400' : '' , 'Jueves_1400' : '' , 'Viernes_1400' : '' , 'Sábado_1400' : '' ,
               'Lunes_1430' : '' , 'Martes_1430' : '' , 'Miércoles_1430' : '' , 'Jueves_1430' : '' , 'Viernes_1430' : '' , 'Sábado_1430' : '' ,
               'Lunes_1500' : '' , 'Martes_1500' : '' , 'Miércoles_1500' : '' , 'Jueves_1500' : '' , 'Viernes_1500' : '' , 'Sábado_1500' : '' ,
               'Lunes_1530' : '' , 'Martes_1530' : '' , 'Miércoles_1530' : '' , 'Jueves_1530' : '' , 'Viernes_1530' : '' , 'Sábado_1530' : '' ,
               'Lunes_1600' : '' , 'Martes_1600' : '' , 'Miércoles_1600' : '' , 'Jueves_1600' : '' , 'Viernes_1600' : '' , 'Sábado_1600' : '' ,
               'Lunes_1630' : '' , 'Martes_1630' : '' , 'Miércoles_1630' : '' , 'Jueves_1630' : '' , 'Viernes_1630' : '' , 'Sábado_1630' : '' ,
               'Lunes_1700' : '' , 'Martes_1700' : '' , 'Miércoles_1700' : '' , 'Jueves_1700' : '' , 'Viernes_1700' : '' , 'Sábado_1700' : '' ,
               'Lunes_1730' : '' , 'Martes_1730' : '' , 'Miércoles_1730' : '' , 'Jueves_1730' : '' , 'Viernes_1730' : '' , 'Sábado_1730' : '' ,
               'Lunes_1800' : '' , 'Martes_1800' : '' , 'Miércoles_1800' : '' , 'Jueves_1800' : '' , 'Viernes_1800' : '' , 'Sábado_1800' : '' ,
               'Lunes_1830' : '' , 'Martes_1830' : '' , 'Miércoles_1830' : '' , 'Jueves_1830' : '' , 'Viernes_1830' : '' , 'Sábado_1830' : '' ,
               'Lunes_1900' : '' , 'Martes_1900' : '' , 'Miércoles_1900' : '' , 'Jueves_1900' : '' , 'Viernes_1900' : '' , 'Sábado_1900' : '' ,
               'Lunes_1930' : '' , 'Martes_1930' : '' , 'Miércoles_1930' : '' , 'Jueves_1930' : '' , 'Viernes_1930' : '' , 'Sábado_1930' : '' ,
               'Lunes_2000' : '' , 'Martes_2000' : '' , 'Miércoles_2000' : '' , 'Jueves_2000' : '' , 'Viernes_2000' : '' , 'Sábado_2000' : '' ,
               'Lunes_2030' : '' , 'Martes_2030' : '' , 'Miércoles_2030' : '' , 'Jueves_2030' : '' , 'Viernes_2030' : '' , 'Sábado_2030' : '' ,
               'Lunes_2100' : '' , 'Martes_2100' : '' , 'Miércoles_2100' : '' , 'Jueves_2100' : '' , 'Viernes_2100' : '' , 'Sábado_2100' : '' ,
               'Lunes_2130' : '' , 'Martes_2130' : '' , 'Miércoles_2130' : '' , 'Jueves_2130' : '' , 'Viernes_2130' : '' , 'Sábado_2130' : '' ,
               'Lunes_2200' : '' , 'Martes_2200' : '' , 'Miércoles_2200' : '' , 'Jueves_2200' : '' , 'Viernes_2200' : '' , 'Sábado_2200' : '' }
    return Espacio

def main():

    # Título
    print()
    print('\t\t-------------------')
    print('\t\tArmador de Horarios')
    print('\t\t-------------------\n')

    # Para leer el número de asignaturas de la primera línea
    # para conocer el número de loops
    n_asignaturasRegex = re.compile(r'\d*\d')

    # Para encontrar la parte del texto que dice 'clave 0000'
    claveAuxRegex = re.compile(r'clave\s\d\d\d\d')
    claveRegex = re.compile(r'\d\d\d\d')

    # Para encontrar la parte del texto que dice '00 grupos'
    n_gruposAuxRegex = re.compile(r'\d*\d\sgrupo(s)*')
    n_GruposRegex = re.compile(r'\d*\d')

    # Para encontrar la parte del texto que dice los días
    DíasRegex = re.compile(r'Lunes|Martes|Miércoles|Jueves|Viernes|Sábado')

    # Para encontrar la parte del texto que dice el horario de clase
    HorarioInicioAuxRegex = re.compile(r'de\s\d*\d(3|0)0')
    HorarioFinAuxRegex = re.compile(r'a\s\d*\d(3|0)0')
    HorarioRegex = re.compile(r'\d*\d(3|0)0')

    # Abrir el archivo Horarios.txt
    HorariosFile = open('Horarios.txt')

    # Diccionario para guardar listas de [Grupo, 'Día', 'Horario']
    # de cada Clave_X
    dict_claves1 = {}

    # Diccionario para guardar la clave real de cada Clave_X
    dict_claves2 = {}

    # Diccionario auxiliar para guardar el número de grupos por Clave_X
    # por poder realizar después el producto cartesiano de permutaciones
    dict_claves3 = {}

    # Para ir contando las líneas del texto. Se va sobreescribiendo
    # en los loops para el input, por lo que no será un diccionario de todas
    # líneas del texto al finalizar el programa.
    dict_lines = {}

    # Leer el archivo Horarios.txt línea 1 donde dice n_Asignaturas
    dict_lines['1_line'] = HorariosFile.readline()
    n_asig = n_asignaturasRegex.search(dict_lines['1_line'])

    # Guardar el número de asignaturas
    n_Asignaturas = int(n_asig.group())
    # Activar en caso de querer ver cómo se va leyendo el archivo
    logging.debug('n_Asignaturas = {0}'.format(n_Asignaturas))

    for asignatura in range(n_Asignaturas):
        input1 = []
        # Leer el archivo Horarios.txt línea por línea y asignar a dict_lines
        dict_lines[str(asignatura+1) + 'line'] = HorariosFile.readline()
        ClaveAux = claveAuxRegex.search(dict_lines[str(asignatura+1) + 'line'])
        Clave = claveRegex.search(ClaveAux.group())
        dict_claves2['Clave_' + str(asignatura+1)] = Clave.group()
        # Activar en caso de querer ver cómo se va leyendo el archivo
        logging.debug('Clave {0}'.format(dict_claves2['Clave_' + str(asignatura+1)]))
        
        GruposAux = n_gruposAuxRegex.search(dict_lines[str(asignatura+1) + 'line'])
        n_Grupos = n_GruposRegex.search(GruposAux.group())
        n_Grupos = int(n_Grupos.group())
        # Activar en caso de querer ver cómo se va leyendo el archivo
        logging.debug('Grupos = {0}'.format(n_Grupos))
        dict_claves3['Clave_' + str(asignatura+1)] = n_Grupos

        for grupo in range(n_Grupos):
            dict_lines[str(grupo+1) + 'line'] = HorariosFile.readline()
            
            # Días = lista con elementos de cada día en forma de str
            Días = DíasRegex.findall(dict_lines[str(grupo+1) + 'line'])

            HorarioInicioAux = HorarioInicioAuxRegex.search(dict_lines[str(grupo+1) + 'line'])
            HorarioInicio  = HorarioRegex.search(HorarioInicioAux.group())
            HorarioFinAux = HorarioFinAuxRegex.search(dict_lines[str(grupo+1) + 'line'])
            HorarioFin = HorarioRegex.search(HorarioFinAux.group())
            inicio = int(HorarioInicio.group())
            final = int(HorarioFin.group())

            # Cambiar el formato de *30* en el input de inicio/fin
            # para hacer las restas en segmentos de media hora
            if (inicio - 30) % 50 == 0:
                inicioaux = inicio + 20
            else:
                inicioaux = inicio
            if (final - 30) % 50 == 0:
                finalaux = final + 20
            else:
                finalaux = final
            # segmentos de media hora en el intervalo dado
            segmentos = (finalaux - inicioaux) / 50
            for segmento in range(int(segmentos)):
                # Agregar el *30* a cada segmento
                if segmento % 2 == 0:
                    Horario = segmento*50 + inicio
                else:
                    # Corrección por si el inicio era *30*
                    if (inicio - 30) % 50 == 0:
                        Horario = segmento*50  + inicioaux
                    else:
                        Horario = segmento*50 - 20 + inicio
                    
                for día in range(len(Días)):
                    input2 = [grupo+1, Días[día], str(Horario)]
                    input1.append(input2)
            dict_claves1['Clave_' + str(asignatura+1)] = input1
            
            # Activar en caso de querer ver cómo se va leyendo el archivo
            logging.debug('Grupo {0}. Días = {1}\t Horario: de {2} a {3}'.format(grupo+1, Días, HorarioInicio.group(), HorarioFin.group()))

    # Cerrar el archivo txt
    HorariosFile.close()
    print('Archivo de texto "Horarios.txt" leído.')

    '''
    # Comprobar cómo se guardó la información
    print('\nCHECKPOINT')
    pprint.pprint(dict_claves1)
    pprint.pprint(dict_claves2)
    pprint.pprint(dict_claves3)
    print('\n')
    '''
    
    # Cuántas combinaciones posibles hay?
    # Calcular el tiempo que tomaría calcular ese número de combinaciones
    print('\n')
    n_combinaciones = 1
    for i in range(len(dict_claves3)):
        n_combinaciones = n_combinaciones*dict_claves3['Clave_' + str(i+1)]
    # Tiempo (en segundos) obtenido empíricamente
    tiempo_s = 0.0056*n_combinaciones - 2.1666

    print('El número total de combinaciones posibles es {0}.'.format(n_combinaciones))

    # Si el tiempo es mayor a 60 segundos, será necesario confirmar
    if tiempo_s > 60:
        tiempo = tiempo_s / 60
        if tiempo >= 60:
            tiempo = tiempo / 60
            print('El tiempo estimado para procesar {0} combinaciones es {1:.2f} horas.'.format(n_combinaciones, tiempo))
        else:
            print('El tiempo estimado para procesar {0} combinaciones es {1:.2f} minutos.'.format(n_combinaciones, tiempo))
        cont = input('¿Desea continuar con el procedimiento? (s) para sí ')
        if cont != 's':
            exit()

    print('\n')
    
    # Barra de progreso
    bar = ChargingBar('PROCESANDO', max = n_combinaciones)
    
    # Contar el tiempo que tarda en procesar
    start_time = time.time()
    
    # Checar que no haya traslapes. Para automatizar las combinaciones
    # se utiliza el producto cartesiano de FiniteSet.
    # Guardar la información de dict_claves3 en una lista
    # de listas llamada 'Grupos' para realizar el producto cartesiano
    # y obtener las combinaciones posibles.
    Grupos = []
    for clave in range(len(dict_claves3)):
        aux = list(range(1,dict_claves3['Clave_' + str(clave+1)]+1))
        Grupos.append(aux)

    producto = FiniteSet(*Grupos[0])
    for i in range(len(Grupos)-1):
        producto = producto*FiniteSet(*Grupos[i+1])

    # Transformar 'producto' en lista para leer índices.
    list_prod = list(producto)
    
    # Loop para buscar traslapes ----------------------------------------------
    
    # Lista de combinaciones sin traslape
    list_buena = []
    # Lista de combinaciones con traslape
    traslapes = []

    # Se encarga de cada combinación
    for comb in range(len(list_prod)):
        Espacio = Espacio_blanco()

        # Se encarga de cada elemento en la combinación
        # Es decir, los grupos
        for grupo in range(n_Asignaturas):

            aux = list_prod[comb][grupo]

            # Se encarga de leer en cada elemento del dict_claves1
            # donde dice ese grupo
            for i in range(len(dict_claves1['Clave_' + str(grupo+1)])):
                auxList = []

                try:
                    bol = dict_claves1['Clave_' + str(grupo+1)][i].index(aux)
                    auxList.append(i)
                except ValueError:
                    pass
                
                for j in range(len(auxList)):
                    x = dict_claves1['Clave_' + str(grupo+1)][auxList[j]]

                    # Si ese horario está vacío, se añadirá un 1. Si ya tiene 1,
                    # se añadirá +1
                    if Espacio[x[1] + '_' + x[2]] == '':
                        Espacio[x[1] + '_' + x[2]] = 1
                    else:
                        Espacio[x[1] + '_' + x[2]] += 1

        # Al terminar la combinación, se tiene Espacio con la
        # cantidad de traslapes por celda
        hayTraslape = 0
        for k in range(n_Asignaturas-1):
            # k+2 porque no se cuenta '' ni 1
            if k+2 in Espacio.values():
                hayTraslape += 1
            else:
                pass

        # Añadir a las listas:
        if hayTraslape == 0:
            list_buena.append(list_prod[comb])
            bar.next()
        else:
            traslapes.append(list_prod[comb])
            bar.next()


    # Terminar la barra de progreso
    bar.finish()
    
    print('\n')

    # Mostrar la diferencia entre tiempo estimado y real 
    if tiempo_s > 60:
        logging.info('Tiempo de procesamiento estimado: {0:.2f} minutos.'.format(tiempo))

    tiempo_real_s = (time.time() - start_time)
    tiempo_real_m = tiempo_real_s / 60
    if tiempo_real_m < 1:
        print('Tiempo de procesamiento: {0:.2f} segundos.'.format(tiempo_real_s))
    else:
        print('Tiempo de procesamiento: {0:.2f} minutos.'.format(tiempo_real_m))
    print('Total de combinaciones posibles: {0}'.format(len(list_prod)))
    print('Se encontraron {0} combinaciones sin traslapes.'.format(len(list_buena)))
    print('Se encontraron {0} combinaciones con traslapes.'.format(len(traslapes)))
    print('\n')

    # Si no hay combinaciones sin traslapes, cerrar.
    if len(list_buena) == 0:
        exit()
        
    impr_ans = input('¿Guardar combinaciones sin traslapes? (s) para sí ')
    if impr_ans == 's':
        f = open('Resultados.txt', 'w')
        for i in range(len(list_buena)):
            f.write('Combinación No.{0}\n'.format(i+1))
            f.write('{0:^15}{1:^15}\n'.format('Clave', 'Grupo'))
            for j in range(len(dict_claves1)):
                aux = list_buena[i][j]
                f.write('{0:^15}{1:^15}\n'.format(int(dict_claves2['Clave_' + str(j+1)]), int(aux)))
            f.write('\n')
        f.close()

if __name__=='__main__':
    main()
