#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)

now = datetime.datetime.now()
print(str(datetime.datetime.now()))

startTime = datetime.timedelta(hours=9,minutes=00,seconds=00).total_seconds()
endTime = datetime.timedelta(hours=9,minutes=13,seconds=00).total_seconds()
fMedoTime = datetime.timedelta(hours=9,minutes=18,seconds=00).total_seconds()
allMedoTime = datetime.timedelta(hours=9,minutes=19,seconds=00).total_seconds()
wanna = 1
mesuLimit = 1
rateLimit = 0.31
stdLimit = 2
sumEd = 0
for dirname, dirnames, filenames in os.walk("C:\\Dropbox\\Data\\"):
    for subdirname in dirnames:
        today = subdirname

        print(today)
        setFile = open(os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "pole.txt"), 'w')
        realfilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + ".txt");
        
        data = sp.genfromtxt(realfilePath, delimiter="\t", dtype='|S20')
        codes = sp.unique(data[data[:,7] != b''][:,7])
        times = sp.unique(data[data[:,0] != b''][:,0])

        if((today.split('-')[1] == '10' and today.split('-')[2] in ['05','06','07','10','11','12','13','14','17','18','19','20','21','24','25','26','27','28','31']) or (today.split('-')[1] == '11' and today.split('-')[2] in ['01','02','03','07','08','09','10','11','14','15','16','17'])):
            termData = data[data[:,0] == times[0]]
            fTime = time.strptime(times[0].decode('utf-8'), '%H:%M:%S')
            f_oTime = datetime.timedelta(hours=fTime.tm_hour,minutes=fTime.tm_min,seconds=fTime.tm_sec).total_seconds() #계산시간
            tmp_time = f_oTime
    
            for ttime in times[1:]:
                try:
                    xstime = time.strptime(ttime.decode('utf-8'), '%H:%M:%S')
                    second_oTime = datetime.timedelta(hours=xstime.tm_hour,minutes=xstime.tm_min,seconds=xstime.tm_sec).total_seconds() #계산시간
                    str_oTime = "ttime.decode('utf-8')"
                    bool_oTime = True

                    if(tmp_time + 9 > second_oTime):
                        continue;
    
                    tempData = data[data[:,0] == ttime]
                    
                    tmp_time = second_oTime
                    print(ttime)
                    termData = sp.append(termData,tempData, axis=0)
    
                except Exception as e:
                    print('*************' + str())
                    raise
    
            data = termData;
            codes = sp.unique(data[data[:,7] != b''][:,7])
            times = sp.unique(data[data[:,0] != b''][:,0])

        tmp_time = 0
        mesuDict = dict()
        mesuStart = dict()
        msRate = dict()
        rmsRate = dict()
        comps = []
        mesuSTime = dict()
        msGradient = dict()
        msGr = dict()
        msSmdms = dict()
        msGrade = dict()
        msSrgrad = dict()
        # if((today.split('-')[1] == '10' and today.split('-')[2] in ['05','06','07','10','11','12','13','14','17','18','19','20','21','24','25','26','27','28','31']) or (today.split('-')[1] == '11' and today.split('-')[2] in ['01','02','03','07','08','09','10','11','14','15','16','17'])):
        #     mesuLimit = 1
        

        ttime = times[-2]

        try:
            xstime = time.strptime(ttime.decode('utf-8'), '%H:%M:%S')
            second_oTime = datetime.timedelta(hours=xstime.tm_hour,minutes=xstime.tm_min,seconds=xstime.tm_sec).total_seconds() #계산시간
            str_oTime = "ttime.decode('utf-8')"
            bool_oTime = True
            
            for i, t in enumerate(times):
                x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
                nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
                if(nt > second_oTime):
                    str_oTime = t.decode('utf-8')
                    second_oTime = nt
                    bool_oTime = True
                    break;

            tmp_time = second_oTime
            
            print(today + str(ttime))
            ttimeData = data[data[:,0] == ttime]
            ttimeData2 = ttimeData[ttimeData[:,3].astype(float) > 28]
            codes = ttimeData2[:,7]
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

                c = exportData[:i+1, 3].astype(float)

                rate = exportData[i, 3].decode('UTF-8')
                grade = int(exportData[i, 1].decode('UTF-8'))
                gr = int(exportData[i, 4].decode('UTF-8'))

                ms_md = (exportData[i,5].astype(float))/(exportData[i,6].astype(float))
                sms_md = sp.sum(exportData[:i+1,5].astype(float))/sp.sum(exportData[:i+1,6].astype(float))
                
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
                
                # maxc = sp.argmax(exportData[i+1:,3].astype(float))
                maxc = len(exportData) - 3
                mesuStart[code.decode('utf-8')] = i
                msGradient[code.decode('utf-8')] = gradient
                msGr[code.decode('utf-8')] = gr
                msSmdms[code.decode('utf-8')] = sms_md 
                msGrade[code.decode('utf-8')] = grade
                msSrgrad[code.decode('utf-8')] = srgrad
                msRate[code.decode('utf-8')] = float(exportData[i, 3].decode('UTF-8'))
                rmsRate[code.decode('utf-8')] = float(exportData[i, 3].decode('UTF-8'))
                setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) +  ',' + str(float(exportData[i, 3].decode('UTF-8'))) + ',' + str(exportData[i,3].decode('UTF-8')) + ',' + str_oTime + ',' + str(gr)  + ',' + str(i)  + ',' + str( min(exportData[0:i, 3].astype(float)) )  + ',' + str( max(exportData[:i, 3].astype(float)) )  + ',' + str(exportData[i, 0].decode('UTF-8')) +  ',' + str( grade )  +  '\n')

        except Exception as e:
            print("---------------------------------------" + str(e))
            continue

        print(today)


setFilePath = os.path.join("C:\\", "Dropbox\\Data\\" + "pole.txt");
setFile = open(setFilePath, 'w')

setFile.write('day' +  ',' + 'sumEd' +    ',' + 'code' +  ',' + 'max' +  ',' + 'termMax' +  ',' + 'md' +  ',' + 'ms' +  ',' + 'ed' +  ',' + 'msTime' +  ',' + 'mdTime' + '\n')

for dirname, dirnames, filenames in os.walk("C:\\Dropbox\\Data\\"):
    for subdirname in dirnames:
        today = subdirname

        set2FilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "pole.txt");
        set2File = open(set2FilePath, 'r')
        
        for line in set2File:
            setFile.write(today + ',' + line)

print("end")            

now = datetime.datetime.now()
print(str(datetime.datetime.now()))