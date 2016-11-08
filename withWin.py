#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)

def readData(filePath):
    try:
        fdata = sp.genfromtxt(filePath, delimiter="\t", dtype='|S20')
    except Exception as e:
        fdata = readData(filePath)
    else:
        return fdata
    finally:
        return fdata

    return fdata

today = datetime.datetime.now().strftime('%Y-%m-%d')
startTime = datetime.timedelta(hours=9,minutes=2,seconds=10).total_seconds()
endTime = datetime.timedelta(hours=9,minutes=29,seconds=30).total_seconds()
ttTime = datetime.timedelta(hours=10,minutes=30,seconds=10).total_seconds()
ttEndTime = datetime.timedelta(hours=11,minutes=10,seconds=30).total_seconds()

realfilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + ".txt");

temp_sec = 0
while(True):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    second_now = datetime.timedelta(hours=hour,minutes=minute,seconds=second).total_seconds()

    if((second_now - temp_sec) < 10):
        time.sleep(10 - (second_now - temp_sec))
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        second_now = datetime.timedelta(hours=hour,minutes=minute,seconds=second).total_seconds()

    temp_sec = second_now

    if(second_now < 32460):
        print("morning")
        continue
    
    data = readData(realfilePath)
    codes = sp.unique(data[-100:-50,7])
    times = data[-99,0]

    if(second_now > ttTime and second_now < ttEndTime):
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
    
            rate = float(exportData[i, 3].decode('UTF-8'))
            
            if(rate < 20):
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

                    if(gradient <= 0 and srgrad > -0.01):
                        setFile = open(os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "m.txt"), 'w')
                        setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) + ',' + str(gradient) +  ',' + str_oTime +  ',' + '1.03' + '\n')
                        setFile.close()        

    if(second_now > ttEndTime):
        print("end")
        break

    if(second_now > endTime):
        print("morning end")
        continue
    
    second_oTime = datetime.timedelta(hours=hour,minutes=minute,seconds=second).total_seconds() #계산시간
    str_oTime = ""
    bool_oTime = False
    
    x = time.strptime(times.decode('utf-8'), '%H:%M:%S')
    nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    str_oTime = times.decode('utf-8')
    second_oTime = nt
    bool_oTime = True
    
    if(second_now < startTime):
        print("morning")
        bool_oTime = False    

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
                ti = sp.append(ti, sp.sqrt(v_time)/2)
                if(second_oTime == sect):
                    i = ei
                    break;
                
            if(i == -1): continue
    
            rate = float(exportData[i, 3].decode('UTF-8'))
            grade = int(exportData[i, 1].decode('UTF-8'))
            gr = int(exportData[i, 4].decode('UTF-8'))
            
            if(grade < 30 and gr > (500000 * (hour - 8)) and rate < 26):
                ms_md = (exportData[i,5].astype(float))/(exportData[i,6].astype(float))
                sms_md = sp.sum((sp.sum(exportData[:i+1,5].astype(float)))/(sp.sum(exportData[:i+1,6].astype(float))))
                
                if(ms_md > 1 and sms_md > 1):

                    if(second_oTime < 32500):
                        if(gr > 2600000 and rate < 15):
                            setFile = open(os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "m.txt"), 'w')
                            setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) + ',' + '100' +  ',' + str_oTime + ',' + '1.05' +  '\n')
                            setFile.close()                        
                        continue;

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

                    if(gradient >= 0.7 and srgrad > -0.01):
                        setFile = open(os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "m.txt"), 'w')
                        setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) + ',' + str(gradient) +  ',' + str_oTime + ',' + '1.05' + '\n')
                        setFile.close()