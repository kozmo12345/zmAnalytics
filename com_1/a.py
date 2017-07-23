#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time
import re

sp.random.seed(3)

def shouldBuy(arr_six, num):
    if(len(arr_six) < num):
        return False

    abs_diff = abs(arr_six[0]*6 - sum(arr_six))
    grd = sp.polyfit(sp.array(range(num)), arr_six, 1)
    grdf = sp.around(grd[0], decimals=2)
    std = sp.std(arr_six)
    if(grdf > -0.3 and grdf < 1 and std < 3):
        # print(arr_six, grdf, std)
        return True
    
    return False

now = datetime.datetime.now()
print(str(datetime.datetime.now()))


today = now.strftime('%Y-%m-%d')

for dirname, dirnames, filenames in os.walk("C:\\Dropbox\\com_1\\Data\\"):
    for subdirname in dirnames:
        today = subdirname

        startTime = datetime.timedelta(hours=9,minutes=00,seconds=00).total_seconds()
        endTime = datetime.timedelta(hours=9,minutes=12,seconds=30).total_seconds()
        fMedoTime = datetime.timedelta(hours=9,minutes=19,seconds=50).total_seconds()
        allMedoTime = datetime.timedelta(hours=9,minutes=23,seconds=20).total_seconds()
        wanna = 1
        mesuLimit = [2]
        rateLimit = 0.31
        rateMLimit = 3.1
        stdLimit = 2
        sumEd = 0
        gradient = 0        

        print(today)
        setFile = open(os.path.join("C:\\", "Dropbox\\com_1\\Data\\" + today + "\\" + today + "moa4.txt"), 'w')
        edFile = open(os.path.join("C:\\", "Dropbox\\com_1\\Data\\" + today + "\\" + today + "ed2.txt"), 'w')
        realfilePath = os.path.join("C:\\", "Dropbox\\com_1\\Data\\" + today + "\\" + today + ".txt");
        
        data = sp.genfromtxt(realfilePath, delimiter="\t", dtype='|S20')
        codes = sp.unique(data[data[:,7] != b''][:,7])
        times = sp.unique(data[data[:,0] != b''][:,0])
        
        if(False):
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
                    
                    if(str(xstime.tm_sec)[-1] == '8'):
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
        pickI = dict()
        isd = dict()
        isd2 = dict()
        cggradDic = dict()
        levelUpDic = dict()
        delayMesu = dict()
        
        prev_oTime = 0
        allmedo = False
        
        for ttime in times:
            try:
                xstime = time.strptime(ttime.decode('utf-8'), '%H:%M:%S')
                second_oTime = datetime.timedelta(hours=xstime.tm_hour,minutes=xstime.tm_min,seconds=xstime.tm_sec).total_seconds() #계산시간
                str_oTime = "ttime.decode('utf-8')"
                bool_oTime = True
                
                if(second_oTime - prev_oTime > 60 and prev_oTime != 0):
                    allmedo = True
                prev_oTime = datetime.timedelta(hours=xstime.tm_hour,minutes=xstime.tm_min,seconds=xstime.tm_sec).total_seconds() #계산시간
                
                if(second_oTime < startTime):
                    continue;
        
                if(second_oTime > endTime and len(comps) == 0):
                    break;
        
                tmp_time = second_oTime
                
                # print(today + str(ttime))
                if(xstime.tm_min > 3):
                    nzData = data[data[:,2] != b'']
                    ttimeData = nzData[nzData[:,0] == ttime]
                    ttimeData2 = ttimeData[ttimeData[:,1].astype(int) < 10]
                    ttimeData3 = ttimeData2[ttimeData2[:,4].astype(int) > 100000]
                    ttimeData4 = ttimeData3[ttimeData3[:,3].astype(float) < 7   ]
                    ttimeData5 = ttimeData4[ttimeData4[:,8].astype(float) > 2200]
                    codes = ttimeData5[:,7]
        
                    if(second_oTime > endTime):
                        codes = comps
        
                    for code in (codes):
                        if(code == b''):
                            continue;
                        exportData = data[data[:,7] == code]
                        exportData = exportData[exportData[:,9].astype(float) != 0]
                        exportData = exportData[exportData[:,9].astype(float) != 500]
        
                        if(len(exportData[:,0])==0):
                            continue;
        
                        xtime = time.strptime(exportData[0,0].decode('utf-8'), '%H:%M:%S')
                        firstSecond = datetime.timedelta(hours=xtime.tm_hour,minutes=xtime.tm_min,seconds=xtime.tm_sec).total_seconds()
        
                        if(len(sp.where(exportData[:, 0] == ttime)[0]) != 0):
                            i = sp.where(exportData[:, 0] == ttime)[0][0]
                        else: continue
        
                        c = exportData[:i+1, 3].astype(float)
        
                        if(code in comps):
                            if(i < mesuStart[code.decode('utf-8')] + 3 ):
                                continue;
        
                            mdpCost = (exportData[i,4].astype(float) - exportData[i-1,4].astype(float)) * exportData[i-1,8].astype(float)
         
                            ms = float(msRate[code.decode('utf-8')])
                            rms = float(rmsRate[code.decode('utf-8')])
                            md = float(exportData[i, 3].decode('UTF-8'))
                            ed = round(md - ms, 2)
                            red = round(md - ms - 1, 2)
                            mdTime = exportData[i, 0].decode('UTF-8')
                            msTime = exportData[mesuStart[code.decode('utf-8')],0].decode('UTF-8')
                            allMax = max(exportData[i:, 3].astype(float))
                            termMin = min(exportData[mesuStart[code.decode('utf-8')]:i+1, 3].astype(float))
                            termMax = max(exportData[mesuStart[code.decode('utf-8')]:i+1, 3].astype(float))
                            msCost = (exportData[mesuStart[code.decode('utf-8')] + 1,4].astype(float) - exportData[mesuStart[code.decode('utf-8')],4].astype(float)) * exportData[mesuStart[code.decode('utf-8')],8].astype(float)
                            mdCost = (exportData[i + 1,4].astype(float) - exportData[i,4].astype(float)) * exportData[i,8].astype(float)
        
                            tempWan = wanna
                            med = ed                               
                            if((ms - md) > 1 or ed > 1):
                                isd[code.decode('utf-8')] = True
                            if(isd[code.decode('utf-8')]):
                                tempWan = 0.4
                            if((ms - md) > 2):
                                isd2[code.decode('utf-8')] = True
                            if(isd2[code.decode('utf-8')]):
                                med = ed * 1.8
                            mmRate = (sp.sum(exportData[i-stdLimit:i+1,5].astype(float)))/(sp.sum(exportData[i-stdLimit:i+1,6].astype(float))) - ((med)/22)
        
                            thGr = int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8'))                  
                            nowGr = int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8'))
                            grRate = 0
                            if(len(exportData[:i, 4]) > 6 and int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8')) != 0 and int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')) != 0):
                                grRate = (int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8'))) / (int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')))
        
                            if(exportData[i, 9].astype('float') < 103 or (ed > 2.8 and int(exportData[i, 4].decode('UTF-8')) < 800000) or (grRate > 1.78 and int(exportData[i, 4].decode('UTF-8')) < 800000) or (grRate > 3 and chegang < 155)):
                                pick[code.decode('utf-8')] = True
                                pickI[code.decode('utf-8')] = i
        
                            cgfit1 = sp.polyfit(sp.array(range(5)), exportData[i-4:i+1,9].astype(float), 1)
                            cggrad1 = sp.around(cgfit1[0], decimals=2)
        
                            cggrad2 = cggrad1
                            if(i > 4):
                                cgfit2 = sp.polyfit(sp.array(range(6)), exportData[i-5:i+1,9].astype(float), 1)
                                cggrad2 = sp.around(cgfit2[0], decimals=2)
                            
                            cggrad3 = cggrad2
                            if(i > 5):
                                cgfit3 = sp.polyfit(sp.array(range(7)), exportData[i-6:i+1,9].astype(float), 1)
                                cggrad3 = sp.around(cgfit3[0], decimals=2)
                            
                            gcggrad = min([cggrad1, cggrad2, cggrad3])
                            chegang = exportData[i,9].astype(float)
                            if(chegang < 120):
                                gcggrad = -10
        
                            nf = 0
                            fl = 0
                            nfaver = 0
                            flaver = 0
                            gap = 0
                            levelUpDic[code.decode('utf-8')] = []
                            levelUpDic[code.decode('utf-8')].append(0)
                            rrrr =  0
        
                            for x in range(0,xstime.tm_min + 1):
                                r = re.compile('09:' + str(x).rjust(2, '0') + ':..')
                                vmatch = sp.vectorize(lambda x:bool(r.match(x)))
                                vmatch(exportData[:,0].astype(str))
                                tmarr = exportData[:,3].astype(str)[vmatch(exportData[:,0].astype(str))].astype(float)
        
                                if(len(tmarr) == 0):
                                    continue;
            
                                if(fl != 0):
                                    if(nfaver != 0):
                                        flaver = (tmarr[0] + fl) / 2
        
                                        if(gap != 0 and gap * 1.5 < (flaver - nfaver)):
                                            levelUpDic[code.decode('utf-8')].append((flaver - nfaver))
                                            rrrr =  flaver - exportData[i, 3].astype(float)
        
                                            if((flaver - nfaver) > 4.26 and ed > 0.4):
                                                pick[code.decode('utf-8')] = True
                                                pickI[code.decode('utf-8')] = i
                                                break;
        
                                            if((flaver - nfaver) > 4.26 and i > mesuStart[code.decode('utf-8')] + 12):
                                                pick[code.decode('utf-8')] = True
                                                pickI[code.decode('utf-8')] = i
                                                break;
        
                                        else:
                                            levelUpDic[code.decode('utf-8')].append(0)
                                        
                                        if(flaver - nfaver < 0):
                                            gap = 1.8
                                        else:
                                            gap = flaver - nfaver
        
                                    nfaver = (fl + tmarr[0]) / 2
                                
                                nf = tmarr[0]
                                fl = tmarr[-1]
        
                            if(code not in comps):
                                continue;
        
                            if((pick[code.decode('utf-8')] and ed >= 0.4) or (i > mesuStart[code.decode('utf-8')] + 18 and pick[code.decode('utf-8')] and ed >= 0.1)):
                                print(ttime, code, 1111111111)
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                                comps.remove(code)
                                medos.append(code)
                                sumEd = sumEd + red
                            elif(pick[code.decode('utf-8')] and pickI[code.decode('utf-8')] > i + 30):
                                print(ttime, code, 9999999999)
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                                comps.remove(code)
                                medos.append(code)
                                sumEd = sumEd + red
                            elif(mesuStart[code.decode('utf-8')] + 60 < i and ed > 0.4 and ed < 2.5):
                                print(ttime, code, 2222222222)
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                                comps.remove(code)
                                medos.append(code)
                                sumEd = sumEd + red
                            elif(allmedo):
                                print(ttime, code, 3333333333)
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                                comps.remove(code)
                                medos.append(code)
                                sumEd = sumEd + red                        
                            elif(mesuStart[code.decode('utf-8')] + 36 < i and ed > -0.1 and ed < 1 and max(exportData[:i,9].astype(float)) < 275):
                                print(ttime, code, 2222222222)
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                                comps.remove(code)
                                medos.append(code)
                                sumEd = sumEd + red
                            elif(float(exportData[i, 3].decode('UTF-8')) > 28.9):
                                print(ttime, code, 2222222222)
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                                comps.remove(code)
                                medos.append(code)
                                sumEd = sumEd + red                        
                            elif((mmRate < rateLimit or mmRate > rateMLimit or fMedoTime < second_oTime) and gcggrad < -1.7 and ed >= tempWan):
                                print(ttime, code, 4444444444)
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                                comps.remove(code)
                                medos.append(code)
                                sumEd = sumEd + red
                            elif(allMedoTime < second_oTime):
                                print(ttime, code, 5555555555)
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                                comps.remove(code)
                                medos.append(code)
                                sumEd = sumEd + red
                            elif(len(exportData[:,3].astype(float)) - 4 < i):
                                print(ttime, code, 7777777777)
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                                comps.remove(code)
                                medos.append(code)
                                sumEd = sumEd + red                   
        
                        if(second_oTime > endTime or allmedo):
                            continue;
        
                        rate = exportData[i, 3].decode('UTF-8')
                        grade = int(exportData[i, 1].decode('UTF-8'))
                        gr = int(exportData[i, 4].decode('UTF-8'))
        
                        ms_md = (exportData[i,5].astype(float))/(exportData[i,6].astype(float))
                        sms_md = sp.sum(sp.unique(exportData[:i+1,5].astype(float)))/sp.sum(sp.unique(exportData[:i+1,6].astype(float)))
                        gr1 = int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-1, 4].decode('UTF-8')) != 0
                        
                        cgfit = sp.polyfit(sp.array(range(i+1)), exportData[:i+1,9].astype(float), 1)
                        cggrad = sp.around(cgfit[0], decimals=2)
                        chegang = exportData[i,9].astype(float)
        
                        if(code.decode('utf-8') not in cggradDic):
                            cggradDic[code.decode('utf-8')] = []
                        else:
                            cggradDic[code.decode('utf-8')].append(cggrad)
        
                        grRate = 0
                        if(len(exportData[:i, 4]) > 6 and int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8')) != 0 and int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')) != 0):
                            thGr = int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8'))                  
                            nowGr = int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8'))
                            grRate = nowGr / thGr
        
                        if(chegang < 140 or chegang > 300):
                            continue;
        
                        if(cggrad < -0.1):
                            x = sp.array(range(i+1))
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
                            ltdc = exportData[i,4].astype(float) - exportData[i-1,4].astype(float)
        
                            wlevel = 1
                            if(code.decode('utf-8') in mesuDict):
                                wlevel = mesuDict[code.decode('utf-8')] + 2
        
                            if(True):
        
                                if(code.decode('utf-8') in mesuDict):
                                    mesuDict[code.decode('utf-8')] = mesuDict[code.decode('utf-8')] + 1
                                else:
        
                                    mesuSTime[code.decode('utf-8')] = str_oTime
                                    mesuDict[code.decode('utf-8')] = mesuDict.get(code.decode('utf-8'), 0)
                                num = 6
                                if(shouldBuy(exportData[i-num+1:i+1,9].astype(float), num) and code not in comps and code not in medos):
        
                                    if(True in (exportData[:i+1, 9].astype(float) < chegang - 8)):
                                        continue;
        
                                    if(exportData[i, 3].astype(float) < 4 or exportData[i, 3].astype(float) > 19.6):
                                        print(ttime, code, 'nostttttt')
                                        continue;
        
        
                                    cost = int(exportData[i, 8].decode('UTF-8'))
                                    if(cost > 9000):
                                        # print(ttime, code, 'nos909090')
                                        nos.append(code)
                                        continue;
        
                                    if(i < 4):
                                        s = 0
                                        continue;
                                    else:
                                        s = i-4
        
                                    comps.append((code))
                                    mesuStart[code.decode('utf-8')] = i
                                    msGradient[code.decode('utf-8')] = gradient
                                    msGr[code.decode('utf-8')] = gr
                                    msSmdms[code.decode('utf-8')] = sms_md 
                                    msGrade[code.decode('utf-8')] = grade
                                    msSrgrad[code.decode('utf-8')] = 0
                                    msRate[code.decode('utf-8')] = float(exportData[i, 3].decode('UTF-8'))
                                    rmsRate[code.decode('utf-8')] = float(exportData[i, 3].decode('UTF-8'))
                                    pick[code.decode('utf-8')] = False
                                    pickI[code.decode('utf-8')] = 0
                                    isd[code.decode('utf-8')] = False
                                    isd2[code.decode('utf-8')] = False                            
                                    setFile.write(str(ttime) + ',' + str(code.decode('utf-8')) + ',' + str(float(rate)) +  ',' + str(float(exportData[i, 3].decode('UTF-8'))) + '\n')
        
            except Exception as e:
                dd
                print("---------------------------------------" + str(e))
                continue
        
        print(today)


