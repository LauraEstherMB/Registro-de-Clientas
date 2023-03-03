# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:58:37 2023

@author: SAPTOOLS-X10
"""

import pandas as pd

Tabla = pd.read_excel('Libro1.xlsx')

nombre_clienta = input("¿Cúal es su nombre?").lower()
""""nombre_clienta_conv = nombre_clienta.lower()"""
apellido_clienta = input("¿Cúal es su apellido?").lower()
"""apellido_clienta_conv = apellido_clienta.lower()"""

Tabla_conv_n = Tabla['Nombre'].str.lower()
Tabla_conv_a = Tabla['Apellido'].str.lower()

if (nombre_clienta in Tabla_conv_n.values) and (apellido_clienta in Tabla_conv_a.values):
    indice_n = Tabla_conv_n[Tabla_conv_n == nombre_clienta].index[0]
    indice_a = Tabla_conv_a[Tabla_conv_a == apellido_clienta].index[0]

    buena_n = Tabla.loc[indice_n, 'Buena']
    buena_a = Tabla.loc[indice_a, 'Buena']
    if buena_n == buena_a == 1: 
        print("No es posible coger su cita, contacte con nosotros.")
    elif buena_n != buena_a:
            print ("Necesitas registrarte") 
    else:
        print("¿Para cuando desea su cita?")        
else:
    print("Necesitas registrarte.")
    