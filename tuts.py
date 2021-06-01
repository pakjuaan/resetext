import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np

#from sklearn import datasets
from sklearn import svm

train = pd.read_csv('mnist_train.csv')
test = pd.read_csv('mnist_test.csv')
#print(train.iloc[0]) 
clf = svm.SVC(gamma=0.001, C=100)

x,y = train.iloc[0:3].drop(['label'], axis=1), train['label'].iloc[0:3]
clf.fit(x,y)

h = train.drop(['label'], axis=1)
#print(h.iloc[0])
'''plt.imshow(h.iloc[[0]])
plt.show()'''
print("Prediction: ", clf.predict(h.iloc[[2]]))
