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
fMedoTime = datetime.timedelta(hours=10,minutes=10,seconds=00).total_seconds()
allMedoTime = datetime.timedelta(hours=15,minutes=19,seconds=00).total_seconds()
wanna = 1.2
mesuLimit = 1
rateLimit = 0.44
sumEd = 0
for dirname, dirnames, filenames in os.walk("C:\\Dropbox\\Data\\"):
    for subdirname in dirnames:
        today = subdirname
        # if(today != '2016-09-21'):
        #     break;
        # today = '2016-11-21'
        # if((today.split('-')[1] == '10' and today.split('-')[2] in ['05','06','07','10','11','12','13','14','17','18','19','20','21','24','25','26','27','28','31']) or (today.split('-')[1] == '11' and today.split('-')[2] in ['01','02','03','07','08','09','10'])):
        #     continue

        print(today)
        setFile = open(os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "moa3.txt"), 'w')
        edFile = open(os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "ed.txt"), 'w')
        realfilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + ".txt");
        tempFile = open(os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "tempFile.txt"), 'w')
        
        data = sp.genfromtxt(realfilePath, delimiter="\t", dtype='|S20')
        codes = sp.unique(data[data[:,7] != b''][:,7])
        times = sp.unique(data[data[:,0] != b''][:,0])

        if((today.split('-')[1] == '10' and today.split('-')[2] in ['05','06','07','10','11','12','13','14','17','18','19','20','21','24','25','26','27','28','31']) or (today.split('-')[1] == '11' and today.split('-')[2] in ['01','02','03','07','08','09','10','11','14','15','16','17'])):
        # if(True):
        
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
                    if(second_oTime > allMedoTime + 15):
                        break
    
                except Exception as e:
                    print('*************' + str())
                    raise
    
            data = termData;
            codes = sp.unique(data[data[:,7] != b''][:,7])
            times = sp.unique(data[data[:,0] != b''][:,0])
  
        # for x in data:
        #     tempFile.writelines(str(x) + '\n');

        # break

        tmp_time = 0
        mesuDict = dict()
        mesuStart = dict()
        msRate = dict()
        comps = []
        mesuSTime = dict()
        # if((today.split('-')[1] == '10' and today.split('-')[2] in ['05','06','07','10','11','12','13','14','17','18','19','20','21','24','25','26','27','28','31']) or (today.split('-')[1] == '11' and today.split('-')[2] in ['01','02','03','07','08','09','10','11','14','15','16','17'])):
        #     mesuLimit = 1

        for ttime in times:
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
                
                if(second_oTime < startTime):
                    continue;

                if(second_oTime > endTime and len(comps) == 0):
                    break;

                if(second_oTime > allMedoTime):
                    dcodes = comps
                    for code in dcodes:
                        ms = float(msRate[code.decode('utf-8')])
                        md = 0
                        ed = round(md - ms, 2)
                        mdTime = 'endTime'
                        msTime = exportData[mesuStart[code.decode('utf-8')],0].decode('UTF-8')
                        allMax = max(exportData[:, 3].astype(float))
                        termMax = max(exportData[mesuStart[code.decode('utf-8')]:, 3].astype(float))
                        edFile.write(str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(ed) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(mesuDict[code.decode('utf-8')]) + ',' + str(mesuSTime[code.decode('utf-8')]) + '\n')
                        comps.remove(code)
                        sumEd = sumEd +ed
                    break;
                tmp_time = second_oTime
                
                print(today + str(ttime))
                if(bool_oTime == True):
                    ttimeData = data[data[:,0] == ttime]
                    ttimeData2 = ttimeData[ttimeData[:,1].astype(int) < 21]
                    ttimeData3 = ttimeData2[ttimeData2[:,4].astype(int) > 460000]
                    ttimeData4 = ttimeData3[ttimeData3[:,3].astype(float) < 25]
                    codes = ttimeData4[:,7]

                    if(second_oTime > endTime):
                        codes = comps

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

                        if(code in comps):
                            mmRate = (sp.sum(exportData[i-4:i+1,5].astype(float)))/(sp.sum(exportData[i-4:i+1,6].astype(float)))
                            # if((today.split('-')[1] == '10' and today.split('-')[2] in ['05','06','07','10','11','12','13','14','17','18','19','20','21','24','25','26','27','28','31']) or (today.split('-')[1] == '11' and today.split('-')[2] in ['01','02','03','07','08','09','10','11','14','15','16','17'])):
                            #     mmRate  = (sp.sum(exportData[i-14:i+1,5].astype(float)))/(sp.sum(exportData[i-14:i+1,6].astype(float)))
                            
                            ms = float(msRate[code.decode('utf-8')])
                            md = float(exportData[i + 1, 3].decode('UTF-8'))
                            ed = round(md - ms, 2)
                            mdTime = ttime.decode('UTF-8')
                            msTime = exportData[mesuStart[code.decode('utf-8')],0].decode('UTF-8')
                            allMax = max(exportData[:, 3].astype(float))
                            termMax = max(exportData[mesuStart[code.decode('utf-8')]:i+1, 3].astype(float))
                            # if(exportData[i,5].astype(float)) == 0 and (exportData[i,6].astype(float) == 0):
                            #     edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(ed) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(mesuDict[code.decode('utf-8')]) + ',' + str(mesuSTime[code.decode('utf-8')]) + '\n')
                            #     comps.remove(code)
                            if(float(exportData[i, 3].decode('UTF-8')) > 28.9):
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(ed) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(mesuDict[code.decode('utf-8')]) + ',' + str(mesuSTime[code.decode('utf-8')]) + '\n')
                                comps.remove(code)
                                sumEd = sumEd +ed
                            elif(float(exportData[i, 3].decode('UTF-8')) > 19.5 and ed >= wanna):
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(ed) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(mesuDict[code.decode('utf-8')]) + ',' + str(mesuSTime[code.decode('utf-8')]) + '\n')
                                comps.remove(code)
                                sumEd = sumEd +ed
                            elif((mmRate < rateLimit or fMedoTime < second_oTime) and ed >= wanna):
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(ed) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(mesuDict[code.decode('utf-8')]) + ',' + str(mesuSTime[code.decode('utf-8')]) + '\n')
                                comps.remove(code)
                                sumEd = sumEd +ed
                            elif(allMedoTime < second_oTime):
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(ed) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(mesuDict[code.decode('utf-8')]) + ',' + str(mesuSTime[code.decode('utf-8')]) + '\n')
                                comps.remove(code)
                                sumEd = sumEd +ed

                        if(second_oTime > endTime):
                            continue;

                        if(len(comps) > 0):
                            continue;
    
                        if(True in (c > 21)):
                            continue;
                        rate = exportData[i, 3].decode('UTF-8')
                        grade = int(exportData[i, 1].decode('UTF-8'))
                        gr = int(exportData[i, 4].decode('UTF-8'))

                        ms_md = (exportData[i,5].astype(float))/(exportData[i,6].astype(float))
                        sms_md = sp.sum(exportData[:i+1,5].astype(float))/sp.sum(exportData[:i+1,6].astype(float))
                        
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
                            
                            maxc = sp.argmax(exportData[i+1:,3].astype(float))
    
                            if(gradient >= 0.7 and srgrad > -0.01):
                                if(code.decode('utf-8') in mesuDict):
                                    mesuDict[code.decode('utf-8')] = mesuDict[code.decode('utf-8')] + 1
                                else:
                                    mesuSTime[code.decode('utf-8')] = str_oTime
                                    mesuDict[code.decode('utf-8')] = mesuDict.get(code.decode('utf-8'), 0)

                                if(mesuDict[code.decode('utf-8')] == mesuLimit and ((code) not in comps)):
                                    comps.append((code))
                                    mesuStart[code.decode('utf-8')] = i
                                    msRate[code.decode('utf-8')] = float(exportData[i, 3].decode('UTF-8'))
                                    setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) +  ',' + str(float(exportData[i, 3].decode('UTF-8'))) + ',' + str(exportData[maxc + i + 1,3].decode('UTF-8')) + ',' + str_oTime + ',' + str(gr)  + ',' + str(i)  + ',' + str( min(exportData[i:i + maxc + 1, 3].astype(float)) )  + ',' + str( max(exportData[:i, 3].astype(float)) )  + ',' + str(exportData[i +maxc, 0].decode('UTF-8')) +  ',' + str( grade )  +  '\n')

            except Exception as e:
                print("---------------------------------------" + str(e))
                continue

        print(today)

