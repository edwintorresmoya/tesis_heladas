import pandas as pd
import os
import pdb
from numba import jit
from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt
from funciones import un_busca_cod
import matplotlib.dates as mdates
#import rlcompleter
#pdb.Pdb.complete=rlcompleter.Completer(locals()).complete

#@jit
###Como obtener las gráficas fig 2a

#def grafica2a():
#    start = timer()
#    #Gráfica de las heladas que se presentaron cada año sólo tiene en cuenta las estaciones automáticas
#
#    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')
#    lista_archivos = pd.DataFrame({'col_1':os.listdir()})
#    lista_tmp = lista_archivos[lista_archivos.col_1.str.contains('tmp_2m')]
#    
#    #Loop entre cada uno de los archivos de temperatura
#    fig = plt.figure()
#    ax = fig.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#
#    fig2 = plt.figure()
#    ax2 = fig2.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#    for i in lista_tmp.col_1:
#        print(i)
#        base = pd.read_csv(i)
#        base = base[base.val_tmp == 0]
#        if len(base)<10:
#            continue
#        base.date = pd.to_datetime(base.date)
#        base['year_1'] = base.date.dt.year
#        base_0 = base
#        base_20 = base
#
#        base_0['cond_1'] = np.where(base.tmp_2m > 0, 0, 1).tolist() # si la temperatura es menor a 0 entonces se convierte en 1 para ser sumado
#        base_plot0 = base_0.groupby(base_0.year_1).sum()[['cond_1']].reset_index()
#        base_plot0.year_1 = pd.to_datetime(base_plot0.year_1, format='%Y')
#
#        #Gráficas de las heladas
#        ax.plot_date(base_plot0.year_1, base_plot0.cond_1, '-', label = un_busca_cod(i[2:10]))
#        ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size':6})
#
#        
#        base_20['cond_1'] = np.where(base.tmp_2m < 25, 0, 1).tolist() # si la temperatura es menor a 0 entonces se convierte en 1 para ser sumado
#        base_plot0 = base_20.groupby(base_20.year_1).sum()[['cond_1']].reset_index()
#        base_plot0.year_1 = pd.to_datetime(base_plot0.year_1, format='%Y')
#        # se va a hacer una resta de todos los valores de temperatura
#
#        #Gráficas de las heladas
#        ax2.plot_date(base_plot0.year_1, base_plot0.cond_1, '-', label = un_busca_cod(i[2:10]))
#        ax2.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size':6})
#
#    fig.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/prabha/grafica2/bajas_tmp.png')
#    fig2.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/prabha/grafica2/altas_tmp.png')
#    #plt.show()
#    
#    print('tiempo->',(timer() - start))
#grafica2a()

###Gráficas de la figura 4

