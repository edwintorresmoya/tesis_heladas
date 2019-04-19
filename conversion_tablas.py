#Script creado para hacer las tablas que se van a usar para hacer los diagramas de Taylor para las correcciones propuestas por la profesora
import pandas as pd
import os
import pdb
pdb.set_trace()
recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem_20181124_con_correccion_3.csv')
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_estaciones_dominios')
for i in recep_t.cod_1.unique():
    print(i)
    para_t = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
    para_t['orden'] = para_t.tipo_1.str[-2:]
    para_t = para_t.sort_values(['orden', 'tipo_1'])
    para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
    if len(para_t) < 2:
        continue
    para_t.to_csv( str(i)[0:8]+'.csv')
#    PLT.rcParams["figure.figsize"] = (8,5)
#    diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
#                    para_t.std_pura.iloc[0], # se toma la desviación estándar real
#                    '  ', rango=(0, para_t.std_estandar.max()))# Se toma el código
# 
# 
#    PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_taylor_20181023/taylor_'+ str(i)[:-2]+'.png', dpi = 100)
#    PLT.close()
#
