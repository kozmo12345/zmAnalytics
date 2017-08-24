#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time
import re
import math

sp.random.seed(3)

now = datetime.datetime.now()
print(str(datetime.datetime.now()))

startTime = datetime.timedelta(hours=9,minutes=00,seconds=00).total_seconds()
endTime = datetime.timedelta(hours=9,minutes=12,seconds=30).total_seconds()
fMedoTime = datetime.timedelta(hours=9,minutes=19,seconds=50).total_seconds()
allMedoTime = datetime.timedelta(hours=9,minutes=24,seconds=20).total_seconds()
wanna = 1
mesuLimit = [2]
rateLimit = 0.31
rateMLimit = 3.1
stdLimit = 2
sumEd = 0
gradient = 0
today = now.strftime('%Y-%m-%d')
today = '2017-03-22'

print(today)
setFile = open(os.path.join("C:\\", "Dropbox\\com_1\\" + today + "\\" + today + "moa3.txt"), 'w')
edFile = open(os.path.join("C:\\", "Dropbox\\com_1\\" + today + "\\" + today + "ed.txt"), 'w')
realfilePath = os.path.join("C:\\", "Dropbox\\com_1\\" + today + "\\" + today + ".txt");

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
endIndex = dict()
bbamd =  dict()
levelUpDic = dict()
delayMesu = dict()
findRate = dict()

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
        if(bool_oTime == True):
            nzData = data[data[:,2] != b'']
            ttimeData = nzData[nzData[:,0] == ttime]
            ttimeData2 = ttimeData[ttimeData[:,1].astype(int) < 99]
            ttimeData3 = ttimeData2[ttimeData2[:,4].astype(int) > 97000]
            ttimeData4 = ttimeData3[ttimeData3[:,3].astype(float) < 30]
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

                if(i < 2): continue;

                c = exportData[:i+1, 3].astype(float)

                # if(code.decode('utf-8') == '064820'): #testst
                #     thGr = int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8'))                  
                #     nowGr = int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8'))
                #     if(thGr != 0 and nowGr != 0):
                #         print(ttime, code , c[-1],nowGr / thGr, exportData[i,8].astype(int), exportData[i,9].astype(float))

                #     else:
                #         print(ttime, code, 'stopted')

                if(code in comps):
                    if(i < mesuStart[code.decode('utf-8')] + 3):
                        continue;

                    mdpCost = (exportData[i,4].astype(float) - exportData[i-1,4].astype(float)) * exportData[i-1,8].astype(float)

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
                    mdpCost = (exportData[i,4].astype(float) - exportData[i-1,4].astype(float)) * exportData[i-1,8].astype(float)

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
                    chegang = exportData[i,9].astype(float)

                    thGr = int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8'))                  
                    nowGr = int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8'))
                    grRate = 0
                    if(len(exportData[:i, 4]) > 6 and int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8')) != 0 and int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')) != 0):
                        grRate = (int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8'))) / (int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')))

                    if(exportData[i, 9].astype('float') < 103 or (ed > 2.8 and int(exportData[i, 4].decode('UTF-8')) < 800000) or (grRate > 1.78 and int(exportData[i, 4].decode('UTF-8')) < 800000) or (grRate > 3 and chegang < 160)):
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

                    if(chegang < 120):
                        gcggrad = -10

                    endcggrad = 0
                    if(endIndex[code.decode('utf-8')] != 0):
                        end_arr = exportData[endIndex[code.decode('utf-8')]:i+1,9].astype(float)
                        endcgfit = sp.polyfit(sp.array(range(len(end_arr))), end_arr, 1)
                        endcggrad = sp.around(endcgfit[0], decimals=2)

                    s3 = (exportData[i-4,4].astype(float) - exportData[i-5,4].astype(float)) * exportData[i-4,8].astype(float)
                    s2 = (exportData[i-3,4].astype(float) - exportData[i-4,4].astype(float)) * exportData[i-3,8].astype(float)
                    s1 = (exportData[i-2,4].astype(float) - exportData[i-3,4].astype(float)) * exportData[i-2,8].astype(float)
                    s0 = (exportData[i-1,4].astype(float) - exportData[i-2,4].astype(float)) * exportData[i-1,8].astype(float)
                    
                    s4 = ( s0 + s1 + s2 + s3 )/4
                    ssss = (exportData[i,4].astype(float) - exportData[i-1,4].astype(float)) * exportData[i,8].astype(float)
                    srate = round(ssss/s4, 2)
 
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


                    cheArr = sp.split(exportData[mesuStart[code.decode('utf-8')]:i+1,9].astype(float), [6, 12, 18, 24, 30, 36, 42])
                    cheList = [sp.mean(x) for x in cheArr if (True)]
                    cheCList = [b - a for a,b in zip(cheList,cheList[1:])]
                    cheFor = sp.array([value for value in cheCList if not math.isnan(value)][-4:])

                    raArr = sp.split(exportData[mesuStart[code.decode('utf-8')]:i+1,3].astype(float), [6, 12, 18, 24, 30, 36, 42])
                    raList = [sp.mean(x) for x in raArr if (True)]
                    raCList = [b - a for a,b in zip(raList,raList[1:])]
                    raFor = sp.array([value for value in raCList if not math.isnan(value)][-4:])                    
                    # msSrgrad[code.decode('utf-8')] = cheCList

                    # if(code.decode('utf-8') == '064820'): #testst
                    #     print(ttime,code,raCList)
                    # print(sp.array([value for value in cheCList if not math.isnan(value)][-4:]))
                    # print(sp.array([value for value in cheCList if not math.isnan(value)][-4:]) > 0)
                    # print(len(sp.array([value for value in cheCList if not math.isnan(value)][-4:])))

                    if(code not in comps):
                        continue;

                    if(mesuStart[code.decode('utf-8')] + 53 < i and chegang < 200):
                        print(ttime, code, 1111111111)
                        edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                        comps.remove(code)
                        medos.append(code)
                        sumEd = sumEd + red
                        del endIndex[code.decode('utf-8')]

                    elif((i - mesuStart[code.decode('utf-8')]) % 6 == 0 and ed > 1.95):
                        print(ttime, code, 1111111111)
                        edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                        comps.remove(code)
                        medos.append(code)
                        sumEd = sumEd + red
                        del endIndex[code.decode('utf-8')]

                    # elif(not sp.any(cheFor > 0) and (len(cheFor) > 3) and not sp.any(raFor > 0.5) and (len(raFor) > 3)):
                    #     print(ttime, code, 2222222222)
                    #     edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                    #     comps.remove(code)
                    #     medos.append(code)
                    #     sumEd = sumEd + red
                    #     del endIndex[code.decode('utf-8')]

                    elif(code.decode('utf-8') in bbamd and ed > 0.7 and chegang < 200 and mesuStart[code.decode('utf-8')] + 3 < i):
                        print(ttime, code, 2222222222)
                        edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                        comps.remove(code)
                        medos.append(code)
                        sumEd = sumEd + red
                        del endIndex[code.decode('utf-8')]

                    elif(mesuStart[code.decode('utf-8')] + 62 < i):
                        print(ttime, code, 33333333333)
                        edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                        comps.remove(code)
                        medos.append(code)
                        sumEd = sumEd + red
                        del endIndex[code.decode('utf-8')]

                    elif(mdpCost > 280000000 and exportData[i,9].astype(float) - exportData[i-1,9].astype(float) < -20 and exportData[i-1,4].astype(float) - exportData[i-2,4].astype(float) != 0):
                        print(ttime, code, 33333333333)
                        edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                        comps.remove(code)
                        medos.append(code)
                        sumEd = sumEd + red
                        del endIndex[code.decode('utf-8')]

                    elif((exportData[i,4].astype(float) - exportData[i-1,4].astype(float))/exportData[i,4].astype(float) > 0.05 and exportData[i,9].astype(float) - exportData[i-1,9].astype(float) < -60 and exportData[i-1,4].astype(float) - exportData[i-2,4].astype(float) != 0):
                        print(ttime, code, 33333333333)
                        edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                        comps.remove(code)
                        medos.append(code)
                        sumEd = sumEd + red
                        del endIndex[code.decode('utf-8')]                        

                    # elif((exportData[i,9].astype(float) - exportData[i-2,9].astype(float) < -10) and ((exportData[i,4].astype(float) - exportData[i-2,4].astype(float)) * exportData[i,8].astype(float) > 300000000)):
                    #     print(ttime, code, 4444444444444)
                    #     edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                    #     comps.remove(code)
                    #     medos.append(code)
                    #     sumEd = sumEd + red
                    #     del endIndex[code.decode('utf-8')]

                    elif( len(exportData[:,4].astype(float)) - 4 < i):
                        print(ttime, code, 5555555555555)
                        edFile.write( str(code.decode('utf-8')) + ',' + str(allMax) +  ',' + str(termMin) + ',' + str(termMax) + ',' + str(md) + ',' + str(ms) + ',' + str(red) + ',' + str(msTime) + ',' + str(mdTime) + ',' + str(msCost) + ',' + str(mdCost) + ',' + str(msGradient[code.decode('utf-8')]) + ',' + str(msGr[code.decode('utf-8')]) + ',' + str(msSmdms[code.decode('utf-8')]) + ',' + str(msGrade[code.decode('utf-8')]) + ',' + str(msSrgrad[code.decode('utf-8')]) +'\n')
                        comps.remove(code)
                        medos.append(code)
                        sumEd = sumEd + red
                        del endIndex[code.decode('utf-8')]

                

                if(second_oTime > endTime and code.decode('utf-8') in endIndex and endIndex[code.decode('utf-8')] != 0):
                    endIndex[code.decode('utf-8')] = i;

                if((second_oTime > endTime) or allmedo):
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

                if(chegang < 80 and exportData[i, 1].astype(int) < 4 and code not in nos):
                    print(ttime,code,'nos804804804')
                    nos.append(code)
                    continue;

                if(code.decode('utf-8') in delayMesu and delayMesu[code.decode('utf-8')] + 1 < i and delayMesu[code.decode('utf-8')] + 6 > i and grRate < 0.89 and (int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-1, 4].decode('UTF-8'))) > 1000 and (int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8'))) > 1000 and code not in comps and gr1 and chegang < 400):

                    fcgfit1 = sp.polyfit(sp.array(range(4)), exportData[i-3:i+1,9].astype(float), 1)
                    fcggrad1 = sp.around(fcgfit1[0], decimals=2)
        
                    fcgfit2 = sp.polyfit(sp.array(range(5)), exportData[i-4:i+1,9].astype(float), 1)
                    fcggrad2 = sp.around(fcgfit2[0], decimals=2)
         
                    fcgfit3 = sp.polyfit(sp.array(range(6)), exportData[i-5:i+1,9].astype(float), 1)
                    fcggrad3 = sp.around(fcgfit3[0], decimals=2)

                    fcggrad = min([fcggrad1, fcggrad2, fcggrad3])

                    maxminamin = max(exportData[i-5:i+1,3].astype(float)) - min(exportData[i-5:i+1,3].astype(float))
                    if(maxminamin > 5):
                        del delayMesu[code.decode('utf-8')]
                        continue;

                    if(findRate[code.decode('utf-8')] + 3 < exportData[i, 3].astype(float)):
                        del delayMesu[code.decode('utf-8')]
                        continue;

                    if(findRate[code.decode('utf-8')] + 1.5 < exportData[i, 3].astype(float)):
                        delayMesu[code.decode('utf-8')] = delayMesu[code.decode('utf-8')] + 1
                        continue;

                    if(fcggrad < -18 and xstime.tm_min < 8 and chegang > 160):
                        del delayMesu[code.decode('utf-8')]
                        continue;

                    if(exportData[i, 3].astype(float) < 4.6 and chegang < 140):
                        del delayMesu[code.decode('utf-8')]
                        continue;

                    mole = (exportData[i, 4].astype(int) - exportData[i-1, 4].astype(int))/exportData[i, 4].astype(int)
                    mole2 = (exportData[i, 4].astype(int) - exportData[i-2, 4].astype(int))/exportData[i, 4].astype(int)

                    cost = exportData[i, 8].astype(int)
                    if(cost < 1980 or cost > 8800):
                        print(ttime, code, 'nos00070007')
                        del delayMesu[code.decode('utf-8')]
                        del findRate[code.decode('utf-8')]
                        continue;

                    if(mole2 < 0.007):
                        print(ttime, code, 'nos00070007')
                        del delayMesu[code.decode('utf-8')]
                        del findRate[code.decode('utf-8')]
                        continue;

                    if(exportData[i, 3].astype(float) > 16.3):
                        print(ttime, code, 'nos163163')
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

                    comps.append((code))
                    mesuStart[code.decode('utf-8')] = i
                    msGradient[code.decode('utf-8')] = 0
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
                    endIndex[code.decode('utf-8')] = 0
                    del delayMesu[code.decode('utf-8')]
                    setFile.write(str(ttime) + ',' + str(code.decode('utf-8')) + ',' + str(float(rate)) +  ',' + str(float(exportData[i, 3].decode('UTF-8'))) + '\n')
                    continue

                if(((ms_md > 0.96 and sms_md > 1 and gr > 340000 and not (cggrad < -4 and chegang < 160)) or (cggrad > 2.3 and chegang > 163)) and grade < 16 and exportData[i, 3].astype(float) > 5 and gr1):
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

                    if(gradient >= 0.65 + (0.02 * wlevel) and srgrad > 0 and ltdc != 0):
                        if(code.decode('utf-8') in mesuDict):
                            mesuDict[code.decode('utf-8')] = mesuDict[code.decode('utf-8')] + 1
                        else:

                            mesuSTime[code.decode('utf-8')] = str_oTime
                            mesuDict[code.decode('utf-8')] = mesuDict.get(code.decode('utf-8'), 0)

                        if(mesuDict[code.decode('utf-8')] in mesuLimit and ((code) not in comps) and (code not in nos) and (code not in medos)):
                            if(exportData[i, 3].astype(float) < 4 or exportData[i, 3].astype(float) > 19.6):
                                print(ttime, code, 'nostttttt')
                                continue;

                            if(xstime.tm_min < 2):
                                print(ttime, code, 'nos00000')
                                nos.append(code)
                                continue;

                            cost = int(exportData[i, 8].decode('UTF-8'))
                            if(cost > 9000):
                                print(ttime, code, 'nos909090')
                                nos.append(code)
                                continue;

                            if(i < 4):
                                s = 0
                                continue;
                            else:
                                s = i-4
                            
                            mmlist = sp.array(exportData[s:i,6].astype(float))/(sp.array(srlist[s:i])*100000)
                            mmfit = sp.polyfit(x[:len(exportData[s:i,5])], mmlist, level)
                            mmgrad = sp.around(mmfit[0]*10, decimals=3)

                            ammlist = sp.array(exportData[s:i,5].astype(float))/(sp.array(srlist[s:i])*100000)
                            ammfit = sp.polyfit(x[:len(exportData[s:i,5])], ammlist, level)
                            ammgrad = sp.around(ammfit[0]*10, decimals=3)                                    

                            if((mmgrad > 8.1 and ammgrad < 7.2)):
                                print(ttime, code, 'nos111111')
                                nos.append(code)
                                continue;

                            if(True in (exportData[0:i,3].astype(float) > 22.5)):
                                print(ttime, code, 'nos2222222')
                                nos.append(code)
                                continue;

                            lfit = sp.polyfit(sp.array(range(3)), y[-3:], level)
                            lg = sp.around(lfit[0]*10, decimals=2)

                            # if((lg > 2 and True in (sp.bincount(exportData[0:i,4].astype(int)) > 3)) or lg > 13.8):
                            #     print(ttime, code, 'nos333333')
                            #     nos.append(code)
                            #     continue;                       
                            
                            tpg = 0
                            for ii in range(1,i):
                                pi = ii * 3
                                if(pi >= i):
                                    break

                                pfit = sp.polyfit(x[:pi], y[-pi:], level)
                                pgradient = sp.around(pfit[0]*10, decimals=2)
                                if(tpg < pgradient and not sp.isinf(pgradient)):
                                    tpg = pgradient
                            tpg = tpg * sp.sqrt(ii * 0.77)

                            maxr = 100000
                            sry = (exportData[i-4:i+1,4].astype(float))/maxr
                            ssrlist = [b - a for a,b in zip(sry,sry[1:])]
                            ssrfit = sp.polyfit(x[:4], ssrlist, level)
                            ssrgrad = sp.around(ssrfit[0]*10, decimals=2)

                            if(gradient < 1.1 and ssrgrad < -1):
                                print(ttime, code, 'nos555555')
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

                            if(chegang < 129 and lcggrad < -1.8 or lcggrad > 60):
                                print(ttime, code, 'nos66666')
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
                                print(ttime, code, 'nos88888')
                                nos.append(code)
                                continue;

                            tmesu = ((exportData[i,4].astype(float) - exportData[i-1,4].astype(float)) * exportData[i,8].astype(float)) + ((exportData[i - 1,4].astype(float) - exportData[i - 2,4].astype(float)) * exportData[i-1,8].astype(float))

                            if(tmesu > 250000000 and xstime.tm_min >= 6 and exportData[i, 3].astype(float) < 6.9):
                                print(ttime, code, 'nos99999')
                                nos.append(code)
                                continue;                                 

                            if(chegang > 250 and xstime.tm_min <= 3 and exportData[i,3].astype(float) < 5.7):
                                print(ttime, code, 'nos10101010')
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
                            
                            maxminamin = max(exportData[i-5:i+1,3].astype(float)) - min(exportData[i-5:i+1,3].astype(float))
                            if(maxminamin > 5):
                                print(ttime, code, 'nos121211212')
                                nos.append(code)
                                continue;

                            if(fcggrad < -19.5 and xstime.tm_min < 10 and chegang > 195):
                                # nosDic[code.decode('utf-8')].append('9')
                                print(ttime, code, 'nos19191919')
                                nos.append(code)
                                continue;                                

                            grRate1 = 0
                            if(len(exportData[:i, 4]) > 7 and int(exportData[i-1, 4].decode('UTF-8')) - int(exportData[i-4, 4].decode('UTF-8')) != 0 and int(exportData[i-4, 4].decode('UTF-8')) - int(exportData[i-7, 4].decode('UTF-8')) != 0):
                                grRate1 = (int(exportData[i-1, 4].decode('UTF-8')) - int(exportData[i-4, 4].decode('UTF-8'))) / (int(exportData[i-4, 4].decode('UTF-8')) - int(exportData[i-7, 4].decode('UTF-8')))                                        

                            grRate2 = 0
                            if(len(exportData[:i, 4]) > 8 and int(exportData[i-2, 4].decode('UTF-8')) - int(exportData[i-5, 4].decode('UTF-8')) != 0 and int(exportData[i-5, 4].decode('UTF-8')) - int(exportData[i-8, 4].decode('UTF-8')) != 0):
                                grRate2 = (int(exportData[i-2, 4].decode('UTF-8')) - int(exportData[i-5, 4].decode('UTF-8'))) / (int(exportData[i-5, 4].decode('UTF-8')) - int(exportData[i-8, 4].decode('UTF-8')))                                        

                            grRate3 = 0
                            if(len(exportData[:i, 4]) > 9 and int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')) != 0 and int(exportData[i-6, 4].decode('UTF-8')) - int(exportData[i-9, 4].decode('UTF-8')) != 0):
                                grRate3 = (int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8'))) / (int(exportData[i-6, 4].decode('UTF-8')) - int(exportData[i-9, 4].decode('UTF-8')))                                        

                            grRate4 = 0
                            if(len(exportData[:i, 4]) > 10 and int(exportData[i-4, 4].decode('UTF-8')) - int(exportData[i-7, 4].decode('UTF-8')) != 0 and int(exportData[i-7, 4].decode('UTF-8')) - int(exportData[i-10, 4].decode('UTF-8')) != 0):
                                grRate4 = (int(exportData[i-4, 4].decode('UTF-8')) - int(exportData[i-7, 4].decode('UTF-8'))) / (int(exportData[i-7, 4].decode('UTF-8')) - int(exportData[i-10, 4].decode('UTF-8')))                                        

                            grRate5 = 0
                            if(len(exportData[:i, 4]) > 11 and int(exportData[i-5, 4].decode('UTF-8')) - int(exportData[i-8, 4].decode('UTF-8')) != 0 and int(exportData[i-8, 4].decode('UTF-8')) - int(exportData[i-11, 4].decode('UTF-8')) != 0):
                                grRate5 = (int(exportData[i-5, 4].decode('UTF-8')) - int(exportData[i-8, 4].decode('UTF-8'))) / (int(exportData[i-8, 4].decode('UTF-8')) - int(exportData[i-11, 4].decode('UTF-8')))                                        

                            if(code in nos):
                                continue;

                            if(grRate > 5.89 or grRate1 > 5.89 or grRate2 > 5.89 or grRate3 > 5.89 or grRate4 > 5.89 or grRate5 > 5.89):
                                print(ttime, code, 'nos5858585858')
                                nos.append(code)
                                continue;

                            if(grRate > 1.8 or grRate1 > 1.8 or grRate2 > 1.8 or grRate3 > 1.8 or grRate4 > 1.8 or grRate5 > 1.8 or chegang > 400 or exportData[i, 3].astype(float) - exportData[i-1, 3].astype(float) > 2):
                                delayMesu[code.decode('utf-8')] = i
                                findRate[code.decode('utf-8')] = exportData[delayMesu[code.decode('utf-8')], 3].astype(float)
                                continue;

                            mole2 = (exportData[i, 4].astype(int) - exportData[i-2, 4].astype(int))/exportData[i, 4].astype(int)

                            if(mole2 < 0.007):
                                print(ttime, code, 'nos00070007')
                                nos.append(code)
                                continue;

                            cost = exportData[i, 8].astype(int)
                            if(cost < 1980 or cost > 8800):
                                # nosDic[code.decode('utf-8')].append('3')
                                nos.append(code)
                                continue;

                            if(exportData[i, 3].astype(float) > 16.3):
                                print(ttime, code, 'nos1717171717')
                                nos.append(code)
                                continue;

                            if(gr > 660000 and gr < 2200000 and mole2 < 0.09):
                                bbamd[code.decode('utf-8')] = i

                            if(mmgrad > 10.07 and ammgrad < 15):
                                bbamd[code.decode('utf-8')] = i

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
                            endIndex[code.decode('utf-8')] = 0
                            setFile.write(str(ttime) + ',' + str(code.decode('utf-8')) + ',' + str(float(rate)) +  ',' + str(float(exportData[i, 3].decode('UTF-8'))) + '\n')

    except Exception as e:
        ss
        print("---------------------------------------" + str(e))
        continue

print(today)