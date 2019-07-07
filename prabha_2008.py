import pandas as pd
import os
import pdb
#from numba import jit
from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt
from funciones import un_busca_cod
from funciones import busca_cod
import matplotlib.dates as mdates

###Como obtener las gráficas fig 2a

#def grafica2a():
#    aaa = 0
#    ## Lista de los marcadores
#    lista_marcadores = ".",",","o","v","^","<",">","1","2","3","4","8","s","p","P","*","h","H","+","x","X","D","d","|","_"
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
#    ax2 = fig2.add_axes([0.12, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
#    for i in lista_tmp.col_1:
#        print(i)
#        base = pd.read_csv(i)
#        base = base[base.val_tmp == 0]
#        if len(base)<10:
#            continue
#        else:
#            aaa += 1
#            print('conteo ',aaa)
#        base.date = pd.to_datetime(base.date)
#
############
#        min_d = base.date.min()
#        max_d = base.date.max()
#        fecha_i = pd.to_datetime(str(min_d)[0:13])
#        fecha_f = pd.to_datetime(str(max_d)[0:13])
#        fechas_d = pd.DataFrame({'date':[]})
#        fechas_d.date = pd.date_range(fecha_i, fecha_f, freq="60min")
#        base = pd.merge(base, fechas_d, how='inner', on='date')    
##############
#        base['year_1'] = base.date.dt.year
#        base_0 = base
#        base_20 = base
#
#        base_0['cond_1'] = np.where(base.tmp_2m > 0, 0, 1).tolist() # si la temperatura es menor a 0 entonces se convierte en 1 para ser sumado
#        base_plot0 = base_0.groupby(base_0.year_1).sum()[['cond_1']].reset_index()
#        base_plot0.year_1 = pd.to_datetime(base_plot0.year_1, format='%Y')
#
#        #Gráficas de las heladas
#        ax.plot_date(base_plot0.year_1, base_plot0.cond_1, '-', label = un_busca_cod(i[2:10]), marker = lista_marcadores[aaa])
#        ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size':6})
#        ax.set_xlabel('Año')
#        ax.set_ylabel('Número de horas bajo 0°C')
#
#        
#        base_20['cond_1'] = np.where(base.tmp_2m < 25, 0, 1).tolist() # si la temperatura es menor a 0 entonces se convierte en 1 para ser sumado
#        base_plot0 = base_20.groupby(base_20.year_1).sum()[['cond_1']].reset_index()
#        base_plot0.year_1 = pd.to_datetime(base_plot0.year_1, format='%Y')
#        # se va a hacer una resta de todos los valores de temperatura
#
#        #Gráficas de las heladas
#        ax2.plot_date(base_plot0.year_1, base_plot0.cond_1, '-', label = un_busca_cod(i[2:10],), marker = lista_marcadores[aaa])
#        ax2.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size':6})
#        ax2.set_xlabel('Año')
#        ax2.set_ylabel('Número de horas sobre 25°C')
#
#    fig.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/grafica2/bajas_tmp.png')
#    fig2.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/grafica2/altas_tmp.png')
#    #plt.show()
#    
#    print('tiempo->',(timer() - start))
#grafica2a()

##Gráficas de la figura 4

def grafica4a():
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
            fig1.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/grafica4/'+'mbe_'+str(i)+'_'+j[0:8]+'.png')

grafica4a()




def grafica4bcd():
    ## Gráfica de las subgráficas bcd
    start = timer()
    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/comparacion_grafica_otras_var/tablas')
    lista_archivos = pd.DataFrame({'col_1':os.listdir()})
    lista_tmp = lista_archivos[lista_archivos.col_1.str.contains('.csv')]
    lista_tmp['year_1'] = lista_tmp.col_1.str[0:6]
    lista_tmp['cod'] = lista_tmp.col_1.str[7:15]
    lista_tmp['wrf'] = lista_tmp.col_1.str[16:23]
    lista_tmp['dom'] = lista_tmp.col_1.str[24:27]
    #lista_tmp['tipo'] = lista_tmp.col_1.str[27:-4]


    ##Usado para sacar las fechas para los plots

    for year_1 in lista_tmp.year_1.unique().tolist():
        for cod in lista_tmp.cod.unique().tolist():
            for col, tipo in zip(['Td', 'wb', 'vel_vi10'],#datos reales
                    ['dewpoint', 'wetbulb', 'vel_viento']):#Datos modelados

                # Filtro para que no cree gráficas vacias
                archivo1 = year_1 + '_' + cod + '_ideam_i'+'_d01'+ tipo + '.csv'
                # 200702_21206790_ideam_c_d01dewpoint.csv
                if(archivo1 not in lista_tmp.col_1.tolist()):
                    print('salto')
                    continue

                fig1 = plt.figure()
                ax1 = fig1.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas

                for wrf in lista_tmp.wrf.unique().tolist():
                    for dom in lista_tmp.dom.unique().tolist():
                        archivo = year_1 + '_' + cod + '_' +wrf+'_'+dom+ tipo + '.csv'
                        # 200702_21206790_ideam_c_d01dewpoint.csv
                        if(archivo not in lista_tmp.col_1.tolist()):
                            print('salto')
                            continue
                        print(archivo)
                        #Leer los archivos
                        base = pd.read_csv(archivo)
                        if len(base) < 10:
                            continue
                        
                        print(archivo)
        
        
                        #fig2 = plt.figure()
                        #ax2 = fig2.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
                        #fig3 = plt.figure()
                        #ax3 = fig3.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
                        #fig4 = plt.figure()
                        #ax4 = fig4.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
                        ##Usado para sacar los valores que de icm y de Colombia
                        #lista_loop = base.columns[base.columns.str.contains('ideam')]
                        #lista_loop_2 = lista_loop[lista_loop.str.contains('icm') | lista_loop.str.contains('colombia')]
                        base.date = pd.to_datetime(base.date)
                        base['hora'] = base.date.dt.hour
                        base['frec'] = 1
                        ###MBE
                        base['tmp_mbe'] = base[tipo] - base[col]
                        base_mbe = base.groupby('hora').sum()[['frec', 'tmp_mbe']].reset_index()
                        base_mbe['plot_mbe'] = base_mbe.tmp_mbe / base_mbe.frec
                        
                        ###MAE
                        base['tmp_mae'] = abs(base[tipo] - base[col])
                        base_mae = base.groupby('hora').sum()[['frec', 'tmp_mae']].reset_index()
                        base_mae['plot_mae'] = base_mae.tmp_mae / base_mae.frec
                        
                        ##RMSE
                        base['tmp_rmse'] = (base[tipo] - base[col])**2
                        base_rmse = base.groupby('hora').sum()[['frec', 'tmp_rmse']].reset_index()
                        base_rmse['plot_rmse'] = base_rmse.tmp_rmse / base_rmse.frec
            
                        ##Pearson
                        pearson = base[col].corr(base[tipo])
            
                        ## d
                        xo = base[tipo]
                        
                        d = 1 - sum(((xo - base[col].mean()) - (base[col] - base[col].mean()))**2
                                ) /  sum((abs(xo - base[col].mean()) - abs(base[col] - base[col].mean()))**2)
            
            
                        if dom == 'd01':
                            mar_1 = 's'
                        else:
                            mar_1 = '^'
                            
                        if wrf == 'ideam_c':
                            col_2 = 'black'
                            modelacion = 'ideam_colombia_'
                        else:
                            col_2 = 'dimgrey'
                            modelacion = 'ideam_icm_'
            
                        fecha_1 = []
                        for oo in base_mbe.hora:
                            print(oo)
                            if oo < 6:
                                fecha_1.append(pd.to_datetime(oo, format ='%H') + pd.Timedelta('1 days'))
                            else:
                                fecha_1.append(pd.to_datetime(oo, format ='%H'))
                        base_mbe['date_1'] = fecha_1
                        base_mbe = base_mbe.sort_values('date_1')

            
                        ax1.plot_date(base_mbe.date_1, base_mbe.plot_mbe, '-', label = (modelacion + dom), marker = mar_1, color = col_2)
                        ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size':6})
                        ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H"))
                
                ax1.hlines(y = 0, xmin = base_mbe.date_1.min(), xmax = base_mbe.date_1.max(), linestyle = ':', color = 'silver')
                fig1.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/grafica4bcd/'+year_1+'_'+cod+'_'+tipo+'.png')
    print('tiempo->',(timer() - start))        
