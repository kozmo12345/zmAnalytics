#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)


x = sp.array([1, 2, 3, 4, 5, 6, 7, 8])
y = sp.array([0.09, 0.25, 0.15, 0.35, 0.15, 0.11, 0.23, 0.3])
level = 1
fit = sp.polyfit(x, y, level)
gradient = sp.around(fit[0], decimals=2)

print(gradient)

# ry = (exportData[:i+1,4].astype(float))/maxr
# srlist = [b - a for a,b in zip(ry,ry[1:])]
# srfit = sp.polyfit(x[:-1], srlist, level)
# srgrad = sp.around(srfit[0]*10, decimals=2)

                             

