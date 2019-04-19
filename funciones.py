#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 18:48:44 2018
Script que recopila algunas de las funciones creadas para este proyecto
@author: edwin
"""



import pandas as pd

def busca_cod(base_1, col_cod='cod'):
    #Función creada para buscar los nombres de las estaciones automáticas o convencionales a partír del código
    #tmp_tabla = busca_cod(tmp_tabla, 'cod')
    #El código de la base a usar debe ser numérico
    base_1[col_cod] = base_1[col_cod].convert_objects(convert_numeric=True)
    lista_estaciones = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/est_usadas_lista.csv')
    lista_estaciones.columns.values[0] = 'cod_1'
    lista_estaciones.columns = lista_estaciones.columns.str.strip()
    lista_estaciones.columns.values[1] = 'Nombre'
    
    name_0 = pd.merge(left=base_1, right=lista_estaciones, 
                    left_on=col_cod, right_on='cod_1', how='left')
    
    return(name_0)
    #busca_cod(tmp_tabla, 'cod')
    
def un_busca_cod(cod=21201200.0):
    aa = (busca_cod(pd.DataFrame({'cod':[cod]}))['Nombre'][0])
    return(aa)
    
    
    

#Función creada para listar los nombres de las tablas
def lista_nombres(base):
        base2 = pd.DataFrame(list(base))
        return(base2)
                

def busca_columna(base, contains):
    #Función creada para buscar el número de la posición de la columna con ciertas letras
    # busca_columna(base=estacion_3, contains='prec') Busca en las columas de estacion_3
    # Las letras prec y devielve una lista [1, 6] con las ubicaciones de las columnas
    lista_base = pd.DataFrame({'a':base.columns.unique()})
    salida = []
    for i in lista_base.a:
        if contains in i:
            salida.append(lista_base[lista_base.a == i].index[0])
    return(salida)

def regresion(mejor, peor, base):
    m = (-1)/(peor - mejor)
    b = -peor*((-1)/(peor-mejor))
    return((base * m) + b)
def regresion(mejor, peor, base):
    m = (-1)/(peor - mejor)
    b = -peor*((-1)/(peor-mejor))
    return((base * m) + b)
#Función para crear las fechas con 2 dígitos usadas una por una
def fechas_un_digito(valor):
    valor = str(valor)
    if len(valor) < 2:
        valor_2 = '0'+valor
        return(valor_2)
    else:
        return(valor)

###Función complementaria usadas para trabajar con una lista
from funciones import fechas_un_digito
def fechas_un_digito_columna(columna):
    base_vacia = []
    columna = columna.tolist()
    for pp in columna:
        base_vacia.append(fechas_un_digito(pp))
    base_vacia_t = pd.DataFrame({'aaa':base_vacia}).reset_index().drop('index', axis = 1)
    return(base_vacia_t)