grafica4bcd()




def tabla4bcd():
    # Usado para sacar las tablas unidas que se van a plotear que serían iguales a las gráficas 4 del artículo
    # Gráficas de otras variables diferenta a la temperatura

    start = timer()
    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/comparacion_grafica_otras_var/tablas')
    lista_archivos = pd.DataFrame({'col_1':os.listdir()})
    lista_tmp = lista_archivos[lista_archivos.col_1.str.contains('.csv')]
    lista_tmp['year_1'] = lista_tmp.col_1.str[0:6]
    lista_tmp['cod'] = lista_tmp.col_1.str[7:15]
    lista_tmp['wrf'] = lista_tmp.col_1.str[16:23]
    lista_tmp['dom'] = lista_tmp.col_1.str[24:27]
    #lista_tmp['tipo'] = lista_tmp.col_1.str[27:-4]


    ##Usado para sacar las fechas para los plots

    for year_1 in lista_tmp.year_1.unique().tolist():
        for col, tipo in zip(['Td', 'wb', 'vel_vi10'],#datos reales
                ['dewpoint', 'wetbulb', 'vel_viento']):#Datos modelados
            base_v = pd.DataFrame({'hora':np.arange(0,23).tolist()})
            for cod in lista_tmp.cod.unique().tolist():

                # Filtro para que no cree gráficas vacias
                archivo1 = year_1 + '_' + cod + '_ideam_i'+'_d01'+ tipo + '.csv'
                # 200702_21206790_ideam_c_d01dewpoint.csv
                if(archivo1 not in lista_tmp.col_1.tolist()):
                    print('salto')
                    continue

                #fig1 = plt.figure()
                #ax1 = fig1.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas

                for wrf in lista_tmp.wrf.unique().tolist():
                    for dom in lista_tmp.dom.unique().tolist():
                        archivo = year_1 + '_' + cod + '_' +wrf+'_'+dom+ tipo + '.csv'
                        # 200702_21206790_ideam_c_d01dewpoint.csv
                        if(archivo not in lista_tmp.col_1.tolist()):
                            print('salto')
                            continue
                        print(archivo)
                        #Leer los archivos
                        base = pd.read_csv(archivo)
                        if len(base) < 10:
                            continue
                        
                        print(archivo)
        
        
                        if dom == 'd01':
                            mar_1 = 's'
                        else:
                            mar_1 = '^'
                            
                        if wrf == 'ideam_c':
                            col_2 = 'black'
                            modelacion = 'ideam_colombia_'
                        if wrf == 'ideam_3':
                            col_2 = 'blue'
                            modelacion = 'ideam_icm_3_'
                        else:
                            col_2 = 'dimgrey'
                            modelacion = 'ideam_icm_'
            
                        #fig2 = plt.figure()
                        #ax2 = fig2.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
                        #fig3 = plt.figure()
                        #ax3 = fig3.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
                        #fig4 = plt.figure()
                        #ax4 = fig4.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
                        ##Usado para sacar los valores que de icm y de Colombia
                        #lista_loop = base.columns[base.columns.str.contains('ideam')]
                        #lista_loop_2 = lista_loop[lista_loop.str.contains('icm') | lista_loop.str.contains('colombia')]
                        base.date = pd.to_datetime(base.date)
                        ################ ADición para cambio de profesora Astrid

                        base = base[(base.date >= base.date[0]) & (base.date < (base.date[0] + pd.Timedelta('1 days')))]

                        #### Fin de la adición 
                        base['hora'] = base.date.dt.hour
                        base['frec'] = 1
                        ###MBE
                        base['tmp_mbe'] = base[tipo] - base[col]
                        base_mbe = base.groupby('hora').sum()[['frec', 'tmp_mbe']].reset_index()
                        base_mbe['plot_mbe'] = base_mbe.tmp_mbe / base_mbe.frec
                        base_mbe.columns.values[3] = cod+'_'+wrf+'_'+dom
                        base_v = pd.merge(base_mbe[['hora', cod+'_'+wrf+'_'+dom]], base_v, on='hora', how='outer')
            base_v.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/tablas4/'+year_1+'_'+col+'.csv')            
tabla4bcd()



