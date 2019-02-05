#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Lectura y Escritura de Datos entre Arduino y PC
Utilización de Lector RFID-RC522, Arduino UNO R3
Fecha:27-01-2019
Desarrollador: Pablo Escobar
pabloiinfpuna@gmail.com
Club de Informática FP-UNA
python 3.5
'''

import serial
import time 
import sys

'''
	1.Configura el puerto Serial
	2.Espera hasta que se ingrese un valor válido
	3.Almacena el valor de la lectura de la tarjeta RFID en un archivo txt con fecha y hora
	4.Retorna el valor obtenido de la lectura de la tarjeta
'''
class ControlArduino:
   
    def __init__(self):
        pass

    def conexion_arduino_serial(self):
        '''
            ESTA FUNCIÓN SE ENCARGA DE REALIZAR LA CONECCIÓN ENTRE LA COMPUTADORA Y EL ARDUINO
            POR PUERTO SERIAL 
        '''
        global arduino 
        try:
            arduino = serial.Serial('COM3',baudrate=9600, timeout=1.0)
        except serial.serialutil.SerialException as e:
            print("\nNO SE PUEDE CONECTAR AL PUERTO COM3 O NO EXISTE CONECCIÓN ")
            sys.exit(1)
        

    def lectura_arduino_serial(self):
        '''
            ESTA FUNCIÓN SE ENCARGA DE LA LECTURA DEL PUERTO SERIAL DEL ARDUINO
            Y EXTRAE EL IDENTIFICADOR DE LA TARJETA RFID. RETORNA EL IDENTIFICADOR.
            OBS. COMO HISTORIAL ALMACENA LA LECTURA DE LA COMPUTADORA DEL PUERTO SERIAL
            CON FECHA Y HORA

        '''
        try:		
            #Variable para saber la cantidad de elementos leido de una tarjeta RFID
            longitud = 0 
            ###PROCESO DE LECTURA###
            while longitud<=0:
                try:
                    #Realizo la lectura del puerto serial
                    line = arduino.readline()
                    #Extraigo el UID de la tarjeta, para luego procesarla
                    uid = line.decode('ascii',errors='replace')
                    longitud=len(uid)-2
                    #print(uid,end='')
                except KeyboardInterrupt: ###En caso de presionar ctrl+c 
                    print("Cerrando...")
                    break
            ###PROCESO DE ALMACENAR EL UID LEIDO EN UN ARCHIVO "Historial.txt" CON FECHA Y HORA###
            if longitud!=0:
                f=open('historial_lectura.txt','a')
                if f is None:
                    print("\nNo se pudo abrir el archivo Historial")
                else:
                    f.write("Tiempo : "+time.strftime("%c")+" - UID : "+uid)
                    #print("\nSe almacenó Correctamente los datos en el Archivo historial")
                    f.close()
            #Retorno el uid leido 
            return uid[:-2]
        except serial.serialutil.SerialException as e:
            print('No puede realizar la lectura de la tarjeta\nNo existe comunicación Serial!\n')
            sys.exit(1)
 
    def escritura_arduino_serial(self,comando):           
        '''
            ESTA FUNCIÓN SE ENCARGA DE  ENVIAR TODA LA INFORMACIÓN 
            NECESARIA AL ARDUINO POR PUERTO SERIAL 
        '''
        time.sleep(1.5) 
        arduino.write(comando)
        #FALTA EL PROCESO DE DEFINIR QUE INFORMACIÓN ESPECÍFICA QUIERO PASARLE

    def proceso_conexion_lectura(self):
        ###PROCESO DE CONEXIÓN CON EL ARDUINO Y FUNCIONES
        ''' 
            conexion_arduino_serial()  --- Conexión entre computadora y arduino
            lectura_arduino_serial()   --- Lectura del RFID (retorna el ID de la tarjeta)
            escritura_arduino_serial() --- Escribe en el arduino
        '''
        print("POR FAVOR... COLOQUE SU TARJETA POR EL LECTOR RFID!!! ")
        self.conexion_arduino_serial()
        uid_encontrado=self.lectura_arduino_serial()
        print("LECTURA: "+uid_encontrado)