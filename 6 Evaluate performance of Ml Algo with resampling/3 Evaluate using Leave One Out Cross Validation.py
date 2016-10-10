import pandas
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
num_folds = 10
num_instances = len(X)
loocv = cross_validation.LeaveOneOut(n=num_instances)
model = LogisticRegression()
results = cross_validation.cross_val_score(model, X, Y, cv=loocv)
print("Accuracy: %.3f%% (%.3f%%)") % (results.mean()*100.0, results.std()*100.0)# -*- coding: utf-8 -*-