analFilePath = os.path.join("C:\\", "Dropbox\\Data\\" + "anal.txt");
analFile = open(analFilePath, 'w')

edFilePath = os.path.join("C:\\", "Dropbox\\Data\\" + "ed.txt");
edFile = open(edFilePath, 'w')

edFile.write('day' +  ',' + 'sumEd' +    ',' + 'code' +  ',' + 'max' +  ',' + 'termMax' +  ',' + 'md' +  ',' + 'ms' +  ',' + 'ed' +  ',' + 'msTime' +  ',' + 'mdTime' + '\n')

for dirname, dirnames, filenames in os.walk("C:\\Dropbox\\Data\\"):
    for subdirname in dirnames:
        today = subdirname

        # if((today.split('-')[1] == '10' and today.split('-')[2] in ['05','06','07','10','11','12','13','14','17','18','19','20','21','24','25','26','27','28','31']) or (today.split('-')[1] == '11' and today.split('-')[2] in ['01','02','03','07','08','09','10'])):
        #     continue

        setFilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "moa3.txt");
        setFile = open(setFilePath, 'r')
        
        for line in setFile:
            analFile.write(today + ',' + line)

        set2FilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "ed.txt");
        set2File = open(set2FilePath, 'r')
        
        for line in set2File:
            edFile.write(today + ',' + str(sumEd) + ',' + line)

print("end")            

now = datetime.datetime.now()
print(str(datetime.datetime.now()))