def tablas4a():
    # Tablas de la temperatura que serán de utilidad para sacar las gráficas
    # gráficas de la temperatura
    # Es una función que regresa las tablas del mbe índice para ser ploteadas
    for i in ['201602','201712','200702','201408','201508','201509']:
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


        #Gráficas

        base_v = pd.DataFrame({'hora':np.arange(0,23).tolist()})
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
                ###################
                if caso[-3:] == 'd01':
                    mar_1 = 's'
                else:
                    mar_1 = '^'
                    
                if caso[6:-4] == 'icm':
                    col_2 = 'black'
                else:
                    col_2 = 'dimgrey'

                if ll[9:16] == 'ideam-c':
                    wrf = 'ideam_c'
                else:
                    wrf = 'ideam_i'

                #####################
                base.date = pd.to_datetime(base.date)
                ################ ADición para cambio de profesora Astrid

                base = base[(base.date >= base.date[0]) & (base.date < (base.date[0] + pd.Timedelta('1 days')))]

                #### Fin de la adición 
                base['hora'] = base.date.dt.hour
                base['frec'] = 1
                ###MBE
                base['tmp_mbe'] = base[ll] - base.tmp_2m
                base_mbe = base.groupby('hora').sum()[['frec', 'tmp_mbe']].reset_index()
                base_mbe['plot_mbe'] = base_mbe.tmp_mbe / base_mbe.frec
                base_mbe.columns.values[3] = cod+'_'+wrf+'_'+caso[-3:]
                base_v = pd.merge(base_mbe[['hora', cod+'_'+wrf+'_'+caso[-3:]]], base_v, on='hora', how='outer')
        base_v.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/tablas4/'+i+'_tmp_2m'+'.csv')            
tablas4a()


################################
## Gráfica tipo 4
################################

def grafica_casos():
    #### Script creado para hacer las gráficas de la totalidad de los datos
    #### La columna llamada ideam es la que tiene los valores de la estación automática Tibaitatá
    #### El Grupo de estaciones corresponde a la configuración icm
    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/prabha/tablas4')
    lista = pd.DataFrame({'col_1':os.listdir()})
    print('hola')
    lista['year_1'] = lista.col_1.str[0:6]
    lista['var_1'] = lista.col_1.str[7:-4]
    for nombre, year_1, var_1 in zip(lista.col_1, lista.year_1, lista.var_1):

        base = pd.read_csv(nombre)
        if len(base.columns[base.columns.str.contains('21206990')]) < 1:

            base_ideam_i1 = base[base.columns[base.columns.str.contains('24015110_ideam_i_d01')].tolist()]
            base_ideam_i2 = base[base.columns[base.columns.str.contains('24015110_ideam_i_d02')].tolist()]
            base_ideam_c1 = base[base.columns[base.columns.str.contains('24015110_ideam_c_d01')].tolist()]
            base_ideam_c2 = base[base.columns[base.columns.str.contains('24015110_ideam_c_d02')].tolist()]
            base_ideam_31 = base[base.columns[base.columns.str.contains('24015110_ideam_3_d01')].tolist()]
            base_ideam_32 = base[base.columns[base.columns.str.contains('24015110_ideam_3_d02')].tolist()]
            base_otras1 = base[base.columns[~base.columns.str.contains('24015110')].tolist()]
        else:

            base_ideam_i1 = base[base.columns[base.columns.str.contains('21206990_ideam_i_d01')].tolist()]
            base_ideam_i2 = base[base.columns[base.columns.str.contains('21206990_ideam_i_d02')].tolist()]
            base_ideam_c1 = base[base.columns[base.columns.str.contains('21206990_ideam_c_d01')].tolist()]
            base_ideam_c2 = base[base.columns[base.columns.str.contains('21206990_ideam_c_d02')].tolist()]
            base_ideam_31 = base[base.columns[base.columns.str.contains('21206990_ideam_3_d01')].tolist()]
            base_ideam_32 = base[base.columns[base.columns.str.contains('21206990_ideam_3_d02')].tolist()]
            base_otras1 = base[base.columns[~base.columns.str.contains('21206990')].tolist()]

        # Se seleccionan los valores de la columna que tengan sólo ideam-i = icm
        base_otras = base_otras1[base_otras1.columns[base_otras1.columns.str.contains('ideam_i')].tolist()]

        #base_ideam_d02_mean =  base_ideam[base_ideam.columns[base_ideam.columns.str.contains('d02')].tolist()].mean(axis=1)
        #base_ideam_d01_mean =  base_ideam[base_ideam.columns[base_ideam.columns.str.contains('d01')].tolist()].mean(axis=1)
        base_otras_d01_mean = base_otras[base_otras.columns[~base_otras.columns.str.contains('d01')].tolist()].mean(axis=1)
        base_otras_d02_mean = base_otras[base_otras.columns[~base_otras.columns.str.contains('d02')].tolist()].mean(axis=1)

        #base_ideam_d02_std = base_ideam[base_ideam.columns[base_ideam.columns.str.contains('d02')].tolist()].std(axis=1)
        #base_ideam_d01_std = base_ideam[base_ideam.columns[base_ideam.columns.str.contains('d02')].tolist()].std(axis=1)
        base_otras_d01_std = base_otras[base_otras.columns[~base_otras.columns.str.contains('d01')].tolist()].std(axis=1)
        base_otras_d02_std = base_otras[base_otras.columns[~base_otras.columns.str.contains('d02')].tolist()].std(axis=1)

        base_2 = pd.concat([base.hora, base_ideam_i1, base_ideam_i2, base_ideam_c1, base_ideam_c2, base_ideam_31, base_ideam_32, base_otras_d01_mean, base_otras_d02_mean, base_otras_d01_std, base_otras_d02_std, ], axis=1)

        base_2.columns.values[1:] = ['ideam_i1', 'ideam_i2', 'ideam_c1', 'ideam_c2', 'ideam_31', 'ideam_32', 'otras_d01_mean', 'otras_d02_mean', 'otras_d01_std', 'otras_d02_std']

        #base_2 = pd.concat([base.hora, base_ideam_d02_mean, base_ideam_d01_mean, base_otras_d01_mean, base_otras_d02_mean, base_ideam_d02_std, base_ideam_d01_std, base_otras_d01_std, base_otras_d02_std, ], axis=1)

        #base_2.columns.values[1:] = ['ideam_d02_mean', 'ideam_d01_mean', 'otras_d01_mean', 'otras_d02_mean', 'ideam_d02_std', 'ideam_d01_std', 'otras_d01_std', 'otras_d02_std']

        fecha_1 = []
        for oo in base.hora:
            print(oo)
            #if oo < 6:#Modificaciones antes de la profe Astrid
            if oo < 13:
                fecha_1.append(pd.to_datetime(oo, format ='%H') + pd.Timedelta('1 days'))
            else:
                fecha_1.append(pd.to_datetime(oo, format ='%H'))
        base_2['date_1'] = fecha_1
        base_2 = base_2.sort_values('date_1')

        fig1 = plt.figure()
        ax1 = fig1.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas       
        ####Se debe hacer la gráfica ya está la tabla



        base_2['ix_1'] = np.arange(1, 25)
        
        
        ax1.errorbar(base_2.ix_1, base_2.otras_d01_mean, yerr=base_2.otras_d01_std, linestyle='-', label = 'GE d01', marker = 's', color = 'forestgreen')
        ax1.errorbar(base_2.ix_1, base_2.otras_d02_mean, yerr=base_2.otras_d02_std, linestyle='-', label = 'GE d02', marker = '^', color = 'forestgreen')

        if (year_1 == '200702') & (var_1 == 'vel_vi10'):


            ax1.errorbar(base_2.ix_1, base_2.ideam_c1, linestyle='--', label = 'La Boyera ideam-colombia d01', marker = 'D', color = 'black')
            ax1.errorbar(base_2.ix_1, base_2.ideam_c2, linestyle='--', label = 'La Boyera ideam-colombia d02', marker = 'v', color = 'black')
            ax1.errorbar(base_2.ix_1, base_2.ideam_31, linestyle='-', label =  'La Boyera icm-mp_physics 3 d01', marker = 's', color = 'midnightblue')
            ax1.errorbar(base_2.ix_1, base_2.ideam_32, linestyle='-', label =  'La Boyera icm-mp_physics 3 d02', marker = '^', color = 'midnightblue')
            ax1.errorbar(base_2.ix_1, base_2.ideam_i1, linestyle='-', label =  'La Boyera icm d01', marker = 's', color = 'darkorange')
            ax1.errorbar(base_2.ix_1, base_2.ideam_i2, linestyle='-', label =  'La Boyera icm d02', marker = '^', color = 'darkorange')
        else:
            ax1.errorbar(base_2.ix_1, base_2.ideam_c1, linestyle='--', label = 'Tibaitatá ideam-colombia d01', marker = 'D', color = 'black')
            ax1.errorbar(base_2.ix_1, base_2.ideam_c2, linestyle='--', label = 'Tibaitatá ideam-colombia d02', marker = 'v', color = 'black')
            ax1.errorbar(base_2.ix_1, base_2.ideam_31, linestyle='-', label = 'Tibaitatá icm-mp_phyics 3 d01', marker = 's', color = 'midnightblue')
            ax1.errorbar(base_2.ix_1, base_2.ideam_32, linestyle='-', label = 'Tibaitatá icm-mp_phyics 3 d02', marker = '^', color = 'midnightblue')
            ax1.errorbar(base_2.ix_1, base_2.ideam_i1, linestyle='-', label = 'Tibaitatá icm d01', marker = 's', color = 'darkorange')
            ax1.errorbar(base_2.ix_1, base_2.ideam_i2, linestyle='-', label = 'Tibaitatá icm d02', marker = '^', color = 'darkorange')
        #ax1.errorbar(base_2.ix_1, base_2.ideam_d01_mean, yerr=base_2.ideam_d01_std, linestyle='-', label = 'Tiba estaciones d01', marker = 's', color = 'black')
        #ax1.errorbar(base_2.ix_1, base_2.ideam_d02_mean, yerr=base_2.ideam_d02_std, linestyle='-', label = 'Tiba estaciones d02', marker = '^', color = 'black')
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
        ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size':6})
        #ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H"))

        ax1.hlines(y = 0, xmin = base_2.ix_1.min(), xmax = base_2.ix_1.max(), linestyle = ':', color = 'silver')
        ax1.xaxis.set_ticks(np.arange(1, 25, 1))
        ax1.set_xticklabels(base_2.hora.tolist(), rotation = 90)
        ax1.set_xlabel('Hora')
        if var_1 == 'vel_vi10':
            unidades = r'$ms^{-1}$'
        else:
            unidades = '°C'

        ax1.set_ylabel('MBE('+unidades+')')
        fig1.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/grafica4abcd_final/'+nombre[:-4]+'.png')

