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

now = datetime.datetime.now()
today = now.strftime('%Y-%m-%d')

startTime = datetime.timedelta(hours=9,minutes=00,seconds=00).total_seconds()
endTime = datetime.timedelta(hours=9,minutes=13,seconds=00).total_seconds()
fMedoTime = datetime.timedelta(hours=10,minutes=10,seconds=00).total_seconds()
allMedoTime = datetime.timedelta(hours=10,minutes=45,seconds=00).total_seconds()
closeTime = datetime.timedelta(hours=15,minutes=15,seconds=00).total_seconds()

comps = []
mesuLimit = 3
wanna = 2
realfilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + ".txt");
dirn = os.path.dirname(realfilePath)
try:
    os.stat(dirn)
except:
    try:
        os.makedirs(dirn)
    except OSError as exc: 
        if exc.errno == errno.EEXIST and os.path.isdir(dirn):
            pass
        else:
            raise

setFilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "m.txt");
dirn2 = os.path.dirname(setFilePath)
try:
    os.stat(dirn2)
except:
    try:
        os.makedirs(dirn2)
    except OSError as exc: 
        if exc.errno == errno.EEXIST and os.path.isdir(dirn2):
            pass
        else:
            raise

mdFilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "d.txt");
dirn3 = os.path.dirname(setFilePath)
try:
    os.stat(dirn3)
except:
    try:
        os.makedirs(dirn3)
    except OSError as exc: 
        if exc.errno == errno.EEXIST and os.path.isdir(dirn3):
            pass
        else:
            raise

realfile = open(realfilePath, 'a')
realfile.close()

setFile = open(setFilePath, 'w')
setFile.close()

mdFile = open(mdFilePath, 'w')
mdFile.close()

mesuStart = dict()

while(True):
    data = sp.genfromtxt(realfilePath, delimiter="\t", dtype='|S20')
    
    try:
        times = sp.unique(data[data[:,0] != b''][:,0])
    except Exception as e:
        print('not yet')
        continue
    
    tmp_time = 0
    mesuDict = dict()
    now = datetime.datetime.now()
    nowTime = datetime.timedelta(hours=now.hour,minutes=now.minute,seconds=now.second).total_seconds()

    # if(nowTime > endTime and len(comps) == 0):
    #     break;

    # if(nowTime - 100 > allMedoTime):
    #     break;

    for comp in comps:
        mesuDict[comp] = -1

    print(today + str(times[len(times)-1]))
    print(comps)
    print(mesuDict)
    for ttime in (times):
        
        try:
            xstime = time.strptime(ttime.decode('utf-8'), '%H:%M:%S')
            second_oTime = datetime.timedelta(hours=xstime.tm_hour,minutes=xstime.tm_min,seconds=xstime.tm_sec).total_seconds() #계산시간
            str_oTime = ""
            bool_oTime = False
            
            for t in times:
                x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
                nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
                if(nt > second_oTime):
                    str_oTime = t.decode('utf-8')
                    second_oTime = nt
                    bool_oTime = True
                    break;
            
            if(second_oTime < startTime):
                continue;
            
            if(tmp_time + 8 > second_oTime):
                continue;

            if(second_oTime > endTime and len(mesuDict) == 0):
                break;

            tmp_time = second_oTime
            
            if(bool_oTime == True):
                ttimeData = data[data[:,0] == ttime]
                ttimeData2 = ttimeData[ttimeData[:,1].astype(int) < 20]
                ttimeData3 = ttimeData2[ttimeData2[:,4].astype(int) > 460000]
                ttimeData4 = ttimeData3[ttimeData3[:,3].astype(float) < 25]
                codes = ttimeData4[:,7]
                if(second_oTime > endTime and len(comps) > 0):
                    codes = comps;
                for code in (codes):
                    if(code == b''):
                        continue;
                    exportData = data[data[:,7] == code]
                    
                    xtime = time.strptime(exportData[0,0].decode('utf-8'), '%H:%M:%S')
                    firstSecond = datetime.timedelta(hours=xtime.tm_hour,minutes=xtime.tm_min,seconds=xtime.tm_sec).total_seconds()
                
                    ti = sp.array([])

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
                    c = exportData[:i+1, 3].astype(float)

                    if(code in comps and code.decode('utf-8') in mesuStart and code.decode('utf-8') in mesuDict and mesuDict[code.decode('utf-8')] >= mesuLimit):
                        mmRate = (sp.sum(exportData[i-4:i+1,5].astype(float)))/(sp.sum(exportData[i-4:i+1,6].astype(float)))
                        print(code.decode('utf-8') + '    ' + str(mmRate))
                        if(mmRate < 0.4):
                            mdFile = open(mdFilePath, 'a')
                            mdFile.write(str(code.decode('utf-8')) + ',' + str(float(exportData[i + 1, 3].decode('UTF-8'))) + ',' + str(exportData[i, 0].decode('UTF-8')) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + '\n')
                            mdFile.close()
                            comps.remove(code)

                    if(second_oTime > endTime):
                        continue;
    
                    if(True in (c > 21)):
                        continue;
                    rate = exportData[i, 3].decode('UTF-8')
                    grade = int(exportData[i, 1].decode('UTF-8'))
                    gr = int(exportData[i, 4].decode('UTF-8'))
    
                    ms_md = (exportData[i,5].astype(float))/(exportData[i,6].astype(float))
                    sms_md = sp.sum((sp.sum(exportData[:i+1,5].astype(float)))/(sp.sum(exportData[:i+1,6].astype(float))))

                    if(ms_md > 1 and sms_md > 1 and grade < 20):
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
           
                            if(code.decode('utf-8') in mesuDict):
                                mesuDict[code.decode('utf-8')] = mesuDict[code.decode('utf-8')] + 1
                            else:
                                mesuDict[code.decode('utf-8')] = mesuDict.get(code.decode('utf-8'), 0)
                            
                            if(mesuDict[code.decode('utf-8')] == mesuLimit and ((code) not in comps)):
                                print(str(ttime) + " " + str(gradient) + " " + str(srgrad) + " " + str(grade))
                                comps.append((code))
                                mesuStart[code.decode('utf-8')] = i - 4
                                cost = exportData[i, 8].decode('UTF-8')
                                setFile = open(setFilePath, 'a')
                                setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) + ',' + str(gradient) +  ',' + str_oTime + ',' + str(wanna) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(cost) + '\n')
                                setFile.close()
                             
        except Exception as e:
            print('--------------------' + str(e))
            continue

print(today)