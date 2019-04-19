
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.gridspec as gridspect

def lista_nombres(base):
        base2 = pd.DataFrame(list(base))
        return(base2)

# Importación de datos de las estaciones automáticas
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_2005')
lista_estaciones_2 = pd.DataFrame(list(os.listdir()))

base = pd.read_csv('21206990.csv') # Estación Tibaitata automática

#Creación de una sola columna de datos de temperatura
a = base[-base.tmp_2m.isnull()][['date','tmp_2m']]
a.columns = ['date','tmp_2m']
b = base[base.tmp_2m.isnull()& -base.tmp_2m_min.isnull()][['date','tmp_2m_min']]
b.columns = ['date', 'tmp_2m']
c = base[base.tmp_2m.isnull()& base.tmp_2m_min.isnull() & -base.tmp_2m_max.isnull()][['date','tmp_2m_max']]
c.columns = ['date','tmp_2m']

n_tmp = pd.concat([a,b,c])

base_2 = pd.merge(left=base, right=n_tmp, on='date', how='outer')

#Validación de los datos por límites extremos
base_3 = base_2[base_2.tmp_2m_y.notnull()]
base_3 = base_3[(base_3.tmp_2m_y < 50) & (base_3.tmp_2m_y > -30)].reset_index(drop=True)
base_3.date = pd.to_datetime(base_3.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
base_3.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_2005/base_3.csv')
############################ Gráfica para la determinación de las estaciones que tienen mejor comportamiento


os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_validado_20180522')
for i in os.listdir():
    print(i)
    base = pd.read_csv(i)
    base.date = pd.to_datetime(base.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
    plt.plot_date(base.date, base.tmp_2m)
    plt.title(i)
    plt.legend(loc='upper right')
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas/crudas/' + i +'crudas.jpg', figsize=(20,10) ,dpi = 199)
    plt.close()
    
    
    base_3 = base[base.tmp_2m.notnull()][base.range == 0][base.tmp_2mspikes == 0][base.tmp_2m_dif == 0][base.tmp_2m_roll_1 == 0]
    
    plt.plot_date(base_3.date, base_3.tmp_2m)
    plt.title(i)
    
    plt.axhline(y=(base_3.tmp_2m.mean() + 2*base_3.tmp_2m.std()), color = 'black')
    plt.axhline(y=(base_3.tmp_2m.mean() - 2*base_3.tmp_2m.std()), color = 'black')
    plt.axhline(y=(base_3.tmp_2m.mean() + 3*base_3.tmp_2m.std()), color = 'r')
    plt.axhline(y=(base_3.tmp_2m.mean() - 3*base_3.tmp_2m.std()), color = 'r')
    plt.axhline(y=(base_3.tmp_2m.mean() + 3.5*base_3.tmp_2m.std()), color = 'navy')
    plt.axhline(y=(base_3.tmp_2m.mean() - 3.5*base_3.tmp_2m.std()), color = 'navy')
    plt.axhline(y=(base_3.tmp_2m.mean() + 4*base_3.tmp_2m.std()), color = 'goldenrod')
    plt.axhline(y=(base_3.tmp_2m.mean() - 4*base_3.tmp_2m.std()), color = 'goldenrod')
    plt.legend(loc='upper right')
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas/' + i +'.jpg', figsize=(20,10) ,dpi = 199)
    plt.close()
    
    
    base_3['dia'] = base_3.date.dt.to_period('D')
    plt.plot_date(base_3.date, base_3.tmp_2m)
    plt.title(i)
    
    max_med = base_3.groupby(['dia'])['tmp_2m'].max().median()
    max_sd = base_3.groupby(['dia'])['tmp_2m'].max().std()

    min_med = base_3.groupby(['dia'])['tmp_2m'].min().median()
    min_sd = base_3.groupby(['dia'])['tmp_2m'].min().std()
    
    
    #plt.plot_date(base_3.date, base_3.tmp_2m)
    plt.axhline(y=(max_med), color = 'black')
    plt.axhline(y=(max_med + max_sd), color = 'r')
    plt.axhline(y=(max_med + (2.5 * max_sd)), color = 'r')
    plt.axhline(y=(max_med + (max_sd*3)), color = 'goldenrod')
    
    plt.axhline(y=(min_med), color = 'black')
    plt.axhline(y=(min_med - min_sd), color = 'r')
    plt.axhline(y=(min_med - (2.5 * min_sd)), color = 'r')
    plt.axhline(y=(min_med - (min_sd*3)), color = 'goldenrod')

    plt.legend(loc='upper right')
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas/max/' + i +'.jpg', figsize=(20,10) ,dpi = 199)
    plt.close()
    
    base_3 = np.NaN 
    
    
    


os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_validado_20180522')
#base = pd.read_csv('21206990_tmp_2m.csv')


base = pd.read_csv('21206960_tmp_2m.csv')

base.date = pd.to_datetime(base.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
base_3 = base[base.tmp_2m.notnull()][base.range == 0][base.tmp_2mspikes == 0][base.tmp_2m_dif == 0][base.tmp_2m_roll_1 == 0]
base_3.date = pd.to_datetime(base_3.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
base['dia'] = base_3.date.dt.to_period('D')
base.groupby(['dia'])['tmp_2m'].max()


max_med = base.groupby(['dia'])['tmp_2m'].max().median()
max_sd = base.groupby(['dia'])['tmp_2m'].max().std()

min_med = base.groupby(['dia'])['tmp_2m'].min().median()
min_sd = base.groupby(['dia'])['tmp_2m'].min().std()

plt.plot_date(base_3.date, base_3.tmp_2m)
plt.axhline(y=(max_med), color = 'black')
plt.axhline(y=(max_med + max_sd), color = 'r')
plt.axhline(y=(max_med + (2.5 * max_sd)), color = 'r')
plt.axhline(y=(max_med + (max_sd*3)), color = 'goldenrod')

plt.axhline(y=(min_med), color = 'black')
plt.axhline(y=(min_med - min_sd), color = 'r')
plt.axhline(y=(min_med - (2.5 * min_sd)), color = 'r')
plt.axhline(y=(min_med - (min_sd*3)), color = 'goldenrod')

base[-base.tmp_2m.notnull()] #Usado para quitar los NA
base[base.range == 1] #Cuando el rando es igual a 1 esto significa que los datos está fuera de los límites
base[base.tmp_2mspikes == 1] #Cuando se presenta un spike se reporta como 1
#Inversos

base[base.tmp_2m.notnull()] #Usado para quitar los NA
base[base.range == 0] #Cuando el rando es igual a 1 esto significa que los datos está fuera de los límites
base[base.tmp_2mspikes == 0] #Cuando se presenta un spike se reporta como 1
base[base.tmp_2m_dif == 0] #Cuando se presenta un spike se reporta como 1

 
base_3 = base
plt.plot_date(base_3.date, base_3.tmp_2m)
 
 
base_3 = base[base.tmp_2m.notnull()]
plt.plot_date(base_3.date, base_3.tmp_2m)
 
base_3 = base[base.tmp_2m.notnull()][base.range == 0]
plt.plot_date(base_3.date, base_3.tmp_2m)
 

base_3 = base[base.tmp_2m.notnull()][base.range == 0][base.tmp_2mspikes == 0][base.tmp_2m_dif == 0][base.tmp_2m_roll_1 == 0]

##Buscar la ultima desviación estándar


base_3.tmp_2m

plt.plot_date(base_3.date, base_3.tmp_2m)
plt.axhline(y=(base_3.tmp_2m.mean() + 3*base_3.tmp_2m.std()), color = 'r')
plt.axhline(y=(base_3.tmp_2m.mean() - 3*base_3.tmp_2m.std()), color = 'r')
plt.hlines(y=(base_3.tmp_2m.mean), xmin=(base_3.date.min()), xmax=(base_3.date.max()))
plt.vlines(x=base_hist[base_hist.year == ii].TS.mean() , ymin=0, ymax=3000, color = c)
plt.vlines(x=base_hist[base_hist.year == ii].TS.mean() , ymin=0, ymax=3000, color = c)
inicio_1 = pd.to_datetime('2008/09/11 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fin_1 = pd.to_datetime('2008/09/13 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')



#Bajas temperaturas


resume = base_3[base_3.tmp_2m < 0][['tmp_2m', 'date']]
n_f = pd.DatetimeIndex(resume.date)
resume['year'] = n_f.year
resume['month'] = n_f.month
resume['day'] = n_f.day
resume['val'] = 1

eventos = resume.groupby(['year', 'month', 'day'])['val'].sum()
os.chdir('/home/edwin/Downloads/basura2')
#eventos.to_csv('eventos.csv')


#Altas temperaturas mayores a 20°C
#

resume2 = base_3[base_3.tmp_2m > 25][['tmp_2m', 'date']]
n_f = pd.DatetimeIndex(resume2.date)
resume2['year'] = n_f.year 
resume2['month'] = n_f.month
resume2['day'] = n_f.day
resume2['val'] = 1

eventos_altas = resume2.groupby(['year', 'month', 'day'])['val'].sum()
eventos_altas
os.chdir('/home/edwin/Downloads/basura2')
#eventos.to_csv('eventos_altas.csv')

#gra_tiem('20150907','20150909','sal_20180522') # Fecha no usada











#############Convencional Datos de las estaciones convencionales

path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam'
os.chdir(path)
conv_tiba = pd.read_csv('conv_tiba.csv')
conv_tiba.date = pd.to_datetime(conv_tiba.date, format ='%Y%m%d %H:%M:%S', errors='coerce')

conv_tiba.sort_values(by=['TS'])

##Lista de estaciones convencionales

cod_conv = pd.read_csv('codigo_est_aut_zon.csv')

ideam_rs_3_nona = pd.read_csv('ideam_zona_nonan.csv')
ideam_rs_3_nona.date = pd.to_datetime(ideam_rs_3_nona.date, format ='%Y%m%d %H:%M:%S', errors='coerce')

#estaciones de la Zona 

conv_zona = ideam_rs_3_nona[ideam_rs_3_nona.cod.isin(cod_conv.cod)]

#conv_zona.to_csv('datos_con_zona_csv') # Base creada para sacar los datos de la zona de estudio

conv_zona = pd.read_csv('datos_con_zona_csv')
conv_zona.date = pd.to_datetime(conv_zona.date, format ='%Y%m%d %H:%M:%S', errors='coerce')

#
#

###Primera fecha helada del 2007 caso 1
base_3 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/v_21206990_tmp_2m.csv')
base_3 = base_3[base_3.val_tmp == 0]
base_3.date = pd.to_datetime(base_3.date, format ='%Y-%m-%d %H:%M:%S', errors='coerce')


inicio_1 = pd.to_datetime('2007/01/31 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fin_1 = pd.to_datetime('2007/02/05 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')

base_3[(base_3.date > inicio_1) & (base_3.date < fin_1)].sort_values('tmp_2m').head() # ojo estos son sólo los primeros datos
base_3[(base_3.date > inicio_1) & (base_3.date < fin_1)].sort_values('tmp_2m').tail(50)

inicio_1 = pd.to_datetime('2007/02/03 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fin_1 = pd.to_datetime('2007/02/05 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')

conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1) & (conv_zona.TS > 20)].sort_values('TS')

print((busca_cod(conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1) & (conv_zona.TS > 20)].sort_values('TS'))[['TS', 'cod', 'Nombre', 'MPIO']]).to_latex(index=False))

conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1)][conv_zona.cod == 21205420].sort_values('TS')


inicio_1 = pd.to_datetime('2007/02/04 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fin_1 = pd.to_datetime('2007/02/05 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')

base_3[(base_3.date > inicio_1) & (base_3.date < fin_1)].sort_values('date')










###Primera fecha helada del 2014 caso 2

inicio_1 = pd.to_datetime('2014/08/29 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fin_1 = pd.to_datetime('2014/08/31 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')

base_3[(base_3.date > inicio_1) & (base_3.date < fin_1)].sort_values('tmp_2m').head()
base_3[(base_3.date > inicio_1) & (base_3.date < fin_1)].sort_values('tmp_2m').tail()

conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1)].sort_values('TS')
print((busca_cod(conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1) & (conv_zona.TS < 0.1)].sort_values('TS'))[['TS', 'cod', 'Nombre', 'MPIO']]).to_latex(index=False))
print((busca_cod(conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1) & (conv_zona.TS > 20)].sort_values('TS'))[['TS', 'cod', 'Nombre', 'MPIO']]).to_latex(index=False))


conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1)][conv_zona.cod == 21205420].sort_values('TS')



base_3[(base_3.date > inicio_1) & (base_3.date < fin_1)].sort_values('date')


#
#
# Casos de altas temperaturas
#
#

##Caso 3 Caso para el 20150907 es un caso en fechas del fenómeno del niño y corresponde al periodo más largo

###Primera fecha helada del 2009 caso 3 caso de alta temperatura en mes común
#No hay temperaturas menores a 0°C


inicio_1 = pd.to_datetime('2015/09/07 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fin_1 = pd.to_datetime('2015/09/09 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')

base_3[(base_3.date > inicio_1) & (base_3.date < fin_1)].sort_values('tmp_2m').head()

conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1) & (conv_zona.TS > 20)].sort_values('TS')
print((busca_cod(conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1) & (conv_zona.TS < 0.1)].sort_values('TS'))[['TS', 'cod', 'Nombre', 'MPIO']]).to_latex(index=False))
print((busca_cod(conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1) & (conv_zona.TS > 20)].sort_values('TS'))[['TS', 'cod', 'Nombre', 'MPIO']]).to_latex(index=False))

conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1)][conv_zona.cod == 21205420].sort_values('TS')

base_3[(base_3.date > inicio_1) & (base_3.date < fin_1)].sort_values('date')
base_3[(base_3.date > inicio_1) & (base_3.date < fin_1)].sort_values('tmp_2m')