grafica_casos()






#################################
## Gráfica tipo 7
################################

def grafica7():
    # Gráficas de la temperatura para sólo la temperatura en el numeral a de la figura 4
    for i in ['201602','201712','200702','201408','201508','201509']:
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

        for mm in ['icm_d','icm_3']:
            print(mm)
            fig1 = plt.figure()
            ax1 = fig1.add_axes([0.1, 0.13, 0.8, 0.85])
            fig2 = plt.figure()
            ax2 = fig2.add_axes([0.1, 0.13, 0.8, 0.85])
            fig3 = plt.figure()
            ax3 = fig3.add_axes([0.1, 0.13, 0.8, 0.85])
            fig4 = plt.figure()
            ax4 = fig4.add_axes([0.1, 0.13, 0.8, 0.85])
            for j in lista_tmp.col_1:

                print(j)
                base = pd.read_csv(j)
                if len(base) < 10:
                    continue
                base.date = pd.to_datetime(base.date)

                #Usado para sacar los valores que de icm y de Colombia
                lista_loop = base.columns[base.columns.str.contains('ideam')]
                lista_loop_2 = lista_loop[lista_loop.str.contains(mm) | lista_loop.str.contains('colombia')]
                #lista_loop_2 = lista_loop[lista_loop.str.contains('icm') | lista_loop.str.contains('colombia')]

                ###Gráfica de las comparaciones entre estaciones
                ax1.plot(base[(base.tmp_2m == base.tmp_2m.max())&(base.tmp_2m > 10)][lista_loop_2[0]], base[(base.tmp_2m == base.tmp_2m.max())&(base.tmp_2m > 10)].tmp_2m, 's', color = 'k', label= 'T max')
                ax1.plot(base[base.date.dt.hour == 18][lista_loop_2[0]], base[base.date.dt.hour == 18].tmp_2m, '+', color = 'k', label= 'T(1800 hrs)')
                ax1.plot(base[base.date.dt.hour == 22][lista_loop_2[0]], base[base.date.dt.hour == 22].tmp_2m, '*', color = 'k', label= 'T(2200 hrs)')
                ax1.plot(base[base.tmp_2m == base.tmp_2m.min()][lista_loop_2[0]], base[base.tmp_2m == base.tmp_2m.min()].tmp_2m, 'o', color = 'k', label= 'T min')

                ax2.plot(base[(base.tmp_2m == base.tmp_2m.max())&(base.tmp_2m > 10)][lista_loop_2[1]], base[(base.tmp_2m == base.tmp_2m.max())&(base.tmp_2m > 10)].tmp_2m, 's', color = 'k', label= 'T max')
                ax2.plot(base[base.date.dt.hour == 18][lista_loop_2[1]], base[base.date.dt.hour == 18].tmp_2m, '+', color = 'k', label= 'T(1800 hrs)')
                ax2.plot(base[base.date.dt.hour == 22][lista_loop_2[1]], base[base.date.dt.hour == 22].tmp_2m, '*', color = 'k', label= 'T(2200 hrs)')
                ax2.plot(base[base.tmp_2m == base.tmp_2m.min()][lista_loop_2[1]], base[base.tmp_2m == base.tmp_2m.min()].tmp_2m, 'o', color = 'k', label= 'T min')

                ax3.plot(base[(base.tmp_2m == base.tmp_2m.max())&(base.tmp_2m > 10)][lista_loop_2[2]], base[(base.tmp_2m == base.tmp_2m.max())&(base.tmp_2m > 10)].tmp_2m, 's', color = 'k', label= 'T max')
                ax3.plot(base[base.date.dt.hour == 18][lista_loop_2[2]], base[base.date.dt.hour == 18].tmp_2m, '+', color = 'k', label = 'T(1800) hrs')
                ax3.plot(base[base.date.dt.hour == 22][lista_loop_2[2]], base[base.date.dt.hour == 22].tmp_2m, '*', color = 'k', label = 'T(2200) hrs')
                ax3.plot(base[base.tmp_2m == base.tmp_2m.min()][lista_loop_2[2]], base[base.tmp_2m == base.tmp_2m.min()].tmp_2m, 'o', color = 'k', label= 'T min')

                ax4.plot(base[(base.tmp_2m == base.tmp_2m.max())&(base.tmp_2m > 10)][lista_loop_2[3]], base[(base.tmp_2m == base.tmp_2m.max())&(base.tmp_2m > 10)].tmp_2m, 's', color = 'k', label= 'T max')
                ax4.plot(base[base.date.dt.hour == 18][lista_loop_2[3]], base[base.date.dt.hour == 18].tmp_2m, '+', color = 'k', label= 'T(1800) hrs')
                ax4.plot(base[base.date.dt.hour == 22][lista_loop_2[3]], base[base.date.dt.hour == 22].tmp_2m, '*', color = 'k', label= 'T(2200) hrs')
                ax4.plot(base[base.tmp_2m == base.tmp_2m.min()][lista_loop_2[3]], base[base.tmp_2m == base.tmp_2m.min()].tmp_2m, 'o', color = 'k', label= 'T min')

            
            
       #    #Usado para polear sólo un lable 
            ax1.plot(base[base.date.dt.hour == 22][lista_loop_2[0]], base[base.date.dt.hour == 22].tmp_2m, '*', color = 'k', label= 'T(2200 hrs)')
            ax2.plot(base[base.date.dt.hour == 22][lista_loop_2[1]], base[base.date.dt.hour == 22].tmp_2m, '*', color = 'k', label= 'T(2200 hrs)')
            ax3.plot(base[base.date.dt.hour == 22][lista_loop_2[2]], base[base.date.dt.hour == 22].tmp_2m, '*', color = 'k', label= 'T(2200 hrs)')
            ax4.plot(base[base.date.dt.hour == 22][lista_loop_2[3]], base[base.date.dt.hour == 22].tmp_2m, '*', color = 'k', label= 'T(2200 hrs)')
            
            
            
            
            
            ax1.plot([-5, base.tmp_2m.max()],[-5, base.tmp_2m.max()], linestyle = ':', color = 'gray')
            ax2.plot([-5, base.tmp_2m.max()],[-5, base.tmp_2m.max()], linestyle = ':', color = 'gray')
            ax3.plot([-5, base.tmp_2m.max()],[-5, base.tmp_2m.max()], linestyle = ':', color = 'gray')
            ax4.plot([-5, base.tmp_2m.max()],[-5, base.tmp_2m.max()], linestyle = ':', color = 'gray')
            ax1.plot([-5, (base.tmp_2m.max()-5)],[-0, (base.tmp_2m.max())], linestyle = ':', color = 'silver')
            ax2.plot([-5, (base.tmp_2m.max()-5)],[-0, (base.tmp_2m.max())], linestyle = ':', color = 'silver')
            ax3.plot([-5, (base.tmp_2m.max()-5)],[-0, (base.tmp_2m.max())], linestyle = ':', color = 'silver')
            ax4.plot([-5, (base.tmp_2m.max()-5)],[-0, (base.tmp_2m.max())], linestyle = ':', color = 'silver')
            ax1.plot([-0, (base.tmp_2m.max())],[-5, (base.tmp_2m.max()-5)], linestyle = ':', color = 'silver')
            ax2.plot([-0, (base.tmp_2m.max())],[-5, (base.tmp_2m.max()-5)], linestyle = ':', color = 'silver')
            ax3.plot([-0, (base.tmp_2m.max())],[-5, (base.tmp_2m.max()-5)], linestyle = ':', color = 'silver')
            ax4.plot([-0, (base.tmp_2m.max())],[-5, (base.tmp_2m.max()-5)], linestyle = ':', color = 'silver')
            
            handles, labels = ax1.get_legend_handles_labels()
            ax1.legend(handles, labels[0:4])
            handles, labels = ax2.get_legend_handles_labels()
            ax2.legend(handles, labels[0:4])
            handles, labels = ax3.get_legend_handles_labels()
            ax3.legend(handles, labels[0:4])
            handles, labels = ax4.get_legend_handles_labels()
            ax4.legend(handles, labels[0:4])

            ax1.set_ylabel('Observaciones (°C)')
            ax2.set_ylabel('Observaciones (°C)')
            ax3.set_ylabel('Observaciones (°C)')
            ax4.set_ylabel('Observaciones (°C)')

            if mm == 'icm_d':
                ax1.set_xlabel('Configuración IDEAM-Colombia (°C)')
                ax2.set_xlabel('Configuración IDEAM-Colombia (°C)')
                ax3.set_xlabel('Configuración icm (°C)')
                ax4.set_xlabel('Configuración icm (°C)')
            else:
                ax1.set_xlabel('Configuración IDEAM-Colombia (°C)')
                ax2.set_xlabel('Configuración IDEAM-Colombia (°C)')
                ax3.set_xlabel('Configuración icm-mp_physics 3 (°C)')
                ax4.set_xlabel('Configuración icm-mp_physics 3 (°C)')

            if mm == 'icm_d':

                fig1.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/grafica7/'+str(i)+'_'+'ideam_c_d01.png')
                fig2.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/grafica7/'+str(i)+'_'+'ideam_c_d02.png')
                fig3.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/grafica7/'+str(i)+'_'+'ideam_i_d01.png')
                fig4.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/grafica7/'+str(i)+'_'+'ideam_i_d02.png')
            else:
                fig1.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/grafica7/'+str(i)+'_'+'ideam_c_d01.png')
                fig2.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/grafica7/'+str(i)+'_'+'ideam_c_d02.png')
                fig3.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/grafica7/'+str(i)+'_'+'ideam_3_d01.png')
                fig4.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/grafica7/'+str(i)+'_'+'ideam_3_d02.png')


