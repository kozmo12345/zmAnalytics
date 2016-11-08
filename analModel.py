#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)

for dirname, dirnames, filenames in os.walk("C:\\Dropbox\\Data\\"):
    for subdirname in dirnames:
        today = subdirname

        try:
           thread.start_new_thread( print_time, ("Thread-1", 2, ) )
           thread.start_new_thread( print_time, ("Thread-2", 4, ) )
        except:
           print "Error: unable to start thread"        

        setFilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "moa.txt");
        realfilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + ".txt");
        analFilePath = os.path.join("C:\\", "Dropbox\\Data\\" + "anal.txt");
        analFile = open(analFilePath, 'a')
        
        data = sp.genfromtxt(realfilePath, delimiter="\t", dtype='|S20')
        setData = sp.genfromtxt(setFilePath, delimiter=",", dtype='|S20')
        
        if(len(setData) == 0):
            continue;

        codes = sp.unique(setData[setData[:,0] != b''][:,0])
        times = sp.unique(data[data[:,0] != b''][:,0])
        
        startTime = datetime.timedelta(hours=9,minutes=2,seconds=50).total_seconds()
        endTime = datetime.timedelta(hours=9,minutes=3,seconds=10).total_seconds()
        
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
                            gradient = sp.around(fit[0]*10, decimals=4)
            
                            maxr = 100000
                            ry = (exportData[:i+1,4].astype(float))/maxr
                            srlist = [b - a for a,b in zip(ry,ry[1:])]
                            srfit = sp.polyfit(x[:-1], srlist, level)
                            srgrad = sp.around(srfit[0]*10, decimals=4)
                            
                            tmaxr = maxr/2
                            ttry = (exportData[:i+1,5].astype(float))/maxr
                            tsrfit = sp.polyfit(x[:], ttry, level)
                            msgrad = sp.around(tsrfit[0]*10, decimals=4)

                            t2try = (exportData[:i+1,6].astype(float))/maxr
                            t2srfit = sp.polyfit(x[:], t2try, level)
                            mdgrad = sp.around(t2srfit[0]*10, decimals=4)

                            slist = [b - a for a,b in zip(y,y[1:])]
                            sfit = sp.polyfit(x[:-1], slist, level)
                            sgrad = sp.around(sfit[0]*10, decimals=4)                            
                            
                            smaxr = exportData[i,4].astype(float)/(v_time)
                            
                            dsry = (exportData[:i+1,4].astype(float))/smaxr
                            dssrlist = [b - a for a,b in zip(dsry,dsry[1:])]
                            dssrfit = sp.polyfit(x[:-1], dssrlist, level)
                            dssrgrad = sp.around(dssrfit[0]*10, decimals=2)

                            maxc = sp.argmax(exportData[i+1:,3].astype(float))
        
                            if(gradient >= 0.7 and srgrad > -0.01):
                                analFile.write( today + ',' +  str(code.decode('utf-8')) + ',' + str(msgrad) + ',' + str(mdgrad) + ',' + str(float(exportData[maxc + i + 1,3].decode('UTF-8')) - float(rate)) + ',' + str(exportData[maxc + i + 1,0].decode('UTF-8')) + ',' + str_oTime + ',' + str(gr) + ',' + str(i) + "," + str(sgrad) + "," + str(dssrgrad) + "," + str(gradient) + '\n')
                                
        print(today)            