#gra_tiem('20150907','20150909','sal_20180522') # Fecha no usada


##Caso 4 Caso para el 20150907 es un caso en fechas del fenómeno del niño y corresponde al periodo más largo

###Primera fecha helada del 2009 caso 4 caso de alta temperatura en mes común

inicio_1 = pd.to_datetime('2015/08/26 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fin_1 = pd.to_datetime('2015/08/28 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')

base_3[(base_3.date > inicio_1) & (base_3.date < fin_1)].sort_values('tmp_2m').head()

conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1) & (conv_zona.TS > 20)].sort_values('TS')
print((busca_cod(conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1) & (conv_zona.TS < 0.1)].sort_values('TS'))[['TS', 'cod', 'Nombre', 'MPIO']]).to_latex(index=False))
print((busca_cod(conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1) & (conv_zona.TS > 20)].sort_values('TS'))[['TS', 'cod', 'Nombre', 'MPIO']]).to_latex(index=False))

conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1)][conv_zona.cod == 21205420].sort_values('TS')

base_3[(base_3.date > inicio_1) & (base_3.date < fin_1)].sort_values('date')
base_3[(base_3.date > inicio_1) & (base_3.date < fin_1)].sort_values('tmp_2m')

eventos_altas
###Final de los casos
gra_tiem('20091202','20091204','altas_1') # Fecha no usada
gra_tiem('20150826','20150828','altas_1')





