# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:43:36 2017

@author: My Computer
"""

from os import listdir
import os.path

stationDict = {'gra':'grw','lab':'lbh','mbb':'mrb'}

def readPickFile(choosenIndex):
    readFile = open(pickFile[choosenIndex])
    allLine = readFile.readlines(1)
    readFile.close()
    
    # Cut the line according to the space delimited
    splitedLine = []
    for line in allLine:
        splitedLine.append(line.strip().split())
    
    
    station = []
    phase = []
    polarity = []
    dateTime = []
    for line in splitedLine:
        if len(line) > 0:
            
            # extract the station
            staI = line[0].lower()
            
            sta = staI[2:5]
            # convert to match station code
            if (sta == "gra") | (sta == "lab") | (sta == "mbb"):
                sta = stationDict[sta]
            
            station.append(sta)
            
            # extract phase
            pha = line[4].lower()
            phase.append(pha)
            
            # extract polarity
            if(line[5].lower() == "d"):
                pol = "-"
            else:
                pol = "+"
            polarity.append(pol)
            
            # Extract DateTime
            date = line[6][2:8]
            time = line[7] + line[8]
            dateTime.append(date+time)
    
    # Create correct pha format
    hypoFile = []
    for i in range(len(station)):
        row = station[i]+"  "+phase[i]+" "+polarity[i]+" "+dateTime[i]+"\n"
        hypoFile.append(row)
        
    return hypoFile
    
def writePickFile(hypoFile):
    filename = "merapi.pha"
    if(os.path.isfile(filename)):
        outFile = open(filename,"a")
        outFile.write("\n")
    else:
        outFile = open(filename,"w")
    for row in hypoFile:
        outFile.write(row)
    outFile.close()
    
    
# Scan All available .pick files
allFiles = listdir(".")
index = 0
pickFile = []
for aFile in allFiles:
    if aFile.endswith(".pick"):
        index+=1
        pickFile.append(aFile)
        print str(index) + " - " + aFile
                 
choosenIndex = input("Silahakan pilih file .pick dengan memasukan indexnya <1> : ")

# Correct the value1
choosenIndex -= 1;

if index < choosenIndex:
    print "index yang anda masukan salah"
    
hypoFile = readPickFile(choosenIndex)
writePickFile(hypoFile)