#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:44:35 2018

@author: edwin
"""

#https://matplotlib.org/2.0.2/api/figure_api.html#matplotlib.figure.Figure.set_size_inches

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()



t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()



######################

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

ts = np.exp(ts.cumsum())

ts.plot(logy=True)
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
df.plot(legend=False)



############################

import pandas as pd
import matplotlib.pyplot as plt

table={'time':[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
       'data':[1,1,2,2,2,1,2,3,4,5,1,2,2,2,3],
       'type':['a','a','a','a','a','b','b','b','b','b','c','c','c','c','c']}
df=pd.DataFrame(table, columns=['time','data','type'])

groups = df.groupby('type')

fig, ax = plt.subplots()
for name, group in groups:
    ax.plot(group['time'], group['data'], label=name)
ax.legend(loc='best')

plt.show()



import numpy as np

countListFast = [1492.0, 497.0, 441.0, 218.0, 101.0, 78.0, 103.0]
countListSlow = [1718.0, 806.0, 850.0, 397.0, 182.0, 125.0, 106.0]

errorRateListOfFast = ['9.09', '9.09', '9.38', '9.40', '7.89', '8.02', '10.00']
errorRateListOfSlow = ['10.00', '13.04', '14.29', '12.50', '14.29', '14.53', '11.11']

opacity = 0.4
bar_width = 0.35

plt.xlabel('Tasks')
plt.ylabel('Error Rate')

plt.xticks(range(len(errorRateListOfFast)),('[10-20)', '[20-30)', '[30-50)', '[50-70)','[70-90)', '[90-120)', ' [120 < )'), rotation=30)
bar1 = plt.bar(np.arange(len(errorRateListOfFast))+ bar_width, errorRateListOfFast, bar_width, align='center', alpha=opacity, color='b', label='Fast <= 6 sec.')
bar2 = plt.bar(range(len(errorRateListOfSlow)), errorRateListOfSlow, bar_width, align='center', alpha=opacity, color='r', label='Slower > 6 sec.')

# Add counts above the two bar graphs
for rect in bar1 + bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

plt.legend()
plt.tight_layout()
plt.show()


##################### Matplotlib SENTDEX



x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x, y, label = 'First line')
plt.plot(x2, y2, label = 'second line')
plt.xlabel('Plot number')
plt.ylabel('Eje y')
plt.title('Grafica 1\nCheck it') # COmo un enter
plt.legend()
plt.show()

#Barchart and histograms

x = [2,4,6,8,10]
y = [6,8,7,2,3]

x2 = [1,3,5,7,9]
y2 = [10,14,12,87,2]


plt.bar(x, y, label = 'Bar', color = 'blue')
plt.bar(x2, y2, label = 'Bar2', color = 'c')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafica 1\nCheck it') # COmo un enter
plt.legend()
plt.show()

#Histogram

pop_ages = list(np.random.uniform(10, 89, 20))

ids = [x for x in range(len(pop_ages))]

#plt.bar(ids, pop_ages)

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120]

plt.hist(pop_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafica 1\nCheck it') # COmo un enter
plt.legend()
plt.show()


###Scaterplot

x = [np.random.normal(0,1,100)]
y = [np.random.normal(0,1,100)]

plt.scatter(x, y, label='labe_li', color = 'k', marker='3', s =100)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafica 1\nCheck it') # COmo un enter
plt.legend()
plt.show()

##Stackplots

days = [1,2,3,4,5]
sleeping= [7,6,9,8,4]
eating= [2,3,4,3,2]
working= [8,9,8,7,4]
playing= [12,15,13,14,16]
# =============================================================================
# 
# plt.plot([], [], color = 'm', label = 'Sleeping')
# plt.plot([], [], color = 'c', label = 'Working')
# plt.plot([], [], color = 'r', label = 'Eating')
# plt.plot([], [], color = 'k', label = 'Playing')
# 
# =============================================================================

#plt.stackplot(days, sleeping, working, eating, playing, colors = ['m','c','r','k'])

plt.stackplot(days,sleeping,working,eating,playing,colors = ['m','c','r','k'],labels = ['sleeping','working','eating','playing'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafica 1\nCheck it') # COmo un enter
plt.legend()
plt.show()
##Pie chart


days = [1,2,3,4,5]
sleeping= [7,6,9,8,4]
eating= [2,3,4,3,2]
working= [8,9,8,7,4]
playing= [12,15,13,14,16]

slices = [7,2,2,13]
acti = ['sleeping','working','eating','playing']
cols = ['m','c','r','b']

plt.pie(slices,
        labels=acti, 
        colors=cols, 
        startangle=90,#inicie arriba 
        shadow=True, #Sombra como el relieve
        explode=(0,0.5,0,0), # para sacar la porción
        autopct='%1.1f%%') # imprimir los porcentajes

plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafica 1\nCheck it') # COmo un enter
plt.legend()
plt.show()


## Multiples images inside

import numpy as np
import matplotlib.pyplot as plt

box = dict(facecolor='yellow', pad=5, alpha=0.2)

fig = plt.figure()
fig.subplots_adjust(left=0.2, wspace=0.6)


# ax1 = fig.add_subplot(221)
ax1 = plt.subplot2grid((3,2), (0,0))
ax1.plot(2000*np.random.rand(10))
ax1.set_title('ylabels not aligned')
ax1.set_ylabel('misaligned 1', bbox=box)
ax1.set_ylim(0, 2000)

# ax3 = fig.add_subplot(223)
ax3 = plt.subplot2grid((3,2), (1,0))
ax3.set_ylabel('misaligned 2',bbox=box)
ax3.plot(np.random.rand(10))


labelx = -0.3  # axes coords

# ax2 = fig.add_subplot(222)
ax2 = plt.subplot2grid((3,2), (0,1))
ax2.set_title('ylabels aligned')
ax2.plot(2000*np.random.rand(10))
ax2.set_ylabel('aligned 1', bbox=box)
ax2.yaxis.set_label_coords(labelx, 0.5)
ax2.set_ylim(0, 2000)

# ax4 = fig.add_subplot(224)
ax4 = plt.subplot2grid((3,2), (1,1))
ax4.plot(np.random.rand(10))
ax4.set_ylabel('aligned 2', bbox=box)
ax4.yaxis.set_label_coords(labelx, 0.5)

ax5 = plt.subplot2grid((3,2), (2,0), colspan=2)
ax5.plot(np.random.rand(10))
ax5.set_ylabel('misaligned 3', bbox=box)

plt.show()

####

grid_size = (1,3)
import random
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()

def create_plot():
    xs = []
    ys = []
    for i in range(10):
        x = i
        y = random.randrange(10)
        
        xs.append(x)
        ys.append(y)
    return xs, ys

ax1 = fig.add_subplot(211) # Esto significa dos gráficas paralelas
ax2 = fig.add_subplot(212)

x, y = create_plot()
ax1.plot(x, y)

x, y = create_plot()
ax2.plot(x, y)

plt.show()

##################################

style.use('fivethirtyeight')

fig = plt.figure()

def create_plot():
    xs = []
    ys = []
    for i in range(10):
        x = i
        y = random.randrange(10)
        
        xs.append(x)
        ys.append(y)
    return xs, ys

ax1 = fig.add_subplot(221) # Esto significa dos gráficas paralelas
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)

x, y = create_plot()
ax1.plot(x, y)

x, y = create_plot()
ax2.plot(x, y)

x, y = create_plot()
ax3.plot(x, y)

plt.show()


############################

style.use('fivethirtyeight')

fig = plt.figure()

def create_plot():
    xs = []
    ys = []
    for i in range(10):
        x = i
        y = random.randrange(10)
        
        xs.append(x)
        ys.append(y)
    return xs, ys

ax1 = plt.subplot2grid((6,2), (0,0), rowspan=1, colspan=1)
ax2 = plt.subplot2grid((6,2), (2,1), rowspan=2, colspan=1)
ax3 = plt.subplot2grid((6,2), (4,0), rowspan=2, colspan=1)



ax1.stackplot(stackplot_1.index, stackplot_1.data, stackplot_1.missin_data,
                          colors = ['m','c'],
                          labels = ['Datos', 'No-datos'])


ax2.plot_date(x=estacion_na.date, y=estacion_na.TS)
ax2.plot_date(x=estacion_na.date, y=estacion_na.std_2)
ax2.plot_date(x=estacion_na.date, y=estacion_na.std_2)

x, y = create_plot()
ax3.plot(x, y)

plt.show()


ax1 = plt.subplot2grid((3,2), (0,0), rowspan=1, colspan=1)
ax2 = plt.subplot2grid((3,2), (1,0), rowspan=1, colspan=1)
ax3 = plt.subplot2grid((3,2), (1,1), rowspan=1, colspan=1)
ax4 = plt.subplot2grid((3,2), (1,2), rowspan=1, colspan=1)
ax5 = plt.subplot2grid((3,2), (3,0), rowspan=1, colspan=2)


ax1.stackplot(stackplot_1.index, stackplot_1.data, stackplot_1.missin_data,
                          colors = ['m','c'],
                          labels = ['Datos', 'No-datos'])

plt.plot_date(x=estacion_na.date, y=estacion_na.TS)
plt.plot_date(x=estacion_na.date, y=estacion_na.std_2)
plt.plot_date(x=estacion_na.date, y=estacion_na.std_2)


plt.stackplot(stackplot_4.index, stackplot_4.spikes, stackplot_4.discont,
              colors = ['m','c'],
              labels = ['Saltos', 'Discontinuidades'])


plt.xlabel('year')
plt.ylabel('Frecuencia')
plt.title(str(j)+'_year_'+ ideam_con[ideam_con.indice == i].iloc[0][0]) # COmo un enter
plt.legend()


plt.stackplot(stackplot_2.index, stackplot_2.data, stackplot_2.missin_data,
              colors = ['m','c'],
              labels = ['Datos', 'No-datos'])

plt.stackplot(stackplot_3.index, stackplot_3.spikes, stackplot_3.discont,
                          colors = ['m','c'],
                          labels = ['Saltos', 'Discontinuidades'])


#Hay un archivo y no se dónde está

estacion_na.index.get_loc(914)