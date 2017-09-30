import csv
import pandas as pd
import datetime as datetime
import time

dataS = ['D','E','F']
dataH = ['A','B','C']
date = '20170918'
dataHD = pd.DataFrame({'DataH': dataH, 'Date': date})
dataHD.to_csv('DATAHIS.csv', header=True, index=False)
dataSD = pd.DataFrame({'DataS': dataS, 'Date': date})
dataSD.to_csv('DATASTAF.csv', header=True, index=False)
