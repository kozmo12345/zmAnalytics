#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)

now = datetime.datetime.now()
today = '2016-11-03'
hour = now.hour
minute = now.minute
second = now.second - 1

setFile = open(os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "mo.txt"), 'w')
realfilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + ".txt");

data = sp.genfromtxt(realfilePath, delimiter="\t", dtype='|S20')
codes = sp.unique(data[data[:,7] != b''][:,7])
times = sp.unique(data[data[:,0] != b''][:,0])

startTime = datetime.timedelta(hours=9,minutes=1,seconds=30).total_seconds()
endTime = datetime.timedelta(hours=9,minutes=20,seconds=00).total_seconds()

for timeIndex, ttime in enumerate(times):
    print(ttime)
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

    if(bool_oTime == True):
        for ci, code in enumerate(codes):
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
                ti = sp.append(ti, (v_time)/10)
                if(second_oTime == sect):
                    i = ei
                    break;
                
            if(i == -1): continue
    
            rate = exportData[i, 3].decode('UTF-8')
            grade = int(exportData[i, 1].decode('UTF-8'))
            gr = int(exportData[i, 4].decode('UTF-8'))
            
            if(grade < 30 and gr > 460000  and float(rate) < 26):
                ms_md = (exportData[i,5].astype(float))/(exportData[i,6].astype(float))
                sms_md = sp.sum((sp.sum(exportData[:i+1,5].astype(float)))/(sp.sum(exportData[:i+1,6].astype(float))))
            
                if(ms_md > 1 and sms_md > 1):
                    x = ti
                    y = exportData[:i+1,3].astype(float)
                    if(len(y) <= 1):
                        break
                    level = 1
                    fit = sp.polyfit(x, y, level)
                    gradient = sp.around(fit[0]*10, decimals=2)
    
                    maxr = 100000
                    ry = (exportData[:i+1,4].astype(float))/maxr
                    srlist = [b - a for a,b in zip(ry,ry[1:])]
                    srfit = sp.polyfit(x[:-1], srlist, level)
                    srgrad = sp.around(srfit[0]*10, decimals=2)
                    
                    maxc = sp.argmax(exportData[i+1:,3].astype(float))

                    smaxr = exportData[i,4].astype(float)/(v_time)

                    sry = (exportData[:i+1,4].astype(float))/smaxr
                    ssrlist = [b - a for a,b in zip(sry,sry[1:])]
                    ssrfit = sp.polyfit(x[:-1], ssrlist, level)
                    ssrgrad = sp.around(ssrfit[0]*10, decimals=2)

                    if(gradient >= 0.7 and srgrad > -0.01):
                        setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) + ',' + str(exportData[maxc + i + 1,3]) +  ',' + str(ssrgrad) +  ',' + str_oTime + ',' + str(gr)  + '\n')
                        
print(today)