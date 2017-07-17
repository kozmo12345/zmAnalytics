#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time
import re

sp.random.seed(3)

end_arr = [98.55, 98.77, 98.92, 99.71, 100.94, 99.94, 100.11, 98.78, 94.02, 94.11, 94.16, 93.65, 93.65, 93.66, 93.67, 93.68, 93.70, 93.30, 93.33, 93.31, 93.95, 94.04, 94.30, 94.50, 95.44, 96.10, 97.09, 97.39, 97.06, 96.50, 96.53, 96.47, 96.49, 96.32, 96.34, 96.33, 95.99, 95.87, 92.22, 91.95, 91.92, 91.70, 91.10, 91.05, 91.47, 91.47, 91.26, 91.20, 89.16]
endcgfit = sp.polyfit(sp.array(range(len(end_arr))), end_arr, 1)
endcggrad = sp.around(endcgfit[0], decimals=2)

print(endcggrad)