#def grafica4a():
#    # Gráficas de la temperatura para sólo la temperatura en el numeral a de la figura 4
#    for i in ['200702','201408','201508','201509']:
#        print(i)
#        os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_estaciones_dominios/tablas_series_'+i)
#        lista_archivos = pd.DataFrame({'col_1':os.listdir()})
#        lista_tmp = lista_archivos[lista_archivos.col_1.str.contains('.csv')]
#        #horas_6 = ['6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','0','1','2','3','4','5']
#        #lista_horas = ['2','2','2','2','2','2','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
#        #lista_horas = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0,1,1,2,3,4,5,6]
#        #fechas_horas = pd.to_datetime(lista_horas, format = '%d')
#        #fechas_horas = pd.to_datetime(horas_6, format = '%H')
#        #horas_3 = []
#        #for xx in lista_horas:
#        #    adicional = pd.Timedelta(xx + ' hours')
#        #    horas_3.append(adicional)
#        #horas_4 = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22']
#
#
#        a_d = pd.to_datetime('20000101 6:00')
#        b_d = pd.to_datetime('20000102 6:00')
#        horas_3 = []
#        while a_d < b_d:
#            horas_3.append(a_d)
#            a_d += pd.Timedelta('1 hours') 
#
#
#
#        #Gráficas
#
#        for j in lista_tmp.col_1:
#
#            print(j)
#            base = pd.read_csv(j)
#            if len(base) < 10:
#                continue
#
#            fig1 = plt.figure()
#            ax1 = fig1.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#            fig2 = plt.figure()
#            ax2 = fig2.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#            fig3 = plt.figure()
#            ax3 = fig3.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#            fig4 = plt.figure()
#            ax4 = fig4.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#            #Usado para sacar los valores que de icm y de Colombia
#            lista_loop = base.columns[base.columns.str.contains('ideam')]
#            lista_loop_2 = lista_loop[lista_loop.str.contains('icm') | lista_loop.str.contains('colombia')]
#            for ll in lista_loop_2.tolist():
#                cod = ll[0:8]
#                caso = ll[9:]
#                if i == '201408':
#                    caso = ll[11:]
#                print(ll)
#                base.date = pd.to_datetime(base.date)
#                base['hora'] = base.date.dt.hour
#                base['frec'] = 1
#                ###MBE
#                base['tmp_mbe'] = base[ll] - base.tmp_2m
#                base_mbe = base.groupby('hora').sum()[['frec', 'tmp_mbe']].reset_index()
#                base_mbe['plot_mbe'] = base_mbe.tmp_mbe / base_mbe.frec
#                
#                ###MAE
#                base['tmp_mae'] = abs(base[ll] - base.tmp_2m)
#                base_mae = base.groupby('hora').sum()[['frec', 'tmp_mae']].reset_index()
#                base_mae['plot_mae'] = base_mae.tmp_mae / base_mae.frec
#                
#                ##RMSE
#                base['tmp_rmse'] = (base[ll] - base.tmp_2m)**2
#                base_rmse = base.groupby('hora').sum()[['frec', 'tmp_rmse']].reset_index()
#                base_rmse['plot_rmse'] = base_rmse.tmp_rmse / base_rmse.frec
#
#                ##Pearson
#                pearson = base.tmp_2m.corr(base[ll])
#
#                ## d
#                xo = base[ll]
#                
#                d = 1 - sum(((xo - base.tmp_2m.mean()) - (base.tmp_2m - base.tmp_2m.mean()))**2
#                        ) /  sum((abs(xo - base.tmp_2m.mean()) - abs(base.tmp_2m - base.tmp_2m.mean()))**2)
#
#
#                if caso[-3:] == 'd01':
#                    mar_1 = 's'
#                else:
#                    mar_1 = '^'
#                    
#                if caso[6:-4] == 'icm':
#                    col_2 = 'black'
#                else:
#                    col_2 = 'dimgrey'
#
#                fecha_1 = []
#                for oo in base_mbe.hora:
#                    print(oo)
#                    if oo < 6:
#                        fecha_1.append(pd.to_datetime(oo, format ='%H') + pd.Timedelta('1 days'))
#                    else:
#                        fecha_1.append(pd.to_datetime(oo, format ='%H'))
#                base_mbe['date_1'] = fecha_1
#                base_mbe = base_mbe.sort_values('date_1')
#
#                ax1.plot_date(base_mbe.date_1, base_mbe.plot_mbe, '-', label = caso, marker = mar_1, color = col_2)
#                ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size':6})
#                ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H"))
#
#            ax1.hlines(y = 0, xmin = base_mbe.date_1.min(), xmax = base_mbe.date_1.max(), linestyle = ':', color = 'silver')
#            fig1.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/prabha/grafica4/'+'mbe_'+str(i)+'_'+j[0:8]+'.png')
#
#grafica4a()