grafica7()




def tablas_variables():
    # Usado para sacar las tablas unidas que se van a plotear que serían iguales a las gráficas 4 del artículo

    start = timer()
    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/comparacion_grafica_otras_var/tablas')
    lista_archivos = pd.DataFrame({'col_1':os.listdir()})
    lista_tmp = lista_archivos[lista_archivos.col_1.str.contains('.csv')]
    lista_tmp['year_1'] = lista_tmp.col_1.str[0:6]
    lista_tmp['cod'] = lista_tmp.col_1.str[7:15]
    lista_tmp['wrf'] = lista_tmp.col_1.str[16:23]
    lista_tmp['dom'] = lista_tmp.col_1.str[24:27]
    #lista_tmp['tipo'] = lista_tmp.col_1.str[27:-4]


    ##Usado para sacar las fechas para los plots

    for year_1 in lista_tmp.year_1.unique().tolist():
        for col, tipo in zip(['Td', 'wb', 'vel_vi10'],#datos reales
                ['dewpoint', 'wetbulb', 'vel_viento']):#Datos modelados
            base_v = pd.DataFrame({'hora':np.arange(0,23).tolist()})
            for cod in lista_tmp.cod.unique().tolist():

                # Filtro para que no cree gráficas vacias
                archivo1 = year_1 + '_' + cod + '_ideam_i'+'_d01'+ tipo + '.csv'
                # 200702_21206790_ideam_c_d01dewpoint.csv
                if(archivo1 not in lista_tmp.col_1.tolist()):
                    print('salto')
                    continue

                #fig1 = plt.figure()
                #ax1 = fig1.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas

                for wrf in lista_tmp.wrf.unique().tolist():
                    for dom in lista_tmp.dom.unique().tolist():
                        archivo = year_1 + '_' + cod + '_' +wrf+'_'+dom+ tipo + '.csv'
                        # 200702_21206790_ideam_c_d01dewpoint.csv
                        if(archivo not in lista_tmp.col_1.tolist()):
                            print('salto')
                            continue
                        print(archivo)
                        #Leer los archivos
                        base = pd.read_csv(archivo)
                        if len(base) < 10:
                            continue
                        
                        print(archivo)
        
        
                        if dom == 'd01':
                            mar_1 = 's'
                        else:
                            mar_1 = '^'
                            
                        if wrf == 'ideam_c':
                            col_2 = 'black'
                            modelacion = 'ideam_colombia_'
                        else:
                            col_2 = 'dimgrey'
                            modelacion = 'ideam_icm_'
            
                        #fig2 = plt.figure()
                        #ax2 = fig2.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
                        #fig3 = plt.figure()
                        #ax3 = fig3.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
                        #fig4 = plt.figure()
                        #ax4 = fig4.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
                        ##Usado para sacar los valores que de icm y de Colombia
                        #lista_loop = base.columns[base.columns.str.contains('ideam')]
                        #lista_loop_2 = lista_loop[lista_loop.str.contains('icm') | lista_loop.str.contains('colombia')]
                        base.date = pd.to_datetime(base.date)
                        base['hora'] = base.date.dt.hour
                        base['frec'] = 1
                        ###MBE
                        base['tmp_mbe'] = base[tipo] - base[col]
                        base_mbe = base.groupby('hora').sum()[['frec', 'tmp_mbe']].reset_index()
                        base_mbe['plot_mbe'] = base_mbe.tmp_mbe / base_mbe.frec
                        base_mbe.columns.values[3] = cod+'_'+wrf+'_'+dom
                        base_v = pd.merge(base_mbe[['hora', cod+'_'+wrf+'_'+dom]], base_v, on='hora', how='outer')
            base_v.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/tablas4/'+year_1+'_'+col+'.csv')            
