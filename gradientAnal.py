#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)

now = datetime.datetime.now()
today = '2016-10-05'
code = b'081150'

setFile = open(os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "grdi.txt"), 'w')
realfilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + ".txt");

data = sp.genfromtxt(realfilePath, delimiter="\t", dtype='|S20')
times = sp.unique(data[data[:,0] != b''][:,0])

startTime = datetime.timedelta(hours=9,minutes=0,seconds=00).total_seconds()
endTime = datetime.timedelta(hours=9,minutes=30,seconds=00).total_seconds()
vrest = 3

for timeIndex, ttime in enumerate(times):
    xstime = time.strptime(ttime.decode('utf-8'), '%H:%M:%S')
    second_oTime = datetime.timedelta(hours=xstime.tm_hour,minutes=xstime.tm_min,seconds=xstime.tm_sec).total_seconds() #계산시간
    str_oTime = ""
    bool_oTime = False
    
    for i, t in enumerate(times):
        x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
        nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
        if(nt > second_oTime):
            str_oTime = t.decode('utf-8')
            second_oTime = nt
            bool_oTime = True
            break;

    if(second_oTime < startTime):
        bool_oTime = False

    if(second_oTime > endTime):
        break;

    print(str_oTime)
    if(bool_oTime == True):
        exportData = data[data[:,7] == code]

        xtime = time.strptime(exportData[0,0].decode('utf-8'), '%H:%M:%S')
        firstSecond = datetime.timedelta(hours=xtime.tm_hour,minutes=xtime.tm_min,seconds=xtime.tm_sec).total_seconds()
        
        ti = sp.array([])
        c = exportData[:, 3].astype(float)
        i = -1
        for ei, et in enumerate(exportData[:, 0]):
            tsi = time.strptime(et.decode('utf-8'), '%H:%M:%S')
            sect = datetime.timedelta(hours=tsi.tm_hour,minutes=tsi.tm_min,seconds=tsi.tm_sec).total_seconds()
            v_time = sect - firstSecond
            ti = sp.append(ti, (v_time)/vrest)
            if(second_oTime == sect):
                i = ei
                break;
          
        if(i == -1): continue

        maxr = 100000
        ry = (exportData[:i+1,4].astype(float))/maxr        
        srlist = [b - a for a,b in zip(ry,ry[1:])]

        rate = exportData[i, 3].decode('UTF-8')
        grade = int(exportData[i, 1].decode('UTF-8'))
        gr = int(exportData[i, 4].decode('UTF-8'))
        grt = int(exportData[i-1, 4].decode('UTF-8'))
        grth = int(exportData[i-2, 4].decode('UTF-8'))
        grf = int(exportData[i-3, 4].decode('UTF-8'))
        grfi = int(exportData[i-4, 4].decode('UTF-8'))

        gra = ((grt-grth) + (grth-grf) + (grf-grfi))/3
        x = ti
        y = exportData[:i+1,3].astype(float)
        if(len(y) <= 1):
            continue;
        level = 1

        # fit = sp.polyfit(x, y, level)
        # gradient = sp.around(fit[0]*10, decimals=2)
    
        # ry = (exportData[:i+1,4].astype(float))
        # srlist = [b - a for a,b in zip(ry,ry[1:])]
        # srfit = sp.polyfit(x[:-1], srlist, level)
        # srgrad = sp.around(srfit[0]*10, decimals=2)
        
        # maxc = sp.argmax(exportData[i+1:,3].astype(float))

        # smaxr = exportData[i,4].astype(float)/(v_time)

        setFile.write( str(str_oTime) + ',' + str(float(rate)) + ',' + str(sp.mean(srlist)) + '\n')
                        
print(today)