#def grafica4bcd():
#    ## Gráfica de las subgráficas bcd
#    start = timer()
#    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/comparacion_grafica_otras_var/tablas')
#    lista_archivos = pd.DataFrame({'col_1':os.listdir()})
#    lista_tmp = lista_archivos[lista_archivos.col_1.str.contains('.csv')]
#    lista_tmp['year_1'] = lista_tmp.col_1.str[0:6]
#    lista_tmp['cod'] = lista_tmp.col_1.str[7:15]
#    lista_tmp['wrf'] = lista_tmp.col_1.str[16:23]
#    lista_tmp['dom'] = lista_tmp.col_1.str[24:27]
#    #lista_tmp['tipo'] = lista_tmp.col_1.str[27:-4]
#
#
#    ##Usado para sacar las fechas para los plots
#
#    for year_1 in lista_tmp.year_1.unique().tolist():
#        for cod in lista_tmp.cod.unique().tolist():
#            for col, tipo in zip(['Td', 'wb', 'vel_vi10'],#datos reales
#                    ['dewpoint', 'wetbulb', 'vel_viento']):#Datos modelados
#
#                # Filtro para que no cree gráficas vacias
#                archivo1 = year_1 + '_' + cod + '_ideam_i'+'_d01'+ tipo + '.csv'
#                # 200702_21206790_ideam_c_d01dewpoint.csv
#                if(archivo1 not in lista_tmp.col_1.tolist()):
#                    print('salto')
#                    continue
#
#                fig1 = plt.figure()
#                ax1 = fig1.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#
#                for wrf in lista_tmp.wrf.unique().tolist():
#                    for dom in lista_tmp.dom.unique().tolist():
#                        archivo = year_1 + '_' + cod + '_' +wrf+'_'+dom+ tipo + '.csv'
#                        # 200702_21206790_ideam_c_d01dewpoint.csv
#                        if(archivo not in lista_tmp.col_1.tolist()):
#                            print('salto')
#                            continue
#                        print(archivo)
#                        #Leer los archivos
#                        base = pd.read_csv(archivo)
#                        if len(base) < 10:
#                            continue
#                        
#                        print(archivo)
#        
#        
#                        #fig2 = plt.figure()
#                        #ax2 = fig2.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#                        #fig3 = plt.figure()
#                        #ax3 = fig3.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#                        #fig4 = plt.figure()
#                        #ax4 = fig4.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#                        ##Usado para sacar los valores que de icm y de Colombia
#                        #lista_loop = base.columns[base.columns.str.contains('ideam')]
#                        #lista_loop_2 = lista_loop[lista_loop.str.contains('icm') | lista_loop.str.contains('colombia')]
#                        base.date = pd.to_datetime(base.date)
#                        base['hora'] = base.date.dt.hour
#                        base['frec'] = 1
#                        ###MBE
#                        base['tmp_mbe'] = base[tipo] - base[col]
#                        base_mbe = base.groupby('hora').sum()[['frec', 'tmp_mbe']].reset_index()
#                        base_mbe['plot_mbe'] = base_mbe.tmp_mbe / base_mbe.frec
#                        
#                        ###MAE
#                        base['tmp_mae'] = abs(base[tipo] - base[col])
#                        base_mae = base.groupby('hora').sum()[['frec', 'tmp_mae']].reset_index()
#                        base_mae['plot_mae'] = base_mae.tmp_mae / base_mae.frec
#                        
#                        ##RMSE
#                        base['tmp_rmse'] = (base[tipo] - base[col])**2
#                        base_rmse = base.groupby('hora').sum()[['frec', 'tmp_rmse']].reset_index()
#                        base_rmse['plot_rmse'] = base_rmse.tmp_rmse / base_rmse.frec
#            
#                        ##Pearson
#                        pearson = base[col].corr(base[tipo])
#            
#                        ## d
#                        xo = base[tipo]
#                        
#                        d = 1 - sum(((xo - base[col].mean()) - (base[col] - base[col].mean()))**2
#                                ) /  sum((abs(xo - base[col].mean()) - abs(base[col] - base[col].mean()))**2)
#            
#            
#                        if dom == 'd01':
#                            mar_1 = 's'
#                        else:
#                            mar_1 = '^'
#                            
#                        if wrf == 'ideam_c':
#                            col_2 = 'black'
#                            modelacion = 'ideam_colombia_'
#                        else:
#                            col_2 = 'dimgrey'
#                            modelacion = 'ideam_icm_'
#            
#                        fecha_1 = []
#                        for oo in base_mbe.hora:
#                            print(oo)
#                            if oo < 6:
#                                fecha_1.append(pd.to_datetime(oo, format ='%H') + pd.Timedelta('1 days'))
#                            else:
#                                fecha_1.append(pd.to_datetime(oo, format ='%H'))
#                        base_mbe['date_1'] = fecha_1
#                        base_mbe = base_mbe.sort_values('date_1')
#
#            
#                        ax1.plot_date(base_mbe.date_1, base_mbe.plot_mbe, '-', label = (modelacion + dom), marker = mar_1, color = col_2)
#                        ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size':6})
#                        ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H"))
#                
#                ax1.hlines(y = 0, xmin = base_mbe.date_1.min(), xmax = base_mbe.date_1.max(), linestyle = ':', color = 'silver')
#                fig1.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/prabha/grafica4bcd/'+year_1+'_'+cod+'_'+tipo+'.png')
#    print('tiempo->',(timer() - start))        
#grafica4bcd()