base_3[(base_3.date > inicio_1) & (base_3.date < fin_1)].sort_values('tmp_2m').tail()

conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1)].sort_values('TS')

conv_zona[(conv_zona.date > inicio_1) & (conv_zona.date < fin_1)][conv_zona.cod == 21205420].sort_values('TS')

plt.plot_date(base_3[(base_3.date > inicio_1) & (base_3.date < fin_1)].sort_values('tmp_2m').date, base_3[(base_3.date > inicio_1) & (base_3.date < fin_1)].sort_values('tmp_2m_y').tmp_2m_y)

inicio_1 = pd.to_datetime('2007/02/04 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fin_1 = pd.to_datetime('2007/02/05 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')

base_3[(base_3.date > inicio_1) & (base_3.date < fin_1)].sort_values('date')

###################################
###################################
######################################################################
###################################
######################################################################
################################### Forma como se comprobó la validación
######################################################################
###################################
######################################################################
###################################
###################################


###Uno de los casos de altas temperaturas fue detectado en el 20080912

#! voy a revisar si el control hasta ahora hecho lo encuentra

###################################
###################################
###################################

#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_2005_data')
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_validado_20180522')
hyd_tiba = pd.read_csv('21206990_tmp_2m.csv')
hyd_tiba.date = pd.to_datetime(hyd_tiba .date, format ='%Y%m%d %H:%M:%S', errors='coerce')

inicio_1 = pd.to_datetime('2008/09/11 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fin_1 = pd.to_datetime('2008/09/13 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')

n_base= hyd_tiba[(hyd_tiba.date > inicio_1) & (hyd_tiba.date < fin_1)]

plt.plot_date(n_base.date, n_base.tmp_2m)
plt.plot_date(n_base.date,  n_base.spikes_connan)

plt.plot_date(n_base.date, n_base.tmp_2m)
plt.plot_date(n_base.date,  n_base.tmp_2mspikes)

plt.plot_date(n_base.date, n_base.tmp_2m)
plt.plot_date(n_base.date,  n_base.tmp_2m_dif_1)

plt.plot_date(n_base.date, n_base.tmp_2m)
plt.plot_date(n_base.date,  n_base.tmp_2m_dif)

plt.plot_date(n_base.date, n_base.tmp_2m)
plt.plot_date(n_base.date,  n_base.tmp_2m_roll_1)

plt.plot_date(n_base.date, n_base.tmp_2m)
plt.plot_date(n_base.date,  n_base.tmp_2m_roll)



n_base[n_base.tmp_2m_roll_1 == 0]

plt.plot_date(n_base.date, n_base.tmp_2m)

plt.plot_date(n_base[n_base.tmp_2m.notnull()][n_base.range == 0
                     ][n_base.tmp_2mspikes == 0][n_base.tmp_2m_dif == 0
                      ].date, n_base[n_base.tmp_2m.notnull()][n_base.range == 0
                      ][n_base.tmp_2mspikes == 0][n_base.tmp_2m_dif == 0].tmp_2m)
    


plt.plot_date(n_base[n_base.tmp_2m.notnull()][n_base.range == 0][n_base.tmp_2mspikes == 0][n_base.tmp_2m_dif == 0][n_base.tmp_2m_roll== 0].date, n_base[n_base.tmp_2m.notnull()][n_base.range == 0][n_base.tmp_2mspikes == 0][n_base.tmp_2m_dif == 0][n_base.tmp_2m_roll== 0].tmp_2m)

plt.plot_date(n_base[n_base.tmp_2m.notnull()][n_base.range == 0][n_base.tmp_2mspikes == 0][n_base.tmp_2m_dif == 0][n_base.tmp_2m_roll_1== 0].date, n_base[n_base.tmp_2m.notnull()][n_base.range == 0][n_base.tmp_2mspikes == 0][n_base.tmp_2m_dif == 0][n_base.tmp_2m_roll_1== 0].tmp_2m)

plt.plot_date(n_base[n_base.tmp_2m_roll_1== 0].date, n_base[n_base.tmp_2m_roll_1 == 0].tmp_2m)

n_base['mean_1'] = n_base.tmp_2m.rolling(window=9, center=True, min_periods=1).mean()


n_base['std_1'] = n_base.tmp_2m.rolling(window=9, center=True, min_periods=1).std()

n_base['spikes_connan'] = np.where((((n_base.mean_1 - (n_base.std_2 * 1)) > 
                                      n_base.tmp_2m) | (n_base.tmp_2m > (n_base.mean_1 + 
                                        (n_base.std_2 * 1)))), 1,0)

n_base['a'] = np.where(((n_base.tmp_2m > (n_base.mean_1 + 
                                        (n_base.std_2 * 1)))), 'T','F')

n_base['b'] = np.where((((n_base.mean_1 - (n_base.std_2 * 1)) > 
                                      n_base.tmp_2m) ), 'T','F')


n_base[['mean_1','std_1' ,'tmp_2m','a','b','spikes_connan']]

# =============================================================================
# 
# 
# 
# 
# 
# 
# 
# =============================================================================

conv_tiba = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideamdatos_con_zona_csv')
conv_tiba.date = pd.to_datetime(conv_tiba.date, format ='%Y%m%d %H:%M:%S', errors='coerce')

conv_zona.tipo.unique() # list of unique values
###

conv_zona_min = conv_zona[(conv_zona.tipo == 8)] # Valores mínimos

conv_zona_max = conv_zona[(conv_zona.tipo == 2)] # Valores máximos
#conv_zona_max = conv_zona[(conv_zona.tipo == 4)] # Valores máximos

conv_zona_mean = conv_zona[(conv_zona.tipo == 1)] # Valores promedio


# HIstograma para la descripción de las funciones

#gaus = np.random.randn(1000)
#plt.hist(gaus)
#gaus.dtype
conv_zona.TS.dtype
conv_zona.TS.plot.hist(bins = 20, color = 'k')

#Plot de histogramas por años
n_f = pd.DatetimeIndex(conv_zona.date)
conv_zona['year'] = n_f.year

[conv_zona.year == 1983]
conv_zona[conv_zona.year == 1983].TS.plot.hist(bins = 20, color = 'k')


annos = conv_zona.year.unique()[1:-1]

base_hist = conv_zona[conv_zona.tipo == 1]


from matplotlib.pyplot import cm 
###Plot del cambio de la temperatura a través del tiempo para la zona
color=iter(cm.rainbow(np.linspace(0.5,.9,46)))
#c=next(color)
c=next(color)
#Gráfica del primer año
plt.hist(base_hist[base_hist.year == np.sort(annos)[7]][base_hist.tipo == 1].TS, bins = 20, range = [base_hist[base_hist.tipo == 1].TS.min(), base_hist[base_hist.tipo == 1].TS.max()], label = str(int(np.sort(annos)[0])), color = c)
plt.vlines(x=base_hist[base_hist.year == np.sort(annos)[7]].TS.mean() , ymin=0, ymax=3000, color = c)
plt.xlabel('Temperatura °C')
plt.ylabel('Frecuencia')
plt.legend(loc='upper right')
plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph/grafica_tiempo_1971.png', figsize=(20,10) ,dpi = 199)


#Gráfica del compendio de años
a123 = []
annos_print = [1981.0, 1991.0, 2001.0, 2011.0]
for ii in np.sort(annos)[7:-2]:
    c=next(color)
    if ii in annos_print:
        plt.hist(base_hist[base_hist.year == ii][base_hist.tipo == 1].TS, bins = 20, range = [base_hist[base_hist.tipo == 1].TS.min(), base_hist[base_hist.tipo == 1].TS.max()], color = c,  label = str(int(ii)))
        plt.vlines(x=base_hist[base_hist.year == ii].TS.mean() , ymin=0, ymax=3000, color = c)
        plt.legend(loc='upper right')
    else:
        plt.hist(base_hist[base_hist.year == ii][base_hist.tipo == 1].TS, bins = 20, range = [base_hist[base_hist.tipo == 1].TS.min(), base_hist[base_hist.tipo == 1].TS.max()], color = c)
        plt.vlines(x=base_hist[base_hist.year == ii].TS.mean() , ymin=0, ymax=3000, color = c)
    a123.append(base_hist[base_hist.year == ii].TS.mean())
    
    #print(ii)
plt.hist(base_hist[base_hist.year == np.sort(annos)[-2]][base_hist.tipo == 1].TS, bins = 20, range = [base_hist[base_hist.tipo == 1].TS.min(), base_hist[base_hist.tipo == 1].TS.max()], label = str(int(np.sort(annos)[-2])), color = c)
plt.vlines(x=base_hist[base_hist.year == np.sort(annos)[-2]].TS.mean() , ymin=0, ymax=3000, color = c)
plt.legend(loc='upper right')

plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph/grafica_tiempo.png', figsize=(20,10) ,dpi = 199)
plt.close()

#Gráfica del último año
plt.hist(base_hist[base_hist.year == 2016].TS, bins = 20, range = [base_hist.TS.min(), base_hist.TS.max()], label = '2016', color = c)
plt.vlines(x=base_hist[base_hist.year == 2016].TS.mean() , ymin=0, ymax=3000, color=c)
plt.legend(loc='upper right')
plt.xlabel('Temperatura °C')
plt.ylabel('Frecuencia')

plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph/grafica_tiempo_2016.png', figsize=(20,10) ,dpi = 199)
plt.close()


   
conv_zona.TS.plot.hist(bins = 20, color = 'k')

n_f = pd.DatetimeIndex(resume2.date)

conv_zona_max.TS.plot.hist(bins = 20, color = 'k')
conv_zona_min.TS.plot.hist(bins = 20, color = 'k')

conv_zona_cero = conv_zona_min[(conv_zona_min.TS < 0)]
#conv_zona_cero.to_csv('conv_zona_cero.csv')

path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam'
os.chdir(path)

conv_zona_veinte = conv_zona_max[(conv_zona_max.TS > 20)]
conv_zona_veinte.to_csv('conv_zona_veinte.csv')
conv_zona.TS.plot.hist(bins = 20, color = 'k')
conv_zona_cero.TS.plot.hist()
conv_zona_veinte.TS.plot.hist()

conv_zona_cero.shape
conv_zona_cero.TS.plot()
conv_zona_cero.date.dt.month.plot.hist(bins=12)
conv_zona_cero.date.dt.year.plot.hist(bins=20)
plt.plot(conv_zona_cero['date'], conv_zona_cero['TS'])

plt.plot_date(conv_zona_cero['date'], conv_zona_cero['TS'], color = 'royalblue', markersize =2)
plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph/tmp_debajo0.png', figsize=(20,10) ,dpi = 199)
plt.close()



plt.plot_date(conv_zona_veinte['date'], conv_zona_veinte['TS'], color = 'lightcoral', markersize =2)
plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph/tmp_sobre20.png', figsize=(20,10) ,dpi = 199)
plt.close()

###Plot de los histogramas por meses

conv_zona.TS.mean()

conv_zona_2 = conv_zona
n_f1 = pd.DatetimeIndex(conv_zona_2.date)
conv_zona_2['year'] = n_f.year
conv_zona_2['month'] = n_f.month
conv_zona_2['day'] = n_f.day
conv_zona_2['val'] = 1

#Base de los meses mas probables de helada
base_meses = conv_zona_2[conv_zona_2.TS < 0].groupby(['month'])['val'].sum()
base_meses.to_csv('/home/edwin/Downloads/basura2/salida.csv')
base_meses = pd.read_csv('/home/edwin/Downloads/basura2/salida.csv',header=None)
meses = pd.DataFrame({'mes':['ene', 'feb','mar','abr','may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']})
base_meses.columns = ['mes', 'frecuencia']
base_meses.mes = meses.mes
    #Gráfica de los meses en los que se presentan heladas
plt.bar(base_meses.index, base_meses.frecuencia, color = 'royalblue')
plt.xticks(range(0,12), ['ene', 'feb','mar','abr','may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'])
plt.ylabel('Frecuencia')
plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph/frec_bajas_tmp.png', figsize=(20,10) ,dpi = 199)
plt.close()


#Base de los meses mas probables de eventos de altas temperatura
base_meses = conv_zona_2[conv_zona_2.TS > 20].groupby(['month'])['val'].sum()
base_meses.to_csv('/home/edwin/Downloads/basura2/salida2.csv')
base_meses = pd.read_csv('/home/edwin/Downloads/basura2/salida2.csv',header=None)
meses = pd.DataFrame({'mes':['ene', 'feb','mar','abr','may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']})
base_meses.columns = ['mes', 'frecuencia']
base_meses.mes = meses.mes
    #Gráfica de los meses en los que se presentan heladas
plt.bar(base_meses.index, base_meses.frecuencia, color = 'lightcoral')
plt.xticks(range(0,12), ['ene', 'feb','mar','abr','may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'])
plt.ylabel('Frecuencia')
plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph/frec_altas_tmp.png', figsize=(20,10) ,dpi = 199)
plt.close()

##Loop para savar las gráficas del comportamiento de las temperaturas para las diferentes estaciones
    
    for i in conv_zona_2.cod.unique():
        print(i)
        
        
##Calculos de la primera gŕafica
        if len(conv_zona_2[(conv_zona_2.TS < 0) & (conv_zona_2.cod == i)].groupby(['month'])['val'].sum()) <1:
            continue
        base_meses = conv_zona_2[(conv_zona_2.TS < 0) & (conv_zona_2.cod == i)].groupby(['month'])['val'].sum()
        base_meses.to_csv('/home/edwin/Downloads/basura2/salida.csv')
        base_meses = pd.read_csv('/home/edwin/Downloads/basura2/salida.csv',header=None)
        meses = pd.DataFrame({'mes':['ene', 'feb','mar','abr','may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'], 
                              'month_1':[1,2,3,4,5,6,7,8,9,10,11,12]})
        
        base_meses.columns = ['month_1', 'frecuencia']
        base_merge = pd.merge(base_meses, meses, on='month_1', how='outer')
        base_merge_1 = base_merge.sort_values('month_1').reset_index()
        

#Calculos de la segunda gráfica
        if len(conv_zona_2[(conv_zona_2.TS > 20) & (conv_zona_2.cod == i)].groupby(['month'])['val'].sum()) <1:
            continue
        base_meses_2 = conv_zona_2[(conv_zona_2.TS > 20) & (conv_zona_2.cod == i)].groupby(['month'])['val'].sum()
        base_meses_2.to_csv('/home/edwin/Downloads/basura2/salida.csv')
        base_meses_2 = pd.read_csv('/home/edwin/Downloads/basura2/salida.csv',header=None)
        meses = pd.DataFrame({'mes':['ene', 'feb','mar','abr','may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'], 
                              'month_1':[1,2,3,4,5,6,7,8,9,10,11,12]})
        
        base_meses_2.columns = ['month_1', 'frecuencia']
        base_merge_3 = pd.merge(base_meses_2, meses, on='month_1', how='outer')
        base_merge_3 = base_merge_3.sort_values('month_1').reset_index()
            #Gráfica de los meses en los que se presentan heladas  
        


            #Gráfica de los meses en los que se presentan heladas

        
        
        
                ##Inicio de la gráfica
        fig = plt.figure(1)
        fig.set_size_inches(25,7.5)
        fig.suptitle('Frecuencia mensual de ocurrencia de temperaturas bajo 0°C (Izquerda) y temperaturas sobre 20°C (Derecha) de la estación ' + str(i))
        
        gridspect.GridSpec(1,2)
            
       
        
        #####Primera gráfica
        plt.subplot2grid((1,2), (0,0), rowspan=1, colspan=1)
        plt.bar(base_merge_1.index, base_merge_1.frecuencia, color = 'royalblue')
        plt.xticks(range(0,12), ['ene', 'feb','mar','abr','may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'])
        plt.ylabel('Frecuencia')
        plt.title('Temperaturas debajo de 0°C')
        

      
        
        
        #####Segunda gráfica
        plt.subplot2grid((1,2), (0,1), rowspan=1, colspan=1)
        plt.bar(base_merge_3.index, base_merge_3.frecuencia, color = 'lightcoral')
        plt.xticks(range(0,12), ['ene', 'feb','mar','abr','may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'])
        plt.ylabel('Frecuencia')
        plt.title('Temperaturas sobre 20°C')      
        
        plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/comp_tmp/'+str(i)+'.png', figsize=(20,10) ,dpi = 199)
        
        
        
        
        if len(conv_zona_2[(conv_zona_2.TS < 0) & (conv_zona_2.cod == i)].groupby(['month'])['val'].sum()) <1:
            continue
        base_meses = conv_zona_2[(conv_zona_2.TS < 0) & (conv_zona_2.cod == i)].groupby(['month'])['val'].sum()
        base_meses.to_csv('/home/edwin/Downloads/basura2/salida.csv')
        base_meses = pd.read_csv('/home/edwin/Downloads/basura2/salida.csv',header=None)
        meses = pd.DataFrame({'mes':['ene', 'feb','mar','abr','may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'], 
                              'month_1':[1,2,3,4,5,6,7,8,9,10,11,12]})
        
        base_meses.columns = ['month_1', 'frecuencia']
        base_merge = pd.merge(base_meses, meses, on='month_1', how='outer')
        base_merge = base_merge.sort_values('month_1').reset_index()
            #Gráfica de los meses en los que se presentan heladas
        plt.bar(base_merge.index, base_merge.frecuencia, color = 'royalblue')
        plt.xticks(range(0,12), ['ene', 'feb','mar','abr','may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'])
        plt.ylabel('Frecuencia')
        plt.title('Estación código '+str(i))
        plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/comp_tmp/altas/'+str(i)+'.png', figsize=(20,10) ,dpi = 199)
        plt.close()
    
    
    #Base de los meses mas probables de eventos de altas temperatura
    
        if len(conv_zona_2[(conv_zona_2.TS > 20) & (conv_zona_2.cod == i)].groupby(['month'])['val'].sum()) <1:
            continue
        base_meses = conv_zona_2[(conv_zona_2.TS < 0) & (conv_zona_2.cod == i)].groupby(['month'])['val'].sum()
        base_meses.to_csv('/home/edwin/Downloads/basura2/salida.csv')
        base_meses = pd.read_csv('/home/edwin/Downloads/basura2/salida.csv',header=None)
        meses = pd.DataFrame({'mes':['ene', 'feb','mar','abr','may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'], 
                              'month_1':[1,2,3,4,5,6,7,8,9,10,11,12]})
        
        base_meses.columns = ['month_1', 'frecuencia']
        base_merge = pd.merge(base_meses, meses, on='month_1', how='outer')
        base_merge = base_merge.sort_values('month_1').reset_index()
            #Gráfica de los meses en los que se presentan heladas
        plt.bar(base_merge.index, base_merge.frecuencia, color = 'lightcoral')
        plt.xticks(range(0,12), ['ene', 'feb','mar','abr','may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'])
        plt.ylabel('Frecuencia')
        plt.title('Estación código '+str(i))
        plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/comp_tmp/bajas/'+str(i)+'.png', figsize=(20,10) ,dpi = 199)
        plt.close()
    
    
    

## Horas con heladas

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_validados_20180620')
base = pd.read_csv('21206990.csv')
base.date = pd.to_datetime(base.date, format ='%Y%m%d %H:%M:%S', errors='coerce')

base_3 = base
base_4 = base_3[base_3.val_tmp == 0]
n_f2 = pd.DatetimeIndex(base_3[base_3.val_tmp == 0].date)
base_4['hora'] = n_f2.hour
base_4['val'] = 1
base_4_sum = base_4[base_4.tmp_2m < 0].groupby(['hora'])['val'].sum()
base_4_sum = base_4_sum.reset_index()

    #Gráfica de las horas en las que se presentan las heladas
plt.bar(base_4_sum.hora, base_4_sum.val, color = 'royalblue')
plt.xticks(range(0,24),range(0,24), rotation = 90)
plt.ylabel('Frecuencia')

plt.xlabel('Hora')
plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph/hora_heladas.png', figsize=(20,10) ,dpi = 199)
plt.close()


## Horas con tmp_altas
#base_3
#n_f2 = pd.DatetimeIndex(base_3.date)
#base_4 = base_3
#base_4['hora'] = n_f2.hour
#base_4['val'] = 1
base_4_sum = base_4[base_4.tmp_2m > 20].groupby(['hora'])['val'].sum()
base_4_sum = base_4_sum.reset_index()

    #Gráfica de las horas en las que se presentan las heladas
plt.bar(base_4_sum.hora, base_4_sum.val, color = 'lightcoral')
plt.xticks(range(0,24),range(0,24), rotation = 90)
plt.ylabel('Frecuencia')

plt.xlabel('Hora')
plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph/hora_tmp_altas.png', figsize=(20,10) ,dpi = 199)
plt.close()


###### Puesta en formato latex las estaciones usadas del IDEAM

t_latex = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estaciones_usadas_latex.csv')
print(t_latex.to_string(index=False).to_latex())


