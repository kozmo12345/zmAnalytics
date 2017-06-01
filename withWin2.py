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

def createFiles(realfilePath, setFilePath, mdFilePath):
    try:
        realfile = open(realfilePath, 'a')
        realfile.close()
        
        setFile = open(setFilePath, 'w')
        setFile.close()
        
        mdFile = open(mdFilePath, 'w')
        mdFile.close()
    except Exception as e:
        createFiles(realfilePath, setFilePath, mdFilePath)
    else:
        pass

now = datetime.datetime.now()
today = now.strftime('%Y-%m-%d')

startTime = datetime.timedelta(hours=9,minutes=00,seconds=00).total_seconds()
endTime = datetime.timedelta(hours=9,minutes=12,seconds=30).total_seconds()
fMedoTime = datetime.timedelta(hours=9,minutes=18,seconds=30).total_seconds()
allMedoTime = datetime.timedelta(hours=9,minutes=25,seconds=30).total_seconds()
closeTime = datetime.timedelta(hours=15,minutes=19,seconds=00).total_seconds()

comps = []
medos = []
nos = []
mesuLimit = [2]
wanna = 1
rateLimit = 0.31
rateMLimit = 3.8
gradient = 0
realfilePath = os.path.join("C:\\", "Dropbox\\Diff\\" + today + "\\" + today + ".txt");
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

mesuStart = dict()
msRate = dict()
isd = dict()
isd2 = dict()
levelUpDic = dict()
pick = dict()
delayMesu = dict()
isRe = False

with open(setFilePath, 'r') as f:
    for line in f:
        imCode = line.split(",")[0].strip()
        if(imCode != ''):
            isRe = True
        if(imCode != '' and int(line.split(",")[8].strip()) == 2):
            comps.append(str.encode(imCode))
            mesuStart[imCode] = float(line.split(",")[7].strip())
            msRate[imCode] = float(line.split(",")[1].strip())
            isd[imCode] = False
            isd2[imCode] = False
            pick[imCode] = False
        elif(imCode != '' and int(line.split(",")[8].strip()) == 1):
            nos.append(str.encode(imCode))
        else:
            continue;

