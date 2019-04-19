#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 20:13:03 2018

@author: edwin
"""

import os
import pandas as pd

import matplotlib.pyplot as plt

# =============================================================================
# os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_2005')
# 
# ########### Extracción de las estaciones con máximos y mínimos
# lista_parametros = (list(os.listdir()))
# 
# a = []
# b = []
# c = []
# 
# for u in lista_parametros[1:]:
#     print(u)
#     hyd_tiba = pd.read_csv(u)
#     hyd_tiba.date = pd.to_datetime(hyd_tiba .date, format ='%Y%m%d %H:%M:%S', errors='coerce')
#     print(u, hyd_tiba.date.max(), hyd_tiba.date.min())
#     a.append(u)
#     b.append(hyd_tiba.date.max())
#     c.append(hyd_tiba.date.min())
# 
# tabla = pd.DataFrame({'cod':a, 'max_1':b, 'min_1':c})
# 
# os.chdir('/home/edwin/Downloads')
# 
# tabla.to_csv('cod_fech_tesis.csv')
# 
# =============================================================================

tabla.min_1 < pd.to_datetime('2007-1-1 00:00:00', format ='%Y-%m-%d %H:%M:%S', errors='coerce')

for cod_est_1 in tabla[tabla.min_1 < pd.to_datetime('2007-1-1 00:00:00', format ='%Y-%m-%d %H:%M:%S', errors='coerce')].iloc[2:,0].str[0:8]:
    print(cod_est_1)
    ## Lectura de los archivos
    os.chdir('/home/edwin/wrf_b/2_resultados') #Datos reales
    
    base1 = pd.read_pickle('resumen_tmp.pickle')
    
    #os.chdir('/home/edwin/wrf_b/2_resultados/')###Datos ejemplo
    
    #os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_2005')
    
    #base1 = pd.read_pickle('resumen_tmp_agrometeo.pickle')
    
    ###############
    def lista_nombres(base):
        base2 = pd.DataFrame(list(base))
        return(base2)
    #################
    
    base2 = base1.iloc[1:,[0,1,2,3,5,7,8]]
    #Configuración de las fechas
    base2.date_1 = pd.to_datetime(base2.date_1, format ='%Y-%m-%d_%H:%M:%S', errors='coerce')
    
    base2['cod'] = base2.cod.astype(str).str[0:8]
    
    base2['tipo'] = base2.cod +'__'+ base2.parametro + '__' + base2.combinacion 
    
    base3 = base2.pivot_table(values='T2', index=['date_1'], columns=['tipo'])
    base31 = base2.pivot_table(values='T2', index=['date_1'], columns=['cod', 'parametro', 'combinacion'])
    
    #base3.to_csv('base3.csv')
    
    os.chdir('/home/edwin/wrf_b/resultados')
    base3 = pd.read_csv('base3.csv')
    base3.date_1 = pd.to_datetime(base3.date_1, format ='%Y-%m-%d %H:%M:%S', errors='coerce')
    
    base3.plot(legend=False)
    plt.savefig('salida.png', figsize=(20,10) ,dpi = 199)
    plt.close()
    
    
    # =============================================================================
    # base4 = base2.pivot_table(values='T2', index=['date_1'], columns=['cod', 'parametro', 'combinacion'])
    # 
    # base4.columns
    # 
    # base4['cod_est_1']['ra_lw_physics'].iloc[:,2].head()
    # base4['cod_est_1']['ra_sw_physics'].iloc[:,2].head()
    # base4['cod_est_1']['mp_zero_out'].iloc[:,2].head()
    # 
    # base4['21201200']['ra_lw_physics'].iloc[:,1]
    # base4['21201200']['ra_sw_physics'].iloc[:,1]
    # base4['21201200']['mp_zero_out'].iloc[:,1]
    # 
    # 
    # base4['cod_est_1']['mp_zero_out'].iloc[:,1]
    # 
    # 
    # aa = base4['cod_est_1']['mp_zero_out']
    # bb = base4['cod_est_1']['ra_lw_physics'].iloc[:,1]
    # cc = base4['cod_est_1']['mp_zero_out']
    # base4['cod_est_1', 'ra_lw_physics'].plot()
    # base4['cod_est_1', 'sf_sfclay_physics'].plot()
    # 
    # base4[['cod_est_1','21201200']].columns.values
    # base4[['cod_est_1','21201200']].columns.get_level_values(0)
    # base4[['cod_est_1','21201200']].columns.remove_unused_levels()# Mirar los niveles
    # base4[['cod_est_1','21201200'],['mp_zero_out']]
    # 
    # nombres = [col for col in base3.columns if 'cod_est_1' in col]
    # base3[nombres].plot(legend=False)
    # 
    # 
    # =============================================================================
    
    ####Selección de HYDRAS
    
    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_2005')
    hyd_tiba = pd.read_csv(cod_est_1+'.csv')
    hyd_tiba.date = pd.to_datetime(hyd_tiba .date, format ='%Y%m%d %H:%M:%S', errors='coerce')
    hyd_tiba = hyd_tiba.sort_values(by='date').reset_index(drop=True)
    
    
    print(hyd_tiba.date.max())
    print(hyd_tiba.date.min())
    
    inicio = '2007-02-01' 
    final = '2007-02-05'
    
    
    hyd_tiba[hyd_tiba.date <= pd.to_datetime(inicio + ' 0:0:0',format ='%Y%m%d %H:%M:%S', errors='coerce')]
    
    min_rang_1 = hyd_tiba[hyd_tiba.date == max(hyd_tiba[((hyd_tiba.date <= pd.to_datetime(inicio + ' 0:0:0',
                                                format ='%Y%m%d %H:%M:%S', errors='coerce')))].date)].index[0]
        
    max_rang_1 = hyd_tiba[hyd_tiba.date == min(hyd_tiba[((hyd_tiba.date >= pd.to_datetime(final + ' 0:0:0',
                                                format ='%Y%m%d %H:%M:%S', errors='coerce')))].date)].index[0]
    
    print('rango' ,(max_rang_1 - min_rang_1), '#########################')
    
    ####Unión de las temperaturas a una sola temperatura
    
    
    a = hyd_tiba[-hyd_tiba.tmp_2m.isnull()][['date','tmp_2m']]
    a.columns = ['date','tmp_2m']
    b = hyd_tiba[hyd_tiba.tmp_2m.isnull()& -hyd_tiba.tmp_2m_min.isnull()][['date','tmp_2m_min']]
    b.columns = ['date', 'tmp_2m']
    c = hyd_tiba[hyd_tiba.tmp_2m.isnull()& hyd_tiba.tmp_2m_min.isnull() & -hyd_tiba.tmp_2m_max.isnull()][['date','tmp_2m_max']]
    c.columns = ['date','tmp_2m']
    
    n_tmp = pd.concat([a,b,c])
    
    hyd_tiba_2 = pd.merge(left=hyd_tiba, right=n_tmp, on='date', how='outer')
    
    ####Final de la unión
    
    hyd_tiba_3 = hyd_tiba_2[hyd_tiba_2.tmp_2m_y.notnull()]
    hyd_tiba_3 = hyd_tiba_3[(hyd_tiba_3.tmp_2m_y < 50) & (hyd_tiba_3.tmp_2m_y > -30)].reset_index(drop=True)
    
    min_rang_2 = hyd_tiba_3[hyd_tiba_3.date == max(hyd_tiba_3[((hyd_tiba_3.date <= pd.to_datetime(inicio + ' 0:0:0',
                                                format ='%Y%m%d %H:%M:%S', errors='coerce')))].date)].index[0]
        
    max_rang_2 = hyd_tiba_3[hyd_tiba_3.date == min(hyd_tiba_3[((hyd_tiba_3.date >= pd.to_datetime(final + ' 0:0:0',
                                                format ='%Y%m%d %H:%M:%S', errors='coerce')))].date)].index[0]
    
    
    
        
    plt.plot_date(x=hyd_tiba_3.iloc[min_rang_2:max_rang_2,:].date, y=hyd_tiba_3.iloc[min_rang_2:max_rang_2,:].tmp_2m_y, linestyle='-')
    
    datos_hydras = hyd_tiba_3.iloc[min_rang_2:max_rang_2,:][['date','tmp_2m_y']]
    
    print(datos_hydras.date.max(), datos_hydras.date.min(), '#######')
    
    
    
    ### Extracciónde todas las parametrizaciones para comprar con la estación
    #base3['date'] = base3.index
    
    nombres = [col for col in base3.columns if cod_est_1 in col]
    nombres.append('date_1')
    #Ajustar los dator horarios porque los datos vienen 5 horas adelantadas porque es UTC
    base5 = base3[nombres]
    una_hora = base5['date_1'].iloc[1] - base5['date_1'].iloc[0]
    base5['date'] = base5.date_1 - (una_hora * 5)
    
    
    
    ##Unión de los datos de wrf y la estación Hydras
    
    base6 = pd.merge(left=base5, right=datos_hydras, on='date')#, how='inner')
    base6 = base6.drop(['date_1'], axis=1)
    
    
    base6.index = base6.date
    
    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph')
    
    base6.plot(legend = False)
    plt.savefig('modelos_'+cod_est_1+'_20180404.png', figsize=(20,10) ,dpi = 199)
    plt.close()