analFilePath = os.path.join("C:\\", "Dropbox\\com_1\\Data\\" + "anal2.txt");
analFile = open(analFilePath, 'w')

edFilePath = os.path.join("C:\\", "Dropbox\\com_1\\Data\\" + "ed2.txt");
edFile = open(edFilePath, 'w')

edFile.write('day' +  ',' + 'sumEd' +  ',' + 'code' +  ',' + 'max' ',' + 'termMin' +  ',' + 'termMax' +  ',' + 'md' +  ',' + 'ms' +  ',' + 'ed' +  ',' + 'msTime' +  ',' + 'mdTime' + '\n')

for dirname, dirnames, filenames in os.walk("C:\\Dropbox\\com_1\\Data\\"):
    for subdirname in dirnames:
        today = subdirname

        setFilePath = os.path.join("C:\\", "Dropbox\\com_1\\Data\\" + today + "\\" + today + "moa4.txt");
        setFile = open(setFilePath, 'r')
        
        for line in setFile:
            analFile.write(today + ',' + line)

        set2FilePath = os.path.join("C:\\", "Dropbox\\com_1\\Data\\" + today + "\\" + today + "ed2.txt");
        set2File = open(set2FilePath, 'r')
        
        for line in set2File:
            edFile.write(today + ',' + str(sumEd) + ',' + line)

print("end")            

now = datetime.datetime.now()
print(str(datetime.datetime.now()))