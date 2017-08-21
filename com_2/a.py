#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time
import re

sp.random.seed(3)

def std_based_outlier(code,ms, md):
    if(len(ms) < 2):
        return ms, md

    ms = ms[ms!=0]
    md = md[md!=0]

    for i in range(0, len(ms)):
        if(np.abs(ms[i] - ms[:].mean()) > (2.9*ms[:].std())):
            ms[i] = 0
            md[i] = 0
        
        if(np.abs(md[i] - md[:].mean()) > (2.9*md[:].std())):
            ms[i] = 0
            md[i] = 0

    return ms, md

now = datetime.datetime.now()
print(str(datetime.datetime.now()))

ones = list()

startTime = datetime.timedelta(hours=9,minutes=00,seconds=00).total_seconds()
endTime = datetime.timedelta(hours=9,minutes=12,seconds=30).total_seconds()
fMedoTime = datetime.timedelta(hours=9,minutes=19,seconds=50).total_seconds()
allMedoTime = datetime.timedelta(hours=9,minutes=24,seconds=20).total_seconds()

mesuLimit = [2]
rateLimit = 0.31
rateMLimit = 3.8
stdLimit = 2
sumEd = 0
originM = 0
for dirname, dirnames, filenames in os.walk("C:\\Dropbox\\com_2\\Data\\"):
    for subdirname in dirnames:
        today = subdirname
        # if(today != '2017-02-28'):
        #     break;
        # today = '2017-05-22'
        print(today)
        setFile = open(os.path.join("C:\\", "Dropbox\\com_2\\Data\\" + today + "\\" + today + "moa3.txt"), 'w')
        edFile = open(os.path.join("C:\\", "Dropbox\\com_2\\Data\\" + today + "\\" + today + "ed2.txt"), 'w')
        realfilePath = os.path.join("C:\\", "Dropbox\\com_2\\Data\\" + today + "\\" + today + ".txt");
        
        data = sp.genfromtxt(realfilePath, delimiter="\t", dtype='|S20')
        codes = sp.unique(data[data[:,7] != b''][:,7])
        times = sp.unique(data[data[:,0] != b''][:,0])

        wanna = 1
        gradient = 0
        tmp_time = 0
        mesuDict = dict()
        mesuArr = dict()
        mesuAver = dict()
        mesuStart = dict()
        msRate = dict()
        rmsRate = dict()
        comps = []
        medos = []
        nos = []
        mdms = dict()
        mesuSTime = dict()
        msGradient = dict()
        msGr = dict()
        msSmdms = dict()
        msGrade = dict()
        msSrgrad = dict()
        pick = dict()
        isd = dict()
        isd2 = dict()
        mesuIndex = dict()
        cggradDic = dict()
        nosDic = dict()
        levelUpDic = dict()
        delayMesu = dict()
        findRate = dict()
        gradiDic = dict()
        endIndex = dict()
        bbamd =  dict()
        prev_oTime = 0
        allmedo = False

        print(today + ' data')
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
                
                if(bool_oTime == True):
                    nzData = data[data[:,2] != b'']
                    ttimeData = nzData[nzData[:,0] == ttime]                    
                    ttimeData2 = ttimeData[ttimeData[:,1].astype(int) < 51]
                    ttimeData3 = ttimeData2[ttimeData2[:,4].astype(int) > 57000]
                    ttimeData4 = ttimeData3[ttimeData3[:,3].astype(float) < 18]
                    ttimeData5 = ttimeData4[ttimeData4[:,8].astype(float) > 800]
                    codes = ttimeData5[:,7]

                    if(second_oTime > endTime):
                        codes = comps

                    for code in (codes):
                        if(code == b''):
                            continue;
                        exportData = data[data[:,7] == code]
                        exportData = exportData[exportData[:,9].astype(float) != 0]
                        
                        if(len(exportData[:,0])==0):
                            continue;
 
                        xtime = time.strptime(exportData[0,0].decode('utf-8'), '%H:%M:%S')
                        firstSecond = datetime.timedelta(hours=xtime.tm_hour,minutes=xtime.tm_min,seconds=xtime.tm_sec).total_seconds()

                        if(len(sp.where(exportData[:, 0] == ttime)[0]) != 0):
                            i = sp.where(exportData[:, 0] == ttime)[0][0]
                        else: continue

                        if(i < 2):
                            continue;

                        if(code in comps):
                            if(i < mesuStart[code.decode('utf-8')] + 3):
                                continue;

                            ms = float(msRate[code.decode('utf-8')])
                            rms = float(rmsRate[code.decode('utf-8')])
                            md = float(exportData[i, 3].decode('UTF-8'))
                            ed = round(md - ms, 2)
                            red = round(md - ms - 1, 3)
                            mdTime = exportData[i, 0].decode('UTF-8')
                            msTime = exportData[mesuStart[code.decode('utf-8')],0].decode('UTF-8')
                            allMax = max(exportData[i:, 3].astype(float))
                            termMin = min(exportData[mesuStart[code.decode('utf-8')]:i+1, 3].astype(float))
                            minChe = min(exportData[mesuStart[code.decode('utf-8')]:i+1, 9].astype(float))
                            termMax = max(exportData[mesuStart[code.decode('utf-8')]:i+1, 3].astype(float))
                            msCost = (exportData[mesuStart[code.decode('utf-8')] + 1,4].astype(float) - exportData[mesuStart[code.decode('utf-8')],4].astype(float)) * exportData[mesuStart[code.decode('utf-8')],8].astype(float)
                            mdCost = (exportData[i + 1,4].astype(float) - exportData[i,4].astype(float)) * exportData[i,8].astype(float)
                            mdpCost = (exportData[i,4].astype(float) - exportData[i-2,4].astype(float)) * exportData[i-1,8].astype(float)
                            mdpCost2 = (exportData[i-1,4].astype(float) - exportData[i-2,4].astype(float)) * exportData[i-2,8].astype(float)
                            
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

                            chegang = exportData[i,9].astype(float)

                            if(code.decode('utf-8') not in pick):
                                continue;

                            nosDic[code.decode('utf-8')] = exportData[mesuStart[code.decode('utf-8')],8].astype(float)

                            # if(code.decode('utf-8') in bbamd):
                            #     msSrgrad[code.decode('utf-8')] = 99

                            if(mesuStart[code.decode('utf-8')] + 53 < i and chegang < 200):
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) + ',' + str(nosDic[code.decode('utf-8')]) +  ',' + str(mesuIndex[code.decode('utf-8')]) + '\n')
                                comps.remove(code)
                                sumEd = sumEd + red
                                medos.append(code)
                                del pick[code.decode('utf-8')]
                                del endIndex[code.decode('utf-8')]

                            elif(code.decode('utf-8') in bbamd and ed > 0.7 and chegang < 200 and mesuStart[code.decode('utf-8')] + 3 < i):
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) + ',' + str(nosDic[code.decode('utf-8')]) +  ',' + str(mesuIndex[code.decode('utf-8')]) + '\n')
                                comps.remove(code)
                                sumEd = sumEd + red
                                medos.append(code)
                                del pick[code.decode('utf-8')]
                                del endIndex[code.decode('utf-8')]

                            elif(mesuStart[code.decode('utf-8')] + 62 < i):
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) + ',' + str(nosDic[code.decode('utf-8')]) +  ',' + str(mesuIndex[code.decode('utf-8')]) + '\n')
                                comps.remove(code)
                                sumEd = sumEd + red
                                medos.append(code)
                                del pick[code.decode('utf-8')]
                                del endIndex[code.decode('utf-8')]

                            elif( len(exportData[:,4].astype(float)) - 4 < i):
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) + ',' + str(nosDic[code.decode('utf-8')]) +  ',' + str(mesuIndex[code.decode('utf-8')]) + '\n')
                                comps.remove(code)
                                sumEd = sumEd + red
                                medos.append(code)
                                del pick[code.decode('utf-8')]
                                del endIndex[code.decode('utf-8')]


                        if(second_oTime > endTime and code.decode('utf-8') in endIndex):
                            endIndex[code.decode('utf-8')] = i;

                        if(second_oTime > endTime or allmedo):
                            continue;

                        rate = exportData[i, 3].decode('UTF-8')
                        grade = int(exportData[i, 1].decode('UTF-8'))
                        gr = int(exportData[i, 4].decode('UTF-8'))

                        gr1 = int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-1, 4].decode('UTF-8'))
                        ms_md = (exportData[i,5].astype(float))/(exportData[i,6].astype(float))
                        sms_md = sp.sum(sp.unique(exportData[:i+1,5].astype(float)))/sp.sum(sp.unique(exportData[:i+1,6].astype(float)))

                        cgfit = sp.polyfit(sp.array(range(i+1)), exportData[:i+1,9].astype(float), 1)
                        cggrad = sp.around(cgfit[0], decimals=2)
                        chegang = exportData[i,9].astype(float)
                        grRate = 0

                        if(chegang < 80 and exportData[i, 1].astype(int) < 4 and code not in nos):
                            nos.append(code)
                            continue;

                        if(len(exportData[:i, 4]) > 6 and int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8')) != 0 and int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')) != 0):
                            grRate = (int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8'))) / (int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')))
                        
                        if(code.decode('utf-8') in delayMesu and delayMesu[code.decode('utf-8')] + 1 < i and delayMesu[code.decode('utf-8')] + 6 > i and grRate < 0.89 and (int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-1, 4].decode('UTF-8'))) > 1000 and code not in comps and chegang < 400):

                            fcgfit1 = sp.polyfit(sp.array(range(4)), exportData[i-3:i+1,9].astype(float), 1)
                            fcggrad1 = sp.around(fcgfit1[0], decimals=2)
        
                            fcgfit2 = sp.polyfit(sp.array(range(5)), exportData[i-4:i+1,9].astype(float), 1)
                            fcggrad2 = sp.around(fcgfit2[0], decimals=2)                            

                            fcgfit3 = sp.polyfit(sp.array(range(6)), exportData[i-5:i+1,9].astype(float), 1)
                            fcggrad3 = sp.around(fcgfit3[0], decimals=2)

                            fcggrad = min([fcggrad1, fcggrad2, fcggrad3])

                            maxminamin = max(exportData[i-5:i+1,3].astype(float)) - min(exportData[i-5:i+1,3].astype(float))

                            if(findRate[code.decode('utf-8')] + 3 < exportData[i, 3].astype(float)):
                                del delayMesu[code.decode('utf-8')]
                                del findRate[code.decode('utf-8')]
                                continue;

                            if(findRate[code.decode('utf-8')] + 1.5 < exportData[i, 3].astype(float)):
                                delayMesu[code.decode('utf-8')] = delayMesu[code.decode('utf-8')] + 1
                                continue;                                

                            if(fcggrad < -18 and xstime.tm_min < 8 and chegang > 160):
                                del delayMesu[code.decode('utf-8')]
                                del findRate[code.decode('utf-8')]
                                continue;

                            if(exportData[i, 3].astype(float) < 4.6 and chegang < 140):
                                del delayMesu[code.decode('utf-8')]
                                del findRate[code.decode('utf-8')]
                                continue;

                            mole = (exportData[i, 4].astype(int) - exportData[i-1, 4].astype(int))/exportData[i, 4].astype(int)

                            mole2 = (exportData[i, 4].astype(int) - exportData[i-2, 4].astype(int))/exportData[i, 4].astype(int)

                            # if(exportData[i, 4].astype(float) > 2000000 and mole < 0.03):
                            #     del delayMesu[code.decode('utf-8')]
                            #     del findRate[code.decode('utf-8')]
                            #     continue;

                            if(exportData[i, 3].astype(float) > 16.3):
                                print(ttime, code, 'dela 1717171717')
                                del delayMesu[code.decode('utf-8')]
                                del findRate[code.decode('utf-8')]
                                continue;                                

                            if(mole2 < 0.007):
                                print(ttime, code, 'nos00070007')
                                del delayMesu[code.decode('utf-8')]
                                del findRate[code.decode('utf-8')]
                                continue;

                            cost = exportData[i, 8].astype(int)
                            if(cost < 1980 or cost > 8800):
                                print(ttime, code, 'nos00070007')
                                del delayMesu[code.decode('utf-8')]
                                del findRate[code.decode('utf-8')]
                                continue;

                            # if(exportData[i,5].astype(float)/exportData[i,6].astype(float) < 0.57 and mmgrad < 15 and ammgrad > 13.2):
                            #     del delayMesu[code.decode('utf-8')]
                            #     del findRate[code.decode('utf-8')]
                            #     continue;

                            cheFee2 = (exportData[i, 4].astype(int) - exportData[i-1, 4].astype(int)) * exportData[i-2, 8].astype(int)
                            cheFee3 = (exportData[i-1, 4].astype(int) - exportData[i-2, 4].astype(int)) * exportData[i-2, 8].astype(int)
                            if(gr < 86000 and (cheFee2 > 200000 and cheFee2 < 4000000) or (cheFee3 > 200000 and cheFee3 < 4000000)):
                                del delayMesu[code.decode('utf-8')]
                                del findRate[code.decode('utf-8')]
                                continue;

                            if(gr > 660000 and gr < 2200000 and mole2 < 0.09):
                                bbamd[code.decode('utf-8')] = i

                            if(i < 4):
                                s = 0
                                continue;
                            else:
                                s = i-4
                            maxr = 100000
                            x = sp.array(range(i+1))
                            ry = (exportData[:i+1,4].astype(float))/maxr
                            srlist = [b - a for a,b in zip(ry,ry[1:])]                                                                                    
                            sry = (exportData[i-4:i+1,4].astype(float))/maxr
                            ssrlist = [b - a for a,b in zip(sry,sry[1:])]
                            ssrfit = sp.polyfit(x[:4], ssrlist, 1)
                            ssrgrad = sp.around(ssrfit[0]*10, decimals=2)

                            mmlist = sp.array(exportData[s+1:i+1,6].astype(float))/(sp.array(srlist[s:i])*100000)
                            mmfit = sp.polyfit(x[:len(exportData[s+1:i+1,5])], mmlist, 1)
                            mmgrad = sp.around(mmfit[0]*10, decimals=3)

                            ammlist = sp.array(exportData[s+1:i+1,5].astype(float))/(sp.array(srlist[s:i])*100000)
                            ammfit = sp.polyfit(x[:len(exportData[s+1:i+1,5])], ammlist, 1)
                            ammgrad = sp.around(ammfit[0]*10, decimals=3)

                            if(mmgrad > 10.07 and ammgrad < 15):
                                bbamd[code.decode('utf-8')] = i

                            fcgfit7 = sp.polyfit(sp.array(range(2)), exportData[i-1:i+1,9].astype(float), 1)
                            fcggrad7 = sp.around(fcgfit7[0], decimals=2)
        
                            fcgfit8 = sp.polyfit(sp.array(range(3)), exportData[i-2:i+1,9].astype(float), 1)
                            fcggrad8 = sp.around(fcgfit8[0], decimals=2)

                            ones.append([code.decode('utf-8'), today, second_oTime, 1])
                            comps.append((code))
                            mesuStart[code.decode('utf-8')] = i
                            msGradient[code.decode('utf-8')] = gradient
                            msGr[code.decode('utf-8')] = gr
                            msSmdms[code.decode('utf-8')] = (exportData[i, 4].astype(int) - exportData[i-1, 4].astype(int)) * exportData[i-1, 8].astype(int)
                            msGrade[code.decode('utf-8')] = (exportData[i-1, 4].astype(int) - exportData[i-2, 4].astype(int)) * exportData[i-2, 8].astype(int)
                            msSrgrad[code.decode('utf-8')] = float(exportData[i+7, 3].decode('UTF-8')) - float(exportData[i, 3].decode('UTF-8'))
                            msRate[code.decode('utf-8')] = float(exportData[i, 3].decode('UTF-8'))
                            rmsRate[code.decode('utf-8')] = float(exportData[i+1, 3].decode('UTF-8'))
                            pick[code.decode('utf-8')] = False
                            mesuIndex[code.decode('utf-8')] = exportData[i,9].astype(float) - exportData[i-1,9].astype(float)
                            isd[code.decode('utf-8')] = False
                            isd2[code.decode('utf-8')] = False
                            endIndex[code.decode('utf-8')] = 0
                            del delayMesu[code.decode('utf-8')]
                            del findRate[code.decode('utf-8')]
                            originM = originM + 1
                            setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) +  ',' + str(float(exportData[i, 3].decode('UTF-8'))) +  '\n')                            
 
                        if(code.decode('utf-8') not in cggradDic):
                            cggradDic[code.decode('utf-8')] = []
                        else:
                            cggradDic[code.decode('utf-8')].append(cggrad)                        
                        cost = int(exportData[i, 8].decode('UTF-8'))    
                        if(((cggrad > 2.3 and chegang > 163)) and grade < 16 and exportData[i, 3].astype(float) > 5 and code.decode('utf-8') not in delayMesu and gr1):
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
                            ltdc2 = exportData[i+1,4].astype(float) - exportData[i,4].astype(float)
                            
                            wlevel = 1
                            if(code.decode('utf-8') in mesuDict):
                                wlevel = mesuDict[code.decode('utf-8')] + 2

                            if(code.decode('utf-8') not in gradiDic):
                                gradiDic[code.decode('utf-8')] = []
                            else:
                                gradiDic[code.decode('utf-8')].append(gradient)   

                            cheFee1 = (exportData[i,4].astype(int) - exportData[i-1,4].astype(float)) * (exportData[i,8].astype(int) + exportData[i-1,8].astype(float)) / 2

                            if(gradient >= 0.65 + (0.02 * wlevel) and cheFee1 > (10000000 + 5000000 * wlevel/2) and srgrad > 0 and ltdc > 0):
                                if(code.decode('utf-8') in mesuDict):
                                    mesuDict[code.decode('utf-8')] = mesuDict[code.decode('utf-8')] + 1

                                    if(mesuDict[code.decode('utf-8')] == 1):
                                        mesuAver[code.decode('utf-8')] = second_oTime - mesuArr[code.decode('utf-8')]
                                        mesuArr[code.decode('utf-8')] = second_oTime                                 
                                    if(mesuDict[code.decode('utf-8')] == 2):
                                        mesuAver[code.decode('utf-8')] = mesuAver[code.decode('utf-8')] + second_oTime - mesuArr[code.decode('utf-8')]

                                else:
                                    mesuSTime[code.decode('utf-8')] = str_oTime
                                    mesuDict[code.decode('utf-8')] = mesuDict.get(code.decode('utf-8'), 0)
                                    mesuArr[code.decode('utf-8')] = second_oTime

                                if(mesuDict[code.decode('utf-8')] in mesuLimit and ((code) not in comps) and (code not in medos) and (code not in nos)):
                                    nosDic[code.decode('utf-8')] = []

                                    if(exportData[i, 3].astype(float) < 4 or exportData[i, 3].astype(float) > 18.9):
                                        nos.append(code)
                                        # nosDic[code.decode('utf-8')].append('1')
                                        continue;

                                    if(xstime.tm_min < 2):
                                        nos.append(code)
                                        continue;

                                    cost = int(exportData[i, 8].decode('UTF-8'))
                                    # if(cost > 9000):
                                    #     # nosDic[code.decode('utf-8')].append('3')
                                    #     nos.append(code)
                                    #     continue;

                                    if(i < 4):
                                        s = 0
                                        continue;
                                    else:
                                        s = i-4

                                    maxr = 100000
                                    sry = (exportData[i-4:i+1,4].astype(float))/maxr
                                    ssrlist = [b - a for a,b in zip(sry,sry[1:])]
                                    ssrfit = sp.polyfit(x[:4], ssrlist, level)
                                    ssrgrad = sp.around(ssrfit[0]*10, decimals=2)

                                    mmlist = sp.array(exportData[s+1:i+1,6].astype(float))/(sp.array(srlist[s:i])*100000)
                                    mmfit = sp.polyfit(x[:len(exportData[s+1:i+1,5])], mmlist, level)
                                    mmgrad = sp.around(mmfit[0]*10, decimals=3)

                                    ammlist = sp.array(exportData[s+1:i+1,5].astype(float))/(sp.array(srlist[s:i])*100000)
                                    ammfit = sp.polyfit(x[:len(exportData[s+1:i+1,5])], ammlist, level)
                                    ammgrad = sp.around(ammfit[0]*10, decimals=3)
                                    
                                    # if((mmgrad > 8.1 and ammgrad < 7.2)):
                                    #     nos.append(code)
                                    #     continue;

                                    if(True in (exportData[0:i,3].astype(float) > 22.5)):
                                        # nosDic[code.decode('utf-8')].append('5')
                                        nos.append(code)
                                        continue;

                                    lfit = sp.polyfit(sp.array(range(3)), y[-3:], level)
                                    lg = sp.around(lfit[0]*10, decimals=2)

                                    if(gradient < 1.1 and ssrgrad < -1):
                                        # nosDic[code.decode('utf-8')].append('7')
                                        nos.append(code)
                                        continue;

                                    fcgfit1 = sp.polyfit(sp.array(range(4)), exportData[i-3:i+1,9].astype(float), 1)
                                    fcggrad1 = sp.around(fcgfit1[0], decimals=2)
        
                                    fcggrad2 = fcggrad1
                                    if(i > 3):
                                        fcgfit2 = sp.polyfit(sp.array(range(5)), exportData[i-4:i+1,9].astype(float), 1)
                                        fcggrad2 = sp.around(fcgfit2[0], decimals=2)
         
                                    fcggrad = min([fcggrad1, fcggrad2])

                                    lcggrad = fcggrad
                                    
                                    if(i > 4):
                                        lcgfit = sp.polyfit(sp.array(range(6)), exportData[i-5:i+1,9].astype(float), 1)
                                        lcggrad = sp.around(lcgfit[0], decimals=2)

                                    if((chegang < 129 and lcggrad < -1.8) or lcggrad > 60):
                                        # nosDic[code.decode('utf-8')].append('8')
                                        nos.append(code)
                                        continue;

                                    tpg = 0
                                    msi = 0
                                    for ii in range(1,i):
                                        pi = ii * 3
                                        if(pi >= i):
                                            break

                                        pfit = sp.polyfit(x[:pi], y[-pi:], level)
                                        pgradient = sp.around(pfit[0]*10, decimals=2)
                                        if(tpg < pgradient and not sp.isinf(pgradient)):
                                            tpg = pgradient
                                            msi = pi

                                    tlen = len(cggradDic[code.decode('utf-8')])
                                    tfit = sp.polyfit(sp.array(range(tlen)), cggradDic[code.decode('utf-8')], 1)
                                    tgrad = sp.around(tfit[0], decimals=2)                                            

                                    if(tgrad < -6):
                                        # nosDic[code.decode('utf-8')].append('10')
                                        nos.append(code)
                                        continue;
                                    
                                    tmesu = ((exportData[i,4].astype(float) - exportData[i-1,4].astype(float)) * exportData[i,8].astype(float)) + ((exportData[i - 1,4].astype(float) - exportData[i - 2,4].astype(float)) * exportData[i-1,8].astype(float))
                                    if(tmesu > 250000000 and xstime.tm_min >= 6 and exportData[i, 3].astype(float) < 6.9):
                                        nos.append(code)
                                        continue;

                                    if(chegang > 250 and xstime.tm_min <= 3 and exportData[i,3].astype(float) < 5.7):
                                        nos.append(code)
                                        continue;

                                    levelUpDic[code.decode('utf-8')] = []
                
                                    for x in range(0,xstime.tm_min + 1):
                                        r = re.compile('09:' + str(x).rjust(2, '0') + ':..')
                                        vmatch = sp.vectorize(lambda x:bool(r.match(x)))
                                        vmatch(exportData[:i+1,0].astype(str))
                                        tmarr = exportData[:i+1,3].astype(str)[vmatch(exportData[:i+1,0].astype(str))].astype(float)
                                        if(len(tmarr) == 0):
                                            continue;
        
                                        levelUpDic[code.decode('utf-8')].append((tmarr[-1] - tmarr[0]))
        
                                    if(True in (sp.array(levelUpDic[code.decode('utf-8')]) > 7.4)):
                                        print(ttime, code, 'nos121211212')
                                        nos.append(code)
                                        continue;

                                    if(len(exportData[:i+1,3].astype(float)) < 6):
                                        maxminamin = 0
                                    else:        
                                        maxminamin = max(exportData[i-5:i+1,3].astype(float)) - min(exportData[i-5:i+1,3].astype(float))
                                    if(maxminamin > 5):
                                        print(ttime, code, 'nos123321')
                                        nos.append(code)
                                        continue;

                                    # if(fcggrad < -15 and lg > 5):
                                    #     # nosDic[code.decode('utf-8')].append('9')
                                    #     nos.append(code)
                                    #     continue;                                                                        

                                    if(fcggrad < -19.5 and xstime.tm_min < 10 and chegang > 195):
                                        # nosDic[code.decode('utf-8')].append('9')
                                        nos.append(code)
                                        continue;

                                    grRate1 = 0
                                    if(len(exportData[:i, 4]) > 7 and int(exportData[i-1, 4].decode('UTF-8')) - int(exportData[i-4, 4].decode('UTF-8')) != 0 and int(exportData[i-4, 4].decode('UTF-8')) - int(exportData[i-7, 4].decode('UTF-8')) != 0):
                                        grRate1 = (int(exportData[i-1, 4].decode('UTF-8')) - int(exportData[i-4, 4].decode('UTF-8'))) / (int(exportData[i-4, 4].decode('UTF-8')) - int(exportData[i-7, 4].decode('UTF-8'))) + (exportData[i-1, 4].astype(int) / 10000000)
        
                                    grRate2 = 0
                                    if(len(exportData[:i, 4]) > 8 and int(exportData[i-2, 4].decode('UTF-8')) - int(exportData[i-5, 4].decode('UTF-8')) != 0 and int(exportData[i-5, 4].decode('UTF-8')) - int(exportData[i-8, 4].decode('UTF-8')) != 0):
                                        grRate2 = (int(exportData[i-2, 4].decode('UTF-8')) - int(exportData[i-5, 4].decode('UTF-8'))) / (int(exportData[i-5, 4].decode('UTF-8')) - int(exportData[i-8, 4].decode('UTF-8'))) + (exportData[i-2, 4].astype(int) / 10000000)
        
                                    grRate3 = 0
                                    if(len(exportData[:i, 4]) > 9 and int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')) != 0 and int(exportData[i-6, 4].decode('UTF-8')) - int(exportData[i-9, 4].decode('UTF-8')) != 0):
                                        grRate3 = (int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8'))) / (int(exportData[i-6, 4].decode('UTF-8')) - int(exportData[i-9, 4].decode('UTF-8'))) + (exportData[i-3, 4].astype(int) / 10000000)
        
                                    grRate4 = 0
                                    if(len(exportData[:i, 4]) > 10 and int(exportData[i-4, 4].decode('UTF-8')) - int(exportData[i-7, 4].decode('UTF-8')) != 0 and int(exportData[i-7, 4].decode('UTF-8')) - int(exportData[i-10, 4].decode('UTF-8')) != 0):
                                        grRate4 = (int(exportData[i-4, 4].decode('UTF-8')) - int(exportData[i-7, 4].decode('UTF-8'))) / (int(exportData[i-7, 4].decode('UTF-8')) - int(exportData[i-10, 4].decode('UTF-8'))) + (exportData[i-4, 4].astype(int) / 10000000)
        
                                    grRate5 = 0
                                    if(len(exportData[:i, 4]) > 11 and int(exportData[i-5, 4].decode('UTF-8')) - int(exportData[i-8, 4].decode('UTF-8')) != 0 and int(exportData[i-8, 4].decode('UTF-8')) - int(exportData[i-11, 4].decode('UTF-8')) != 0):
                                        grRate5 = (int(exportData[i-5, 4].decode('UTF-8')) - int(exportData[i-8, 4].decode('UTF-8'))) / (int(exportData[i-8, 4].decode('UTF-8')) - int(exportData[i-11, 4].decode('UTF-8'))) + (exportData[i-5, 4].astype(int) / 10000000)

                                    if(grRate > 5.89 or grRate1 > 5.89 or grRate2 > 5.89 or grRate3 > 5.89 or grRate4 > 5.89 or grRate5 > 5.89):
                                        nos.append(code)
                                        continue;

                                    if(grRate > 1.8 or grRate1 > 1.8 or grRate2 > 1.8 or grRate3 > 1.8 or grRate4 > 1.8 or grRate5 > 1.8 or chegang > 400 or exportData[i, 3].astype(float) - exportData[i-1, 3].astype(float) > 2):
                                        delayMesu[code.decode('utf-8')] = i
                                        findRate[code.decode('utf-8')] = exportData[delayMesu[code.decode('utf-8')], 3].astype(float)
                                        continue;

                                    # if(exportData[i,5].astype(float)/exportData[i,6].astype(float) < 0.57 and mmgrad < 15 and ammgrad > 13.2):
                                    #     nos.append(code)
                                    #     continue;                                        

                                    mole = (exportData[i, 4].astype(int) - exportData[i-1, 4].astype(int))/exportData[i, 4].astype(int)

                                    mole2 = (exportData[i, 4].astype(int) - exportData[i-2, 4].astype(int))/exportData[i, 4].astype(int)

                                    # if(exportData[i, 4].astype(float) > 2000000 and mole < 0.03):
                                    #     nos.append(code)
                                    #     continue;

                                    grilen = len(gradiDic[code.decode('utf-8')][-4:])
                                    grifit = sp.polyfit(sp.array(range(grilen)), gradiDic[code.decode('utf-8')][-4:], 1)
                                    grigrad = sp.around(grifit[0], decimals=2)                                               

                                    if(exportData[i, 3].astype(float) > 16.3):
                                        print(ttime, code, 'nos1717171717')
                                        nos.append(code)
                                        continue;

                                    if(mole2 < 0.007):
                                        print(ttime, code, 'nos00070007')
                                        nos.append(code)
                                        continue;

                                    cost = exportData[i, 8].astype(int)
                                    if(cost < 1980 or cost > 8800):
                                        # nosDic[code.decode('utf-8')].append('3')
                                        nos.append(code)
                                        continue;

                                    cheFee2 = (exportData[i, 4].astype(int) - exportData[i-1, 4].astype(int)) * exportData[i-2, 8].astype(int)
                                    cheFee3 = (exportData[i-1, 4].astype(int) - exportData[i-2, 4].astype(int)) * exportData[i-2, 8].astype(int)
                                    if(gr < 86000 and (cheFee2 > 200000 and cheFee2 < 4000000) or (cheFee3 > 200000 and cheFee3 < 4000000)):
                                        nos.append(code)
                                        continue;

                                    if(gr > 660000 and gr < 2200000 and mole2 < 0.09):
                                        bbamd[code.decode('utf-8')] = i

                                    if(mmgrad > 10.07 and ammgrad < 15):
                                        bbamd[code.decode('utf-8')] = i

                                    fcgfit7 = sp.polyfit(sp.array(range(2)), exportData[i-1:i+1,9].astype(float), 1)
                                    fcggrad7 = sp.around(fcgfit7[0], decimals=2)
                
                                    fcgfit8 = sp.polyfit(sp.array(range(3)), exportData[i-2:i+1,9].astype(float), 1)
                                    fcggrad8 = sp.around(fcgfit8[0], decimals=2)

                                    ones.append([code.decode('utf-8'), today, second_oTime, 1])
                                    comps.append((code))
                                    mesuStart[code.decode('utf-8')] = i
                                    msGradient[code.decode('utf-8')] = gradient
                                    msGr[code.decode('utf-8')] = gr
                                    msSmdms[code.decode('utf-8')] = (exportData[i, 4].astype(int) - exportData[i-1, 4].astype(int)) * exportData[i-1, 8].astype(int)
                                    msGrade[code.decode('utf-8')] = (exportData[i-1, 4].astype(int) - exportData[i-2, 4].astype(int)) * exportData[i-2, 8].astype(int)
                                    msSrgrad[code.decode('utf-8')] = float(exportData[i+7, 3].decode('UTF-8')) - float(exportData[i, 3].decode('UTF-8'))
                                    msRate[code.decode('utf-8')] = float(exportData[i, 3].decode('UTF-8'))
                                    rmsRate[code.decode('utf-8')] = float(exportData[i+1, 3].decode('UTF-8'))
                                    pick[code.decode('utf-8')] = False
                                    mesuIndex[code.decode('utf-8')] = exportData[i,9].astype(float) - exportData[i-1,9].astype(float)
                                    isd[code.decode('utf-8')] = False
                                    isd2[code.decode('utf-8')] = False
                                    endIndex[code.decode('utf-8')] = 0
                                    originM = originM + 1
                                    setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) +  ',' + str(float(exportData[i, 3].decode('UTF-8'))) +  '\n')

            except Exception as e:
                ss
                errFilePath = os.path.join("C:\\", "Dropbox\\com_2\\Data\\" + "err.txt");
                errFile = open(errFilePath, 'a')
                errFile.write(today + '\t' + str(e) + '\n')
                continue

        print(today)