tablas_variables()


### Frost Index

def grafica22():
    aaa = 0
    ## Lista de los marcadores
    lista_marcadores = ".",",","o","v","^","<",">","1","2","3","4","8","s","p","P","*","h","H","+","x","X","D","d","|","_"
    start = timer()
    #Gráfica de las heladas que se presentaron cada año sólo tiene en cuenta las estaciones automáticas

    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')
    lista_archivos = pd.DataFrame({'col_1':os.listdir()})
    lista_tmp = lista_archivos[lista_archivos.col_1.str.contains('tmp_2m')]
    
    #Loop entre cada uno de los archivos de temperatura
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas

    fig2 = plt.figure()
    ax2 = fig2.add_axes([0.12, 0.1, 0.6, 0.75])# 0.1 es el corrimiento y 0.6 y 0.75 son las escalas
    for i in lista_tmp.col_1:
        print(i)
        base = pd.read_csv(i)
        base = base[base.val_tmp == 0]
        if len(base)<10:
            continue
        else:
            aaa += 1
            print('conteo ',aaa)
        base.date = pd.to_datetime(base.date)
        ## sacar los datos por horas sin tener en cuenta las horas intermedias
        min_d = base.date.min()
        max_d = base.date.max()
        fecha_i = pd.to_datetime(str(min_d)[0:13])
        fecha_f = pd.to_datetime(str(max_d)[0:13])
        fechas_d = pd.DataFrame({'date':[]})
        fechas_d.date = pd.date_range(fecha_i, fecha_f, freq="60min")
        base = pd.merge(base, fechas_d, how='inner', on='date')    

        base['year_1'] = base.date.dt.year
        base_0 = base
        base_20 = base

        base_0['cond_1'] = np.where(base.tmp_2m < 0, (base.tmp_2m * -1), 0).tolist() # si la temperatura es menor a 0 entonces se convierte en 1 para ser sumado
        base_plot0 = base_0.groupby(base_0.year_1).sum()[['cond_1']].reset_index()
        base_plot0.year_1 = pd.to_datetime(base_plot0.year_1, format='%Y')

        #Gráficas de las heladas
        ax.plot_date(base_plot0.year_1, base_plot0.cond_1, '-', label = un_busca_cod(i[2:10]), marker = lista_marcadores[aaa])
        ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size':6})
        ax.set_xlabel('Año')
        ax.set_ylabel('Índice de Congelamiento (°C-horas)')

        
        base_20['cond_1'] = np.where(base.tmp_2m > 25, (base.tmp_2m - 25), 1).tolist() # si la temperatura es menor a 0 entonces se convierte en 1 para ser sumado
        base_plot0 = base_20.groupby(base_20.year_1).sum()[['cond_1']].reset_index()
        base_plot0.year_1 = pd.to_datetime(base_plot0.year_1, format='%Y')
        # se va a hacer una resta de todos los valores de temperatura

        #Gráficas de las heladas
        ax2.plot_date(base_plot0.year_1, base_plot0.cond_1, '-', label = un_busca_cod(i[2:10],), marker = lista_marcadores[aaa])
        ax2.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size':6})
        ax2.set_xlabel('Año')
        ax2.set_ylabel('Índice de Altas Temperaturas (°C-horas)')

    fig.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/grafica22/bajas_tmp.png')
    fig2.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/grafica22/altas_tmp.png')
    #plt.show()
    
    print('tiempo->',(timer() - start))
