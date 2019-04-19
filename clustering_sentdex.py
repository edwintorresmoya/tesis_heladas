#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:55:54 2018

@author: edwin
"""

### Clustering 

# Flat clustering
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd


df = pd.read_csv('Downloads/titanic.csv')



style.use('ggplot')

import numpy as np
from sklearn.cluster import KMeans

X = np.array([[1,2],
              [1.5,1.8],
              [5,8],
              [8,8],
              [1,0.6],
              [9,11]])

#plt.scatter(X[:,0], X[:,1], s = 20, linewidths=5)

clf = KMeans(n_clusters=2)
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_

colors = ["g.","r.","c.","b.","k.","o."]

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 20)
    
plt.scatter(centroids[:,0], centroids[:,1], marker='x', linewidths=5, s = 50)



#This is a random tool
##############
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing, cross_validation
style.use('ggplot')

#df = pd.read_csv('Downloads/titanic.csv')
df = pd.read_excel('Downloads/titanic.xls')
df.drop(['body', 'name'], 1, inplace = True)
df.convert_objects(convert_numeric=True)
df.fillna(0, inplace=True)
#print(df.head())

def handle_non(df):import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd


df = pd.read_csv('Downloads/titanic.csv')



style.use('ggplot')

import numpy as np
from sklearn.cluster import KMeans

X = np.array([[1,2],
              [1.5,1.8],
              [5,8],
              [8,8],
              [1,0.6],
              [9,11]])

#plt.scatter(X[:,0], X[:,1], s = 20, linewidths=5)

clf = KMeans(n_clusters=2)
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_

colors = ["g.","r.","c.","b.","k.","o."]
    columns = df.columns.values
    
    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]
        
        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x+=1
                    
            df[column] = list(map(convert_to_int, df[column]))
            
    return df

df = handle_non(df)
df.drop(['boat'], 1, inplace = True)

X = np.array(df.drop(['survived'], 1).astype(float))
X = preprocessing.scale(X)

y = np.array(df['survived'])

clf = KMeans(n_clusters=2)
clf.fit(X)

correct = 0

for i in range(len(X)):
    predic_me = np.array(X[i].astype(float))
    predic_me = predic_me.reshape(-1, len(predic_me))
    prediction = clf.predict(predic_me)
    if prediction[0] == y[i]:
        correct += 1
print(correct/len(X))
         
    
##### Practical part

import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')




X = np.array([[1,2],
              [1.5,1.8],
              [5,8],
              [8,8],
              [1,0.6],
              [9,11]])

plt.scatter(X[:,0], X[:,1], s = 30)
colors = ["g.","r.","c.","b.","k.","o."]

class K_Means:
    def __init___(self, k = 2, tol = 0.001, max_iter = 300): # Tolerance = 0.001 = máximo de tolerancia aceptada, máximo número de iteraciones
        self.k = k 
        self.tol = tol
        self.max_iter = max_iter
        
    def fit(self, data):
        self.centroids = {}
        
        for i in range(self.k):
            self.centroids[i] = data[i]
            
        for i in range(self.max_iter):
            self.classifications = {}
            
            for i in range(self.k):
                self.classifications[i] = []
                
            for featureset in data:
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)
                
            prev_centroids = dict(self.centroids)
            
            for classification in self.classifications:
                #pass
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)
            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid - original_centroid)/original_centroid *100) > self.tol:
                    optimized = False
                    
            if optimized:
                breack
        
    
    def predict(self, data):
        distances = [np.linalg.norm(data-self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification
    
clf = K_Means()
clf.fit(X, k=2)

#for centroid in clf
        
        