startTime = datetime.timedelta(hours=9,minutes=00,seconds=00).total_seconds()
endTime = datetime.timedelta(hours=9,minutes=12,seconds=30).total_seconds()
fMedoTime = datetime.timedelta(hours=9,minutes=19,seconds=50).total_seconds()
allMedoTime = datetime.timedelta(hours=9,minutes=24,seconds=20).total_seconds()
mesuLimit = [2]
rateLimit = 0.31
rateMLimit = 3.8
stdLimit = 2
for dirname, dirnames, filenames in os.walk("C:\\Dropbox\\com_2\\diff\\"):
    for subdirname in dirnames:
        today = subdirname
        # if(today != '2017-03-31'):
        #     break;
        # today = '2017-04-05'

        print(today)
        setFile = open(os.path.join("C:\\", "Dropbox\\com_2\\diff\\" + today + "\\" + today + "moa3.txt"), 'w')
        edFile = open(os.path.join("C:\\", "Dropbox\\com_2\\diff\\" + today + "\\" + today + "ed2.txt"), 'w')
        realfilePath = os.path.join("C:\\", "Dropbox\\com_2\\diff\\" + today + "\\" + today + ".txt");
        
        data = sp.genfromtxt(realfilePath, delimiter="\t", dtype='|S20')
        codes = sp.unique(data[data[:,7] != b''][:,7])
        times = sp.unique(data[data[:,0] != b''][:,0])

        wanna = 1
        gradient = 0
        tmp_time = 0
        mesuDict = dict()
        mesuArr = dict()
        mesuAver = dict()
        mesuStart = dict()
        msRate = dict()
        rmsRate = dict()
        comps = []
        medos = []
        nos = []
        mdms = dict()
        mesuSTime = dict()
        msGradient = dict()
        msGr = dict()
        msSmdms = dict()
        msGrade = dict()
        msSrgrad = dict()
        pick = dict()
        isd = dict()
        isd2 = dict()
        mesuIndex = dict()
        cggradDic = dict()
        nosDic = dict()
        levelUpDic = dict()
        delayMesu = dict()
        findRate = dict()
        gradiDic = dict()
        endIndex = dict()
        bbamd =  dict()
        prev_oTime = 0
        allmedo = False

        print(today + ' diff')
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

                if(bool_oTime == True):
                    nzData = data[data[:,2] != b'']
                    # diffGr = ( xstime.tm_min - 2 ) * 10000
                    ttimeData = nzData[nzData[:,0] == ttime]                    
                    ttimeData2 = ttimeData[ttimeData[:,1].astype(int) < 51]
                    ttimeData3 = ttimeData2[ttimeData2[:,4].astype(int) > 57000]
                    ttimeData4 = ttimeData3[ttimeData3[:,3].astype(float) < 18]
                    ttimeData5 = ttimeData4[ttimeData4[:,8].astype(float) > 800]
                    codes = ttimeData5[:,7]

                    if(second_oTime > endTime):
                        codes = comps

                    for code in (codes):
                        if(code == b''):
                            continue;
                        exportData = data[data[:,7] == code]
                        exportData = exportData[exportData[:,9].astype(float) != 0]

                        if(len(exportData[:,0])==0):
                            continue;
                        
                        xtime = time.strptime(exportData[0,0].decode('utf-8'), '%H:%M:%S')
                        firstSecond = datetime.timedelta(hours=xtime.tm_hour,minutes=xtime.tm_min,seconds=xtime.tm_sec).total_seconds()
                    
                        if(len(sp.where(exportData[:, 0] == ttime)[0]) != 0):
                            i = sp.where(exportData[:, 0] == ttime)[0][0]
                        else: continue

                        if(i < 2):
                            continue;

                        if(code in comps):
                            if(i < mesuStart[code.decode('utf-8')] + 3):
                                continue;

                            ms = float(msRate[code.decode('utf-8')])
                            rms = float(rmsRate[code.decode('utf-8')])
                            md = float(exportData[i, 3].decode('UTF-8'))
                            ed = round(md - ms, 2)
                            red = round(md - ms - 1, 3)
                            mdTime = exportData[i, 0].decode('UTF-8')
                            msTime = exportData[mesuStart[code.decode('utf-8')],0].decode('UTF-8')
                            allMax = max(exportData[i:, 3].astype(float))
                            termMin = min(exportData[mesuStart[code.decode('utf-8')]:i+1, 3].astype(float))
                            minChe = min(exportData[mesuStart[code.decode('utf-8')]:i+1, 9].astype(float))
                            termMax = max(exportData[mesuStart[code.decode('utf-8')]:i+1, 3].astype(float))
                            msCost = (exportData[mesuStart[code.decode('utf-8')] + 1,4].astype(float) - exportData[mesuStart[code.decode('utf-8')],4].astype(float)) * exportData[mesuStart[code.decode('utf-8')],8].astype(float)
                            mdCost = (exportData[i + 1,4].astype(float) - exportData[i,4].astype(float)) * exportData[i,8].astype(float)
                            mdpCost = (exportData[i,4].astype(float) - exportData[i-2,4].astype(float)) * exportData[i-1,8].astype(float)
                            mdpCost2 = (exportData[i-1,4].astype(float) - exportData[i-2,4].astype(float)) * exportData[i-2,8].astype(float)
                            
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

                            chegang = exportData[i,9].astype(float)

                            if(code.decode('utf-8') not in pick):
                                continue;

                            nosDic[code.decode('utf-8')] = exportData[mesuStart[code.decode('utf-8')],8].astype(float)

                            # if(code.decode('utf-8') in bbamd):
                            #     msSrgrad[code.decode('utf-8')] = 99

                            if(mesuStart[code.decode('utf-8')] + 53 < i and chegang < 200):
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) + ',' + str(nosDic[code.decode('utf-8')]) +  ',' + str(mesuIndex[code.decode('utf-8')]) + '\n')
                                comps.remove(code)
                                sumEd = sumEd + red
                                medos.append(code)
                                del pick[code.decode('utf-8')]
                                del endIndex[code.decode('utf-8')]

                            elif(code.decode('utf-8') in bbamd and ed > 0.7 and chegang < 200 and mesuStart[code.decode('utf-8')] + 3 < i):
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) + ',' + str(nosDic[code.decode('utf-8')]) +  ',' + str(mesuIndex[code.decode('utf-8')]) + '\n')
                                comps.remove(code)
                                sumEd = sumEd + red
                                medos.append(code)
                                del pick[code.decode('utf-8')]
                                del endIndex[code.decode('utf-8')]

                            elif(mesuStart[code.decode('utf-8')] + 62 < i):
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) + ',' + str(nosDic[code.decode('utf-8')]) +  ',' + str(mesuIndex[code.decode('utf-8')]) + '\n')
                                comps.remove(code)
                                sumEd = sumEd + red
                                medos.append(code)
                                del pick[code.decode('utf-8')]
                                del endIndex[code.decode('utf-8')]

                            elif( len(exportData[:,4].astype(float)) - 4 < i):
                                edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) + ',' + str(nosDic[code.decode('utf-8')]) +  ',' + str(mesuIndex[code.decode('utf-8')]) + '\n')
                                comps.remove(code)
                                sumEd = sumEd + red
                                medos.append(code)
                                del pick[code.decode('utf-8')]
                                del endIndex[code.decode('utf-8')]


                        if(second_oTime > endTime and code.decode('utf-8') in endIndex):
                            endIndex[code.decode('utf-8')] = i;

                        if(second_oTime > endTime or allmedo):
                            continue;

                        rate = exportData[i, 3].decode('UTF-8')
                        grade = int(exportData[i, 1].decode('UTF-8'))
                        gr = int(exportData[i, 4].decode('UTF-8'))

                        gr1 = int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-1, 4].decode('UTF-8'))
                        ms_md = (exportData[i,5].astype(float))/(exportData[i,6].astype(float))
                        sms_md = sp.sum(sp.unique(exportData[:i+1,5].astype(float)))/sp.sum(sp.unique(exportData[:i+1,6].astype(float)))

                        cgfit = sp.polyfit(sp.array(range(i+1)), exportData[:i+1,9].astype(float), 1)
                        cggrad = sp.around(cgfit[0], decimals=2)
                        chegang = exportData[i,9].astype(float)
                        
                        if(chegang < 80 and exportData[i, 1].astype(int) < 4 and code not in nos):
                            nos.append(code)
                            continue;

                        grRate = 0
                        if(len(exportData[:i, 4]) > 6 and int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8')) != 0 and int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')) != 0):
                            grRate = (int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8'))) / (int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')))

                        if(code.decode('utf-8') in delayMesu and delayMesu[code.decode('utf-8')] + 1 < i and delayMesu[code.decode('utf-8')] + 6 > i and grRate < 0.89 and (int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-1, 4].decode('UTF-8'))) > 1000 and (int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-1, 4].decode('UTF-8'))) > 1000 and code not in comps and chegang < 400):
                            # if(exportData[i, 3].astype(float) > exportData[delayMesu[code.decode('utf-8')], 3].astype(float)):
                            #     continue

                            fcgfit1 = sp.polyfit(sp.array(range(4)), exportData[i-3:i+1,9].astype(float), 1)
                            fcggrad1 = sp.around(fcgfit1[0], decimals=2)
        
                            fcgfit2 = sp.polyfit(sp.array(range(5)), exportData[i-4:i+1,9].astype(float), 1)
                            fcggrad2 = sp.around(fcgfit2[0], decimals=2)

                            fcgfit3 = sp.polyfit(sp.array(range(6)), exportData[i-5:i+1,9].astype(float), 1)
                            fcggrad3 = sp.around(fcgfit3[0], decimals=2)
         
                            fcggrad = min([fcggrad1, fcggrad2, fcggrad3])

                            maxminamin = max(exportData[i-5:i+1,3].astype(float)) - min(exportData[i-5:i+1,3].astype(float))

                            if(findRate[code.decode('utf-8')] + 3 < exportData[i, 3].astype(float)):
                                del delayMesu[code.decode('utf-8')]
                                del findRate[code.decode('utf-8')]
                                continue;

                            if(findRate[code.decode('utf-8')] + 1.5 < exportData[i, 3].astype(float)):
                                delayMesu[code.decode('utf-8')] = delayMesu[code.decode('utf-8')] + 1
                                continue;

                            if(fcggrad < -18 and xstime.tm_min < 8 and chegang > 160):
                                del delayMesu[code.decode('utf-8')]
                                del findRate[code.decode('utf-8')]
                                continue;

                            if(exportData[i, 3].astype(float) < 4.6 and chegang < 140):
                                del delayMesu[code.decode('utf-8')]
                                del findRate[code.decode('utf-8')]
                                continue;

                            mole = (exportData[i, 4].astype(int) - exportData[i-1, 4].astype(int))/exportData[i, 4].astype(int)

                            mole2 = (exportData[i, 4].astype(int) - exportData[i-2, 4].astype(int))/exportData[i, 4].astype(int)

                            # if(exportData[i, 4].astype(float) > 2000000 and mole < 0.03):
                            #     del delayMesu[code.decode('utf-8')]
                            #     del findRate[code.decode('utf-8')]
                            #     continue;

                            if(exportData[i, 3].astype(float) > 16.3):
                                print(ttime, code, 'dela 1717171717')
                                del delayMesu[code.decode('utf-8')]
                                del findRate[code.decode('utf-8')]
                                continue;

                            if(mole2 < 0.007):
                                print(ttime, code, 'nos00070007')
                                del delayMesu[code.decode('utf-8')]
                                del findRate[code.decode('utf-8')]
                                continue;

                            cost = exportData[i, 8].astype(int)
                            if(cost < 1980 or cost > 8800):
                                print(ttime, code, 'nos00070007')
                                del delayMesu[code.decode('utf-8')]
                                del findRate[code.decode('utf-8')]
                                continue;

                            # if(exportData[i,5].astype(float)/exportData[i,6].astype(float) < 0.57 and mmgrad < 15 and ammgrad > 13.2):
                            #     del delayMesu[code.decode('utf-8')]
                            #     del findRate[code.decode('utf-8')]
                            #     continue;

                            cheFee2 = (exportData[i, 4].astype(int) - exportData[i-1, 4].astype(int)) * exportData[i-2, 8].astype(int)
                            cheFee3 = (exportData[i-1, 4].astype(int) - exportData[i-2, 4].astype(int)) * exportData[i-2, 8].astype(int)
                            if(gr < 86000 and (cheFee2 > 200000 and cheFee2 < 4000000) or (cheFee3 > 200000 and cheFee3 < 4000000)):
                                del delayMesu[code.decode('utf-8')]
                                del findRate[code.decode('utf-8')]
                                continue;

                            if(gr > 660000 and gr < 2200000 and mole2 < 0.09):
                                print(ttime, code, 'dela 2200000')
                                bbamd[code.decode('utf-8')] = i

                            if(i < 4):
                                s = 0
                                continue;
                            else:
                                s = i-4
                            maxr = 100000
                            x = sp.array(range(i+1))
                            ry = (exportData[:i+1,4].astype(float))/maxr
                            srlist = [b - a for a,b in zip(ry,ry[1:])]                                                                                    
                            sry = (exportData[i-4:i+1,4].astype(float))/maxr
                            ssrlist = [b - a for a,b in zip(sry,sry[1:])]
                            ssrfit = sp.polyfit(x[:4], ssrlist, 1)
                            ssrgrad = sp.around(ssrfit[0]*10, decimals=2)

                            mmlist = sp.array(exportData[s+1:i+1,6].astype(float))/(sp.array(srlist[s:i])*100000)
                            mmfit = sp.polyfit(x[:len(exportData[s+1:i+1,5])], mmlist, 1)
                            mmgrad = sp.around(mmfit[0]*10, decimals=3)

                            ammlist = sp.array(exportData[s+1:i+1,5].astype(float))/(sp.array(srlist[s:i])*100000)
                            ammfit = sp.polyfit(x[:len(exportData[s+1:i+1,5])], ammlist, 1)
                            ammgrad = sp.around(ammfit[0]*10, decimals=3)

                            if(mmgrad > 10.07 and ammgrad < 15):
                                bbamd[code.decode('utf-8')] = i

                            fcgfit7 = sp.polyfit(sp.array(range(2)), exportData[i-1:i+1,9].astype(float), 1)
                            fcggrad7 = sp.around(fcgfit7[0], decimals=2)
        
                            fcgfit8 = sp.polyfit(sp.array(range(3)), exportData[i-2:i+1,9].astype(float), 1)
                            fcggrad8 = sp.around(fcgfit8[0], decimals=2)
        
                            ones.append([code.decode('utf-8'), today, second_oTime, 2])
                            comps.append((code))
                            mesuStart[code.decode('utf-8')] = i
                            msGradient[code.decode('utf-8')] = gradient
                            msGr[code.decode('utf-8')] = gr
                            msSmdms[code.decode('utf-8')] = (exportData[i, 4].astype(int) - exportData[i-1, 4].astype(int)) * exportData[i-1, 8].astype(int)
                            msGrade[code.decode('utf-8')] = (exportData[i-1, 4].astype(int) - exportData[i-2, 4].astype(int)) * exportData[i-2, 8].astype(int)
                            msSrgrad[code.decode('utf-8')] = float(exportData[i+7, 3].decode('UTF-8')) - float(exportData[i, 3].decode('UTF-8'))
                            msRate[code.decode('utf-8')] = float(exportData[i, 3].decode('UTF-8'))
                            rmsRate[code.decode('utf-8')] = float(exportData[i+1, 3].decode('UTF-8'))
                            pick[code.decode('utf-8')] = False
                            mesuIndex[code.decode('utf-8')] = exportData[i,9].astype(float) - exportData[i-1,9].astype(float)
                            isd[code.decode('utf-8')] = False
                            isd2[code.decode('utf-8')] = False
                            endIndex[code.decode('utf-8')] = 0
                            del delayMesu[code.decode('utf-8')]
                            del findRate[code.decode('utf-8')]
                            originM = originM + 1
                            setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) +  ',' + str(float(exportData[i, 3].decode('UTF-8'))) +  '\n')                            
 
                        if(code.decode('utf-8') not in cggradDic):
                            cggradDic[code.decode('utf-8')] = []
                        else:
                            cggradDic[code.decode('utf-8')].append(cggrad)
                        cost = int(exportData[i, 8].decode('UTF-8'))    
                        if(((cggrad > 2.3 and chegang > 163)) and grade < 16 and exportData[i, 3].astype(float) > 5 and code.decode('utf-8') not in delayMesu and gr1):
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
                            ltdc2 = exportData[i+1,4].astype(float) - exportData[i,4].astype(float)
                            
                            wlevel = 1
                            if(code.decode('utf-8') in mesuDict):
                                wlevel = mesuDict[code.decode('utf-8')] + 2

                            if(code.decode('utf-8') not in gradiDic):
                                gradiDic[code.decode('utf-8')] = []
                            else:
                                gradiDic[code.decode('utf-8')].append(gradient)  

                            cheFee1 = (exportData[i,4].astype(int) - exportData[i-1,4].astype(float)) * (exportData[i,8].astype(int) + exportData[i-1,8].astype(float)) / 2

                            if(gradient >= 0.65 + (0.02 * wlevel) and cheFee1 > (10000000 + 5000000 * wlevel/2) and srgrad > 0 and ltdc > 0):
                                if(code.decode('utf-8') in mesuDict):
                                    mesuDict[code.decode('utf-8')] = mesuDict[code.decode('utf-8')] + 1

                                    if(mesuDict[code.decode('utf-8')] == 1):
                                        mesuAver[code.decode('utf-8')] = second_oTime - mesuArr[code.decode('utf-8')]
                                        mesuArr[code.decode('utf-8')] = second_oTime                                 
                                    if(mesuDict[code.decode('utf-8')] == 2):
                                        mesuAver[code.decode('utf-8')] = mesuAver[code.decode('utf-8')] + second_oTime - mesuArr[code.decode('utf-8')]

                                else:
                                    mesuSTime[code.decode('utf-8')] = str_oTime
                                    mesuDict[code.decode('utf-8')] = mesuDict.get(code.decode('utf-8'), 0)
                                    mesuArr[code.decode('utf-8')] = second_oTime
                                    # if(code.decode('utf-8') == '001420'):
                                    #     print(i)
                                    #     time.sleep(3)

                                if(mesuDict[code.decode('utf-8')] in mesuLimit and ((code) not in comps) and (code not in medos) and (code not in nos)):
                                    nosDic[code.decode('utf-8')] = []

                                    if(exportData[i, 3].astype(float) < 4 or exportData[i, 3].astype(float) > 18.9):
                                        # nosDic[code.decode('utf-8')].append('1')
                                        nos.append(code)
                                        continue;

                                    if(xstime.tm_min < 2):
                                        nos.append(code)
                                        continue;

                                    cost = int(exportData[i, 8].decode('UTF-8'))
                                    # if(cost > 9000):
                                    #     # nosDic[code.decode('utf-8')].append('3')
                                    #     nos.append(code)
                                    #     continue;

                                    if(i < 4):
                                        s = 0
                                        continue;
                                    else:
                                        s = i-4

                                    maxr = 100000
                                    sry = (exportData[i-4:i+1,4].astype(float))/maxr
                                    ssrlist = [b - a for a,b in zip(sry,sry[1:])]
                                    ssrfit = sp.polyfit(x[:4], ssrlist, level)
                                    ssrgrad = sp.around(ssrfit[0]*10, decimals=2)

                                    mmlist = sp.array(exportData[s+1:i+1,6].astype(float))/(sp.array(srlist[s:i])*100000)
                                    mmfit = sp.polyfit(x[:len(exportData[s+1:i+1,5])], mmlist, level)
                                    mmgrad = sp.around(mmfit[0]*10, decimals=3)

                                    ammlist = sp.array(exportData[s+1:i+1,5].astype(float))/(sp.array(srlist[s:i])*100000)
                                    ammfit = sp.polyfit(x[:len(exportData[s+1:i+1,5])], ammlist, level)
                                    ammgrad = sp.around(ammfit[0]*10, decimals=3)                                    
                                    
                                    # if((mmgrad > 8.1 and ammgrad < 7.2)):
                                    #     nos.append(code)
                                    #     continue;

                                    # if((ammgrad < -9)):
                                    #     nos.append(code)
                                    #     continue;
                                    
                                    if(True in (exportData[0:i,3].astype(float) > 22.5)):
                                        # nosDic[code.decode('utf-8')].append('5')
                                        nos.append(code)
                                        continue;

                                    lfit = sp.polyfit(sp.array(range(3)), y[-3:], level)
                                    lg = sp.around(lfit[0]*10, decimals=2)
                                    # if((lg > 2 and True in (sp.bincount(exportData[0:i,4].astype(int)) > 3)) or lg > 13.8):
                                    #     # nosDic[code.decode('utf-8')].append('6')
                                    #     nos.append(code)
                                    #     continue;

                                    if(gradient < 1.1 and ssrgrad < -1):
                                        # nosDic[code.decode('utf-8')].append('7')
                                        nos.append(code)
                                        continue;

                                    fcgfit1 = sp.polyfit(sp.array(range(4)), exportData[i-3:i+1,9].astype(float), 1)
                                    fcggrad1 = sp.around(fcgfit1[0], decimals=2)
        
                                    fcggrad2 = fcggrad1
                                    if(i > 3):
                                        fcgfit2 = sp.polyfit(sp.array(range(5)), exportData[i-4:i+1,9].astype(float), 1)
                                        fcggrad2 = sp.around(fcgfit2[0], decimals=2)
         
                                    fcggrad = min([fcggrad1, fcggrad2])

                                    lcggrad = fcggrad
                                    
                                    if(i > 4):
                                        lcgfit = sp.polyfit(sp.array(range(6)), exportData[i-5:i+1,9].astype(float), 1)
                                        lcggrad = sp.around(lcgfit[0], decimals=2)

                                    if((chegang < 129 and lcggrad < -1.8) or lcggrad > 60):
                                        # nosDic[code.decode('utf-8')].append('8')
                                        nos.append(code)
                                        continue;

                                    tpg = 0
                                    msi = 0
                                    for ii in range(1,i):
                                        pi = ii * 3
                                        if(pi >= i):
                                            break

                                        pfit = sp.polyfit(x[:pi], y[-pi:], level)
                                        pgradient = sp.around(pfit[0]*10, decimals=2)
                                        if(tpg < pgradient and not sp.isinf(pgradient)):
                                            tpg = pgradient
                                            msi = pi

                                    tlen = len(cggradDic[code.decode('utf-8')])
                                    tfit = sp.polyfit(sp.array(range(tlen)), cggradDic[code.decode('utf-8')], 1)
                                    tgrad = sp.around(tfit[0], decimals=2)                                            

                                    if(tgrad < -6):
                                        # nosDic[code.decode('utf-8')].append('10')
                                        nos.append(code)
                                        continue;
                                    
                                    tmesu = ((exportData[i,4].astype(float) - exportData[i-1,4].astype(float)) * exportData[i,8].astype(float)) + ((exportData[i - 1,4].astype(float) - exportData[i - 2,4].astype(float)) * exportData[i-1,8].astype(float))
                                    if(tmesu > 250000000 and xstime.tm_min >= 6 and exportData[i, 3].astype(float) < 6.9):
                                        nos.append(code)
                                        continue;

                                    if(chegang > 250 and xstime.tm_min <= 3 and exportData[i,3].astype(float) < 5.7):
                                        nos.append(code)
                                        continue;          

                                    levelUpDic[code.decode('utf-8')] = []
                
                                    for x in range(0,xstime.tm_min + 1):
                                        r = re.compile('09:' + str(x).rjust(2, '0') + ':..')
                                        vmatch = sp.vectorize(lambda x:bool(r.match(x)))
                                        vmatch(exportData[:i+1,0].astype(str))
                                        tmarr = exportData[:i+1,3].astype(str)[vmatch(exportData[:i+1,0].astype(str))].astype(float)
                                        if(len(tmarr) == 0):
                                            continue;
        
                                        levelUpDic[code.decode('utf-8')].append((tmarr[-1] - tmarr[0]))
        
                                    if(True in (sp.array(levelUpDic[code.decode('utf-8')]) > 7.4)):
                                        print(ttime, code, 'nos121211212')
                                        nos.append(code)
                                        continue;

                                    if(len(exportData[:i+1,3].astype(float)) < 6):
                                        maxminamin = 0
                                    else:        
                                        maxminamin = max(exportData[i-5:i+1,3].astype(float)) - min(exportData[i-5:i+1,3].astype(float))
                                    if(maxminamin > 5):
                                        print(ttime, code, 'nos123321')
                                        nos.append(code)
                                        continue;

                                    # if(fcggrad < -15 and lg > 5):
                                    #     # nosDic[code.decode('utf-8')].append('9')
                                    #     nos.append(code)
                                    #     continue;

                                    if(fcggrad < -19.5 and xstime.tm_min < 10 and chegang > 195):
                                        # nosDic[code.decode('utf-8')].append('9')
                                        nos.append(code)
                                        continue;

                                    grRate1 = 0
                                    if(len(exportData[:i, 4]) > 7 and int(exportData[i-1, 4].decode('UTF-8')) - int(exportData[i-4, 4].decode('UTF-8')) != 0 and int(exportData[i-4, 4].decode('UTF-8')) - int(exportData[i-7, 4].decode('UTF-8')) != 0):
                                        grRate1 = (int(exportData[i-1, 4].decode('UTF-8')) - int(exportData[i-4, 4].decode('UTF-8'))) / (int(exportData[i-4, 4].decode('UTF-8')) - int(exportData[i-7, 4].decode('UTF-8'))) + (exportData[i-1, 4].astype(int) / 10000000)
        
                                    grRate2 = 0
                                    if(len(exportData[:i, 4]) > 8 and int(exportData[i-2, 4].decode('UTF-8')) - int(exportData[i-5, 4].decode('UTF-8')) != 0 and int(exportData[i-5, 4].decode('UTF-8')) - int(exportData[i-8, 4].decode('UTF-8')) != 0):
                                        grRate2 = (int(exportData[i-2, 4].decode('UTF-8')) - int(exportData[i-5, 4].decode('UTF-8'))) / (int(exportData[i-5, 4].decode('UTF-8')) - int(exportData[i-8, 4].decode('UTF-8'))) + (exportData[i-2, 4].astype(int) / 10000000)
        
                                    grRate3 = 0
                                    if(len(exportData[:i, 4]) > 9 and int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')) != 0 and int(exportData[i-6, 4].decode('UTF-8')) - int(exportData[i-9, 4].decode('UTF-8')) != 0):
                                        grRate3 = (int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8'))) / (int(exportData[i-6, 4].decode('UTF-8')) - int(exportData[i-9, 4].decode('UTF-8'))) + (exportData[i-3, 4].astype(int) / 10000000)
        
                                    grRate4 = 0
                                    if(len(exportData[:i, 4]) > 10 and int(exportData[i-4, 4].decode('UTF-8')) - int(exportData[i-7, 4].decode('UTF-8')) != 0 and int(exportData[i-7, 4].decode('UTF-8')) - int(exportData[i-10, 4].decode('UTF-8')) != 0):
                                        grRate4 = (int(exportData[i-4, 4].decode('UTF-8')) - int(exportData[i-7, 4].decode('UTF-8'))) / (int(exportData[i-7, 4].decode('UTF-8')) - int(exportData[i-10, 4].decode('UTF-8'))) + (exportData[i-4, 4].astype(int) / 10000000)
        
                                    grRate5 = 0
                                    if(len(exportData[:i, 4]) > 11 and int(exportData[i-5, 4].decode('UTF-8')) - int(exportData[i-8, 4].decode('UTF-8')) != 0 and int(exportData[i-8, 4].decode('UTF-8')) - int(exportData[i-11, 4].decode('UTF-8')) != 0):
                                        grRate5 = (int(exportData[i-5, 4].decode('UTF-8')) - int(exportData[i-8, 4].decode('UTF-8'))) / (int(exportData[i-8, 4].decode('UTF-8')) - int(exportData[i-11, 4].decode('UTF-8'))) + (exportData[i-5, 4].astype(int) / 10000000)

                                    if(grRate > 5.89 or grRate1 > 5.89 or grRate2 > 5.89 or grRate3 > 5.89 or grRate4 > 5.89 or grRate5 > 5.89):
                                        nos.append(code)
                                        continue;

                                    if(grRate > 1.8 or grRate1 > 1.8 or grRate2 > 1.8 or grRate3 > 1.8 or grRate4 > 1.8 or grRate5 > 1.8 or chegang > 400 or exportData[i, 3].astype(float) - exportData[i-1, 3].astype(float) > 2):
                                        delayMesu[code.decode('utf-8')] = i
                                        findRate[code.decode('utf-8')] = exportData[delayMesu[code.decode('utf-8')], 3].astype(float)
                                        continue;

                                    # if(exportData[i,5].astype(float)/exportData[i,6].astype(float) < 0.57 and mmgrad < 15 and ammgrad > 13.2):
                                    #     nos.append(code)
                                    #     continue;                                    

                                    mole = (exportData[i, 4].astype(int) - exportData[i-1, 4].astype(int))/exportData[i, 4].astype(int)
                                    # if(exportData[i, 4].astype(float) > 2000000 and mole < 0.03):
                                    #     nos.append(code)
                                    #     continue;                                        

                                    mole2 = (exportData[i, 4].astype(int) - exportData[i-2, 4].astype(int))/exportData[i, 4].astype(int)

                                    grilen = len(gradiDic[code.decode('utf-8')][-4:])
                                    grifit = sp.polyfit(sp.array(range(grilen)), gradiDic[code.decode('utf-8')][-4:], 1)
                                    grigrad = sp.around(grifit[0], decimals=2)                                               

                                    if(exportData[i, 3].astype(float) > 16.3):
                                        print(ttime, code, 'nos1717171717')
                                        nos.append(code)
                                        continue;

                                    if(mole2 < 0.007):
                                        print(ttime, code, 'nos00070007')
                                        nos.append(code)
                                        continue;

                                    cost = exportData[i, 8].astype(int)
                                    if(cost < 1980 or cost > 8800):
                                        # nosDic[code.decode('utf-8')].append('3')
                                        nos.append(code)
                                        continue;

                                    cheFee2 = (exportData[i, 4].astype(int) - exportData[i-1, 4].astype(int)) * exportData[i-2, 8].astype(int)
                                    cheFee3 = (exportData[i-1, 4].astype(int) - exportData[i-2, 4].astype(int)) * exportData[i-2, 8].astype(int)
                                    if(gr < 86000 and (cheFee2 > 200000 and cheFee2 < 4000000) or (cheFee3 > 200000 and cheFee3 < 4000000)):
                                        nos.append(code)
                                        continue;

                                    if(gr > 660000 and gr < 2200000 and mole2 < 0.09):
                                        bbamd[code.decode('utf-8')] = i

                                    if(mmgrad > 10.07 and ammgrad < 15):
                                        bbamd[code.decode('utf-8')] = i

                                    fcgfit7 = sp.polyfit(sp.array(range(2)), exportData[i-1:i+1,9].astype(float), 1)
                                    fcggrad7 = sp.around(fcgfit7[0], decimals=2)
                
                                    fcgfit8 = sp.polyfit(sp.array(range(3)), exportData[i-2:i+1,9].astype(float), 1)
                                    fcggrad8 = sp.around(fcgfit8[0], decimals=2)

                                    ones.append([code.decode('utf-8'), today, second_oTime, 2])
                                    comps.append((code))
                                    mesuStart[code.decode('utf-8')] = i
                                    msGradient[code.decode('utf-8')] = gradient
                                    msGr[code.decode('utf-8')] = gr
                                    msSmdms[code.decode('utf-8')] = (exportData[i, 4].astype(int) - exportData[i-1, 4].astype(int)) * exportData[i-1, 8].astype(int)
                                    msGrade[code.decode('utf-8')] = (exportData[i-1, 4].astype(int) - exportData[i-2, 4].astype(int)) * exportData[i-2, 8].astype(int)
                                    msSrgrad[code.decode('utf-8')] = float(exportData[i+7, 3].decode('UTF-8')) - float(exportData[i, 3].decode('UTF-8'))
                                    msRate[code.decode('utf-8')] = float(exportData[i, 3].decode('UTF-8'))
                                    rmsRate[code.decode('utf-8')] = float(exportData[i+1, 3].decode('UTF-8'))
                                    pick[code.decode('utf-8')] = False
                                    mesuIndex[code.decode('utf-8')] = exportData[i,9].astype(float) - exportData[i-1,9].astype(float)
                                    isd[code.decode('utf-8')] = False
                                    isd2[code.decode('utf-8')] = False
                                    endIndex[code.decode('utf-8')] = 0
                                    originM = originM + 1
                                    setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) +  ',' + str(float(exportData[i, 3].decode('UTF-8'))) +  '\n')

            except Exception as e:
                ss
                errFilePath = os.path.join("C:\\", "Dropbox\\com_2\\diff\\" + "err.txt");
                errFile = open(errFilePath, 'a')
                errFile.write(today + '\t' + str(e) + '\n')
                continue

        print(today)

