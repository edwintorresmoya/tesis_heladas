import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as PLT
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam')
from taylor_diagram_mod import diagrama_taylor


recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_201509.csv')       
recep_t = recep_t.sort_values('suma_esc', ascending=False)
recep_t = recep_t[recep_t.r2 > 0]
recep_t = recep_t.reset_index()
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
    para_t1 = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
    
    
    
    for coun, uu in enumerate(range(0, (len(para_t1) //5) +2)):
        print(coun, uu)
        para_t = para_t1.iloc[(5*uu):((5*uu)+ 5),:]
        #print(para_t)
        
        #para_t = para_t.sort_values(['tipo_1','dom_1'])
        para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
        
        para_t['orden'] = para_t.tipo_1.str[-2:]
        para_t = para_t.sort_values(['orden', 'tipo_1'])
        
        if len(para_t) < 2:
            continue
        PLT.rcParams["figure.figsize"] = (8,5)
        diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
                        para_t.std_pura.iloc[0], # se toma la desviación estándar real
                        '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
        
        
        PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/taylor_simulaciones/201509_5_m/taylor_'+str(coun)+'_'+ str(i)[:-2]+'.png', dpi = 100)
        PLT.close()
    
os.system('spd-say "22222222222222222222222"')