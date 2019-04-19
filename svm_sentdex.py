#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 10:01:53 2018

@author: edwin
"""

#Support Vector Machine (SVM) This is only for two groups

import numpy as np
from sklearn import preprocessing, cross_validation, neighbors, svm 
import pandas as pd

df = pd.read_csv('/home/edwin/Downloads/breast-cancer-wisconsin.data')

df.replace('?', -99999, inplace = True)
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['class'],1))

y  = np.array(df['class'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2) # Take values random

clf = svm.SVC()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)


example_measures = np.array([[4,2,1,1,1,2,3,2,1], [10,6,4,1,1,2,3,2,3]])
example_measures = [np.array([3,1,1,1,2,3,3,1,1])]

prediction = clf.predict(example_measures)
prediction
accuracy
#prediction = clf.predict(X_test)

###Kernels introduction

import numpy as np

x1 = np.array([5,3,2,2,5,2,1])
x2 = np.array([2,1,1,6,4,6,1])

print(np.dot(x1, x2))
print(np.inner(x1, x2))


