"""
Script created to change rmse for nrmse like Astrid suggest me on 20190303
"""
import pandas as pd
import numpy as np
import os
import pdb
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam')
from funciones import regresion
from funciones import busca_cod


for i in ['200702','201408','201508','201509']:
    print(i)
    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_estaciones_dominios/tablas_series_'+i)
    lista_archivos = pd.DataFrame({'aaa':os.listdir()})
    lista_archivos_2 = lista_archivos[lista_archivos.aaa.str.contains('.csv')]
    base_salida = pd.DataFrame({'cod_1':[],'dom_1':[],'tipo_1':[],'r2':[],'rmse':[],'std_1':[],'domin_1':[],'std_pura':[],'std_estandar':[],
        'std_pura_2':[]})
    for j in lista_archivos_2.aaa:
        print(j)
        base = pd.read_csv(j)
        nombres = pd.DataFrame({'n1':base.columns.values})
        base.columns  =  nombres.n1.str.replace('pbl-5_cu-145', 'pbl-5_cu-14') # Corrección por un error
        nombres = pd.DataFrame({'n1':base.columns.values})
        for k in nombres.n1[3:]:
            print(k)
            cod_1 = k[0:8]
            dom_1 = k[-3:]
            tipo_1 = k[9:-4]
            nrmse = ((((base.tmp_2m - base[k])**2).mean())**(0.5))/(base[k].max() - base[k].min())
            r2 = base['tmp_2m'].corr(base[k])
            std_1 = base[k].std()
            std_pura = base['tmp_2m'].std()
            base_salida_1 = pd.DataFrame({'cod_1' : [cod_1], 'dom_1':dom_1, 'tipo_1':tipo_1,
                'rmse' : nrmse, 'r2':r2, 'std_pura':std_pura, 'std_estandar':std_1, 'std_pura_2':std_pura})
            base_salida = pd.concat([base_salida, base_salida_1])

    base_a = pd.DataFrame({'r2_esc':[np.NaN]})
    base_a1 = pd.DataFrame({'rmse_esc':[np.NaN]})
    base_a2 = pd.DataFrame({'std_1_esc':[np.NaN]})



    
    ############ADición de las otras columnas
    for pp in base_salida.cod_1.unique():
	    base_b = pd.DataFrame({'r2_esc':regresion(mejor=base_salida[base_salida.cod_1 == pp].r2.max(),
	              peor=base_salida[base_salida.cod_1 == pp].r2.min(),
	              base=base_salida[base_salida.cod_1 == pp].r2)})
	    base_a = pd.concat([base_a, base_b])
	
	    base_b1 = pd.DataFrame({'rmse_esc':regresion(mejor=base_salida[base_salida.cod_1 == pp].rmse.min(),
	              peor=base_salida[base_salida.cod_1 == pp].rmse.max(),
	              base=base_salida[base_salida.cod_1 == pp].rmse)})
	    base_a1 = pd.concat([base_a1, base_b1])
	
	    base_b2 = pd.DataFrame({'std_1_esc':regresion(mejor=abs(base_salida[base_salida.cod_1 == pp].std_estandar -
	                                                            base_salida[base_salida.cod_1 == pp].std_pura).min(),
	              peor=abs(base_salida[base_salida.cod_1 == pp].std_estandar -
	                                                            base_salida[base_salida.cod_1 == pp].std_pura).max(),
	              base=abs(base_salida[base_salida.cod_1 == pp].std_estandar -
	                                                            base_salida[base_salida.cod_1 == pp].std_pura))})
	    base_a2 = pd.concat([base_a2, base_b2])
	
	
	
	
    base_salida['r2_esc'] = base_a.iloc[1:,0]
    base_salida['rmse_esc'] = base_a1.iloc[1:,0]
    base_salida['std_1_esc'] = base_a2.iloc[1:,0]
    #base_salida['aaaa'] = base_a.r2_esc
    #
    #base_salida['r2_esc'] = base_salida.r2# / base_salida.r2.max()
    #base_salida['rmse_esc'] = 1-(base_salida.rmse / base_salida.rmse.max())
    #base_salida['std_1_esc'] = 1-(base_salida.std_1 / base_salida.std_1.max())
    base_salida['suma_esc'] = (base_salida['r2_esc'] + base_salida['rmse_esc'])/2 # La suma se multiplica por 2 para darle más peso



    base_salida.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_astrid_nrmse/'+i+'.csv')