#def tabla4bcd():
#    # Usado para sacar las tablas unidas que se van a plotear que serían iguales a las gráficas 4 del artículo
#
#    start = timer()
#    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/comparacion_grafica_otras_var/tablas')
#    lista_archivos = pd.DataFrame({'col_1':os.listdir()})
#    lista_tmp = lista_archivos[lista_archivos.col_1.str.contains('.csv')]
#    lista_tmp['year_1'] = lista_tmp.col_1.str[0:6]
#    lista_tmp['cod'] = lista_tmp.col_1.str[7:15]
#    lista_tmp['wrf'] = lista_tmp.col_1.str[16:23]
#    lista_tmp['dom'] = lista_tmp.col_1.str[24:27]
#    #lista_tmp['tipo'] = lista_tmp.col_1.str[27:-4]
#
#
#    ##Usado para sacar las fechas para los plots
#
#    for year_1 in lista_tmp.year_1.unique().tolist():
#        for col, tipo in zip(['Td', 'wb', 'vel_vi10'],#datos reales
#                ['dewpoint', 'wetbulb', 'vel_viento']):#Datos modelados
#            base_v = pd.DataFrame({'hora':np.arange(0,23).tolist()})
#            for cod in lista_tmp.cod.unique().tolist():
#
#                # Filtro para que no cree gráficas vacias
#                archivo1 = year_1 + '_' + cod + '_ideam_i'+'_d01'+ tipo + '.csv'
#                # 200702_21206790_ideam_c_d01dewpoint.csv
#                if(archivo1 not in lista_tmp.col_1.tolist()):
#                    print('salto')
#                    continue
#
#                #fig1 = plt.figure()
#                #ax1 = fig1.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#
#                for wrf in lista_tmp.wrf.unique().tolist():
#                    for dom in lista_tmp.dom.unique().tolist():
#                        archivo = year_1 + '_' + cod + '_' +wrf+'_'+dom+ tipo + '.csv'
#                        # 200702_21206790_ideam_c_d01dewpoint.csv
#                        if(archivo not in lista_tmp.col_1.tolist()):
#                            print('salto')
#                            continue
#                        print(archivo)
#                        #Leer los archivos
#                        base = pd.read_csv(archivo)
#                        if len(base) < 10:
#                            continue
#                        
#                        print(archivo)
#        
#        
#                        if dom == 'd01':
#                            mar_1 = 's'
#                        else:
#                            mar_1 = '^'
#                            
#                        if wrf == 'ideam_c':
#                            col_2 = 'black'
#                            modelacion = 'ideam_colombia_'
#                        else:
#                            col_2 = 'dimgrey'
#                            modelacion = 'ideam_icm_'
#            
#                        #fig2 = plt.figure()
#                        #ax2 = fig2.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#                        #fig3 = plt.figure()
#                        #ax3 = fig3.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#                        #fig4 = plt.figure()
#                        #ax4 = fig4.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#                        ##Usado para sacar los valores que de icm y de Colombia
#                        #lista_loop = base.columns[base.columns.str.contains('ideam')]
#                        #lista_loop_2 = lista_loop[lista_loop.str.contains('icm') | lista_loop.str.contains('colombia')]
#                        base.date = pd.to_datetime(base.date)
#                        base['hora'] = base.date.dt.hour
#                        base['frec'] = 1
#                        ###MBE
#                        base['tmp_mbe'] = base[tipo] - base[col]
#                        base_mbe = base.groupby('hora').sum()[['frec', 'tmp_mbe']].reset_index()
#                        base_mbe['plot_mbe'] = base_mbe.tmp_mbe / base_mbe.frec
#                        base_mbe.columns.values[3] = cod+'_'+wrf+'_'+dom
#                        base_v = pd.merge(base_mbe[['hora', cod+'_'+wrf+'_'+dom]], base_v, on='hora', how='outer')
#            base_v.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/prabha/tablas4/'+year_1+'_'+col+'.csv')            
#tabla4bcd()