grafica22()


## Tablas de d y accuraci
#
#
#base = pd.DataFrame({'a':[0,1,3,3,4, 3,-1,20,30],'b':[0,1,2,3,4,-1, -2, 26, 27 ]})
def fx_d(observaciones, modelo):
    # Función para obtener la tabla 2 de la página 243 del art de Prabha
    d1 = 1 - sum(((modelo - observaciones.mean()) - (observaciones -observaciones.mean()))
            )**2 /sum((abs(modelo - observaciones.mean()) + abs(observaciones - observaciones.mean())))**2
    # Accuracy 0
    if d1 == 1:
        print(d1)
    a = np.where(((observaciones <= 0) & (modelo > 0)), 1, 0).sum()
    b = np.where(((observaciones > 0) &  (modelo > 0)), 1, 0).sum()
    c = np.where(((observaciones <= 0) & (modelo <= 0)),1, 0).sum()
    d = np.where(((observaciones > 0) &  (modelo <= 0)),1, 0).sum()

    if len(observaciones[observaciones < 0]) >= 1:
        acc_0 = 100*(b+c)/(a+b+c+d)
    else:
        acc_0 = np.NaN

    # Accuracy 1

    e = np.where(((observaciones <= 25) & (modelo > 25)), 1, 0).sum()
    f = np.where(((observaciones > 25) &  (modelo > 25)), 1, 0).sum()
    g = np.where(((observaciones <= 25) & (modelo <= 25)),1, 0).sum()
    h = np.where(((observaciones > 25) &  (modelo <= 25)),1, 0).sum()

    if len(observaciones[observaciones > 25]) >= 1:
        acc_25 = 100*(f+g)/(e+f+g+h)
    else:
        acc_25 = np.NaN

    ## MBE
    mbe = 1/len(observaciones) * (modelo - observaciones).sum()
    mae = 1/len(observaciones) * abs((modelo - observaciones)).sum()
    rmse = (1/len(observaciones) * ((modelo - observaciones)**2).sum())**(1/2)
    pearson = np.corrcoef(observaciones, modelo)[0,1]

    return(d1, acc_0, acc_25, mbe, mae, rmse, pearson)
#numero = fx_d(base.a, base.b)
#
#
# Tabla número 2 de Prabha

def table2():
    # usado para crear la tabla que saca la precisión y el valor de "d" para hacer las tablas
    adicionar = pd.DataFrame({'year':[],'id':[], 'd1':[], 'acc_0':[], 'acc_25':[], 'mbe':[], 'mae':[], 'rmse':[], 'pearson':[]})
    for i in ['201602','201712','200702','201408','201508','201509']:
    #for i in ['201508','201509']:
        os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_estaciones_dominios/tablas_series_'+i)
        lista_archivos2 = pd.DataFrame({'col_1':os.listdir()})
        lista_archivos = lista_archivos2[lista_archivos2.col_1.str.contains('.csv')]
        for j in lista_archivos.col_1:
            print(i)
            base = pd.read_csv(j)
            for k in base.columns[3:]:
                resultado = fx_d(base.tmp_2m, base[k])
                adicionar_1 = pd.DataFrame({'year':[i],'id':[k], 'd1':[resultado[0]], 'acc_0':[resultado[1]], 'acc_25':[resultado[2]], 'mbe':[resultado[3]], 'mae':[resultado[4]], 'rmse':[resultado[5]], 'pearson':[resultado[6]]})
                adicionar = pd.concat([adicionar, adicionar_1])
                
                
    adicionar.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/tabla2/tabla_temperatura.csv')
table2()



# Usado para hacer la tabla 4 de las siguientes variables

      
def tabla4_variables():
    # Usado para sacar las tablas unidas que se van a plotear que serían iguales a las gráficas 4 del artículo

    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/comparacion_grafica_otras_var/tablas')
    lista_archivos = pd.DataFrame({'col_1':os.listdir()})
    lista_tmp = lista_archivos[lista_archivos.col_1.str.contains('.csv')]
    #lista_tmp['year_1'] = lista_tmp.col_1.str[0:6]
    #lista_tmp['cod'] = lista_tmp.col_1.str[7:15]
    #lista_tmp['wrf'] = lista_tmp.col_1.str[16:23]
    #lista_tmp['dom'] = lista_tmp.col_1.str[24:27]
    ##lista_tmp['tipo'] = lista_tmp.col_1.str[27:-4]


    ##Usado para sacar las fechas para los plots

    adicionar = pd.DataFrame({'id':[], 'd1':[], 'acc_0':[], 'acc_25':[], 'mbe':[], 'mae':[], 'rmse':[], 'pearson':[]})
    for i in lista_tmp.col_1:
        base = pd.read_csv(i)
        for oo in base.columns:
            if oo == 'humedad':
                base['humedad'] = (base['humedad'] * 100)

        try:
            resultado = fx_d(base.iloc[:,2], base.iloc[:,3])
        except:
            continue
        adicionar_1 = pd.DataFrame({'id':[i], 'd1':[resultado[0]], 'acc_0':[resultado[1]], 'acc_25':[resultado[2]], 'mbe':[resultado[3]], 'mae':[resultado[4]], 'rmse':[resultado[5]], 'pearson':[resultado[6]]})
        adicionar = pd.concat([adicionar, adicionar_1])


    adicionar.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/tabla2/tabla_otras_var.csv')
