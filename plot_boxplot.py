import pandas as pd
import pdb
import os
import matplotlib.pyplot as plt

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col1')

lista_arch = pd.DataFrame({'files_1':os.listdir()})
lista_arch['cod'] =  lista_arch.files_1.str[2:10]
lista_arch['var_1'] = lista_arch.files_1.str[11:-4]

for ii, uu in zip(lista_arch[lista_arch.var_1 == 'val_dir'].files_1, lista_arch[lista_arch.var_1 == 'val_dir'].cod):
    print(ii)
    estacion_3 = pd.read_csv(ii)
    estacion_3.date = pd.to_datetime(estacion_3.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
    estacion_3['hora_n'] = (estacion_3.date.dt.hour)


    # Plot para todos los datos
    estacion_3[(estacion_3.val_dir == 0)].boxplot(by='hora_n', column='dir_viento')
    print(len(estacion_3[(estacion_3.val_dir == -1)]), 'total de las estaciones')
    plt.xlabel('Hora')
    plt.ylabel('Dirección °')
    plt.xticks(rotation=90)
    plt.title('')
    plt.suptitle('')
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/grafica_var_dia2/'+uu+'_dir_viento'+'_1.png' ,dpi = 100)
    plt.close()

    # Plot para los días con heladas
    estacion_3[(estacion_3.val_dir == 0)&(estacion_3.heladas == 1)](by='hora_n', column='dir_viento')
    plt.xlabel('Hora')
    plt.ylabel('Dirección °')
    plt.xticks(rotation=90)
    plt.title('')
    plt.suptitle('')
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/grafica_var_dia2/'+uu+'_dir_viento'+'_3.png' ,dpi = 100)
    plt.close()



    # Plot para los días con altas temperaturas
    estacion_3[(estacion_3.val_dir == 0)&(estacion_3.altas == 1)].boxplot(by='hora_n', column='dir_viento')
    plt.xlabel('Hora')
    plt.ylabel('Dirección °')
    plt.xticks(rotation=90)
    plt.title('')
    plt.suptitle('')
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/grafica_var_dia2/'+uu+'_dir_viento'+'_5.png' ,dpi = 100)
    plt.close()

    pdb.set_trace()


print('hola')
