#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time
import re

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

def createFiles(realfilePath, setFilePath, mdFilePath, pFilePath):
    try:
        realfile = open(realfilePath, 'a')
        realfile.close()
        
        setFile = open(setFilePath, 'w')
        setFile.close()
        
        mdFile = open(mdFilePath, 'w')
        mdFile.close()

        pFile = open(pFilePath, 'w')
        pFile.close()
    except Exception as e:
        createFiles(realfilePath, setFilePath, mdFilePath, pFilePath)
    else:
        pass

now = datetime.datetime.now()
today = now.strftime('%Y-%m-%d')

startTime = datetime.timedelta(hours=9,minutes=00,seconds=00).total_seconds()
endTime = datetime.timedelta(hours=9,minutes=12,seconds=30).total_seconds()
fMedoTime = datetime.timedelta(hours=9,minutes=19,seconds=50).total_seconds()
allMedoTime = datetime.timedelta(hours=9,minutes=33,seconds=30).total_seconds()

comps = []
medos = []
nos = []
mesuLimit = [2]
wanna = 1
rateLimit = 0.31
rateMLimit = 3.8
gradient = 0
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
dirn3 = os.path.dirname(mdFilePath)
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

pFilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "p.txt");
dirn4 = os.path.dirname(pFilePath)
try:
    os.stat(dirn4)
except:
    try:
        os.makedirs(dirn4)
    except OSError as exc: 
        if exc.errno == errno.EEXIST and os.path.isdir(dirn4):
            pass
        else:
            raise

mesuStart = dict()
msRate = dict()
isd = dict()
isd2 = dict()
levelUpDic = dict()
pick = dict()
pickI = dict()
delayMesu = dict()
endIndex = dict()
isRe = False

with open(setFilePath, 'r') as f:
    for line in f:
        imCode = line.split(",")[0].strip()
        if(imCode != ''):
            isRe = True
        if(imCode != '' and int(line.split(",")[8].strip()) == 1):
            comps.append(str.encode(imCode))
            mesuStart[imCode] = float(line.split(",")[7].strip())
            msRate[imCode] = float(line.split(",")[1].strip())
            isd[imCode] = False
            isd2[imCode] = False
            pick[imCode] = False
            endIndex[imCode] = 0
        elif(imCode != '' and int(line.split(",")[8].strip()) == 2):
            nos.append(str.encode(imCode))
        else:
            continue;

if(not isRe):
    createFiles(realfilePath, setFilePath, mdFilePath, pFilePath)

