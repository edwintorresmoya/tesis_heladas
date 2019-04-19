#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 17:09:06 2018

@author: edwin
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam'
os.chdir(path) # Cambia de directorio


ideam_rs_3_nona = pd.read_csv('ideam_zona_nonan.csv')
ideam_rs_3_nona.date = pd.to_datetime(ideam_rs_3_nona.date, format ='%Y%m%d %H:%M:%S', errors='coerce')

lista_estac = pd.read_csv('lista.des')















### Correcicones de Vickers y Mahrt
#harflaged
#Spikes less than 1%

aa = pd.DataFrame({'a':np.random.uniform(8,22,100)})

#base = pd.DataFrame({'bb' : [1, 2, 3, 4, np.NaN, 5, 6, 7, 8, 9]})
#base.bb.rolling(window=10, center=False, min_periods=1).mean()



estacion_v = ideam_rs_3_nona[ideam_rs_3_nona.cod == 21206190]
aa = estacion_v[['TS','cod']]
aa.columns.values[0] = 'a'

aa.iloc[20,0] = 35
aa
aa['b_std_mean'] = aa.a.rolling(window=9, center=True, min_periods=1).mean()
#aa['b_std'] = aa.a.rolling(window=20, center=True, min_periods=1).std()
#aa['b_std_35'] = aa.a.rolling(window=20, center=True, min_periods=1).std() * 3.5
aa['b_std_sum'] = (aa.a.rolling(window=9, center=True, min_periods=1).std() * 2.5) + aa.b_std_mean
aa['b_std_minus'] = (- aa.a.rolling(window=9, center=True, min_periods=1).std() * 2.5) + aa.b_std_mean


aa['cond'] = (aa.b_std_minus < aa.a) & (aa.a < aa.b_std_sum)

aa[aa.cond == False]


aa['cond2'] = ((- aa.a.rolling(window=9, center=True, min_periods=1).std() * 2.5) +
              aa.a.rolling(window=9, center=True, min_periods=1).mean() < aa.a) & (
                      aa.a < (aa.a.rolling(window=9, center=True, min_periods=1).std() * 2.5) + 
                      aa.a.rolling(window=9, center=True, min_periods=1).mean())
aa

aa['b_std2'] = aa.b_std.shift(periods=1)
aa['b_std3'] = aa.b_std / aa.b_std2
aa['b_mean'] = aa.a.rolling(window=5).mean(center=False)


estacion_v = ideam_rs_3_nona[(ideam_rs_3_nona.cod == 21206190) & (ideam_rs_3_nona.tipo == 1)]

aa = estacion_v.TS


base1 = pd.DataFrame({'aa' :np.random.normal(16,1.5,400)})
base2 = pd.DataFrame({'aa' :np.random.normal(20,1.5,50)})
base3 = pd.DataFrame({'aa' :np.random.normal(16,1.5,600)})

fram = [base1, base2, base3]
base3 = pd.concat(fram)
base3['std_1'] = base3.aa.rolling(window=(11)).std()
#base3['elx'] = list(np.arange(0,200))


plt.scatter(x = list(np.arange(0,1050)), y = base3.aa)
plt.scatter(x = list(np.arange(0,1050)), y = base3.std_1)
plt.axhline(y=((base3.std_1.std()*2.5) + base3.std_1.mean()), color = 'r')
plt.axhline(y=((base3.std_1.std()*2.5) + base3.std_1.median()), color = 'b')

# =============================================================================
# base3.aa.std() + base3.aa.median()
# base3.aa.std() + base3.aa.mean()
# base3.std_1.max()
# =============================================================================
cc = base3[base3.std_1 > base3.std_1.std() + base3.std_1.median()]
[base3.std_1.max() > base3.std_1.std() + base3.std_1.mean()]
base3.sort_values(by='std_1', ascending=False).head(50)


[base3.std_1 > base3.std_1.std() + base3.std_1.median()]

base3.aa.rolling(window=(11)).std() > (base3.aa.rolling(window=(11)).std().std() + base3.aa.rolling(window=(11)).std().mean())

base3

base3['sd'] = base3.aa.rolling(window=9, center=True, min_periods=1).std()
min1 = base3.sd.min()
mean1 = base3.sd.mean()


### Probar con las desviaciones estandar "Discontinuity Detection and Removal from Data Time Series"