#def tablas4a():
#    # Tablas de la temperatura que serán de utilidad para sacar las gráficas
#    # Es una función que regresa las tablas del mbe índice para ser ploteadas
#    for i in ['200702','201408','201508','201509']:
#        print(i)
#        os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_estaciones_dominios/tablas_series_'+i)
#        lista_archivos = pd.DataFrame({'col_1':os.listdir()})
#        lista_tmp = lista_archivos[lista_archivos.col_1.str.contains('.csv')]
#        #horas_6 = ['6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','0','1','2','3','4','5']
#        #lista_horas = ['2','2','2','2','2','2','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
#        #lista_horas = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0,1,1,2,3,4,5,6]
#        #fechas_horas = pd.to_datetime(lista_horas, format = '%d')
#        #fechas_horas = pd.to_datetime(horas_6, format = '%H')
#        #horas_3 = []
#        #for xx in lista_horas:
#        #    adicional = pd.Timedelta(xx + ' hours')
#        #    horas_3.append(adicional)
#        #horas_4 = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22']
#
#
#        #Gráficas
#
#        base_v = pd.DataFrame({'hora':np.arange(0,23).tolist()})
#        for j in lista_tmp.col_1:
#
#            print(j)
#            base = pd.read_csv(j)
#            if len(base) < 10:
#                continue
#
#            fig1 = plt.figure()
#            ax1 = fig1.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#            #fig2 = plt.figure()
#            #ax2 = fig2.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#            #fig3 = plt.figure()
#            #ax3 = fig3.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#            #fig4 = plt.figure()
#            #ax4 = fig4.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#            #Usado para sacar los valores que de icm y de Colombia
#            lista_loop = base.columns[base.columns.str.contains('ideam')]
#            lista_loop_2 = lista_loop[lista_loop.str.contains('icm') | lista_loop.str.contains('colombia')]
#            for ll in lista_loop_2.tolist():
#                cod = ll[0:8]
#                caso = ll[9:]
#                if i == '201408':
#                    caso = ll[11:]
#                print(ll)
#                ###################
#                if caso[-3:] == 'd01':
#                    mar_1 = 's'
#                else:
#                    mar_1 = '^'
#                    
#                if caso[6:-4] == 'icm':
#                    col_2 = 'black'
#                else:
#                    col_2 = 'dimgrey'
#
#                if ll[9:16] == 'ideam-c':
#                    wrf = 'ideam_c'
#                else:
#                    wrf = 'ideam_i'
#
#                #####################
#                base.date = pd.to_datetime(base.date)
#                base['hora'] = base.date.dt.hour
#                base['frec'] = 1
#                ###MBE
#                base['tmp_mbe'] = base[ll] - base.tmp_2m
#                base_mbe = base.groupby('hora').sum()[['frec', 'tmp_mbe']].reset_index()
#                base_mbe['plot_mbe'] = base_mbe.tmp_mbe / base_mbe.frec
#                base_mbe.columns.values[3] = cod+'_'+wrf+'_'+caso[-3:]
#                base_v = pd.merge(base_mbe[['hora', cod+'_'+wrf+'_'+caso[-3:]]], base_v, on='hora', how='outer')
#        base_v.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/prabha/tablas4/'+i+'_tmp_2m'+'.csv')            
#tablas4a()


#################################
### Gráfica tipo 4
#################################

