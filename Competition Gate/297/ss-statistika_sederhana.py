import sys

n = sys.stdin.readline()
n = int(n)

dataTemp = sys.stdin.readline()
dataTemp = dataTemp.split(' ')
data = [int(i) for i in dataTemp]

minVal = data[0]
maxVal = data[0]

for val in data:
    if val < minVal:
        minVal = val
    if val > maxVal:
        maxVal = val

print('{} {}'.format(maxVal, minVal))
