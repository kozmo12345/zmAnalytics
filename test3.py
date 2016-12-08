#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time
import numpy as np

sp.random.seed(3)

def std_based_outlier(ms):
    if(len(ms) < 2):
        return ms
    ms[ms==0] = [np.nan]
    for i in range(0, len(ms)):
        if(np.abs(ms[i] - ms[:].mean()) > (2.8*ms[:].std())):
            ms[i] = np.nan    

    ms[np.isnan(ms)] = 0
    return(ms)


df = [6775, 12013, 5777, 296532, 7291, 20255, 30462, 21517, 14902, 6782]

df = sp.asarray(df).astype('float')
print(df)
print(std_based_outlier(df))