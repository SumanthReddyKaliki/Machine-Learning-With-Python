# -*- coding: utf-8 -*-
import numpy
import urllib
url = "https://goo.gl/vhm1eU"
raw_data = urllib.urlopen(url)
dataset = numpy.loadtxt(raw_data, delimiter=",")
print(dataset.shape)
