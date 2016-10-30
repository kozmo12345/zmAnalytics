#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)  # 이후에 같은 데이터를 생성하기 위해

today = datetime.datetime.now().strftime('%Y-%m-%d')

setFile = open(os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "m.txt"), 'w')
realfilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + ".txt");

data = sp.genfromtxt(realfilePath, delimiter="\t", dtype='|S20')
codes = sp.unique(data[data[:,7] != b''][:,7])
times = sp.unique(data[data[:,0] != b''][:,0])

second_oTime = datetime.timedelta(hours=9,minutes=2,seconds=3).total_seconds() #1차계산시간
str_oTime = ""
bool_oTime = False

print(1)
for i, t in enumerate(times):
    x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
    nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    if(nt > second_oTime):
        str_oTime = t.decode('utf-8')
        second_oTime = nt
        bool_oTime = True
        break;

print(2)
if(bool_oTime == True):
    
    for ci, code in enumerate(codes):
        exportData = data[data[:,7] == code]
        
        x = time.strptime(exportData[0,0].decode('utf-8'), '%H:%M:%S')
        firstSecond = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    
        c = exportData[:, 3].astype(float)
        i = -1
        for ei, et in enumerate(exportData[:, 0]):
            tsi = time.strptime(et.decode('utf-8'), '%H:%M:%S')
            sect = datetime.timedelta(hours=tsi.tm_hour,minutes=tsi.tm_min,seconds=tsi.tm_sec).total_seconds()
            if(second_oTime == sect):
                i = ei
                break;
            
        if(i == -1): continue

        rate = exportData[i, 3].decode('UTF-8')
        grade = int(exportData[i, 1].decode('UTF-8'))
        gr = int(exportData[i, 4].decode('UTF-8'))

        if(grade < 30 and gr > 1000000):
            setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) + '\n')
print(3)