#def grafica_casos():
#    #### Scrip creado para hacer las gráficas de la totalidad de los datos
#    #### La columna llamada ideam es la que tiene los valores de la estación automática Tibaitatá
#    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/prabha/tablas4')
#    lista = pd.DataFrame({'col_1':os.listdir()})
#    print('hola')
#    lista['year_1'] = lista.col_1.str[0:6]
#    lista['var_1'] = lista.col_1.str[7:-4]
#    for nombre, year_1, var_1 in zip(lista.col_1, lista.year_1, lista.var_1):
#
#        base = pd.read_csv(nombre)
#        if len(base.columns[base.columns.str.contains('21206990')]) < 1:
#            continue
#        base_ideam_i1 = base[base.columns[base.columns.str.contains('21206990_ideam_i_d01')].tolist()]
#        base_ideam_i2 = base[base.columns[base.columns.str.contains('21206990_ideam_i_d02')].tolist()]
#        base_ideam_c1 = base[base.columns[base.columns.str.contains('21206990_ideam_c_d01')].tolist()]
#        base_ideam_c2 = base[base.columns[base.columns.str.contains('21206990_ideam_c_d02')].tolist()]
#        base_otras = base[base.columns[~base.columns.str.contains('21206990')].tolist()]
#
#        #base_ideam_d02_mean =  base_ideam[base_ideam.columns[base_ideam.columns.str.contains('d02')].tolist()].mean(axis=1)
#        #base_ideam_d01_mean =  base_ideam[base_ideam.columns[base_ideam.columns.str.contains('d01')].tolist()].mean(axis=1)
#        base_otras_d01_mean = base_otras[base_otras.columns[~base_otras.columns.str.contains('d01')].tolist()].mean(axis=1)
#        base_otras_d02_mean = base_otras[base_otras.columns[~base_otras.columns.str.contains('d02')].tolist()].mean(axis=1)
#
#        #base_ideam_d02_std = base_ideam[base_ideam.columns[base_ideam.columns.str.contains('d02')].tolist()].std(axis=1)
#        #base_ideam_d01_std = base_ideam[base_ideam.columns[base_ideam.columns.str.contains('d01')].tolist()].std(axis=1)
#        base_otras_d01_std = base_otras[base_otras.columns[~base_otras.columns.str.contains('d01')].tolist()].std(axis=1)
#        base_otras_d02_std = base_otras[base_otras.columns[~base_otras.columns.str.contains('d02')].tolist()].std(axis=1)
#
#        base_2 = pd.concat([base.hora, base_ideam_i1, base_ideam_i2, base_ideam_c1, base_ideam_c2, base_otras_d01_mean, base_otras_d02_mean, base_otras_d01_std, base_otras_d02_std, ], axis=1)
#
#        base_2.columns.values[1:] = ['ideam_i1', 'ideam_i2', 'ideam_c1', 'ideam_c2', 'otras_d01_mean', 'otras_d02_mean', 'otras_d01_std', 'otras_d02_std']
#
#        #base_2 = pd.concat([base.hora, base_ideam_d02_mean, base_ideam_d01_mean, base_otras_d01_mean, base_otras_d02_mean, base_ideam_d02_std, base_ideam_d01_std, base_otras_d01_std, base_otras_d02_std, ], axis=1)
#
#        #base_2.columns.values[1:] = ['ideam_d02_mean', 'ideam_d01_mean', 'otras_d01_mean', 'otras_d02_mean', 'ideam_d02_std', 'ideam_d01_std', 'otras_d01_std', 'otras_d02_std']
#
#        fecha_1 = []
#        for oo in base.hora:
#            print(oo)
#            if oo < 6:
#                fecha_1.append(pd.to_datetime(oo, format ='%H') + pd.Timedelta('1 days'))
#            else:
#                fecha_1.append(pd.to_datetime(oo, format ='%H'))
#        base_2['date_1'] = fecha_1
#        base_2 = base_2.sort_values('date_1')
#
#        fig1 = plt.figure()
#        ax1 = fig1.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas       
#        ####Se debe hacer la gráfica ya está la tabla
#
#
#
#        base_2['ix_1'] = np.arange(1, 25)
#        
#        
#        ax1.errorbar(base_2.ix_1, base_2.otras_d01_mean, yerr=base_2.otras_d01_std, linestyle='-', label = 'Otras estaciones d01', marker = 's', color = 'dimgrey')
#        ax1.errorbar(base_2.ix_1, base_2.otras_d02_mean, yerr=base_2.otras_d02_std, linestyle='-', label = 'Otras estaciones d02', marker = '^', color = 'dimgrey')
#
#
#        ax1.errorbar(base_2.ix_1, base_2.ideam_c1, linestyle='--', label = 'ideam-colombia d01', marker = 'D', color = 'dimgray')
#        ax1.errorbar(base_2.ix_1, base_2.ideam_c2, linestyle='--', label = 'ideam-colombia d02', marker = 'v', color = 'dimgray')
#        ax1.errorbar(base_2.ix_1, base_2.ideam_i1, linestyle='-', label = 'icm d01', marker = 's', color = 'black')
#        ax1.errorbar(base_2.ix_1, base_2.ideam_i2, linestyle='-', label = 'icm d02', marker = '^', color = 'black')
#        #ax1.errorbar(base_2.ix_1, base_2.ideam_d01_mean, yerr=base_2.ideam_d01_std, linestyle='-', label = 'Tiba estaciones d01', marker = 's', color = 'black')
#        #ax1.errorbar(base_2.ix_1, base_2.ideam_d02_mean, yerr=base_2.ideam_d02_std, linestyle='-', label = 'Tiba estaciones d02', marker = '^', color = 'black')
##                if caso[-3:] == 'd01':
##                    mar_1 = 's'
##                else:
##                    mar_1 = '^'
##                    
##                if caso[6:-4] == 'icm':
##                    col_2 = 'black'
##                else:
##                    col_2 = 'dimgrey'
##
##                if ll[9:16] == 'ideam-c':
##                    wrf = 'ideam_c'
##                else:
##                    wrf = 'ideam_i'
#        ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size':6})
#        #ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H"))
#
#        ax1.hlines(y = 0, xmin = base_2.ix_1.min(), xmax = base_2.ix_1.max(), linestyle = ':', color = 'silver')
#        ax1.xaxis.set_ticks(np.arange(1, 25, 1))
#        ax1.set_xticklabels(base_2.hora.tolist(), rotation = 90)
#        ax1.set_xlabel('Hora')
#        fig1.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/prabha/grafica4abcd_final/'+nombre[:-4]+'.png')
#
#grafica_casos()






