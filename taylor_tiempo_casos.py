##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Thu Feb 21 18:41:12 2019
#Creado para hacer los diagramas de Taylor para la escogencia de los tiempos
#@author: edwin
#"""
#import pandas as pd
#import os
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam')
#import numpy as np
#import matplotlib.pyplot as plt
#from taylor_diagram import diagrama_taylor
#import matplotlib.pyplot as PLT
#
#    #Creado para la realización de los diagramas de taylor de el tiempo
#
#for j in ['200702', '201408', '201508', '201509']:
##for j in ['200702', '201509', '201408']:
#    #j = '200702'
#    #j = '201408'
#    #j = '201508'
#    #j = '201408'
#    j = str(j)
#    print(j)
#    
#    
#
#    tabla_ej1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/tiempo_'+j+'.csv')
#    
#    
#    
#    #tabla_ej1.columns.values[1] = 'cod_1'
#    tabla_ej1 = tabla_ej1.reset_index()
#    
#    for i in tabla_ej1.cod_1.unique():
#        print(i)
#        #######i = 35085080.0
#        
#        para_t = tabla_ej1[(tabla_ej1.cod_1 == i) & (-tabla_ej1.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura', 'std_1_esc']]
#        para_t['orden'] = para_t.tipo_1.str[-2:]
#        para_t = para_t.sort_values(['orden', 'tipo_1'])
#        para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#        if len(para_t) < 2:
#            continue
#        #PLT.rcParams["figure.figsize"] = (13,8)
#        diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                        para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                        '  ')# Se toma el código
#        
#    
#        PLT.rcParams["figure.figsize"] = (13,8)
#        PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_taylor_tiempo_casos/taylor_'+j+ str(i)[:-2]+'.png', dpi = 100)
#        PLT.close()
#        
#        


################## Para Latex
import pandas as pd
import os
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam')
from funciones import busca_cod
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_taylor_tiempo_casos')
lista_1 = os.listdir()
lista_1 = pd.DataFrame({'archi':lista_1})
lista_1['anno_1'] = lista_1.archi.str[7:13]
lista_1['cod'] = lista_1.archi.str[13:21]

lista_1 = lista_1.sort_values(['anno_1', 'cod'], ascending=[True, True])



lista_1 = lista_1.reset_index()
lista_1 = lista_1.drop('index', axis=1)

lista_2 = busca_cod(lista_1)

#lista_2 = lista_2.sort_values(['simu','cod'])

lista_6 = []
for ff in range(1, 100):
    entrada = 6*ff
    lista_6.append(entrada)

textwidth = 0.4
scale = 0.25

lista_2.anno_1 = lista_2.anno_1.replace('200702', 'caso 1')
lista_2.anno_1 = lista_2.anno_1.replace('201408', 'caso 2')
lista_2.anno_1 = lista_2.anno_1.replace('201508', 'caso 3')
lista_2.anno_1 = lista_2.anno_1.replace('201509', 'caso 4')

f = open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_taylor_tiempo_casos.csv','w')

with open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_taylor_tiempo_casos.csv','w') as f:##Usado para crear un archivo que reciba todas los comandos y se guarden en una hoja


        
    for ix,  (cod_1,nombre_1, archi_1, caso) in enumerate(zip(lista_2.cod, lista_2.Nombre, lista_2.archi, lista_2.anno_1)):   
        #print(cod_1,nombre_1, archi_1, caso)
    
    
    
        print('\\begin{subfigure}[normla]{'+str(textwidth)+'\\textwidth}', file =f)
        print('\includegraphics[draft=false, scale='+str(scale)+']{graficas_taylor_tiempo_casos/'+archi_1+'}', file =f)
        print('\caption{'+'Estación '+nombre_1+' código '+str(cod_1)+' '+str(caso)+'.}', file =f)# Las líneas negras representan el período de tiempo entre el 31 de enero del 2007 y el 03 de febrero del 2007.}')
        #print('\label{gra:papa_cund_2}	')
        print('\end{subfigure}', file =f)
        print('~', file =f)
        
        if (ix+1) in lista_6:
            #print(ix)
            print('\end{figure}', file =f)
            print('           ', file =f)
            print('\\begin{figure}[H]\ContinuedFloat', file =f)
            print('\centering', file =f)