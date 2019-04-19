#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 21:48:59 2018

@author: edwin
"""
################ Diagrama de Taylor para los diferentes domínios


import pandas as pd
import os
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam')
import numpy as np
import matplotlib.pyplot as PLT
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam')
from taylor_diagram_mod import diagrama_taylor
import pdb


# Ojo ejecutar el comando taylor_diagrama.py
#'/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem_20181124_con_correccion.csv'
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem_20181124_con_correccion.csv')
recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem_20181124_con_correccion_2.csv')       
recep_t.head()
pdb.set_trace()
#recep_t =recep_t[(recep_t.r2 > 0.8) & (recep_t.rmse < 0.3)]
recep_t =recep_t[(recep_t.rmse < 0.3)]
#
##Se usa para hacer el remplazo de los nombres
#recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
#recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
#recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
#recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
#recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
#21206980
for i in recep_t.cod_1.unique():
    print(i)
    para_t = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
    para_t['orden'] = para_t.tipo_1.str[-2:]
    para_t = para_t.sort_values(['orden', 'tipo_1'])
    para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
    if len(para_t) < 2:
        continue
    PLT.rcParams["figure.figsize"] = (8,5)
    diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
                    para_t.std_pura.iloc[0], # se toma la desviación estándar real
                    '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
    
    
    PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/taylor_mod/taylor_'+ str(i)[:-2]+'.png', dpi = 100)
    PLT.close()

#recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura', 'suma_esc']]

################################################################################
#    #Creado para la realización de los diagramas de taylor de el tiempo
#
#
#for k in ['200702', '201408', '201508', '201509']:
#    print(k)
#
#    tabla_ej1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/tiempo_'+k+'.csv') 
#
##tabla_ej1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_tiempo_20190204.csv')  
#
##tabla_ej1.columns.values[1] = 'cod_1'
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
#                        '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#        
#    
#        PLT.rcParams["figure.figsize"] = (13,8)
#        PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_tiempos_casos/'+ str(i)[:-2]+k+'.png', dpi = 100)
#        PLT.close()
#    
#

#################
#################plots par realizar los plots de a 5
#    
###Plot de los diferentes domínios
#
#    
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem_20181124_con_correccion_2.csv')       
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    #i = 21206950.
#    para_t1 = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    
#    
#    
#    for coun, uu in enumerate(range(0, (len(para_t1) //5) +2)):
#        #print(coun, uu)
#        #coun = 0 ; uu = 0
#        para_t = para_t1.iloc[(5*uu):((5*uu)+ 5),:]
#        #para_t = para_t1.iloc[0:2, :]
#        #print(para_t)
#        
#        #para_t = para_t.sort_values(['tipo_1','dom_1'])
#        para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#        
#        para_t['orden'] = para_t.tipo_1.str[-2:]
#        para_t = para_t.sort_values(['orden', 'tipo_1'])
#        
#        if len(para_t) < 2:
#            continue
#        PLT.rcParams["figure.figsize"] = (8,5)
#        diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                        para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                        '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#        
#        
#        PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/graficas_taylor_dom_div/taylor_'+str(coun)+'_'+ str(i)[:-2]+'.png', dpi = 100)
#        PLT.close()
#
#recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura', 'suma_esc']]
#
#################################################################################
#    #Creado para la realización de los diagramas de taylor de el tiempo
#
#
#tabla_ej1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_tiempo_20190204.csv')
#tabla_ej1 = tabla_ej1.sort_values('suma_esc', ascending=False)
##tabla_ej1.columns.values[1] = 'cod_1'
#tabla_ej1 = tabla_ej1.reset_index()
#
#for i in tabla_ej1.cod_1.unique():
#    print(i)
#    para_t1 = tabla_ej1[(tabla_ej1.cod_1 == int(i)) & (-tabla_ej1.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    
#    
#    
#    for coun, uu in enumerate(range(0, (len(para_t1) //5) +2)):
#        #print(coun, uu)
#        para_t = para_t1.iloc[(5*uu):((5*uu)+ 5),:]
#        #print(para_t)
#        
#        para_t['orden'] = para_t.tipo_1.str[-2:]
#        para_t = para_t.sort_values(['orden', 'tipo_1'])
#        para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#        if len(para_t) < 2:
#            continue
#        PLT.rcParams["figure.figsize"] = (8,5)
#        diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                        para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                        '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#        
#        
#        
#        PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_taylor_tmp_div/taylor_'+str(coun)+'_'+ str(i)[:-2]+'.png', dpi = 100)
#        PLT.close()
#
#
#
#
#
#
#############################################################################
##        
##        Realización de los digramas de Taylor para las diferentes simulaciones
#############################################################################
#############################################################################        
#        
#                # 2007
#                
#############################################################################
############################################################################# 
#
#import pandas as pd
#import os
#import numpy as np
#import matplotlib.pyplot as PLT
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam')
#from taylor_diagram_mod import diagrama_taylor
#
## Ojo ejecutar el comando taylor_diagrama.py
##'/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem_20181124_con_correccion.csv'
##recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem_20181124_con_correccion.csv')
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_200702.csv')       
##recep_t2 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem_20181124_con_correccion_tmp.csv')
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#recep_t = recep_t[recep_t.r2 > 0]
#recep_t = recep_t.reset_index()
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    para_t = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    para_t['orden'] = para_t.tipo_1
#    para_t = para_t.sort_values(['orden', 'tipo_1'])
#    para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#    if len(para_t) < 2:
#        continue
#    PLT.rcParams["figure.figsize"] = (8,5)
#    diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                    para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                    '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#    
#    
#    PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/200702_m/taylor_'+ str(i)[:-2]+'.png', dpi = 100)
#    PLT.close()
#
#
#################plots par realizar los plots de a 5
#    
###Plot de los diferentes domínios
#
#    
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_200702.csv')       
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#recep_t = recep_t[recep_t.r2 > 0]
#recep_t = recep_t.reset_index()
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    para_t1 = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    
#    
#    
#    for coun, uu in enumerate(range(0, (len(para_t1) //5) +2)):#zip([0], [0]):#
#        print(coun, uu)
#        para_t = para_t1.iloc[(5*uu):((5*uu)+ 5),:]
#        #print(para_t)
#        
#        #para_t = para_t.sort_values(['tipo_1','dom_1'])
#        para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#        
#        para_t['orden'] = para_t.tipo_1.str[-2:]
#        para_t = para_t.sort_values(['orden', 'tipo_1'])
#        
#        if len(para_t) < 2:
#            continue
#        PLT.rcParams["figure.figsize"] = (8,5)
#        diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                        para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                        '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#        
#        
#        PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/200702_5_m/taylor_'+str(coun)+'_'+ str(i)[:-2]+'.png', dpi = 100)
#        PLT.close()
#
#
####################################################################
####################################################################     
#        #### 201509
####################################################################        
####################################################################        
#        
#
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_201509.csv')       
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#recep_t = recep_t[recep_t.r2 > 0]
#recep_t = recep_t.reset_index()
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    para_t = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    para_t['orden'] = para_t.tipo_1
#    para_t = para_t.sort_values(['orden', 'tipo_1'])
#    para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#    if len(para_t) < 2:
#        continue
#    
#    diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                    para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                    '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#    PLT.rcParams["figure.figsize"] = (8,5)
#    
#    PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201509_m/taylor_'+ str(i)[:-2]+'.png', dpi = 100)
#    PLT.close()
#    
#os.system('spd-say "11111111111111111111111111111"')
#
#
#################plots par realizar los plots de a 5
#    
###Plot de los diferentes domínios
#
#    
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_201509.csv')       
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#recep_t = recep_t[recep_t.r2 > 0]
#recep_t = recep_t.reset_index()
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    para_t1 = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    
#    
#    
#    for coun, uu in enumerate(range(0, (len(para_t1) //5) +2)):
#        print(coun, uu)
#        para_t = para_t1.iloc[(5*uu):((5*uu)+ 5),:]
#        #print(para_t)
#        
#        #para_t = para_t.sort_values(['tipo_1','dom_1'])
#        para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#        
#        para_t['orden'] = para_t.tipo_1.str[-2:]
#        para_t = para_t.sort_values(['orden', 'tipo_1'])
#        
#        if len(para_t) < 2:
#            continue
#        PLT.rcParams["figure.figsize"] = (8,5)
#        diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                        para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                        '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#        
#        
#        PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201509_5_m/taylor_'+str(coun)+'_'+ str(i)[:-2]+'.png', dpi = 100)
#        PLT.close()
#    
#os.system('spd-say "22222222222222222222222"')
#
#
####################################################################
####################################################################     
#        #### 201408
####################################################################        
####################################################################        
#        
#
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_201408.csv')       
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#recep_t = recep_t[recep_t.r2 > 0]
#recep_t = recep_t.reset_index()
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    para_t = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    para_t['orden'] = para_t.tipo_1
#    para_t = para_t.sort_values(['orden', 'tipo_1'])
#    para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#    if len(para_t) < 2:
#        continue
#    PLT.rcParams["figure.figsize"] = (8,5)
#    diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                    para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                    '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#    
#    
#    PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201408_m/taylor_'+ str(i)[:-2]+'.png', dpi = 100)
#    PLT.close()
#
#os.system('spd-say "3333333333333333333333"')
#################plots par realizar los plots de a 5
#    
###Plot de los diferentes domínios
#
#    
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_201408.csv')       
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#recep_t = recep_t[recep_t.r2 > 0]
#recep_t = recep_t.reset_index()
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    para_t1 = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    
#    
#    
#    for coun, uu in enumerate(range(0, (len(para_t1) //5) +2)):
#        print(coun, uu)
#        para_t = para_t1.iloc[(5*uu):((5*uu)+ 5),:]
#        #print(para_t)
#        
#        #para_t = para_t.sort_values(['tipo_1','dom_1'])
#        para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#        
#        para_t['orden'] = para_t.tipo_1.str[-2:]
#        para_t = para_t.sort_values(['orden', 'tipo_1'])
#        
#        if len(para_t) < 2:
#            continue
#        PLT.rcParams["figure.figsize"] = (8,5)
#        diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                        para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                        '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#        
#        
#        PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201408_5_m/taylor_'+str(coun)+'_'+ str(i)[:-2]+'.png', dpi = 100)
#        PLT.close()
#
#os.system('spd-say "44444444444444444444"')
#
#
#
####################################################################
####################################################################     
#        #### 201508
####################################################################        
####################################################################        
#        
#
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_201508.csv')       
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#recep_t = recep_t[recep_t.r2 > 0]
#recep_t = recep_t.reset_index()
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    para_t = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    para_t['orden'] = para_t.tipo_1
#    para_t = para_t.sort_values(['orden', 'tipo_1'])
#    para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#    if len(para_t) < 2:
#        continue
#    PLT.rcParams["figure.figsize"] = (8,5)
#    diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                    para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                    '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#    
#    
#    PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201508_m/taylor_'+ str(i)[:-2]+'.png', dpi = 100)
#    PLT.close()
#
#os.system('spd-say "55555555555555555555555555"')
#################plots par realizar los plots de a 5
#    
###Plot de los diferentes domínios
#
#    
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_201508.csv')       
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#recep_t = recep_t[recep_t.r2 > 0]
#recep_t = recep_t.reset_index()
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    para_t1 = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    
#    
#    
#    for coun, uu in enumerate(range(0, (len(para_t1) //5) +2)):
#        print(coun, uu)
#        para_t = para_t1.iloc[(5*uu):((5*uu)+ 5),:]
#        #print(para_t)
#        
#        #para_t = para_t.sort_values(['tipo_1','dom_1'])
#        para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#        
#        para_t['orden'] = para_t.tipo_1.str[-2:]
#        para_t = para_t.sort_values(['orden', 'tipo_1'])
#        
#        if len(para_t) < 2:
#            continue
#        PLT.rcParams["figure.figsize"] = (8,5)
#        diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                        para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                        '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#        
#        
#        PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201508_5_m/taylor_'+str(coun)+'_'+ str(i)[:-2]+'.png', dpi = 100)
#        PLT.close()
#
#os.system('spd-say "666666666666666"')
#
#
#
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
#
#
#
#
#
#############################################################################
##        
##        Realización de los digramas de Taylor para las diferentes simulaciones con los casos llamados mejores
#############################################################################
#############################################################################        
#        
#                # 2007
#                
#############################################################################
############################################################################# 
#
#import pandas as pd
#import os
#import numpy as np
#import matplotlib.pyplot as PLT
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam')
#from taylor_diagram_mod import diagrama_taylor
#
## Ojo ejecutar el comando taylor_diagrama.py
##'/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem_20181124_con_correccion.csv'
##recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem_20181124_con_correccion.csv')
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_mejor_200702.csv')       
##recep_t2 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem_20181124_con_correccion_tmp.csv')
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#recep_t = recep_t[recep_t.r2 > 0]
#recep_t = recep_t.reset_index()
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    para_t = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    para_t['orden'] = para_t.tipo_1
#    para_t = para_t.sort_values(['orden', 'tipo_1'])
#    para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#    if len(para_t) < 2:
#        continue
#    PLT.rcParams["figure.figsize"] = (8,5)
#    diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                    para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                    '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#    
#    
#    PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones_mejor/200702_m/taylor_'+ str(i)[:-2]+'.png', dpi = 100)
#    PLT.close()
#
#
#################plots par realizar los plots de a 5
#    
###Plot de los diferentes domínios
#
#    
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_mejor_200702.csv')       
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#recep_t = recep_t[recep_t.r2 > 0]
#recep_t = recep_t.reset_index()
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    para_t1 = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    
#    
#    
#    for coun, uu in enumerate(range(0, (len(para_t1) //5) +2)):#zip([0], [0]):#
#        print(coun, uu)
#        para_t = para_t1.iloc[(5*uu):((5*uu)+ 5),:]
#        #print(para_t)
#        
#        #para_t = para_t.sort_values(['tipo_1','dom_1'])
#        para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#        
#        para_t['orden'] = para_t.tipo_1.str[-2:]
#        para_t = para_t.sort_values(['orden', 'tipo_1'])
#        
#        if len(para_t) < 2:
#            continue
#        PLT.rcParams["figure.figsize"] = (8,5)
#        diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                        para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                        '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#        
#        
#        PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones_mejor/200702_5_m/taylor_'+str(coun)+'_'+ str(i)[:-2]+'.png', dpi = 100)
#        PLT.close()
#
#
####################################################################
####################################################################     
#        #### 201509
####################################################################        
####################################################################        
#        
#
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_mejor_201509.csv')       
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#recep_t = recep_t[recep_t.r2 > 0]
#recep_t = recep_t.reset_index()
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    para_t = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    para_t['orden'] = para_t.tipo_1
#    para_t = para_t.sort_values(['orden', 'tipo_1'])
#    para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#    if len(para_t) < 2:
#        continue
#    
#    diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                    para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                    '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#    PLT.rcParams["figure.figsize"] = (8,5)
#    
#    PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones_mejor/201509_m/taylor_'+ str(i)[:-2]+'.png', dpi = 100)
#    PLT.close()
#    
#os.system('spd-say "11111111111111111111111111111"')
#
#
#################plots par realizar los plots de a 5
#    
###Plot de los diferentes domínios
#
#    
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_mejor_201509.csv')       
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#recep_t = recep_t[recep_t.r2 > 0]
#recep_t = recep_t.reset_index()
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    para_t1 = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    
#    
#    
#    for coun, uu in enumerate(range(0, (len(para_t1) //5) +2)):
#        print(coun, uu)
#        para_t = para_t1.iloc[(5*uu):((5*uu)+ 5),:]
#        #print(para_t)
#        
#        #para_t = para_t.sort_values(['tipo_1','dom_1'])
#        para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#        
#        para_t['orden'] = para_t.tipo_1.str[-2:]
#        para_t = para_t.sort_values(['orden', 'tipo_1'])
#        
#        if len(para_t) < 2:
#            continue
#        PLT.rcParams["figure.figsize"] = (8,5)
#        diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                        para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                        '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#        
#        
#        PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones_mejor/201509_5_m/taylor_'+str(coun)+'_'+ str(i)[:-2]+'.png', dpi = 100)
#        PLT.close()
#    
#os.system('spd-say "22222222222222222222222"')
#
#
####################################################################
####################################################################     
#        #### 201408
####################################################################        
####################################################################        
#        
#
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_mejor_201408.csv')       
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#recep_t = recep_t[recep_t.r2 > 0]
#recep_t = recep_t.reset_index()
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    para_t = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    para_t['orden'] = para_t.tipo_1
#    para_t = para_t.sort_values(['orden', 'tipo_1'])
#    para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#    if len(para_t) < 2:
#        continue
#    PLT.rcParams["figure.figsize"] = (8,5)
#    diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                    para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                    '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#    
#    
#    PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones_mejor/201408_m/taylor_'+ str(i)[:-2]+'.png', dpi = 100)
#    PLT.close()
#
#os.system('spd-say "3333333333333333333333"')
#################plots par realizar los plots de a 5
#    
###Plot de los diferentes domínios
#
#    
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_mejor_201408.csv')       
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#recep_t = recep_t[recep_t.r2 > 0]
#recep_t = recep_t.reset_index()
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    para_t1 = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    
#    
#    
#    for coun, uu in enumerate(range(0, (len(para_t1) //5) +2)):
#        print(coun, uu)
#        para_t = para_t1.iloc[(5*uu):((5*uu)+ 5),:]
#        #print(para_t)
#        
#        #para_t = para_t.sort_values(['tipo_1','dom_1'])
#        para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#        
#        para_t['orden'] = para_t.tipo_1.str[-2:]
#        para_t = para_t.sort_values(['orden', 'tipo_1'])
#        
#        if len(para_t) < 2:
#            continue
#        PLT.rcParams["figure.figsize"] = (8,5)
#        diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                        para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                        '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#        
#        
#        PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones_mejor/201408_5_m/taylor_'+str(coun)+'_'+ str(i)[:-2]+'.png', dpi = 100)
#        PLT.close()
#
#os.system('spd-say "44444444444444444444"')
#
#
#
####################################################################
####################################################################     
#        #### 201508
####################################################################        
####################################################################        
#        
#
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_mejor_201508.csv')       
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#recep_t = recep_t[recep_t.r2 > 0]
#recep_t = recep_t.reset_index()
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    para_t = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    para_t['orden'] = para_t.tipo_1
#    para_t = para_t.sort_values(['orden', 'tipo_1'])
#    para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#    if len(para_t) < 2:
#        continue
#    PLT.rcParams["figure.figsize"] = (8,5)
#    diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                    para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                    '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#    
#    
#    PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones_mejor/201508_m/taylor_'+ str(i)[:-2]+'.png', dpi = 100)
#    PLT.close()
#
#os.system('spd-say "55555555555555555555555555"')
#################plots par realizar los plots de a 5
#    
###Plot de los diferentes domínios
#
#    
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_mejor_201508.csv')       
#recep_t = recep_t.sort_values('suma_esc', ascending=False)
#recep_t = recep_t[recep_t.r2 > 0]
#recep_t = recep_t.reset_index()
##
###Se usa para hacer el remplazo de los nombres
##recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
##recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
##recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
##recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
##recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
##21206980
#for i in recep_t.cod_1.unique():
#    print(i)
#    para_t1 = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
#    
#    
#    
#    for coun, uu in enumerate(range(0, (len(para_t1) //5) +2)):
#        print(coun, uu)
#        para_t = para_t1.iloc[(5*uu):((5*uu)+ 5),:]
#        #print(para_t)
#        
#        #para_t = para_t.sort_values(['tipo_1','dom_1'])
#        para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
#        
#        para_t['orden'] = para_t.tipo_1.str[-2:]
#        para_t = para_t.sort_values(['orden', 'tipo_1'])
#        
#        if len(para_t) < 2:
#            continue
#        PLT.rcParams["figure.figsize"] = (8,5)
#        diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                        para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                        '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
#        
#        
#        PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones_mejor/201508_5_m/taylor_'+str(coun)+'_'+ str(i)[:-2]+'.png', dpi = 100)
#        PLT.close()
#
#os.system('spd-say "666666666666666"')
#
