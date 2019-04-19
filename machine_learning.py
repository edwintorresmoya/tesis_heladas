#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:44:13 2018

@author: edwin
"""

import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
from matplotlib import style
import pickle # Usado para guardar el clasificador



def lista_nombres(base):
    base2 = pd.DataFrame(list(base))
    print(base2)
    return(base2)

df1 = quandl.get('WIKI/GOOGL')

df = df1[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close' , 'Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open'])/df['Adj. Close'] * 100.0



df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

for_col = 'Adj. Close'

df.fillna('-99999', inplace = True)#Llenado de valores, no se puede tener no valores

for_out = int(math.ceil(0.01*len(df))) # math.ceil round the number to the next number
print(for_out)

df['label'] = df[for_col].shift(-for_out) # Crea una nueva columa con los datos corridos hacia arriba

################3

df = df.dropna()

X = np.array(df.drop(['label', ''], 1)) # Crea una base sin la columna label # Features Capital letters | label lower cases

y = np.array(df['label']) # Sólo extrae la columna label

X = preprocessing.scale(X) # Que es esto?


df.dropna(inplace=True)
y = np.array(df['label'])

print(len(X), len(y))

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=10) # jobs are the number of regretion to use, para mejorar el ajuste
#clf = svm.SVR()
#clf = svm.SVR()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)

print(for_out)
print(accuracy)

#Regression and Forecasting and predicting


df['label'] = df[for_col].shift(-for_out) # Crea una nueva columa con los datos corridos hacia arriba
X = np.array(df.drop(['label'], 1)) # Crea una base sin la columna label # Features Capital letters | label lower cases
X = preprocessing.scale(X) #
X_lately = X[-for_out:]
X = X[:-for_out]


df = df.dropna()



y = np.array(df['label']) # Sólo extrae la columna label




df.dropna(inplace=True)
y = np.array(df['label'])

print(len(X), len(y))

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=10) # jobs are the number of regretion to use, para mejorar el ajuste -1 means as many as possbile processors
#clf = svm.SVR()
#clf = svm.SVR()
clf.fit(X_train, y_train) # Estos son los datos con los que se entrenó
##Pickling
with open('linearregression.pickle', 'wb') as f:
    pickle.dump(clf, f)
    
pickle_in = open('linearregression.pickle', 'rb')
clf = pickle.load(pickle_in)

accuracy = clf.score(X_test, y_test) # Estos son los datos con los que se probaron

print(for_out)
print(accuracy)

# Predict

forecast_set = clf.predict(X_lately) # Datos pronosticados

#np.correlate()
print(forecast_set, accuracy, for_out)


style.use('ggplot')

df['forecast'] = np.nan

last_date = df.iloc[-1].name # Extrae la última fechas
last_unix = last_date.timestamp()# = Lo convierte a timestamp
one_day = 8600 # Valor de un día en segundos
next_unix = last_unix + one_day # Suma un día al último día de la base

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]
    
df['Adj. Close'].plot()
df['forecast'].plot()

#### Pickling and Scaling

############ First slope

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import random

style.use('fivethirtyeight')

xs = np.array([1,2,3,4,5,6], dtype = np.float64)
ys = np.array([5,4,6,5,6,7], dtype = np.float64)
plt.scatter(xs, ys)

def create_dataset(hm, variance, step=2, correlation=False):
    
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val+=step
        elif correlation and correlation == 'neg':
            val-=step
    xs = [i for i in range(len(ys))]
    
    return(np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64))

def best_fit_slope(xs, ys):
    m = ((mean(xs) * mean(ys)) - mean(xs *ys)) / (((mean(xs))**2)-mean((xs)**2))
    
    
    
    b = mean(ys) - m * mean(xs)
    
    return(m, b)
    
def sq_err(ys_or, ys_li):
    return(sum((ys_li - ys_or)**2))
    
def coef_det(ys_or, ys_li):
    y_mean_li = [mean(ys_or) for y in ys_or]
    sq_err_reg = sq_err(ys_or, ys_li)
    sq_err_y_mean = sq_err(ys_or, y_mean_li)
    
    return(1-(sq_err_reg / sq_err_y_mean ))
    print(1-(sq_err_reg / sq_err_y_mean ))

xs, ys  = create_dataset(40,10,2,correlation=False)
    
m1, b1 = best_fit_slope(xs, ys)

reg_2 = [ (m1*x) + b1 for x in xs ]




#for x in xs:
#    reg_1.append((m1*x)+b1)
    
pred_x = 8
pred_y = (pred_x * m1) + b1

r_sq = coef_det(ys, reg_2)
print(r_sq )

plt.scatter(xs, ys)
plt.scatter(pred_x, pred_y)
plt.plot(xs, reg_2)

# Accuraci = R^2 or coeficient of determination

#Classification w/K Nearest

#K = Busca los vecinos más cercanos, por ejemplo K = 2, 
#eso quiere decir que buscaría los dos más cercanos. Preferiblemente impar
# Si se tiene 3 grupos lo mejor es escoger le siguiente numero impar
# Confidence = es el grado de acierto
# Euckid = distancia entre los datos.


