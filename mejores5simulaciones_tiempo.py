#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Jan 17 08:52:18 2019
Creado para la extracción de los tiempos finales finales de veras
Extracción de las simulaciones teniendo en cuenta las mejores simulaciones extraídas de las mejores combinaciones.
@author: edwin
"""

################plots par realizar los plots de a 5
    
##Plot de los diferentes domínios

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import pdb
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam')
from funciones import busca_cod
from funciones import un_busca_cod

    
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_200702.csv')       
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#
##Se usa para hacer el remplazo de los nombres
#recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
#recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
#recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
#recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
#recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
#21206980


base_1 = pd.DataFrame()
#for j in ['200702']:
#for j in ['200702', '201408', '201508', '201509']:
for j in ['200702', '201509', '201408']:
    #j = '200702'
    #j = '201408'
    #j = '201508'
    #j = '201408'
    j = str(j)
    #print(j)
    
    

    recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/tiempo_'+j+'.csv')
    
    #recep_t.tipo_1.unique()

    
    recep_t = recep_t.sort_values('suma_esc', ascending=False)
    #Esta parte comentariada se hizo para poder hacer un conteo y unas listas de las estaciones que se usaron para cada uno de los casos
    #recep_t = recep_t[recep_t.tipo_1 != 'ideam-mejor']
    #recep_t = recep_t[recep_t.dom_1 == 'd02']
    #lista = pd.DataFrame({'cod':recep_t[-np.isnan(recep_t.rmse_esc)].cod_1.unique()})
    #print(len(lista))
    #ista.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/estaciones_usadas_year'+j+'.csv')
    
    
#    if j == '201408':
#        recep_t.tipo_1 = recep_t.tipo_1.str[2:]
#        #recep_t = recep_t[recep_t.tipo_1 != 'ideam-mejor']
    
    for i in recep_t.cod_1.unique():
        if i == 35085080:
            continue
#        if (j == '201408'):
#            pass
#            if (i in [21206980.0, 35025080]):
#                #print('Hola '+str(i))
#                continue
        #i = 21206950.0
        #print(i)
        #para_t1 = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
        #db.set_trace()
        para_t1 = recep_t[(recep_t.r2 > 0.8) & (recep_t.rmse < 0.3)  & (recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
        
        
        
        for coun, uu in enumerate([0]): #enumerate(range(0, (len(para_t1) //5) +2)):
            #coun = 0; uu = 0
            #print(coun, uu)
            para_t = para_t1.iloc[(5*uu):((5*uu)+ 5),:]
            #print(para_t)

            ###Usado para poder sacar las tablas para la profe
            if len(recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())]) > 10:
                print(j, '&', un_busca_cod(i), '&',len(para_t))
            
            #para_t = para_t.sort_values(['tipo_1','dom_1'])
            para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
            
            para_t['orden'] = para_t.tipo_1.str[-2:]
            
            ###
            
            para_t['cod'] = str(i)[0:8]
            para_t['simula'] = j
            
            base_1 = base_1.append(para_t[['simula','cod', 'tipo_1', 'dom_1']])
            
#pdb.set_trace()

 # Esta es la base que viene de usar "las mejores combinaciones" la finalidad de esto fué probar si las mejores parametrizaciones reflejan un mejor resultado           
base_1.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/mejores5simulaciones_20190221.csv')

base_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/mejores5simulaciones_20190221.csv')


print(pd.crosstab(base_1.tipo_1, columns='count').to_latex())
