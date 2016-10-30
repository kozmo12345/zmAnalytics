#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)  # 이후에 같은 데이터를 생성하기 위해

today = datetime.datetime.now().strftime('%Y-%m-%d')

set2File = open(os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "m2.txt"), 'w')
realfilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + ".txt");

data = sp.genfromtxt(realfilePath, delimiter="\t", dtype='|S20')
codes = sp.unique(data[data[:,7] != b''][:,7])
times = sp.unique(data[data[:,0] != b''][:,0])
            
second_trTime = datetime.timedelta(hours=9,minutes=10,seconds=49).total_seconds() #2차계산시간
str_trTime = ""
bool_trTime = False

for i, t in enumerate(times):
    x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
    nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    if(nt > second_trTime):
        str_trTime = t.decode('utf-8')
        second_trTime = nt
        bool_trTime = True
        break;

if(bool_trTime == True):
    for ci, code in enumerate(codes):
        exportData = data[data[:,7] == code]
        
        x = time.strptime(exportData[0,0].decode('utf-8'), '%H:%M:%S')
        firstSecond = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    
        ti = sp.array([])
        c = exportData[:, 3].astype(float)
        i = -1
        for ei, et in enumerate(exportData[:, 0]):
            tsi = time.strptime(et.decode('utf-8'), '%H:%M:%S')
            sect = datetime.timedelta(hours=tsi.tm_hour,minutes=tsi.tm_min,seconds=tsi.tm_sec).total_seconds()
            v_time = sect - firstSecond
            ti = sp.append(ti, sp.sqrt(v_time)/2)
            if(second_trTime == sect):
                i = ei
                break;
            
        if(i == -1): continue

        rate = exportData[i, 3].decode('UTF-8')
        grade = int(exportData[i, 1].decode('UTF-8'))
        gr = int(exportData[i, 4].decode('UTF-8'))
    
        if(grade < 30 and gr > 1000000):
            x = ti
            y = exportData[:i+1,3].astype(float)
            if(len(y) <= 1):
                continue
            level = 1
            fit = sp.polyfit(x, y, level)
            print(sp.around(fit[0]*10, decimals=2).astype(float))
            if(sp.around(fit[0]*10, decimals=2).astype(float) < -0.5):
                set2File.write( str(code.decode('utf-8')) + ',' + str(float(rate)) + '\n')                    