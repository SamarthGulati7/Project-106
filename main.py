import csv
import numpy as np
import pandas

def getData(dataPath):
  marks=[]
  days=[]
  with open(dataPath) as f:
    data= csv.DictReader(f)
    for i in data:
      marks.append(float(i["Marks In Percentage"]))
      days.append(float(i["Days Present"]))
  return {"x":marks,"y":days}

def correlationa(dataSource):
  corr= np.corrcoef(dataSource["x"],dataSource["y"])
  #corr= np.corrcoef(dataSource["x"],dataSource["y"])
  print(corr[0,1])

def path():
  dataPath= "Student Marks vs Days Present.csv"
  dataSource= getData(dataPath)  
  correlationa(getData)
path()