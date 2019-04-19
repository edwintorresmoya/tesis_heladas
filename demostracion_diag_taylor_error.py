#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 10:32:23 2019
Script creado para demostrar que el diagrama de Taylor tiene ciertas falencias
Un diagrama de Taylor sólo estaría usando la desviación estándar y la correlación
@author: edwin
"""
base = []
for i in recep_t.cod_1.unique():
    print(recep_t[recep_t.cod_1 == i][['cod_1', 'dom_1', 'tipo_1', 'r2', 'rmse', 'std_1', 'std_pura']].head())
    base = pd.concat(base, recep_t[recep_t.cod_1 == i].head(1))
    
############ Ejemplo creado para demostrar que el diagrama de Taylor tiene ciertas falencias

diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
                    para_t.std_pura.iloc[0], # se toma la desviación estándar real
                    'Código '+ str(i)[:-2])# Se toma el código

base_r = pd.DataFrame({'s_a':[1,2,4,4,5,4,3,5,1, 0]})

base_e = pd.DataFrame({'s_a':[1,2,3,4,5,4,3,2,1, 0], 's_b':[2,3,4,5,6,5,4,3,2,1]})
base_e = pd.DataFrame({'s_a':[1,2,3,4,5,4,3,2,1, 0], 's_b':[12,13,14,15,16,15,14,13,12,11]})
base_e = pd.DataFrame({'s_a':[1,2,3,4,5,4,3,2,1, 0], 's_b':[12,13,14,15,16,15,14,13,0,1]})



para_t1 = pd.DataFrame({'std_estandar':base_e.std(),
                        'r2':[base_r.s_a.corr(base_e.s_a), base_r.s_a.corr(base_e.s_b)],
                        'name':base_e.std().index
                        })



(((base_e['s_b'] - base_r['s_a']) **2).mean()) ** .5


diagrama_taylor(para_t1.iloc[:,[2,1,0]].reset_index().iloc[:,[1,2,3]],#Tabla usada para ingresar los valores
                    base_r.s_a.std(), # se toma la desviación estándar real
                    ' ')# Se toma el código
