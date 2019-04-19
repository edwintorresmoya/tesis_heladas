
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspect
from datetime import datetime  
from datetime import timedelta
import matplotlib.dates as mdates
import pdb



def lista_nombres(base):
    base2 = pd.DataFrame(list(base))
    print(base2)
    return(base2)


variables_1 = pd.DataFrame({'vari_1':['hum_2m', 'precip_1', 'tmp_2m',  'val_rad', 'vel_vi10'], 'valida_1':['val_hum', 'val_prec', 'val_tmp', 'val_rad', 'val_vv'], 'count_1':[1,2,3,4,5],
                            'var_plot':['Humedad %', 'Precipitación mm', 'Temperatura, °C', r'$Radiación W/m^2$', 'm/s']})
variables_2 = ['val_dir']

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/bases_unidas/')
file_list = pd.DataFrame({'list_1':os.listdir()})
file_list['cod'] = file_list.list_1.str[0:8]
estacion_var = []
estacion_1 = pd.DataFrame({'date':[]})

for i, uu in zip(file_list.list_1, file_list.cod):
    #i ='21206990.pickle'
    #uu = 21206990
    print(i, uu)
    estacion_3 = pd.read_pickle(i)
    estacion_3.date = pd.to_datetime(estacion_3.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
    
    for var1, vali_1, count, var_plot in zip(variables_1.vari_1, variables_1.valida_1, variables_1.count_1, variables_1.var_plot):
        print(var1, vali_1, count, var_plot)
        #print(var1)# Usado para buscar el nombre de la variable de estudio porque como se realizó una unión entonces algunas variables se sobre escribieron
        for pp in estacion_3.columns:
            if var1 in pp:
                var2 = pp
        #if var2 in var1:
        #    continue
                    
        print(var2)
        
        if var2 in estacion_3.columns:
            #print(estacion_3[var2])
        
            x = estacion_3[(estacion_3[vali_1] == 0)].hora
            x11 = estacion_3[(estacion_3[vali_1] == 0)].hora_n
            y = estacion_3[(estacion_3[vali_1] == 0)][var2]
            
            if(len(x1) < 1):
                p_total = [0] *100
            else:
                fit = np.polyfit(x11, y, deg = 4)
                p_total = np.poly1d(fit)
            #plt.plot(x1, p_total(x1), "r--")
            
            
            # Datos sin heladas
            x = estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.heladas_antes == 0)].hora
            x1 = estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.heladas_antes == 0)].hora_n
            y = estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.heladas_antes == 0)][var2]
            
            if(len(x1) < 1):
                p_sin_hel = [0] *100
            else:
                fit = np.polyfit(x1, y, deg = 4)
                p_sin_hel = np.poly1d(fit)
            #plt.plot(x1, p_sin_hel(x1), "r--")
            
            # Datos un día antes de la helada
            x = estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.heladas_antes == 1)].hora
            x1 = estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.heladas_antes == 1)].hora_n
            y = estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.heladas_antes == 1)][var2]
            
            if(len(x1) < 1):
                p_antes = [0] *100
            else:
                fit = np.polyfit(x1, y, deg = 4)
                p_antes = np.poly1d(fit)
            #plt.plot(x, p_antes(x1), "r--")
            
            
            # Datos día de la helada
            x = estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.heladas == 1)].hora
            x1 = estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.heladas == 1)].hora_n
            y = estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.heladas == 1)][var2]
            
            if(len(x1) < 1):
                p_helada = [0] *100
            else:
                fit = np.polyfit(x1, y, deg = 4)
                p_helada = np.poly1d(fit)
            #plt.plot(x, p_helada(x1), "r--")
            
            
            ####Plot con altas temperaturas
            x = estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.altas == 1)].hora
            x1 = estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.altas == 1)].hora_n
            y = estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.altas == 1)][var2]
            
            if(len(x1) < 1):
                p_altas = [0] *100
            else:
                fit = np.polyfit(x1, y, deg = 4)
                p_altas = np.poly1d(fit)
            #plt.plot(x, p_altas(x1), "r--")
            
            
            ####Plot con altas temperaturas un día antes
            x = estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.altas_antes == 1)].hora
            x1 = estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.altas_antes == 1)].hora_n
            y = estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.altas_antes == 1)][var2]
            
            if(len(x1) < 1):
                p_altas_antes = [0] *100
            else:
                fit = np.polyfit(x1, y, deg = 4)
                p_altas_antes = np.poly1d(fit)
            #plt.plot(x, p_altas_antes(x1), "r--")
            
            
            if len((x11)) < 1:
                continue
            
            base_3 = pd.DataFrame({'rango_1':np.linspace(min(x11), max(x11), 100)})
            for pp, name_1 in zip([p_total, p_sin_hel, p_antes, p_helada, p_altas, p_altas_antes], ['p_total', 'p_sin_hel', 'p_antes', 'p_helada', 'p_altas', 'p_altas_antes']):
                if pp[1] == 0:
                    continue
                base_3[name_1] = pp(base_3.rango_1)
            if len(base_3.columns.values) < 2:
                continue
            
            
            fecha_1 = pd.to_datetime('1900-01-01 00:32:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
            
            fecha_2 = pd.to_datetime('1900-01-01 23:59:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
            
            ax = base_3.iloc[:,1:].plot()
            ax.set_ylabel(var_plot)
            plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grahelada/'+str(uu)+'_0_'+str(count)+'.png' ,dpi = 100)
            plt.close()
            base_3['date'] = pd.to_datetime(np.linspace(fecha_1.value, fecha_2.value, 100))
            
                
            ##Primera gráfica de las temperaturas
            
            ###Plot de las temperaturas totales = 1
            ###Plot de las temperaturas sin heladas = 2
            ###Plot de las temperaturas con heladas = 3
            ###Plot de las temperaturas antes de la helada = 4
            ###Plot de las temperaturas con altas temperaturas = 5
            ###Plot de las temperaturas antes de las altas temperaturas= 6
            
            
            #Plot de las temperaturas totales
            if var2 in estacion_3.columns:
                
                _=plt.rcParams["figure.figsize"] = (8,6)
                fig, ax = plt.subplots()
                ax.plot_date(estacion_3[(estacion_3[vali_1] == 0)].hora, estacion_3[(estacion_3[vali_1] == 0)][var2], markersize=5, color='gray')
                if 'p_total' in base_3.columns:
                    ax.plot_date(base_3.date,  base_3.p_total, '-', color='k')
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                _=plt.xlabel('Hora')
                _=plt.ylabel(var_plot)
                _=plt.xticks(rotation=90)
                plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grahelada/'+str(uu)+'_1_'+str(count)+'.png' ,dpi = 100)
                plt.close()
            
            
            
            #Plot de las temperaturas sin las heladas
            if 'heladas' in estacion_3.columns:
                
                fig, ax = plt.subplots()
                plt.plot_date(estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.heladas == 0)].hora, estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.heladas == 0)][var2], markersize=5, color='gray')
                if 'p_total' in base_3.columns:
                    ax.plot_date(base_3.date,  base_3.p_total, '-', color='k')
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                _=plt.xlabel('Hora')
                _=plt.ylabel(var_plot)
                _=plt.xticks(rotation=90)     
                plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grahelada/'+str(uu)+'_2_'+str(count)+'.png' ,dpi = 100)
                plt.close()
            
            
            if 'heladas' in estacion_3.columns:
                #Plot de las temperaturas en la helada
                fig, ax = plt.subplots()
                ax.plot_date(estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.heladas == 1)].hora, estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.heladas == 1)][var2], markersize=5, color='gray')
                if 'p_helada' in base_3.columns:
                    ax.plot_date(base_3.date,  base_3.p_helada, '-', color='k')
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                _=plt.xlabel('Hora')
                _=plt.ylabel(var_plot)
                _=plt.xticks(rotation=90)   
                plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grahelada/'+str(uu)+'_3_'+str(count)+'.png' ,dpi = 100)
                plt.close()        
            
            if 'heladas_antes' in estacion_3.columns:
                
                #Plot de las temperaturas antes de la helada
                fig, ax = plt.subplots()
                ax.plot_date(estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.heladas_antes == 1)].hora, estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.heladas_antes == 1)][var2], markersize=5, color='gray')
                if 'p_antes' in base_3.columns:
                    ax.plot_date(base_3.date,  base_3.p_antes, '-', color='k')
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                _=plt.xlabel('Hora')
                _=plt.ylabel(var_plot)
                _=plt.xticks(rotation=90)   
                plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_tmp_dia/'+str(uu)+'_4_'+str(count)+'.png' ,dpi = 100)
                plt.close()
            
            
            if 'altas' in estacion_3.columns:
                #Plot de las altas temperaturas altas
                fig, ax = plt.subplots()
                ax.plot_date(estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.altas == 1)].hora, estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.altas == 1)][var2], markersize=5, color='gray')
                if 'p_altas' in base_3.columns:
                    ax.plot_date(base_3.date,  base_3.p_altas, '-', color='k')
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                _=plt.xlabel('Hora')
                _=plt.ylabel(var_plot)
                _=plt.xticks(rotation=90)   
                plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grahelada/'+str(uu)+'_5_'+str(count)+'.png' ,dpi = 100)
                plt.close()
                
            
            #Plot de las temperaturas antes de la helada
            if 'altas_antes' in estacion_3.columns:
                
                fig, ax = plt.subplots()
                ax.plot_date(estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.altas_antes == 1)].hora, estacion_3[(estacion_3[vali_1] == 0)&(estacion_3.altas_antes == 1)][var2], markersize=5, color='gray')
                if 'p_antes' in base_3.columns:
                    ax.plot_date(base_3.date,  base_3.p_altas_antes, '-', color='k')
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                _=plt.xlabel('Hora')
                _=plt.ylabel(var_plot)
                _=plt.xticks(rotation=90)   
                plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grahelada/'+str(uu)+'_6_'+str(count)+'.png' ,dpi = 100)
                plt.close()