if(not isRe):
    createFiles(realfilePath, setFilePath, mdFilePath)

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

        now = datetime.datetime.now()
        nowTime = datetime.timedelta(hours=now.hour,minutes=now.minute,seconds=now.second).total_seconds()

        wchkfilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + "w2.pchk");
        if not os.path.exists(wchkfilePath):
            wchkfile = open(wchkfilePath, 'a')
            wchkfile.close()
    
        if(nowTime > endTime and len(comps) == 0):
            time.sleep( 4 )
            continue;
    
        if(nowTime > allMedoTime):
            time.sleep( 4 )
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
                    mdpCost = (exportData[i,4].astype(float) - exportData[i-1,4].astype(float)) * exportData[i-1,8].astype(float)

                    med = ed
                    tempWan = wanna
                    if((ms - md) > 1):
                        isd[code.decode('utf-8')] = True
                    if(isd[code.decode('utf-8')]):
                        tempWan = 0.4
                    if((ms - md) > 2):
                        isd2[code.decode('utf-8')] = True
                    if(isd2[code.decode('utf-8')]):
                        med = ed * 1.8

                    if(nowTime - 20 < second_oTime):
                        mmRate = (sp.sum(exportData[i-2:i+1,5].astype(float)))/(sp.sum(exportData[i-2:i+1,6].astype(float))) - (med/22)

                        cgfit1 = sp.polyfit(ti[:5], exportData[i-4:i+1,9].astype(float), 1)
                        cggrad1 = sp.around(cgfit1[0], decimals=2)
    
                        cgfit2 = sp.polyfit(ti[:6], exportData[i-5:i+1,9].astype(float), 1)
                        cggrad2 = sp.around(cgfit2[0], decimals=2)
    
                        cgfit3 = sp.polyfit(ti[:7], exportData[i-6:i+1,9].astype(float), 1)
                        cggrad3 = sp.around(cgfit3[0], decimals=2)
                        
                        gcggrad = min([cggrad1, cggrad2, cggrad3])
                        chegang = exportData[i,9].astype(float)
                        if(chegang < 120):
                            gcggrad = -10

                        print(code.decode('utf-8') + '    ' + str(mmRate) + '    ' + str(str_oTime))

                        grRate = 0
                        if(len(exportData[:i, 4]) > 6 and int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8')) != 0 and int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')) != 0):
                            grRate = (int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8'))) / (int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')))

                        if(grRate > 1.78):
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
                                        if((flaver - nfaver) > 4.26 and ed > 0.4):
                                            mdFile = open(mdFilePath, 'a')
                                            mdFile.write(str(code.decode('utf-8')) + ',' + str(float(exportData[i, 3].decode('UTF-8'))) + ',' + str(exportData[i, 0].decode('UTF-8')) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(exportData[i, 8].decode('UTF-8')) + '\n')
                                            mdFile.close()
                                            medos.append(code)
                                            comps.remove(code)
                                            break;

                                        if((flaver - nfaver) > 4.26 and second_oTime > mesuStart[code.decode('utf-8')] + 120):
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

                        if(code not in comps):
                            continue;

                        if((mmRate < rateLimit or mmRate > rateMLimit) and gcggrad < -1.7 and ed >= tempWan):
                            mdFile = open(mdFilePath, 'a')
                            mdFile.write(str(code.decode('utf-8')) + ',' + str(float(exportData[i, 3].decode('UTF-8'))) + ',' + str(exportData[i, 0].decode('UTF-8')) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(exportData[i, 8].decode('UTF-8')) + '\n')
                            mdFile.close()
                            medos.append(code)
                            comps.remove(code)
                        elif(mdpCost < 5500000 and mdpCost != 0 and md < 3):
                            mdFile = open(mdFilePath, 'a')
                            mdFile.write(str(code.decode('utf-8')) + ',' + str(float(exportData[i, 3].decode('UTF-8'))) + ',' + str(exportData[i, 0].decode('UTF-8')) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(exportData[i, 8].decode('UTF-8')) + '\n')
                            mdFile.close()
                            medos.append(code)
                            comps.remove(code)
                        elif(mesuStart[code.decode('utf-8')] + 600 < second_oTime and ed > 0.4 and ed < 2.5):
                            mdFile = open(mdFilePath, 'a')
                            mdFile.write(str(code.decode('utf-8')) + ',' + str(float(exportData[i, 3].decode('UTF-8'))) + ',' + str(exportData[i, 0].decode('UTF-8')) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(exportData[i, 8].decode('UTF-8')) + '\n')
                            mdFile.close()
                            medos.append(code)
                            comps.remove(code)                            
                        elif(mesuStart[code.decode('utf-8')] + 360 < second_oTime and ed > -0.1 and ed < 1 and max(exportData[:i,9].astype(float)) < 275):
                            mdFile = open(mdFilePath, 'a')
                            mdFile.write(str(code.decode('utf-8')) + ',' + str(float(exportData[i, 3].decode('UTF-8'))) + ',' + str(exportData[i, 0].decode('UTF-8')) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(exportData[i, 8].decode('UTF-8')) + '\n')
                            mdFile.close()
                            medos.append(code)
                            comps.remove(code)
                        elif((pick[code.decode('utf-8')] and ed >= 0.4) or (second_oTime > mesuStart[code.decode('utf-8')] + 180 and pick[code.decode('utf-8')] and ed >= 0.1)):
                            mdFile = open(mdFilePath, 'a')
                            mdFile.write(str(code.decode('utf-8')) + ',' + str(float(exportData[i, 3].decode('UTF-8'))) + ',' + str(exportData[i, 0].decode('UTF-8')) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(exportData[i, 8].decode('UTF-8')) + '\n')
                            mdFile.close()
                            medos.append(code)
                            comps.remove(code)                                             

                if(second_oTime > endTime):
                    continue;

                if(nowTime > endTime):
                    continue;
    
                rate = exportData[i, 3].decode('UTF-8')
                grade = int(exportData[i, 1].decode('UTF-8'))
                gr = int(exportData[i, 4].decode('UTF-8'))

                ms_md = (exportData[i,5].astype(float))/(exportData[i,6].astype(float))
                sms_md = sp.sum(sp.unique(exportData[:i+1,5].astype(float)))/sp.sum(sp.unique(exportData[:i+1,6].astype(float)))
                gr1 = int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-1, 4].decode('UTF-8')) != 0

                cgfit = sp.polyfit(ti, exportData[:i+1,9].astype(float), 1)
                cggrad = sp.around(cgfit[0], decimals=2)
                chegang = exportData[i,9].astype(float)

                grRate = 0
                if(len(exportData[:i, 4]) > 6 and int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8')) != 0 and int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')) != 0):
                    grRate = (int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-3, 4].decode('UTF-8'))) / (int(exportData[i-3, 4].decode('UTF-8')) - int(exportData[i-6, 4].decode('UTF-8')))

                if(code.decode('utf-8') in delayMesu and delayMesu[code.decode('utf-8')] + 1 < i and delayMesu[code.decode('utf-8')] + 6 > i and grRate < 0.89 and (int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-1, 4].decode('UTF-8'))) > 1000 and (int(exportData[i, 4].decode('UTF-8')) - int(exportData[i-1, 4].decode('UTF-8'))) > 1000 and code not in comps):
                    comps.append(code)
                    mesuStart[code.decode('utf-8')] = second_oTime
                    msRate[code.decode('utf-8')] = float(rate)
                    isd[code.decode('utf-8')] = False
                    isd2[code.decode('utf-8')] = False
                    pick[code.decode('utf-8')] = False
                    cost = exportData[i, 8].decode('UTF-8')
                    setFile = open(setFilePath, 'a')
                    setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) + ',' + str(tpg) +  ',' + str_oTime + ',' + str(wanna) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(cost) + ',' + str(second_oTime) + ',' + str(1) + '\n')
                    setFile.close()
                    del delayMesu[code.decode('utf-8')]

                if(code.decode('utf-8') not in cggradDic):
                    cggradDic[code.decode('utf-8')] = []
                else:
                    cggradDic[code.decode('utf-8')].append(cggrad)

                if(((ms_md > 0.96 and sms_md > 1 and gr > 420000) or (cggrad > 2.3 and chegang > 163)) and grade < 16 and exportData[i, 3].astype(float) > 5 and gr1):
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

                            # if(exportData[i, 3].astype(float) < 5.3):
                            #     nos.append(code)
                            #     continue;

                            cost = int(exportData[i, 8].decode('UTF-8'))
                            if(cost > 8500):
                                nos.append(code)
                                continue;                                

                            if(i < 4):
                                s = 0
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
                            if((lg > 2 and True in (exportData[0:i,5].astype(float) == 0)) or lg > 13.8):
                                nos.append(code)
                                continue;                                

                            maxr = 100000
                            sry = (exportData[i-4:i+1,4].astype(float))/maxr
                            ssrlist = [b - a for a,b in zip(sry,sry[1:])]
                            ssrfit = sp.polyfit(x[:4], ssrlist, level)
                            ssrgrad = sp.around(ssrfit[0]*10, decimals=2)

                            if(gradient < 1.1 and ssrgrad < -1):
                                nos.append(code)
                                continue;

                            fcgfit1 = sp.polyfit(ti[:4], exportData[i-3:i+1,9].astype(float), 1)
                            fcggrad1 = sp.around(fcgfit1[0], decimals=2)
        
                            fcgfit2 = sp.polyfit(ti[:5], exportData[i-4:i+1,9].astype(float), 1)
                            fcggrad2 = sp.around(fcgfit2[0], decimals=2)                            
         
                            fcggrad = min([fcggrad1, fcggrad2])

                            if(fcggrad < -14.01):
                                nos.append(code)
                                continue;

                            lcgfit = sp.polyfit(ti[:6], exportData[i-5:i+1,9].astype(float), 1)
                            lcggrad = sp.around(lcgfit[0], decimals=2)

                            if((chegang < 129 and lcggrad < -1.8) or lcggrad > 60):
                                nos.append(code)
                                continue;

                            tlen = len(cggradDic[code.decode('utf-8')])
                            tfit = sp.polyfit(ti[:tlen], cggradDic[code.decode('utf-8')], 1)
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
                            for ii in range(1,i):
                                pi = ii * 3
                                if(pi >= i):
                                    break

                                pfit = sp.polyfit(x[:pi], y[-pi:], level)
                                pgradient = sp.around(pfit[0]*10, decimals=2)
                                if(tpg < pgradient and not sp.isinf(pgradient)):
                                    tpg = pgradient
                            
                            tpg = tpg * sp.sqrt(ii * 0.77)

                            with open(setFilePath, 'r') as f:
                                for line in f:
                                    if(line.split(",")[0] == code.decode('utf-8') and code not in comps):
                                        nos.append(code)
                                        break

                            if(code in nos):
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

                            if(grRate > 1.9 or grRate1 > 1.9 or grRate2 > 1.9 or grRate3 > 1.9 or grRate4 > 1.9):
                                delayMesu[code.decode('utf-8')] = i
                                continue;

                            comps.append(code)
                            mesuStart[code.decode('utf-8')] = second_oTime
                            msRate[code.decode('utf-8')] = float(rate)
                            isd[code.decode('utf-8')] = False
                            isd2[code.decode('utf-8')] = False
                            pick[code.decode('utf-8')] = False
                            cost = exportData[i, 8].decode('UTF-8')
                            setFile = open(setFilePath, 'a')
                            setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) + ',' + str(tpg) +  ',' + str_oTime + ',' + str(wanna) + ',' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ',' + str(cost) + ',' + str(second_oTime) + ',' + str(2) + '\n')
                            setFile.close()

    except Exception as e:
        print('--------------------' + str(e))
        continue

print(today)