for code, today, time, no in ones:
    matchs = [x for x in ones if (x[0] == code and x[1] == today)]
    if(len(matchs) > 1):
        if(matchs[0][2] > matchs[1][2]):
            ones.remove(matchs[0])
        else:
            ones.remove(matchs[1])

analFilePath = os.path.join("C:\\", "Dropbox\\com_2\\Data\\" + "anal.txt");
analFile = open(analFilePath, 'w')

edFilePath = os.path.join("C:\\", "Dropbox\\com_2\\Data\\" + "ed2.txt");
edFile = open(edFilePath, 'w')

edFile.write('day' +  ',' + 'originM' +  ',' + 'sumEd' +  ',' + 'code' +  ',' + 'max' ',' + 'termMin' +  ',' + 'termMax' +  ',' + 'md' +  ',' + 'ms' +  ',' + 'ed' +  ',' + 'msTime' +  ',' + 'mdTime' + '\n')

for dirname, dirnames, filenames in os.walk("C:\\Dropbox\\com_2\\Data\\"):
    for subdirname in dirnames:
        today = subdirname

        setFilePath = os.path.join("C:\\", "Dropbox\\com_2\\Data\\" + today + "\\" + today + "moa3.txt");
        setFile = open(setFilePath, 'r')
        
        for line in setFile:
            analFile.write(today + ',' + line)

        set2FilePath = os.path.join("C:\\", "Dropbox\\com_2\\Data\\" + today + "\\" + today + "ed2.txt");
        set2File = open(set2FilePath, 'r')
        
        for line in set2File:
            edFile.write(today + ',' + str(int(originM)) + ',' + str(sumEd) + ',' + line)


analFilePath = os.path.join("C:\\", "Dropbox\\com_2\\diff\\" + "anal.txt");
analFile = open(analFilePath, 'w')

for dirname, dirnames, filenames in os.walk("C:\\Dropbox\\com_2\\diff\\"):
    for subdirname in dirnames:
        today = subdirname

        setFilePath = os.path.join("C:\\", "Dropbox\\com_2\\diff\\" + today + "\\" + today + "moa3.txt");
        setFile = open(setFilePath, 'r')
        
        for line in setFile:
            analFile.write(today + ',' + line)

        set2FilePath = os.path.join("C:\\", "Dropbox\\com_2\\diff\\" + today + "\\" + today + "ed2.txt");
        set2File = open(set2FilePath, 'r')
        
        for line in set2File:
            edFile.write(today + ',' + str(int(originM)) + ',' + str(sumEd) + ',' + line)

print("end")            

now = datetime.datetime.now()
print(str(datetime.datetime.now()))