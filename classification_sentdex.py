#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 15:31:47 2018

@author: edwin
"""

#Classification w/K Nearest

#K = Busca los vecinos más cercanos, por ejemplo K = 2, 
#eso quiere decir que buscaría los dos más cercanos. Preferiblemente impar
# Si se tiene 3 grupos lo mejor es escoger le siguiente numero impar
# Confidence = es el grado de acierto
# Euckid = distancia entre los datos.

import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd

df = pd.read_csv('/home/edwin/Downloads/breast-cancer-wisconsin.data')

df.replace('?', -99999, inplace = True)
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['class'],1))

y  = np.array(df['class'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2) # Take values random

clf = neighbors.KNeighborsClassifier(n_jobs=-1)
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)


example_measures = np.array([[4,2,1,1,1,2,3,2,1], [10,6,4,1,1,2,3,2,3]])
example_measures = [np.array([3,1,1,1,2,3,3,1,1])]

prediction = clf.predict(example_measures)
prediction = clf.predict(X_test)

####Practical
import numpy as np
from math import sqrt
import warnings
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
import pandas as pd
import random
style.use('fivethirtyeight')
#Euclidean distance

plot1 = [1,3]
plot2 = [2,5]

eucli_dist = sqrt((plot1[0] - plot2[0])**2+(plot1[1] - plot2[1])**2)

dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_features = [5,7]

for i in dataset:
    for ii in dataset[i]:
        plt.scatter(ii[0], ii[1], s=100, color=i)
        
# =============================================================================
# [[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
# plt.scatter(new_features[0], new_features[1])
# =============================================================================

def k_nearest_neigbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K es un valor inferior al número de grupos!')
        
    distances = []
    for group in data:
        for features in data[group]:
            eucli_dist = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([eucli_dist, group])
            #print(eucli_dist )
    votes = [i[1] for i in sorted(distances)[:k]] # Organizó de manor a mayor y la K saca los valores más cercanos
    #rint(distances)
    #print(votes, Counter(votes).most_common(1))
    votes_resul = Counter(votes).most_common(1)[0][0]
    confidence = Counter(votes).most_common(1)[0][1]/k
    print(votes_resul , confidence)
    
    
            
    return votes_resul

result = k_nearest_neigbors(dataset, new_features, k=3)

df = pd.read_csv('/home/edwin/Downloads/breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace = True)
df.drop(['id'], 1, inplace=True)

full_data = df.astype(float).values.tolist() # Converción a lista
#print(full_data[:5])
random.shuffle(full_data) # Cambia el orden de los datos "Aleatorizar"
print(40*'#')
#print(full_data[:5])

test_size = 0.2

train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}
train_data = full_data[:-int(test_size * len(full_data))]
test_data = full_data[-int(test_size * len(full_data)):]

for i in train_data:
    train_set[i[-1]].append(i[:-1]) 
    
for i in test_data:
    test_set[i[-1]].append(i[:-1]) 
    
correct = 0
total = 0

for group in test_set:
    for data in test_set[group]:
        vote = k_nearest_neigbors(train_set, data, k=200) # % es el número de datos más cercanos que se toman para evaluar
        if group == vote:
            correct +=1
        total +=1
        
print('Accuracy', correct/total)


#####Final thoughts on K Nearest Neighbors - Practical Machine Learning Tutorial with Python p.19

