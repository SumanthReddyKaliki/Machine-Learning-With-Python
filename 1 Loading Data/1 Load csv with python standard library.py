# -*- coding: utf-8 -*-
import csv
import numpy
filename='pima-indians-diabetes.data.csv'
raw_data=open(filename,'rb')
reader=csv.reader(raw_data,delimiter=',',quoting=csv.QUOTE_NONE)
x=list(reader)
data=numpy.array(x).astype('float')
print(data.shape)
#print data