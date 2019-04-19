#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 08:52:18 2019
Extracción de los mejores resultados de las simulaciones
@author: edwin

Se va sólo a buscar para el caso 200702 y luego se va a probar con las demás
"""

################plots par realizar los plots de a 5
    
##Plot de los diferentes domínios

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import pdb
    
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
for j in ['200702', '201509', '201408', '201508']:
    #'200702', 
#for j in ['200702', '201509', '201408']:
    #j = '201408'
    j = str(j)
    #print(j)

    recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_'+j+'.csv')       
    recep_t = recep_t.sort_values('suma_esc', ascending=False)
#    recep_t = recep_t[recep_t.tipo_1 != 'ideam-mejor']
#    recep_t = recep_t[recep_t.dom_1 == 'd02']
    
    if j == '201408':
        recep_t.tipo_1 = recep_t.tipo_1.str[2:]
        recep_t = recep_t[recep_t.tipo_1 != 'ideam-mejor']
    
    for i in recep_t.cod_1.unique():
        if (j == '201408'):
            if (i in [21206980.0, 35025080.0, 35035130.0]): # Se descarta estas estaciones porque los datos de la estación ya que posee pocos valores. 
                # /media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_temp_simulaciones <-- Acá están las gráficas
                # /media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/comparacion_grafica <-- Acá están las gráficas
                print('Caso 2')
                continue
        
        #if (j == '201508'):
        #    if (i in [21201200.0, 21205791.0, 21205012.0, 21206920.0, 35035130.0]):
        #        print('Caso 3')
        #        continue
        #    
        #if (j == '201509'):
        #    if (i in [21206920.0, 21206980.0, 35035130.0]):
        #        print('Caso 4')
        #        continue
            
        #i = 21206950.0
        para_t1 = recep_t[(recep_t.r2 > 0.8) & (recep_t.rmse < 0.3)  & (recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
        #if para_t1.std_pura.mean() < 3:
        #    continue
        
        
        
        for coun, uu in enumerate([0]): #enumerate(range(0, (len(para_t1) //5) +2)):
            #coun = 0; uu = 0
            print(coun, uu)
            para_t = para_t1.iloc[(5*uu):((5*uu)+ 5),:]
            #print(para_t)
            
            #para_t = para_t.sort_values(['tipo_1','dom_1'])
            para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
            
            para_t['orden'] = para_t.tipo_1.str[-2:]
            
            ###
            
            para_t['cod'] = str(i)[0:8]
            para_t['simula'] = j
            
            base_1 = base_1.append(para_t[['simula','cod', 'tipo_1', 'dom_1']])
            
#pdb.set_trace()
#base_1.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/mejores5simulaciones_condicional.csv')
#base_1.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/mejores5simulaciones_3.csv')
### El resultado de las parametrizaciones más adecuadas sin tener en cuenta la optimización (mejores) se encuentra en el 
## archivo '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/mejores5simulaciones_4.csv'
#base_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/mejores5simulaciones.csv')
#base_con4 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/mejores5simulaciones_2.csv')


#base_con1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/mejores5simulaciones_condicional.csv')

print(pd.crosstab(base_1.tipo_1, columns='count').to_latex())
