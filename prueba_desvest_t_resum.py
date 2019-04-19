"""
Script creado para buscar en cuál de las tablas hay una desviación estándar diferentea la que está planteada
"""

import pandas as pd
import os
import numpy as np
import pdb

b_llenar = pd.DataFrame()
for i in ['200702', '201408', '201508', '201509']:
    print(i)
    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_estaciones_dominios/tablas_resumen_'+i)
    lista_1 = pd.DataFrame({'aaa':os.listdir()})
    lista_2 = lista_1[lista_1.aaa.str.contains('csv')]
    for j in lista_2.aaa:
        print(j)
        base = pd.read_csv(j)
        for count, k in enumerate(base.std_pura):
            print(k)
            if (k != base.std_pura[0]):
                b_llenar_1 = pd.DataFrame({'year':[i], 'codigo':[j], 'parametro':[base.tipo_1[count]]})
                b_llenar = pd.concat([b_llenar, b_llenar_1])

b_llenar.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estaciones_probl_desvest.txt')
