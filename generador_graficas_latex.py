#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:03:43 2018
Código creado para hacer las gráficas de los anexos
@author: edwin
"""
import os
import pandas as pd
import numpy as np
import pdb
from funciones import busca_cod
##Función para crear gráficas en Latex
#
#
#
#def graph_anex(direc, direc_latex, caption = '', str_i=7, str_f=15, textwidth = 0.4, scale = 0.5):
#    
#    #Función creada para crear la parte interna de las gráficas en latex
#    #direc = dirección de los archivos
#    # Direc_latex = dirección de latex ej. taylor/grap_1.png
#    #Caption = Lo que va a ir escrito en cada una de las gráficas pequeñas
#    # str_de_nombre = Ubicación del código dentro del nombre de cada una de las gráficas
#    # textwidth = ancho del nombre de cada subgráfica
#    # scale_1 = escala de cada imágen
#    
#    lista_estaciones = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/est_usadas_lista.csv')
#    lista_estaciones.columns.values[0] = 'cod_1'
#    lista_estaciones.columns = lista_estaciones.columns.str.strip()
#    
#    #Creado para usar sólo los valores que sean múltiplos de 6
#    
#        
#    lista_6 = []
#    for ff in range(1, 100):
#        entrada = 6*ff
#        lista_6.append(entrada)
#    
#    os.chdir(direc)
#    lista_1 = os.listdir()
#
#    for ix,ii in enumerate(lista_1):
#        #print(ii, ix)
#        
#        j = lista_estaciones[lista_estaciones.cod_1 == int(ii[str_i:str_f])].iloc[0][1]
#        kk = lista_estaciones[lista_estaciones.cod_1 == int(ii[str_i:str_f])].iloc[0][0]
#    
#        #print('\centering')
#        print('\\begin{subfigure}[normla]{'+str(textwidth)+'\\textwidth}')
#        print('\includegraphics[draft=false, scale='+str(scale)+']{'+str(direc_latex+ii)+'}')
#        print('\caption{'+str(caption)+'Estación '+str(j)+' código '+str(kk)+'.}')# Las líneas negras representan el período de tiempo entre el 31 de enero del 2007 y el 03 de febrero del 2007.}')
#        #print('\label{gra:papa_cund_2}	')
#        print('\end{subfigure}')
#        print('~')
#        
#        if (ix+1) in lista_6:
#            #print(ix)
#            print('\end{figure}')
#            print('           ')
#            print('\\begin{figure}[H]\ContinuedFloat')
#            print('\centering')

    
#graph_anex(caption='Hola', direc='/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_taylor', direc_latex='taylor/')
#graph_anex(direc='/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_taylor', direc_latex='taylor/')
#    
##Gráfica de cielo despejado
#graph_anex(direc='/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_radiacion', direc_latex='g_cielo_despejado/', str_i=0, str_f=8)
#
#
#
#
#
#
#
#
#
#
##############Graficador de los no valores de las estaciones automáticas
### Gráfica compuesta principalmente por 4 páneles
#
#
#import os
#import pandas as pd
#
#lista_estaciones = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/est_usadas_lista.csv')
#lista_estaciones.columns.values[0] = 'cod_1'
#lista_estaciones.columns = lista_estaciones.columns.str.strip()
#
#
#
##\begin{figure}[H]
##	\centering
##	\begin{subfigure}[normla]{0.4\textwidth}
##	\includegraphics[draft=false, scale=0.4]{validacion_convencionales/21205420_1_1.png}
##		\caption{Conteo de no valores anuales.}
##		\label{subfig:a1}
##		\end{subfigure}
##		~
##    \begin{subfigure}[normla]{0.4\textwidth}
##	\includegraphics[draft=false, scale=0.4]{validacion_convencionales/21205420_1_2.png}
##		\caption{Conteo de no valores mensuales..}
##		\label{subfig:a2}
##		\end{subfigure}
##		
##    \begin{subfigure}[normla]{0.4\textwidth}
##	\includegraphics[draft=false, scale=0.4]{validacion_convencionales/21205420_1_3.png}
##		\caption{Conteo de saltos anuales.}
##		\label{subfig:a1}
##		\end{subfigure}
##		~
##    \begin{subfigure}[normla]{0.4\textwidth}
##	\includegraphics[draft=false, scale=0.4]{validacion_convencionales/21205420_1_4.png}
##		\caption{Conteo de saltos mensuales.}
##		\label{subfig:a2}
##		\end{subfigure}
##
##	
##	\caption{Visualización del control de calidad hecho a los valores de temperaturas diarias promedio de la estación convencional Tibaitatá código 21205420}
##	\label{gra:areas_promedio}	
##\end{figure}

#Directorio donde está
#import pandas as pd
#import os
#from funciones import un_busca_cod
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/validacion_convencionales/')
#lista_1 = os.listdir()
#
#tabla = pd.DataFrame({'a':os.listdir()})
#
#tabla['cod'] = tabla.a.str[0:8] 
#tabla['tipo'] = tabla.a.str[9]
#tabla['tipo_2'] = tabla.a.str[11]
#
#lista_estaciones = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/est_usadas_lista.csv')
#lista_estaciones.columns.values[0] = 'cod_1'
#lista_estaciones.columns = lista_estaciones.columns.str.strip()
##lista_estaciones[lista_estaciones.cod_1 == int(i)].iloc[0][1]
#
#f = open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/validacion_convencionales.csv','w')
#
#with open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/validacion_convencionales.csv','w') as f:##Usado para crear un archivo que reciba todas los comandos y se guarden en una hoja
#    
#    for i in tabla.cod.unique():
#        #print(i)
#        
#        j = lista_estaciones[lista_estaciones.cod_1 == int(i)].iloc[0][1]
#    
#    
##        print('\\begin{figure}[H]', file =f)
##        print('	\centering', file =f)
#        if (i+'_1_1.png') in lista_1:
#            
#            print('	\\begin{subfigure}[normla]{0.4\\textwidth}', file =f)
#            print('	\includegraphics[draft=false, scale=0.4]{validacion_convencionales/'+i+'_1_1.png}', file =f)
#            print('		\caption{Conteo de no valores anuales para la estación '+un_busca_cod(i)+'código '+str(i)+'.}', file =f)
#            print('		\label{subfig:a1}', file =f)
#            print('		\end{subfigure}', file =f)
#            print('		~', file =f)
#        
#        if (i+'_1_2.png') in lista_1:
#            print('    \\begin{subfigure}[normla]{0.4\\textwidth}', file =f)
#            print('	\includegraphics[draft=false, scale=0.4]{validacion_convencionales/'+i+'_1_2.png}', file =f)
#            print('		\caption{Conteo de no valores mensuales para la estación '+un_busca_cod(i)+'código '+str(i)+'.}', file =f)
#            print('		\label{subfig:a2}', file =f)
#            print('		\end{subfigure}', file =f)
#            print('		', file =f)
#        
#        if (i+'_1_3.png') in lista_1:
#            print('    \\begin{subfigure}[normla]{0.4\\textwidth}', file =f)
#            print('	\includegraphics[draft=false, scale=0.4]{validacion_convencionales/'+i+'_1_3.png}', file =f)
#            print('		\caption{Conteo de saltos anuales para la estación '+un_busca_cod(i)+'código '+str(i)+'.}', file =f)
#            print('		\label{subfig:a1}', file =f)
#            print('		\end{subfigure}', file =f)
#            print('		~', file =f)
#        
#        if (i+'_1_4.png') in lista_1:
#    
#            print('    \\begin{subfigure}[normla]{0.4\\textwidth}', file =f)
#            print('	\includegraphics[draft=false, scale=0.4]{validacion_convencionales/'+i+'_1_4.png}', file =f)
#            print('		\caption{Conteo de saltos mensuales para la estación '+un_busca_cod(i)+'código '+str(i)+'.}', file =f)
#            print('		\label{subfig:a2}', file =f)
#            print('		\end{subfigure}', file =f)
#            print('', file =f)
#            print('	', file =f)
##        print('	\caption{Visualización del control de calidad hecho a los valores de temperaturas diarias promedio de la estación convencional '+j+'}', file =f)
##        print('	\label{gra:areas_promedio}	', file =f)
##        print('\end{figure}', file =f)
#        print('\end{figure}', file =f)
#        print('           ', file =f)
#        print('\\begin{figure}[H]\ContinuedFloat', file =f)
#        print('\centering', file =f)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
############Gráfica de un sólo pánel realizado para los diagrmas de Taylor
#    
#
#
#
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_taylor')
#lista_1 = os.listdir()
#
#for ix,ii in enumerate(lista_1):
#    #print(ii, ix)
#    
#    j = lista_estaciones[lista_estaciones.cod_1 == int(ii[7:15])].iloc[0][1]
#
#    #print('\centering')
#    print('\\begin{subfigure}[normla]{0.4\\textwidth}')
#    print('\includegraphics[draft=false, scale=0.5]{taylor/'+ii+'}')
#    print('\caption{Estación '+j+' código '+str(ii)[7:15]+'.}')# Las líneas negras representan el período de tiempo entre el 31 de enero del 2007 y el 03 de febrero del 2007.}')
#    #print('\label{gra:papa_cund_2}	')
#    print('\end{subfigure}')
#    print('~')
#    
#    
#    if (ix+1) in lista_6:
#        #print(ix)
#        print('\end{figure}')
#        print('           ')
#        print('\\begin{figure}[H]\ContinuedFloat')
#        print('\centering')
#    
#    #print('\caption{Diagrama de Taylor de los diferentes dominios evluados para la estación '+j+'.}')
#    
#    
#    
#    
#
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
######Gráficas de los datos del 2007
#    
#import os
#import pandas as pd
#
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/automaticas_periodos')
#lista_1 = os.listdir()
#
#for ii in lista_1:
#    #print(ii)
#    
#    j = lista_estaciones[lista_estaciones.cod_1 == int(ii[0:8])].iloc[0][1]
#    print('\\begin{subfigure}[normla]{0.5\\textwidth}\ContinuedFloat')
#    print('\includegraphics[draft=false, scale=0.3]{series_2007/'+ii+'}')
#    print('\caption{Estación '+j+' código '+str(ii)[0:8]+'.}')# Las líneas negras representan el período de tiempo entre el 31 de enero del 2007 y el 03 de febrero del 2007.}')
#    #print('\label{gra:papa_cund_2}	')
#    print('\end{subfigure}')
#    print('~')
#		
#    
#    
#
#    print('\\begin{figure}[H]')
#    print('\centering')
#    print('\includegraphics[draft=false, scale=0.4]{series_2007/'+ii+'}')
#    print('\caption{Serie de tiempo de la estación '+j+' código '+str(ii)[0:8]+'. Las líneas negras representan el período de tiempo entre el 31 de enero del 2007 y el 03 de febrero del 2007.}')
#    print('\end{figure}')
#    print('  ')
#    
#    
#graph_anex(direc='/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/automaticas_periodos', direc_latex='series_2007/', str_i=0, str_f=8, scale=.25)
#
#
#
#
#
#
######Gráficas de los datos Validados para el informe 2
#    
#import os
#import pandas as pd
#
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_temperatura')
#lista_1 = os.listdir()
#
#
#lista_estaciones = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/est_usadas_lista.csv')
#lista_estaciones.columns.values[0] = 'cod_1'
#lista_estaciones.columns = lista_estaciones.columns.str.strip()
##lista_estaciones[lista_estaciones.cod_1 == int(i)].iloc[0][1]
#
#graph_1 = []
#for uu in lista_1:
#    if 'v' not in uu:
#        graph_1.append(uu)
#        
#
#for ii in graph_1:
#    #print(ii)
#
#    j = lista_estaciones[lista_estaciones.cod_1 == int(ii[0:8])].iloc[0][1] # Nombre de la estación
# 
#    
#    print('\\begin{figure}[H]')
#    print('\\begin{subfigure}[b]{0.5\\textwidth}')
#    print('\\begin{center}')
#    
#    print('\includegraphics[draft=false, scale=0.4]{autom_validadas/'+str(ii)[0:8]+'v.png}')
#    print('\caption{Estación sin control de calidad}')
#
#    print('	\end{center}')
#    print('\end{subfigure}')
#    print('~')
#    print('\\begin{subfigure}[b]{0.5\\textwidth}')
#    print('\\begin{center}')
#    
#    print('\includegraphics[draft=false, scale=0.4]{autom_validadas/'+str(ii)+'}')
#    print('\caption{Estación con control de calidad}')
#
#	
#
#    print('\end{center}	')
#    print('\end{subfigure}')
#    print('\caption{Control de calidad de la estación '+j+' código '+str(ii)[0:8]+'.}')
#    print('\end{figure}	')
#    print('  ')
#	
#    
#    
##graph_anex(direc='/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/automaticas_periodos', direc_latex='series_2007/', str_i=0, str_f=8, scale=.25)
#
#
#
#
#
#
###Plot de los diagramas de taylor para los domínios todos en uno solo    
#### Gráfica de la comparación entre estaciones automáticas y convencionales en un PDF    
#    
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/latex/grafica_comparacion_temperaturas')
#lista_1 = os.listdir()
#lista_1 = pd.DataFrame({'archi':lista_1})
#lista_1['cod'] = lista_1.archi.str[0:8]
#lista_1['dom_1'] = lista_1.archi.str[-7:-4]
#lista_1['simu'] = lista_1.archi.str[10:-7]
#lista_1.cod = lista_1.cod.convert_objects(convert_numeric=True)
#
#lista_2 = busca_cod(lista_1)
#
#lista_2 = lista_2.sort_values(['simu','cod'])
#
#lista_6 = []
#for ff in range(1, 100):
#    entrada = 6*ff
#    lista_6.append(entrada)
#
#textwidth = 0.4
#scale = 0.5
#    
#f = open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/salida_latex.csv','w')
#
#with open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/salida_latex.csv','w') as f:##Usado para crear un archivo que reciba todas los comandos y se guarden en una hoja
#
#    for ix,  (cod_1, simu_1, dom_2, nombre_1, archi_1) in enumerate(zip(lista_2.cod, lista_2.simu, lista_2.dom_1, lista_2.Nombre, lista_2.archi)):    
#    
#        if str(cod_1)+'_0'+simu_1+dom_2+'.png' in list(lista_2.archi):
#            #print('Hola')
#            
#        
#            print('\\begin{subfigure}[normla]{'+str(textwidth)+'\\textwidth}', file =f)
#            print('\includegraphics[draft=false, scale='+str(scale)+']{grafica_comparacion_temperaturas/'+archi_1+'}', file =f)
#            print('\caption{'+'Estación '+nombre_1+' código '+str(cod_1)+'.}', file =f)# Las líneas negras representan el período de tiempo entre el 31 de enero del 2007 y el 03 de febrero del 2007.}')
#            #print('\label{gra:papa_cund_2}	')
#            print('\end{subfigure}', file =f)
#            print('~', file =f)
#            
#            if (ix+1) in lista_6:
#                #print(ix)
#                print('\end{figure}', file =f)
#                print('           ', file =f)
#                print('\\begin{figure}[H]', file =f)
#                print('\centering', file =f)
#                
#            
#
#
###Plot de los diagramas de taylor para el tiempo todos en uno solo
#### Gráfica de la comparación entre estaciones automáticas y convencionales en un PDF    
#    
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_taylor_tiempo')
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/200702')
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201408')
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201509')
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201508')
#lista_1 = os.listdir()
#lista_1 = pd.DataFrame({'archi':lista_1})
#lista_1['cod'] = lista_1.archi.str[7:15]
##lista_1['dom_1'] = lista_1.archi.str[-7:-4]
##lista_1['simu'] = lista_1.archi.str[10:-7]
##lista_1.cod = lista_1.cod.convert_objects(convert_numeric=True)
#
#lista_2 = busca_cod(lista_1)
#
##lista_2 = lista_2.sort_values(['simu','cod'])
#
#lista_6 = []
#for ff in range(1, 100):
#    entrada = 6*ff
#    lista_6.append(entrada)
#
#textwidth = 0.4
#scale = 0.3
#    
#f = open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/salida_latex.csv','w')
#
#with open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/salida_latex.csv','w') as f:##Usado para crear un archivo que reciba todas los comandos y se guarden en una hoja
#
#    for ix,  (cod_1,nombre_1, archi_1) in enumerate(zip(lista_2.cod, lista_2.Nombre, lista_2.archi)):    
#    
#        if archi_1 in list(lista_2.archi):
#            #print('Hola')
#            
#        
#            print('\\begin{subfigure}[normla]{'+str(textwidth)+'\\textwidth}', file =f)
#            print('\includegraphics[draft=false, scale='+str(scale)+']{../taylor_simulaciones/201508/'+archi_1+'}', file =f)
#            print('\caption{'+'Estación '+nombre_1+' código '+str(cod_1)+'.}', file =f)# Las líneas negras representan el período de tiempo entre el 31 de enero del 2007 y el 03 de febrero del 2007.}')
#            #print('\label{gra:papa_cund_2}	')
#            print('\end{subfigure}', file =f)
#            print('~', file =f)
#            
#            if (ix+1) in lista_6:
#                #print(ix)
#                print('\end{figure}', file =f)
#                print('           ', file =f)
#                print('\\begin{figure}[H]', file =f)
#                print('\centering', file =f)
#                
#                
#                
#                
#
#### Gráfica de taylor divididas de a 5
### Gráfica de los diferentes domínios   
#
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_taylor_dom_div')
#lista_1 = os.listdir()
#lista_1 = pd.DataFrame({'archi':lista_1})
#lista_1['cod'] = lista_1.archi.str[9:17]
#lista_1['nivel'] = lista_1.archi.str[7]
#lista_1 = lista_1.sort_values(['cod','nivel'])
#
#lista_2 = busca_cod(lista_1)
#
##lista_2 = lista_2.sort_values(['simu','cod'])
#
#lista_6 = []
#for ff in range(1, 100):
#    entrada = 6*ff
#    lista_6.append(entrada)
#
#textwidth = 0.4
#scale = 0.3
#    
#f = open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/salida_latex.csv','w')
#
#with open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/salida_latex.csv','w') as f:##Usado para crear un archivo que reciba todas los comandos y se guarden en una hoja
#
#    for ix,  (cod_1,nombre_1, archi_1, niv_1) in enumerate(zip(lista_2.cod, lista_2.Nombre, lista_2.archi, lista_2.nivel)):    
#        #print(cod_1)
#    
#        if cod_1 in [21206940, 21206980, 21206950]:
#            #print('Hola')
#            
#        
#            print('\\begin{subfigure}[normla]{'+str(textwidth)+'\\textwidth}', file =f)
#            print('\includegraphics[draft=false, scale='+str(scale)+']{graficas_taylor_dom_div/'+archi_1+'}', file =f)
#            print('\caption{'+'Estación '+nombre_1+' código '+str(cod_1)+' nivel '+str(niv_1)+'.}', file =f)# Las líneas negras representan el período de tiempo entre el 31 de enero del 2007 y el 03 de febrero del 2007.}')
#            #print('\label{gra:papa_cund_2}	')
#            print('\end{subfigure}', file =f)
#            print('~', file =f)
#            
#            if (ix+1) in lista_6:
#                #print(ix)
#                print('\end{figure}', file =f)
#                print('           ', file =f)
#                print('\\begin{figure}[H]', file =f)
#                print('\centering', file =f)
#            
############ Gráfica de a 5 para los diferentes tiempos
#                
##       Tiempos                
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_taylor_tmp_div')
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/200702_5')
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201408_5')
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201509_5')
#lista_1 = os.listdir()
#lista_1 = pd.DataFrame({'archi':lista_1})
#lista_1['cod'] = lista_1.archi.str[9:17]
#lista_1['nivel'] = lista_1.archi.str[7]
#lista_1 = lista_1.sort_values(['cod','nivel'])
#
#lista_2 = busca_cod(lista_1)
#
##lista_2 = lista_2.sort_values(['simu','cod'])
#
#lista_6 = []
#for ff in range(1, 100):
#    entrada = 6*ff
#    lista_6.append(entrada)
#
#textwidth = 0.4
#scale = 0.3
#    
#f = open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/salida_latex.csv','w')
#
#with open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/salida_latex.csv','w') as f:##Usado para crear un archivo que reciba todas los comandos y se guarden en una hoja
#
#    for ix,  (cod_1,nombre_1, archi_1, niv_1) in enumerate(zip(lista_2.cod, lista_2.Nombre, lista_2.archi, lista_2.nivel)):    
#        print(cod_1)
#    
#        if cod_1 > 1:#Este punto de control no tiene ningún efecto porque fué tomado de el anteriór código
#            #print('Hola')
#            
#        
#            print('\\begin{subfigure}[normla]{'+str(textwidth)+'\\textwidth}', file =f)
#            print('\includegraphics[draft=false, scale='+str(scale)+']{../taylor_simulaciones/201509_5/'+archi_1+'}', file =f)
#            print('\caption{'+'Estación '+nombre_1+' código '+str(cod_1)+' nivel '+str(niv_1)+'.}', file =f)# Las líneas negras representan el período de tiempo entre el 31 de enero del 2007 y el 03 de febrero del 2007.}')
#            #print('\label{gra:papa_cund_2}	')
#            print('\end{subfigure}', file =f)
#            print('~', file =f)
#            
#            if (ix+1) in lista_6:
#                #print(ix)
#                print('\end{figure}', file =f)
#                print('           ', file =f)
#                print('\\begin{figure}[H]', file =f)
#                print('\centering', file =f)
#
#
#
############ Gráfica para todas las estaciones con respecto a su temperatura altas temperaturas y bajas altas_bajas_2007
#                
##       Tiempos                
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_altas_bajas')
#lista_1 = os.listdir()
#lista_1 = pd.DataFrame({'archi':lista_1})
#lista_1['cod'] = lista_1.archi.str[0:8]
#lista_1 = lista_1.sort_values(['cod'])
#
#lista_2 = busca_cod(lista_1)
#
##lista_2 = lista_2.sort_values(['simu','cod'])
#
#lista_6 = []
#for ff in range(1, 100):
#    entrada = 6*ff
#    lista_6.append(entrada)
#
#textwidth = 0.4
#scale = 0.25
#    
#
#for ix,  (cod_1,nombre_1, archi_1) in enumerate(zip(lista_2.cod, lista_2.Nombre, lista_2.archi)):    
#    #print(cod_1,nombre_1, archi_1)
#
#    if cod_1 > 1:#Este punto de control no tiene ningún efecto porque fué tomado de el anteriór código
#        #print('Hola')
#        
#    
#        print('\\begin{subfigure}[normla]{'+str(textwidth)+'\\textwidth}')
#        print('\includegraphics[draft=false, scale='+str(scale)+']{altas_bajas_2007/'+archi_1+'}')
#        print('\caption{'+'Estación '+nombre_1+' código '+str(cod_1)+'.}')# Las líneas negras representan el período de tiempo entre el 31 de enero del 2007 y el 03 de febrero del 2007.}')
#        #print('\label{gra:papa_cund_2}	')
#        print('\end{subfigure}')
#        print('~')
#        
#        if (ix+1) in lista_6:
#            #print(ix)
#            print('\end{figure}')
#            print('           ')
#            print('\\begin{figure}[H]')
#            print('\centering')
#
#
#
#
###################################################################################################################
# Gráficas de la comparación de wrf con respecto a la temperatura del WRF
# comparacion_graficas_otras_var comparacion_grafica_otras_var
##################
#            
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/comparacion_grafica')
#lista_1 = os.listdir()
#lista_1 = pd.DataFrame({'archi':lista_1})
#lista_1['anno_1'] = lista_1.archi.str[0:6]
#lista_1['cod'] = lista_1.archi.str[7:15]
#
#lista_2 = busca_cod(lista_1)
#lista_2 = lista_2[(lista_2.anno_1 == '200702') | (lista_2.anno_1 == '201408') |(lista_2.anno_1 == '201509')]
#
#lista_2.anno_1 = lista_2.anno_1.replace('200702', 'caso 1')
#lista_2.anno_1 = lista_2.anno_1.replace('201408', 'caso 2')
##lista_2.anno_1 = lista_2.anno_1.replace('201508', 'caso 3')
#lista_2.anno_1 = lista_2.anno_1.replace('201509', 'caso 3')
#
#lista_6 = []
#for ff in range(1, 100):
#    entrada = 12*ff
#    lista_6.append(entrada)
#
#textwidth = 0.4
#scale = 0.3
#lista_2 = lista_2.sort_values(by=['cod_1', 'anno_1'])
#f = open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/comparacion_wrf.csv','w')
#
#with open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/comparacion_wrf.csv','w') as f:##Usado para crear un archivo que reciba todas los comandos y se guarden en una hoja
#
#    for ix,  (cod_1, anno_1, archi_1, nombre_1) in enumerate(zip(lista_2.cod, lista_2.anno_1, lista_2.archi, lista_2.Nombre)):    
#        print(ix,  (cod_1, anno_1, archi_1))
#    
#        if cod_1 == 35085808:#Este punto de control no tiene ningún efecto porque fué tomado de el anteriór código
#            print('Hola')
#            continue
#        else:
#            
#        
#            if (ix+2) in lista_6:
#                print('\\begin{subfigure}[normla]{0.6\\textwidth}', file =f)
#            else:
#                print('\\begin{subfigure}[normla]{'+str(textwidth)+'\\textwidth}', file =f)
#            print('\caption{'+'Estación '+nombre_1+'código '+str(cod_1)+' '+anno_1+'.}', file =f)# Las líneas negras representan el período de tiempo entre el 31 de enero del 2007 y el 03 de febrero del 2007.}')
#            print('\includegraphics[draft=false, scale='+str(scale)+']{../comparacion_grafica/'+archi_1+'}', file =f)
#            #print('\label{gra:papa_cund_2}	')
#            print('\end{subfigure}', file =f)
#            print('~', file =f)
#            
#            if (ix+1) in lista_6:
#                #print(ix)
#                print('\end{figure}', file =f)
#                print('           ', file =f)
#                print('\\begin{figure}[H]\ContinuedFloat', file =f)
#                print('\centering', file =f)
#
#pdb.set_trace()
#
#
#
#
###################################################################################################################
# Gráficas de la comparación de wrf con otras variables de la estación automática
# comparacion_graficas_otras_var comparacion_grafica_otras_var
##################
            
import pdb            

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/comparacion_graficas_otras_var')
lista_1 = os.listdir()
lista_1 = pd.DataFrame({'archi':lista_1})
lista_1['anno_1'] = lista_1.archi.str[0:6]
lista_1['cod'] = lista_1.archi.str[7:15]
lista_1['tipo'] = lista_1.archi.str[16:-4]
lista_1.tipo = lista_1.tipo.replace('rain', 'Precipitación')
lista_1.tipo = lista_1.tipo.replace('humedad', 'Humedad')
lista_1.tipo = lista_1.tipo.replace('radiacion', 'Radiación')
lista_1.tipo = lista_1.tipo.replace('vel_viento', 'Velocidad del Viento')
lista_1.tipo = lista_1.tipo.replace('dewpoint', 'Punto de rocío')
lista_1.tipo = lista_1.tipo.replace('wetbulb', 'Bulbo húmedo')

lista_2 = busca_cod(lista_1)

lista_2 = busca_cod(lista_1)
lista_2 = lista_2[(lista_2.anno_1 == '200702') | (lista_2.anno_1 == '201408') |(lista_2.anno_1 == '201509')]
lista_2.anno_1 = lista_2.anno_1.replace('200702', 'caso 1')
lista_2.anno_1 = lista_2.anno_1.replace('201408', 'caso 2')
lista_2.anno_1 = lista_2.anno_1.replace('201509', 'caso 3')

lista_2 = lista_2[lista_2.anno_1.str.contains('caso')]
lista_6 = []
for ff in range(1, 100):
    entrada = 12*ff
    lista_6.append(entrada)

textwidth = 0.4
scale = 0.3
lista_2 = lista_2.sort_values(by=['cod_1', 'anno_1'])
f = open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_otras_variables.csv','w')

with open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_otras_variables.csv','w') as f:##Usado para crear un archivo que reciba todas los comandos y se guarden en una hoja

    for ix,  (cod_1, anno_1, tipo, archi_1, nombre_1) in enumerate(zip(lista_2.cod, lista_2.anno_1, lista_2.tipo, lista_2.archi, lista_2.Nombre)):    
        print(ix,  (cod_1, anno_1, tipo, archi_1))
    
        if cod_1 == 35085808:#Este punto de control no tiene ningún efecto porque fué tomado de el anteriór código
            print('Hola')
            continue
        else:
        
            print('\\begin{subfigure}[normla]{'+str(textwidth)+'\\textwidth}', file =f)
            print('\caption{'+'Estación '+nombre_1+'código '+str(cod_1)+' '+anno_1+' variable '+tipo+'.}', file =f)# Las líneas negras representan el período de tiempo entre el 31 de enero del 2007 y el 03 de febrero del 2007.}')
            print('\includegraphics[draft=false, scale='+str(scale)+']{comparacion_graficas_otras_var/'+archi_1+'}', file =f)
            #print('\label{gra:papa_cund_2}	')
            print('\end{subfigure}', file =f)
            print('~', file =f)
            
            if (ix+1) in lista_6:
                #print(ix)
                print('\end{figure}', file =f)
                print('           ', file =f)
                print('\\begin{figure}[H]', file =f)
                print('\centering', file =f)

pdb.set_trace()



##########
#                #########
#                #Graficas de las diferentes salidas de taylor
#                #########
##########
#            
##os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/200702_m')
##os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201408_m')
##os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201508_m')
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201509_m')
#lista_1 = os.listdir()
#lista_1 = pd.DataFrame({'archi':lista_1})
#
#lista_1['cod'] = lista_1.archi.str[7:15]
#
#lista_2 = busca_cod(lista_1)
#
##lista_6 = []
##entrada = 4
##for ff in range(1, 100):
##    lista_6.append(entrada)
##    entrada += 6
#
#lista_6 = []
#for ff in range(1, 100):
#    entrada = 6*ff
#    lista_6.append(entrada)
#
#
#textwidth = 0.5
#scale = 0.5
#
#f = open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones_2007.csv','w')
#
#with open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones_2007.csv','w') as f:##Usado para crear un archivo que reciba todas los comandos y se guarden en una hoja
#
#    for ix,  (cod_1, nombre_1, archi_1) in enumerate(zip(lista_2.cod, lista_2.Nombre, lista_2.archi)):    
#        print(ix,  (cod_1, nombre_1, archi_1))
#    
#        if cod_1 > 1:#Este punto de control no tiene ningún efecto porque fué tomado de el anteriór código
#            #print('Hola')
#            
#        
#            print('\\begin{subfigure}[normla]{'+str(textwidth)+'\\textwidth}', file =f)
#            print('\caption{Diagrama de Taylor para la Estación '+nombre_1+'código '+str(cod_1)+'.}', file =f)# Las líneas negras representan el período de tiempo entre el 31 de enero del 2007 y el 03 de febrero del 2007.}')
#            #print('\includegraphics[draft=false, scale='+str(scale)+']{../taylor_simulaciones/200702_m/'+archi_1+'}', file =f)
#            #print('\includegraphics[draft=false, scale='+str(scale)+']{../taylor_simulaciones/201408_m/'+archi_1+'}', file =f)
#            #print('\includegraphics[draft=false, scale='+str(scale)+']{../taylor_simulaciones/201508_m/'+archi_1+'}', file =f)
#            print('\includegraphics[draft=false, scale='+str(scale)+']{../taylor_simulaciones/201509_m/'+archi_1+'}', file =f)
#            #print('\label{gra:papa_cund_2}	')
#            print('\end{subfigure}', file =f)
#            print('~', file =f)
#            
#            if (ix+1) in lista_6:
#                #print(ix)
#                print('\end{figure}', file =f)
#                print('           ', file =f)
#                print('\\begin{figure}[H]\ContinuedFloat', file =f)
#
################################################################################
#                ###############################################################################
#                # Diagramas de Taylor para latex para las estaciones que están en duda.
#                ###############################################################################
################################################################################                
#                
#                
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201408_5_m')
##os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201508_5_m')
#
#lista_1 = os.listdir()
#lista_1 = pd.DataFrame({'archi':lista_1})
#lista_1[['nada', 'nivel', 'cod_1']] = lista_1.archi.str.split('_', expand=True)
#lista_1['cod'] = lista_1.cod_1.str[:-4]
#lista_1.cod = pd.to_numeric(lista_1.cod)
#lista_1.nivel = pd.to_numeric(lista_1.nivel)
#
#lista_1 = lista_1.sort_values(['cod','nivel'])
#
#
#lista_1_1 = lista_1[lista_1.cod.isin([21206980])]
##lista_1_1 = lista_1[lista_1.cod.isin([21206920, 35035130, 21205012, 21205791])]
#lista_2 = busca_cod(lista_1_1)
#
##lista_2 = lista_2.sort_values(['simu','cod'])
#
#lista_6 = []
#for ff in range(1, 100):
#    entrada = 6*ff
#    lista_6.append(entrada)
#
#textwidth = 0.4
#scale = 0.3
#    
#f = open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/caso_2_mejores.csv','w')
#
#with open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/caso_2_mejores.csv','w') as f:##Usado para crear un archivo que reciba todas los comandos y se guarden en una hoja
#
#    for ix,  (cod_1,nombre_1, archi_1, niv_1) in enumerate(zip(lista_2.cod, lista_2.Nombre, lista_2.archi, lista_2.nivel)):    
#        #print(cod_1)
#    
#        if cod_1 > 1:#Este punto de control no tiene ningún efecto porque fué tomado de el anteriór código
#            #print('Hola')
#            
#        
#            print('\\begin{subfigure}[normla]{'+str(textwidth)+'\\textwidth}', file =f)
#            print('\caption{'+'Estación '+nombre_1+' código '+str(cod_1)+' nivel '+str(niv_1)+'.}', file =f)# Las líneas negras representan el período de tiempo entre el 31 de enero del 2007 y el 03 de febrero del 2007.}')
#            print('\includegraphics[draft=false, scale='+str(scale)+']{../taylor_simulaciones/201408_5_m/'+archi_1+'}', file =f)
#            #print('\label{gra:papa_cund_2}	')
#            print('\end{subfigure}', file =f)
#            print('~', file =f)
#            
#            if (ix+1) in lista_6:
#                #print(ix)
#                print('\end{figure}', file =f)
#                print('           ', file =f)
#                print('\\begin{figure}[H]\ContinuedFloat', file =f)
#                print('\centering', file =f)
#                
#
################################################################################
#                ###############################################################################
#                #caso 3
#                ###############################################################################
################################################################################                
#                
#                
#
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201508_5_m')
#
#lista_1 = os.listdir()
#lista_1 = pd.DataFrame({'archi':lista_1})
#lista_1[['nada', 'nivel', 'cod_1']] = lista_1.archi.str.split('_', expand=True)
#lista_1['cod'] = lista_1.cod_1.str[:-4]
#lista_1.cod = pd.to_numeric(lista_1.cod)
#lista_1.nivel = pd.to_numeric(lista_1.nivel)
#
#lista_1 = lista_1.sort_values(['cod','nivel'])
#
#
#
#lista_1_1 = lista_1[lista_1.cod.isin([21206920, 35035130, 21205012, 21205791])]
#lista_2 = busca_cod(lista_1_1)
#
##lista_2 = lista_2.sort_values(['simu','cod'])
#
#lista_6 = []
#for ff in range(1, 100):
#    entrada = 6*ff
#    lista_6.append(entrada)
#
#textwidth = 0.4
#scale = 0.3
#    
#f = open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/caso_3_mejores.csv','w')
#
#with open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/caso_3_mejores.csv','w') as f:##Usado para crear un archivo que reciba todas los comandos y se guarden en una hoja
#
#    for ix,  (cod_1,nombre_1, archi_1, niv_1) in enumerate(zip(lista_2.cod, lista_2.Nombre, lista_2.archi, lista_2.nivel)):    
#        #print(cod_1)
#    
#        if cod_1 > 1:#Este punto de control no tiene ningún efecto porque fué tomado de el anteriór código
#            #print('Hola')
#            
#        
#            print('\\begin{subfigure}[normla]{'+str(textwidth)+'\\textwidth}', file =f)
#            print('\caption{'+'Estación '+nombre_1+' código '+str(cod_1)+' nivel '+str(niv_1)+'.}', file =f)# Las líneas negras representan el período de tiempo entre el 31 de enero del 2007 y el 03 de febrero del 2007.}')
#            print('\includegraphics[draft=false, scale='+str(scale)+']{../taylor_simulaciones/201508_5_m/'+archi_1+'}', file =f)
#            #print('\label{gra:papa_cund_2}	')
#            print('\end{subfigure}', file =f)
#            print('~', file =f)
#            
#            if (ix+1) in lista_6:
#                #print(ix)
#                print('\end{figure}', file =f)
#                print('           ', file =f)
#                print('\\begin{figure}[H]\ContinuedFloat', file =f)
#                print('\centering', file =f)
#                
#                
#
################################################################################
#                ###############################################################################
#                #caso 4
#                ###############################################################################
################################################################################                
#                
#                
#
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201509_5_m')
#
#lista_1 = os.listdir()
#lista_1 = pd.DataFrame({'archi':lista_1})
#lista_1[['nada', 'nivel', 'cod_1']] = lista_1.archi.str.split('_', expand=True)
#lista_1['cod'] = lista_1.cod_1.str[:-4]
#lista_1.cod = pd.to_numeric(lista_1.cod)
#lista_1.nivel = pd.to_numeric(lista_1.nivel)
#
#lista_1 = lista_1.sort_values(['cod','nivel'])
#
#
#
#lista_1_1 = lista_1[lista_1.cod.isin([21206920, 35035130, 21206980])]
#lista_2 = busca_cod(lista_1_1)
#
##lista_2 = lista_2.sort_values(['simu','cod'])
#
#lista_6 = []
#for ff in range(1, 100):
#    entrada = 6*ff
#    lista_6.append(entrada)
#
#textwidth = 0.4
#scale = 0.3
#    
#f = open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/caso_4_mejores.csv','w')
#
#with open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/caso_4_mejores.csv','w') as f:##Usado para crear un archivo que reciba todas los comandos y se guarden en una hoja
#
#    for ix,  (cod_1,nombre_1, archi_1, niv_1) in enumerate(zip(lista_2.cod, lista_2.Nombre, lista_2.archi, lista_2.nivel)):    
#        #print(cod_1)
#    
#        if cod_1 > 1:#Este punto de control no tiene ningún efecto porque fué tomado de el anteriór código
#            #print('Hola')
#            
#        
#            print('\\begin{subfigure}[normla]{'+str(textwidth)+'\\textwidth}', file =f)
#            print('\caption{'+'Estación '+nombre_1+' código '+str(cod_1)+' nivel '+str(niv_1)+'.}', file =f)# Las líneas negras representan el período de tiempo entre el 31 de enero del 2007 y el 03 de febrero del 2007.}')
#            print('\includegraphics[draft=false, scale='+str(scale)+']{../taylor_simulaciones/201508_5_m/'+archi_1+'}', file =f)
#            #print('\label{gra:papa_cund_2}	')
#            print('\end{subfigure}', file =f)
#            print('~', file =f)
#            
#            if (ix+1) in lista_6:
#                #print(ix)
#                print('\end{figure}', file =f)
#                print('           ', file =f)
#                print('\\begin{figure}[H]\ContinuedFloat', file =f)
#                print('\centering', file =f)
