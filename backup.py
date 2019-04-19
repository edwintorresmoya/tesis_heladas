import pandas as pd
import os
import pdb
from numba import jit
from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt
from funciones import un_busca_cod
import matplotlib.dates as mdates

@jit
###Como obtener las gráficas fig 2a

#def grafica2a():
#    start = timer()
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




def grafica4bcd():
    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/comparacion_grafica_otras_var/tablas')
    lista_archivos = pd.DataFrame({'col_1':os.listdir()})
    lista_tmp = lista_archivos[lista_archivos.col_1.str.contains('.csv')]
    lista_tmp['year_1'] = lista_tmp.col_1.str[0:6]
    lista_tmp['cod'] = lista_tmp.col_1.str[7:15]
    lista_tmp['wrf'] = lista_tmp.col_1.str[16:23]
    lista_tmp['dom'] = lista_tmp.col_1.str[24:27]
    lista_tmp['tipo'] = lista_tmp.col_1.str[27:-4]


    ##Usado para sacar las fechas para los plots
    a_d = pd.to_datetime('20000100 6:00')
    b_d = pd.to_datetime('20000102 6:00')
    horas_3 = []
    while a_d < b_d:
        horas_3.append(a_d)
        a_d += pd.Timedelta('1 hours') 

    for year_1 in lista_tmp.year_1.unique().tolist():
        for cod in lista_tmp.cod.unique().tolist():
            for wrf in lista_tmp.wrf.unique().tolist():
                for col, tipo in zip(['Td', 'wb', 'vel_vi10'],
                        ['dewpoint', 'wetbulb', 'vel_viento']):

                    #for col, tipo in zip(['hum_2m', 'rad_1', 'precip_1', 'Td', 'wb', 'vel_vi10'],
                    #        ['humedad','radiacion','rain', 'dewpoint', 'wetbulb', 'vel_viento']):
                    archivo = year_1 + '_' + cod + '_' +wrf+'_d01'+ tipo + '.csv'
                    if(archivo not in lista_tmp.col_1.tolist()):
                        continue

                    archivo_dom1 = year_1 + '_' + cod + '_' +wrf+'_d01'+ tipo + '.csv'
                    archivo_dom2 = year_1 + '_' + cod + '_' +wrf+'_d02'+ tipo + '.csv'

                    #Leer los archivos
                    base1 = pd.read_csv(archivo_dom1)
                    base2 = pd.read_csv(archivo_dom2)
                    if len(base) < 10:
                        continue
                    
                    print(archivo)
    
    
                    fig1 = plt.figure()
                    ax1 = fig1.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
                    fig2 = plt.figure()
                    ax2 = fig2.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
                    fig3 = plt.figure()
                    ax3 = fig3.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
                    fig4 = plt.figure()
                    ax4 = fig4.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
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
                        base['frec'] = 1
                        ###MBE
                        base['tmp_mbe'] = base[ll] - base.tmp_2m
                        base_mbe = base.groupby('hora').sum()[['frec', 'tmp_mbe']].reset_index()
                        base_mbe['plot_mbe'] = base_mbe.tmp_mbe / base_mbe.frec
                        
                        ###MAE
                        base['tmp_mae'] = abs(base[ll] - base.tmp_2m)
                        base_mae = base.groupby('hora').sum()[['frec', 'tmp_mae']].reset_index()
                        base_mae['plot_mae'] = base_mae.tmp_mae / base_mae.frec
                        
                        ##RMSE
                        base['tmp_rmse'] = (base[ll] - base.tmp_2m)**2
                        base_rmse = base.groupby('hora').sum()[['frec', 'tmp_rmse']].reset_index()
                        base_rmse['plot_rmse'] = base_rmse.tmp_rmse / base_rmse.frec
        
                        ##Pearson
                        pearson = base.tmp_2m.corr(base[ll])
        
                        ## d
                        xo = base[ll]
                        
                        d = 1 - sum(((xo - base.tmp_2m.mean()) - (base.tmp_2m - base.tmp_2m.mean()))**2
                                ) /  sum((abs(xo - base.tmp_2m.mean()) - abs(base.tmp_2m - base.tmp_2m.mean()))**2)
        
        
                        if caso[-3:] == 'd01':
                            mar_1 = 's'
                        else:
                            mar_1 = '^'
                            
                        if caso[6:-4] == 'icm':
                            col_2 = 'black'
                        else:
                            col_2 = 'dimgrey'
        
                        fecha_1 = []
                        for oo in base_mbe.hora:
                            print(oo)
                            if oo < 6:
                                fecha_1.append(pd.to_datetime(oo, format ='%H') + pd.Timedelta('1 days'))
                            else:
                                fecha_1.append(pd.to_datetime(oo, format ='%H'))
                        base_mbe['date_1'] = fecha_1
                        base_mbe = base_mbe.sort_values('date_1')
        
                        ax1.plot_date(base_mbe.date_1, base_mbe.plot_mbe, '-', label = caso, marker = mar_1, color = col_2)
                        ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size':6})
                        ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H"))
        
                    ax1.hlines(y = 0, xmin = base_mbe.date_1.min(), xmax = base_mbe.date_1.max(), linestyle = ':', color = 'silver')
                    fig1.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/prabha/grafica4/'+'mbe_'+str(i)+'_'+j[0:8]+'.png')
    
    grafica4a()