#################################
### Gráfica tipo 7
#################################

def grafica7():
    # Gráficas de la temperatura para sólo la temperatura en el numeral a de la figura 4
    for i in ['200702','201408','201508','201509']:
        print(i)
        os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_estaciones_dominios/tablas_series_'+i)
        lista_archivos = pd.DataFrame({'col_1':os.listdir()})
        lista_tmp = lista_archivos[lista_archivos.col_1.str.contains('.csv')]
        #horas_6 = ['6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','0','1','2','3','4','5']
        #lista_horas = ['2','2','2','2','2','2','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
        #lista_horas = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0,1,1,2,3,4,5,6]
        #fechas_horas = pd.to_datetime(lista_horas, format = '%d')
        #fechas_horas = pd.to_datetime(horas_6, format = '%H')
        #horas_3 = []
        #for xx in lista_horas:
        #    adicional = pd.Timedelta(xx + ' hours')
        #    horas_3.append(adicional)
        #horas_4 = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22']


        a_d = pd.to_datetime('20000101 6:00')
        b_d = pd.to_datetime('20000102 6:00')
        horas_3 = []
        while a_d < b_d:
            horas_3.append(a_d)
            a_d += pd.Timedelta('1 hours') 



        #Gráficas

        for j in lista_tmp.col_1:

            print(j)
            base = pd.read_csv(j)
            if len(base) < 10:
                continue

            fig1 = plt.figure()
            ax1 = fig1.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
            #fig2 = plt.figure()
            #ax2 = fig2.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
            #fig3 = plt.figure()
            #ax3 = fig3.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
            #fig4 = plt.figure()
            #ax4 = fig4.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
            #Usado para sacar los valores que de icm y de Colombia
            lista_loop = base.columns[base.columns.str.contains('ideam')]
            lista_loop_2 = lista_loop[lista_loop.str.contains('icm') | lista_loop.str.contains('colombia')]
            for ll in lista_loop_2.tolist():
                cod = ll[0:8]
                caso = ll[9:]
                if i == '201408':
                    caso = ll[11:]
                print(ll)
                base.date = pd.to_datetime(base.date)
                base['hora'] = base.date.dt.hour
                pdb.set_trace()
                
                plt.plot()
                ###Gráfica de las comparaciones entre estaciones
                base['tmp_mbe'] = base[ll] - base.tmp_2m
                base_mbe = base.groupby('hora').sum()[['frec', 'tmp_mbe']].reset_index()
                base_mbe['plot_mbe'] = base_mbe.tmp_mbe / base_mbe.frec
                

                ax1.plot_date(base_mbe.date_1, base_mbe.plot_mbe, '-', label = caso, marker = mar_1, color = col_2)
                ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size':6})
                ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H"))

            ax1.hlines(y = 0, xmin = base_mbe.date_1.min(), xmax = base_mbe.date_1.max(), linestyle = ':', color = 'silver')
            fig1.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/prabha/grafica4/'+'mbe_'+str(i)+'_'+j[0:8]+'.png')

grafica7()
