import pandas as pd
import os
import pdb
import matplotlib.pyplot as plt
import pylab

for i in ['200702']:
    print(i)
    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_estaciones_dominios/tablas_series_'+i)
    lista_1 = pd.DataFrame({'aaa':os.listdir()})
    lista_2 = lista_1[lista_1.aaa.str.contains('.csv')]
    for j in lista_2.aaa:
        print(j)
        base = pd.read_csv(j)
        base.date = pd.to_datetime(base.date, format ='%Y-%m-%d %H:%M:%S', errors='coerce')
        
        plt.rcParams["figure.figsize"] = (40,40)

        fig = plt.figure()
        ax = plt.subplot(111)
        for k in  base.columns.values[3:]:
            print(k)
            ax.plot_date(base.date, base[k], '-', label = str(k))
            plt.legend()
        
        ax.plot_date(base.date, base.tmp_2m, '-', label = 'Temperatura referencia', color = 'k', linewidth=7.0)
        plt.legend()
        plt.ylabel('Temperatura °C')
        plt.xlabel('Fecha')
        plt.xticks(rotation='vertical')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_estaciones_dominios/graficas_'+i+'/'+(str(j)[0:8])+'.png', dpi = 199)
        plt.close()