tabla4_variables()


#############################Proceso de las tablas

def extraccion_tablas():

    base_tmp = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/tabla2/tabla_temperatura.csv')
    ## Transformar las tablas para que sea más fácil de usar
    base_tmp['cod'] = base_tmp.id.str[0:8]
    base_tmp['tipo'] = base_tmp.id.str[9:-4]
    base_tmp['dom'] = base_tmp.id.str[-3:]
    
    base_tmp_2 = busca_cod(base_tmp)
    
    ## Primer condicional
    base_filtrada = base_tmp_2[(base_tmp_2.dom == 'd02') & ((base_tmp_2.tipo == 'ideam-icm')|(base_tmp_2.tipo == 's-ideam-icm'))]
    
    for i in [201602, 201712, 200702, 201408, 201508, 201509]:
        base_tabla2 = base_filtrada[base_filtrada.year == i]
        base_tabla2.round(2).to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/tabla2/derivadas/'+str(i)+'tabla2.csv')
    
    print('hola')
    
    ## Tabla de diferentes variables a la temperatura
    base_tmp = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/tabla2/tabla_otras_var.csv')
    ## Transformar las tablas para que sea más fácil de usar
    
    base_tmp['year'] = base_tmp.id.str[0:6]
    base_tmp['cod'] = base_tmp.id.str[7:15]
    base_tmp['tipo'] = base_tmp.id.str[16:23]
    base_tmp['dom'] = base_tmp.id.str[24:27]
    base_tmp['var_1'] = base_tmp.id.str[27:-4]
    
    
    base_tmp_2 = busca_cod(base_tmp)
    
    ## Primer condicional
    base_filtrada = base_tmp_2[(base_tmp_2.dom == 'd02') & ((base_tmp_2.tipo == 'ideam_i')|(base_tmp_2.tipo == 's-ideam_i'))]
    
    for j in base_tmp.var_1.unique():
        for i in [201602, 201712, 200702, 201408, 201508, 201509]:
            base_tabla2 = base_filtrada[(base_filtrada.year == str(i)) & (base_filtrada.var_1 == j)]
            base_tabla2.round(2).to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/tabla2/derivadas/'+j+'_'+str(i)+'_tabla2.csv')

extraccion_tablas()



def table3():
    # usado para crear la tabla 3 que usa máximas, mínimas, 22 y 18 horas
    for i, j in zip(['200702','201509'],['201408','201508']):
    #for i in ['201508','201509']:
        adicionar = pd.DataFrame({'year':[],'id':[], 'd1':[], 'acc_0':[], 'acc_25':[], 'mbe':[], 'mae':[], 'rmse':[], 'pearson':[]})
        os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_estaciones_dominios/tablas_series_'+i)
        lista_archivos2 = pd.DataFrame({'col_1':os.listdir()})
        lista_archivos = lista_archivos2[lista_archivos2.col_1.str.contains('.csv')]

        os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_estaciones_dominios/tablas_series_'+j)
        lista_archivos3 = pd.DataFrame({'col_1':os.listdir()})
        lista_archivos4 = lista_archivos3[lista_archivos3.col_1.str.contains('.csv')]
        
        ## Unión de los archivos
        lista_archivos_union = pd.merge(lista_archivos, lista_archivos4, how='outer', on='col_1')

        for k in lista_archivos_union.col_1:
            try:
                base1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_estaciones_dominios/tablas_series_'+i+'/'+k)
            except:
                base1 = []

            try:
                base2 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_estaciones_dominios/tablas_series_'+j+'/'+k)
                print('paso 1')
                if j == '201408':
                    nombres_col = base2.columns.values.tolist()
                    qq = pd.DataFrame({'a':nombres_col})
                    qq = qq.a.str.replace('_s-', '_')
                    base2.columns = qq

            except:
                base2 = []
                print('paso 1')

            if (len(base1) > 1) & (len(base2)> 1):
                base = base1.append([base2])
                print('doble')
            else:
                if len(base1) > 1:
                    base = base1
                if len(base2) > 1:
                    base = base2

            
            base.date = pd.to_datetime(base.date)
            if len(base[base.date.dt.hour == 18]) < 3:# esto no se apaga en  ningún momento, es para buscar que en los días halla por lo menos más de un día
                continue

#### para usar este código se debe correr 4 veces la primera descomentariando la max y todo lo que esté en su conjunto de datos
### para usar la segunda se debe descomentarear el segundo grupo y comentarear el primer grupo

###############################################################################################

        ###### Usado para cuando se trabajó con las máximas y las mínimas ## Grupo 1
            #condicionales = base.groupby(base.date.dt.day).max()['tmp_2m'].reset_index()
            ##condicionales = base.groupby(base.date.dt.day).min()['tmp_2m'].reset_index()

            #tabla__1 = []
            #for t, y in zip(condicionales.date, condicionales.tmp_2m):
            #    tabla__1.append(base[(base.date.dt.day == t) & (base.tmp_2m == y)].index[0])
            #base = base.iloc[tabla__1,:]
        ######### -----------------

###############################################################################################

        ######### Usado para el cálculo con las horas ## Grupo 2
            base = base[base.date.dt.hour == 22]
        ######### Usado para el cálculo con las horas

###############################################################################################

            #for pp in []
            for k in base.columns[base.columns.str.contains('deam-icm_d02')]:
                resultado = fx_d(base.tmp_2m, base[k])
                adicionar_1 = pd.DataFrame({'year':[i],'id':[k], 'd1':[resultado[0]], 'acc_0':[resultado[1]], 'acc_25':[resultado[2]], 'mbe':[resultado[3]], 'mae':[resultado[4]], 'rmse':[resultado[5]], 'pearson':[resultado[6]]})
                adicionar = pd.concat([adicionar, adicionar_1])
                
                
        #pdb.set_trace()
        adicionar['cod'] = adicionar.id.str[0:8]
        adicionar = busca_cod(adicionar)
        #adicionar.round(2).to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/tabla2/tabla_tmp_tabla_3_max'+i+'_.csv')
        #adicionar.round(2).to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/tabla2/tabla_tmp_tabla_3_min'+i+'_.csv')
        
        adicionar.round(2).to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/tabla2/tabla_tmp_tabla_3_22_'+i+'_.csv')
        #adicionar.round(2).to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/prabha/tabla2/tabla_tmp_tabla_3_18_'+i+'_.csv')
        
table3()
