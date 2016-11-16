#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)

analFilePath = os.path.join("C:\\", "Dropbox\\Data\\" + "ed.txt");
analFile = open(analFilePath, 'w')

analFile.write( 'day,code, rate, nextRate, maxRate, mesuTime, gr, index, minRate, nowMaxRate, maxTime, grade\n')

for dirname, dirnames, filenames in os.walk("C:\\Dropbox\\Data\\"):
    for subdirname in dirnames:
        today = subdirname

        setFilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "ed.txt");
        setFile = open(setFilePath, 'r')
        
        print("file open")
        for line in setFile:
            analFile.write(today + ',' + line)
                                
        print("end")            