# -*- coding: utf-8 -*-
import pandas
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
shape = data.shape
print(shape)
#data tptes for each attribute
types = data.dtypes
print(types)