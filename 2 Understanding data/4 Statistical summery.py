# -*- coding: utf-8 -*-

import pandas
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
pandas.set_option('display.width', 100)
pandas.set_option('precision', 3)
description = data.describe()
print(description)