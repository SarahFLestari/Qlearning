
import numpy as nmp
import math

file = open('DataTugasML3.txt')
allData = []
tabelQ = []

N = 10
E = 1
W = -1
S = -10

with open('DataTugasML3.txt') as f:
    lines = f.readlines()
    x = [float(line.split()[0]) for line in lines]

for i in range(len(x)) :
    allData.append([i+1,x[i]])

for i in range(len(x)) :
    tabelQ.append([i+1,0,0,0,0])
    
print(allData)
print(tabelQ)