while(True):
    data = sp.genfromtxt(realfilePath, delimiter="\t", dtype='|S20')
    
    try:
        times = sp.unique(data[data[:,0] != b''][:,0])
    except Exception as e:
        print('not yet')
        time.sleep( 30 )
        continue
    
    try:
        tmp_time = 0
        mesuDict = dict()
        cggradDic = dict()
        allmedo = False
        prev_oTime = 0
        now = datetime.datetime.now()
        nowTime = 0

        wchkfilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + "w1.pchk");
        if not os.path.exists(wchkfilePath):
            wchkfile = open(wchkfilePath, 'a')
            wchkfile.close()
    
        if(nowTime > endTime and len(comps) == 0):
            time.sleep( 4 )
            continue;
    
        if(nowTime > allMedoTime):
            continue;

        print(today + str(times[len(times)-1]))
        print(comps)
        print(mesuDict)
        print(nos)
        for ttime in (times):

            xstime = time.strptime(ttime.decode('utf-8'), '%H:%M:%S')
            second_oTime = datetime.timedelta(hours=xstime.tm_hour,minutes=xstime.tm_min,seconds=xstime.tm_sec).total_seconds() #계산시간
            str_oTime = ttime.decode('utf-8')

            if(second_oTime > endTime and second_oTime < nowTime - 120 ):
                continue;            
            
            if(second_oTime < startTime):
                continue;
            
            if(second_oTime > endTime and len(comps) == 0):
                break;

            if(second_oTime - prev_oTime > 60 and prev_oTime != 0):
                allmedo = True
            prev_oTime = datetime.timedelta(hours=xstime.tm_hour,minutes=xstime.tm_min,seconds=xstime.tm_sec).total_seconds() #계산시간

            tmp_time = second_oTime

            nzData = data[data[:,2] != b'']            
            ttimeData = nzData[nzData[:,0] == ttime]            
            ttimeData2 = ttimeData[ttimeData[:,1].astype(int) < 31]
            ttimeData3 = ttimeData2[ttimeData2[:,4].astype(int) > 100000]
            ttimeData4 = ttimeData3[ttimeData3[:,3].astype(float) < 25]
            ttimeData5 = ttimeData4[ttimeData4[:,8].astype(float) > 2200]
            codes = ttimeData5[:,7]

            if(second_oTime > endTime and len(comps) > 0):
                codes = comps;

            for ccode in comps:
                if(ccode not in codes):
                    codes = sp.append(codes, ccode)

            for code in (codes):
                if(code == b''):
                    continue;
                exportData = data[data[:,7] == code]
                exportData = exportData[exportData[:,9].astype(float) != 0]

                if(len(exportData[:,0])==0):
                    continue;

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

                if(code in comps and code not in medos and code.decode('utf-8') in mesuStart and second_oTime > mesuStart[code.decode('utf-8')] + 10):
                    ms = float(msRate[code.decode('utf-8')])
                    md = float(exportData[i, 3].decode('UTF-8'))
                    ed = round(md - ms, 2)
                    mdpCost = (exportData[i,4].astype(float) - exportData[i-2,4].astype(float)) * exportData[i-1,8].astype(float)

                    med = ed
                    tempWan = wanna
                    if((ms - md) > 1 or ed > 1):
                        isd[code.decode('utf-8')] = True
                    if(isd[code.decode('utf-8')]):
                        tempWan = 0.4
                    if((ms - md) > 2):
                        isd2[code.decode('utf-8')] = True
                    if(isd2[code.decode('utf-8')]):
                        med = ed * 1.8

                    if(nowTime - 20 < second_oTime):
                        mmRate = (sp.sum(exportData[i-2:i+1,5].astype(float)))/(sp.sum(exportData[i-2:i+1,6].astype(float))) - (med/22)

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

                        endcggrad = 0
                        if(endIndex[code.decode('utf-8')] != 0):
                            end_arr = exportData[endIndex[code.decode('utf-8')]:i+1,9].astype(float)
                            endcgfit = sp.polyfit(sp.array(range(len(end_arr))), end_arr, 1)
                            endcggrad = sp.around(endcgfit[0], decimals=2)

                        print(code.decode('utf-8') + '    ' + str(mmRate) + '    ' + str(str_oTime))

                        grRate = 0
                        if(len(exportData[:i, 4]) > 6 and int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8')) != 0 and int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')) != 0):
                            grRate = (int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8'))) / (int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')))

                        if((ed > 2.8 and int(exportData[i, 4].decode('UTF-8')) < 800000 and not pick[code.decode('utf-8')]) or (grRate > 1.78 and int(exportData[i, 4].decode('UTF-8')) < 800000 and not pick[code.decode('utf-8')]) or (grRate > 3 and chegang < 160)):
                            pick[code.decode('utf-8')] = True

                        nf = 0
                        fl = 0
                        nfaver = 0
                        flaver = 0
                        gap = 0
                        levelUpDic[code.decode('utf-8')] = []
                        levelUpDic[code.decode('utf-8')].append(0)
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
                                        if((flaver - nfaver) > 4.26 and (ed > 0.4 or second_oTime > mesuStart[code.decode('utf-8')] + 120) and not pick[code.decode('utf-8')]):
                                            pick[code.decode('utf-8')] = True
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

                        if(code.decode('utf-8') in pick and pick[code.decode('utf-8')] and (chegang < 200 or mdpCost < 10000000) and code.decode('utf-8') not in pickI):
                            pFile = open(pFilePath, 'a')
                            pFile.write( str(code.decode('utf-8')) + ',' + str_oTime + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(float(md)) + '\n')
                            pFile.close()
                            pickI[code.decode('utf-8')] = second_oTime

                        if(fMedoTime < second_oTime and ed > -0.1 and ed < 2.5 and code.decode('utf-8') not in pickI):
                            pFile = open(pFilePath, 'a')
                            pFile.write( str(code.decode('utf-8')) + ',' + str_oTime + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(float(md)) + '\n')
                            pFile.close()
                            pickI[code.decode('utf-8')] = second_oTime

                        if(code not in comps):
                            continue;

                        if((mmRate < rateLimit or mmRate > rateMLimit) and gcggrad < -1.7 and ed >= tempWan):
                            mdFile = open(mdFilePath, 'a')
                            mdFile.write(str(code.decode('utf-8')) + ',' + str(float(exportData[i, 3].decode('UTF-8'))) + ',' + str(exportData[i, 0].decode('UTF-8')) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(exportData[i, 8].decode('UTF-8')) + '\n')
                            mdFile.close()
                            medos.append(code)
                            comps.remove(code)
                            del endIndex[code.decode('utf-8')]
                        elif(pick[code.decode('utf-8')] and ed > 0.4 and (chegang < 200 or mdpCost < 10000000)):
                            mdFile = open(mdFilePath, 'a')
                            mdFile.write(str(code.decode('utf-8')) + ',' + str(float(exportData[i, 3].decode('UTF-8'))) + ',' + str(exportData[i, 0].decode('UTF-8')) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(exportData[i, 8].decode('UTF-8')) + '\n')
                            mdFile.close()
                            medos.append(code)
                            comps.remove(code)
                            del endIndex[code.decode('utf-8')]
                        elif(mesuStart[code.decode('utf-8')] + 600 < second_oTime and ed > 0.4 and ed < 2.5):
                            mdFile = open(mdFilePath, 'a')
                            mdFile.write(str(code.decode('utf-8')) + ',' + str(float(exportData[i, 3].decode('UTF-8'))) + ',' + str(exportData[i, 0].decode('UTF-8')) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(exportData[i, 8].decode('UTF-8')) + '\n')
                            mdFile.close()
                            medos.append(code)
                            comps.remove(code)
                            del endIndex[code.decode('utf-8')]
                        elif(mesuStart[code.decode('utf-8')] + 360 < second_oTime and ed > -0.1 and ed < 1 and max(exportData[:i,9].astype(float)) < 275):
                            mdFile = open(mdFilePath, 'a')
                            mdFile.write(str(code.decode('utf-8')) + ',' + str(float(exportData[i, 3].decode('UTF-8'))) + ',' + str(exportData[i, 0].decode('UTF-8')) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(exportData[i, 8].decode('UTF-8')) + '\n')
                            mdFile.close()
                            medos.append(code)
                            comps.remove(code)
                            del endIndex[code.decode('utf-8')]
                        elif(allmedo and (chegang < 200 and mdpCost < 10000000)):
                            mdFile = open(mdFilePath, 'a')
                            mdFile.write(str(code.decode('utf-8')) + ',' + str(float(exportData[i, 3].decode('UTF-8'))) + ',' + str(exportData[i, 0].decode('UTF-8')) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(exportData[i, 8].decode('UTF-8')) + '\n')
                            mdFile.close()
                            medos.append(code)
                            comps.remove(code)
                            del endIndex[code.decode('utf-8')]
                        elif(fMedoTime < second_oTime and (chegang < 90 or mdpCost < 5000000) and endcggrad < 0):
                            mdFile = open(mdFilePath, 'a')
                            mdFile.write(str(code.decode('utf-8')) + ',' + str(float(exportData[i, 3].decode('UTF-8'))) + ',' + str(exportData[i, 0].decode('UTF-8')) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(exportData[i, 8].decode('UTF-8')) + '\n')
                            mdFile.close()
                            medos.append(code)
                            comps.remove(code)       
                            del endIndex[code.decode('utf-8')]
                            
                if(second_oTime > endTime and code.decode('utf-8') in endIndex and endIndex[code.decode('utf-8')] != 0):
                    endIndex[code.decode('utf-8')] = i;                                                 

                if(second_oTime > endTime or allmedo):
                    continue;

                if(nowTime > endTime):
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

                if(chegang < 80 and exportData[i, 1].astype(int) < 4 and code not in nos):
                    nos.append(code)
                    continue;

                grRate = 0
                if(len(exportData[:i, 4]) > 6 and int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8')) != 0 and int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')) != 0):
                    grRate = (int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8'))) / (int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')))

                if(code.decode('utf-8') in delayMesu and delayMesu[code.decode('utf-8')] + 1 < i and delayMesu[code.decode('utf-8')] + 6 > i and grRate < 0.89 and (int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-1, 4].decode('UTF-8'))) > 1000 and (int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-1, 4].decode('UTF-8'))) > 1000 and code not in comps and chegang < 400):

                    fcgfit1 = sp.polyfit(sp.array(range(4)), exportData[i-3:i+1,9].astype(float), 1)
                    fcggrad1 = sp.around(fcgfit1[0], decimals=2)

                    fcgfit2 = sp.polyfit(sp.array(range(5)), exportData[i-4:i+1,9].astype(float), 1)
                    fcggrad2 = sp.around(fcgfit2[0], decimals=2)

                    fcgfit3 = sp.polyfit(sp.array(range(6)), exportData[i-5:i+1,9].astype(float), 1)
                    fcggrad3 = sp.around(fcgfit3[0], decimals=2)

                    fcggrad = min([fcggrad1, fcggrad2, fcggrad3])                    

                    findRate = exportData[delayMesu[code.decode('utf-8')], 3].astype(float)

                    maxminamin = max(exportData[i-5:i+1,3].astype(float)) - min(exportData[i-5:i+1,3].astype(float))
                    if(maxminamin > 5):
                        del delayMesu[code.decode('utf-8')]
                        continue;

                    if(findRate + 3 < exportData[i, 3].astype(float)):
                        del delayMesu[code.decode('utf-8')]
                        continue;

                    if(findRate + 1.5 < exportData[i, 3].astype(float)):
                        delayMesu[code.decode('utf-8')] = delayMesu[code.decode('utf-8')] + 1
                        continue;

                    if(fcggrad < -19.5 and xstime.tm_min < 10 and chegang > 195):
                        del delayMesu[code.decode('utf-8')]
                        continue;
                    if(exportData[i, 3].astype(float) < 4.6 and chegang < 140):
                        del delayMesu[code.decode('utf-8')]
                        continue;

                    mole = (exportData[i, 4].astype(int) - exportData[i-1, 4].astype(int))/exportData[i, 4].astype(int)
                    if(exportData[i, 4].astype(float) > 2000000 and mole < 0.03):
                        del delayMesu[code.decode('utf-8')]
                        continue;

                    if(exportData[i, 3].astype(float) > 16.3):
                        del delayMesu[code.decode('utf-8')]
                        continue;                        

                    with open(setFilePath, 'r') as f:
                        for line in f:
                            if(line.split(",")[0] == code.decode('utf-8') and code not in comps):
                                del delayMesu[code.decode('utf-8')]
                                nos.append(code)
                                break

                    if(code in nos):
                        continue;

                    comps.append(code)
                    mesuStart[code.decode('utf-8')] = second_oTime
                    msRate[code.decode('utf-8')] = float(rate)
                    isd[code.decode('utf-8')] = False
                    isd2[code.decode('utf-8')] = False
                    pick[code.decode('utf-8')] = False
                    endIndex[code.decode('utf-8')] = 0
                    cost = exportData[i, 8].decode('UTF-8')
                    setFile = open(setFilePath, 'a')
                    setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) + ',' + str(tpg) +  ',' + str_oTime + ',' + str(wanna) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(cost) + ',' + str(second_oTime) + ',' + str(1) + '\n')
                    setFile.close()
                    del delayMesu[code.decode('utf-8')]

                if(code.decode('utf-8') not in cggradDic):
                    cggradDic[code.decode('utf-8')] = []
                else:
                    cggradDic[code.decode('utf-8')].append(cggrad)

                if(((ms_md > 0.96 and sms_md > 1 and gr > 330000 and not (cggrad < -4 and chegang < 160)) or (cggrad > 2.3 and chegang > 163)) and grade < 16 and exportData[i, 3].astype(float) > 5 and gr1):
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
                            mesuDict[code.decode('utf-8')] = mesuDict.get(code.decode('utf-8'), 0)

                        if(mesuDict[code.decode('utf-8')] in mesuLimit and (code not in comps) and (code not in medos) and (code not in nos)):
                            if(exportData[i, 3].astype(float) < 4 or exportData[i, 3].astype(float) > 19):
                                continue;

                            if(xstime.tm_min < 2):
                                nos.append(code)
                                continue;

                            cost = int(exportData[i, 8].decode('UTF-8'))
                            if(cost > 9000):
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
                                nos.append(code)
                                continue;

                            if(True in (exportData[0:i,3].astype(float) > 22.5)):
                                nos.append(code)
                                continue;

                            lfit = sp.polyfit(x[-3:], y[-3:], level)
                            lg = sp.around(lfit[0]*10, decimals=2)

                            maxr = 100000
                            sry = (exportData[i-4:i+1,4].astype(float))/maxr
                            ssrlist = [b - a for a,b in zip(sry,sry[1:])]
                            ssrfit = sp.polyfit(x[:4], ssrlist, level)
                            ssrgrad = sp.around(ssrfit[0]*10, decimals=2)

                            if(gradient < 1.1 and ssrgrad < -1):
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
                                nos.append(code)
                                continue;

                            tlen = len(cggradDic[code.decode('utf-8')])
                            tfit = sp.polyfit(sp.array(range(tlen)), cggradDic[code.decode('utf-8')], 1)
                            tgrad = sp.around(tfit[0], decimals=2)

                            if(tgrad < -6):
                                nos.append(code)
                                continue;

                            tmesu = ((exportData[i,4].astype(float) - exportData[i-1,4].astype(float)) * exportData[i,8].astype(float)) + ((exportData[i - 1,4].astype(float) - exportData[i - 2,4].astype(float)) * exportData[i-1,8].astype(float))
                            if(tmesu > 250000000 and xstime.tm_min >= 6 and exportData[i, 3].astype(float) < 6.9):
                                nos.append(code)
                                continue;

                            if(chegang > 250 and xstime.tm_min <= 3 and exportData[i,3].astype(float) < 5.7):
                                nos.append(code)
                                continue;

                            tpg = 0

                            levelUpDic[code.decode('utf-8')] = []
                
                            for xm in range(0,xstime.tm_min + 1):
                                r = re.compile('09:' + str(xm).rjust(2, '0') + ':..')
                                vmatch = sp.vectorize(lambda xm:bool(r.match(xm)))
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
                                nos.append(code)
                                continue;

                            if(fcggrad < -15 and lg > 5):
                                nos.append(code)
                                continue;

                            if(fcggrad < -19.5 and xstime.tm_min < 10 and chegang > 195):
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

                            if(grRate > 1.9 or grRate1 > 1.9 or grRate2 > 1.9 or grRate3 > 1.9 or grRate4 > 1.9 or grRate5 > 1.9 or chegang > 400 or exportData[i, 3].astype(float) - exportData[i-1, 3].astype(float) > 2):
                                delayMesu[code.decode('utf-8')] = i
                                continue;

                            mole = (exportData[i, 4].astype(int) - exportData[i-1, 4].astype(int))/exportData[i, 4].astype(int)
                            if(exportData[i, 4].astype(float) > 2000000 and mole < 0.03):
                                nos.append(code)
                                continue;

                            if(exportData[i, 3].astype(float) > 16.3):
                                nos.append(code)
                                continue;      

                            with open(setFilePath, 'r') as f:
                                for line in f:
                                    if(line.split(",")[0] == code.decode('utf-8') and code not in comps):
                                        nos.append(code)
                                        break

                            if(code in nos):
                                continue;

                            comps.append(code)
                            mesuStart[code.decode('utf-8')] = second_oTime
                            msRate[code.decode('utf-8')] = float(rate)
                            isd[code.decode('utf-8')] = False
                            isd2[code.decode('utf-8')] = False
                            pick[code.decode('utf-8')] = False
                            endIndex[code.decode('utf-8')] = 0
                            cost = exportData[i, 8].decode('UTF-8')
                            setFile = open(setFilePath, 'a')
                            setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) + ',' + str(tpg) +  ',' + str_oTime + ',' + str(wanna) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(cost) + ',' + str(second_oTime) + ',' + str(1) + '\n')
                            setFile.close()

    except Exception as e:
        print('--------------------' + str(e))
        continue

print(today)