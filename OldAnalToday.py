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
endTime = datetime.timedelta(hours=9,minutes=12,seconds=30).total_seconds()
fMedoTime = datetime.timedelta(hours=9,minutes=19,seconds=00).total_seconds()
allMedoTime = datetime.timedelta(hours=9,minutes=21,seconds=00).total_seconds()
wanna = 1
mesuLimit = [3]
rateLimit = 0.31
sumEd = 0

today = now.strftime('%Y-%m-%d')
# today = '2016-12-14'
print(today)
setFile = open(os.path.join("C:\\", "Dropbox\\temp\\Data\\" + today + "\\" + today + "moa3.txt"), 'w')
edFile = open(os.path.join("C:\\", "Dropbox\\temp\\Data\\" + today + "\\" + today + "ed.txt"), 'w')
realfilePath = os.path.join("C:\\", "Dropbox\\temp\\Data\\" + today + "\\" + today + ".txt");

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
            # print(ttime)
            termData = sp.append(termData,tempData, axis=0)
            if(second_oTime > allMedoTime + 300):
                break

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
medos = []
nos = []
mesuSTime = dict()
msGradient = dict()
msGr = dict()
msSmdms = dict()
msGrade = dict()
msSrgrad = dict()
pick = dict()

for ttime in times:
    try:
        xstime = time.strptime(ttime.decode('utf-8'), '%H:%M:%S')
        second_oTime = datetime.timedelta(hours=xstime.tm_hour,minutes=xstime.tm_min,seconds=xstime.tm_sec).total_seconds() #계산시간
        str_oTime = "ttime.decode('utf-8')"
        bool_oTime = True
        
        if(second_oTime < startTime):
            continue;

        if(second_oTime > endTime and len(comps) == 0):
            break;

        if(second_oTime > allMedoTime + 100):
            dcodes = comps
            for code in dcodes:
                ms = float(msRate[code.decode('utf-8')])
                rms = float(rmsRate[code.decode('utf-8')])
                md = 0
                ed = round(md - ms, 2)
                red = round(md - rms, 2)
                mdTime = 'endTime'
                msTime = exportData[mesuStart[code.decode('utf-8')],0].decode('UTF-8')
                allMax = max(exportData[:, 3].astype(float))
                termMax = max(exportData[mesuStart[code.decode('utf-8')]:, 3].astype(float))
                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                comps.remove(code)
                medos.append(code)
                sumEd = sumEd + red
            break;
        tmp_time = second_oTime
        
        print(today + str(ttime))
        if(bool_oTime == True):
            ttimeData = data[data[:,0] == ttime]
            ttimeData2 = ttimeData[ttimeData[:,1].astype(int) < 21]
            ttimeData3 = ttimeData2[ttimeData2[:,4].astype(int) > 400000]
            ttimeData4 = ttimeData3[ttimeData3[:,3].astype(float) < 25]
            ttimeData5 = ttimeData4[ttimeData4[:,8].astype(float) > 1900]
            codes = ttimeData5[:,7]

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
                    mmRate = (sp.sum(exportData[i-2:i+1,5].astype(float)))/(sp.sum(exportData[i-2:i+1,6].astype(float)))

                    ms = float(msRate[code.decode('utf-8')])
                    rms = float(rmsRate[code.decode('utf-8')])
                    md = float(exportData[i, 3].decode('UTF-8'))
                    ed = round(md - ms, 2)
                    red = round(md - ms, 2)
                    mdTime = exportData[i, 0].decode('UTF-8')
                    msTime = exportData[mesuStart[code.decode('utf-8')],0].decode('UTF-8')
                    allMax = max(exportData[:, 3].astype(float))
                    termMin = min(exportData[mesuStart[code.decode('utf-8')]:i+1, 3].astype(float))
                    termMax = max(exportData[mesuStart[code.decode('utf-8')]:i+1, 3].astype(float))
                    msCost = (exportData[mesuStart[code.decode('utf-8')] + 1,4].astype(float) - exportData[mesuStart[code.decode('utf-8')],4].astype(float)) * exportData[mesuStart[code.decode('utf-8')],8].astype(float)
                    mdCost = (exportData[i + 1,4].astype(float) - exportData[i,4].astype(float)) * exportData[i,8].astype(float)

                    # if(exportData[i-5,5].astype(float) == 0 and exportData[i-4,5].astype(float) != 0):
                    #     pick[code.decode('utf-8')] = True

                    if(pick[code.decode('utf-8')] and ed >= wanna):
                        print(1111111111)
                        edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                        comps.remove(code)
                        medos.append(code)
                        sumEd = sumEd + red
                    elif(float(exportData[i, 3].decode('UTF-8')) > 28.9):
                        print(2222222222)
                        edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                        comps.remove(code)
                        medos.append(code)
                        sumEd = sumEd + red
                    elif(float(exportData[i, 3].decode('UTF-8')) > 19.5 and ed >= wanna):
                        print(3333333333)
                        edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                        comps.remove(code)
                        medos.append(code)
                        sumEd = sumEd + red
                    elif((mmRate < rateLimit or fMedoTime < second_oTime) and ed >= wanna):
                        print(4444444444)
                        edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                        comps.remove(code)
                        medos.append(code)
                        sumEd = sumEd + red
                    elif(allMedoTime < second_oTime):
                        print(5555555555)
                        edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                        comps.remove(code)
                        medos.append(code)
                        sumEd = sumEd + red

                if(second_oTime > endTime):
                    continue;

                rate = exportData[i, 3].decode('UTF-8')
                grade = int(exportData[i, 1].decode('UTF-8'))
                gr = int(exportData[i, 4].decode('UTF-8'))

                ms_md = (exportData[i,5].astype(float))/(exportData[i,6].astype(float))
                sms_md = sp.sum(exportData[:i+1,5].astype(float))/sp.sum(exportData[:i+1,6].astype(float))
                
                if(code.decode('utf-8') == '060570'):
                    print(ms_md, sms_md, grade)

                if(ms_md > 0.96 and sms_md > 1 and grade < 13):
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
                    
                    if(gradient >= 0.7 and srgrad > 0):
                        if(code.decode('utf-8') in mesuDict):
                            mesuDict[code.decode('utf-8')] = mesuDict[code.decode('utf-8')] + 1
                        else:
                            mesuSTime[code.decode('utf-8')] = str_oTime
                            mesuDict[code.decode('utf-8')] = mesuDict.get(code.decode('utf-8'), 0)

                        if(xstime.tm_min < 2):
                            mesuLimit = [3]
                        elif(xstime.tm_min >= 2):
                            mesuLimit = [2,3]

                        if(mesuDict[code.decode('utf-8')] in mesuLimit and ((code) not in comps)):
                            if(i < 4):
                                s = 0
                            else:
                                s = i-4
                            mmlist = sp.array(exportData[s:i,6].astype(float))/(sp.array(srlist[s:i])*100000)
                            mmfit = sp.polyfit(x[:len(exportData[s:i,5])], mmlist, level)
                            mmgrad = sp.around(mmfit[0]*10, decimals=3)
                            if(mmgrad > 8):
                                nos.append(code)
                                continue;

                            if(True in (exportData[0:i,3].astype(float) > 23.5)):
                                nos.append(code)
                                continue;
                            
                            lfit = sp.polyfit(x[-3:], y[-3:], level)
                            lg = sp.around(lfit[0]*10, decimals=2)
                            if(lg > 2 and True in (exportData[0:i,5].astype(float) == 0)):
                                nos.append(code)
                                continue;   
                            
                            comps.append((code))
                            mesuStart[code.decode('utf-8')] = i
                            msGradient[code.decode('utf-8')] = gradient
                            msGr[code.decode('utf-8')] = gr
                            msSmdms[code.decode('utf-8')] = sms_md 
                            msGrade[code.decode('utf-8')] = grade
                            msSrgrad[code.decode('utf-8')] = srgrad
                            msRate[code.decode('utf-8')] = float(exportData[i, 3].decode('UTF-8'))
                            rmsRate[code.decode('utf-8')] = float(exportData[i, 3].decode('UTF-8'))
                            pick[code.decode('utf-8')] = False
                            setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) +  ',' + str(float(exportData[i, 3].decode('UTF-8'))) + '\n')

    except Exception as e:
        print("---------------------------------------" + str(e))
        continue

print(today)