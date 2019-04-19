#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:47:01 2019

@author: edwin
"""
import pandas as pd
base_llenar = pd.DataFrame()

for i in range(0, 10):
    base_llenar_2 = pd.DataFrame({'tmp':[10*i], 'h':[50*i], 'rad':[100*i]})
    print(base_llenar_2)
    base_llenar = base_llenar.append(base_llenar_2)

pd.to_datetime(base_validada.date, format ='%Y%m%d %H:%M:%S', errors='coerce')

anno_1 = 2007
mes = 2
dia = 7

anno_1 * 10000 + (mes * 100) + (dia)


anno_1 = '2007'
mes = '2'
dia = '7'

f_1 =  anno_1 + '0'+mes + dia

f_2 = pd.to_datetime(f_1, format ='%Y%m%d', errors='coerce')

f3 = []
f4 = []
for i in range(0, 10):
    f4.append(i)
    
    f_2 += pd.Timedelta('1 days')
    f3.append(f_2)
    
f3.append(pd.to_datetime('20070206', format ='%Y%m%d', errors='coerce'))
f4.append(-1)
    
plt.pl

plt.plot_date(f3, f4)
#plt.figure(figsize=[11, 9])

plt.xticks(rotation=90)
plt.xlabel('Fecha')
plt.ylabel('°C')
plt.axhline(0, color = 'k', linestyle = '--')
plt.axhline(20, color = 'k', linestyle = ':')
#plt.vlines(x=[fecha_inicio, fecha_final], ymin=(para_plt.tmp_2m.min() - 5), ymax=(para_plt.tmp_2m.max() + 5), color = 'black')
plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/automaticas_periodos/'+ str(j)[:-2]+'.png', dpi = 100)
plt.close()