#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)

def std_based_outlier(code,ms, md):
    if(len(ms) < 2):
        return ms, md

    ms = ms[ms!=0]
    md = md[md!=0]

    for i in range(0, len(ms)):
        if(np.abs(ms[i] - ms[:].mean()) > (2.9*ms[:].std())):
            ms[i] = 0
            md[i] = 0
        
        if(np.abs(md[i] - md[:].mean()) > (2.9*md[:].std())):
            ms[i] = 0
            md[i] = 0

    return ms, md

now = datetime.datetime.now()
print(str(datetime.datetime.now()))



print(( sp.asarray([1,4,5,6,4,2]) > 3 ).sum())