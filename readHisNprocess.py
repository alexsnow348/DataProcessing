import csv
import pandas as pd
import datetime as datetime
import time
dataHD = pd.read_csv('DATAHIS.csv')
dataSD = pd.read_csv('DATASTAF.csv')
dataS = list(dataSD.DataS)
dataH = list(dataHD.DataH)
date = time.strftime('%Y/%m/%d')
temToday = list()

newDataFirst5Min = ['A', 'D', 'F', 'O', 'a', 'L', 'P', 'S', 'K']
newDataNext5Min = ['A', 'O', 'W', 'b', 'K', 'L']
DataTest = [newDataFirst5Min, newDataNext5Min]

for item in DataTest:
    newVistor = 0
    repeatedVistitor = 0
    repetedToday = 0
    staff = 0
    for each in item:
        if each not in dataS:
            if each in dataH:
                if each not in temToday:
                    repeatedVistitor += 1
                    temToday.append(each)
                else:
                    repetedToday += 1
            else:
                if each not in temToday:
                    newVistor += 1
                    temToday.append(each)
                else:
                    repetedToday += 1
        else:
            staff += 1
    print(" ")
    print("5 Minitues Analysis:")
    print("Staff:" + str(staff))
    print("newVistor:" + str(newVistor))
    print("repeatedVistitor:" + str(repeatedVistitor))
    print("repetedToday:" + str(repetedToday))
    print("todayTemp:")
    print(temToday)
    print('Added line')
