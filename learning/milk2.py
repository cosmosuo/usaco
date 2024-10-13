"""
ID: livyten1
LANG: PYTHON3
TASK: milk2
"""
milkingTimes = []

with open("milk2.in", "r") as fIn:
    N = int(fIn.readline().strip())
    for _ in range(N):
        line = fIn.readline().strip()
        timeRange = [int(word) for word in line.split()]
        milkingTimes.append(timeRange)
    
milkingTimes.sort()

maxGap = 0

combinedTimes = []

curS, curE = milkingTimes[0]

for i in range(1, N):
    s, e = milkingTimes[i]
    if s <= curE: 
        curE = max(curE, e)
    else:
        combinedTimes.append((curS, curE))
        maxGap = max(maxGap, s-curE)
        curS = s
        curE = e

combinedTimes.append([curS, curE])

maxMilkingTimes = 0
for s, e in combinedTimes:
    maxMilkingTimes = max(maxMilkingTimes, e - s)

with open("milk2.out", "w") as fOut:
    fOut.write(f"{maxMilkingTimes} {maxGap}\n")