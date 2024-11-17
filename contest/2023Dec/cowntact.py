#import sys
#sys.stdin = open("cowntact.in")

N = int(input().strip())
cows = input().strip()

groups = []
amount = 0
for c in cows:
    if c == '0' and amount > 0:
        groups.append(amount)
        amount = 0
    elif c == '1':
        amount += 1

if amount > 0:
    groups.append(amount)

leftEdge = (cows[0] == '1')
rightEdge = (cows[len(cows)-1] == '1')
start = 0
end = len(groups)
if leftEdge:
    start = 1
if rightEdge:
    end -= 1

smallestGroup = 1e7
for i in range(start, end):
    if groups[i] < smallestGroup:
        smallestGroup = groups[i]

nights = (smallestGroup - 1) // 2

if leftEdge:
    nights = min(groups[0] - 1, nights)

if rightEdge:
    nights = min(groups[len(groups) - 1] - 1, nights)

minCows = 0 
for g in groups:
    cowsNeeded = g // (nights * 2 + 1)
    if g % (nights * 2 + 1) != 0:
        cowsNeeded += 1
    minCows += cowsNeeded

print(minCows)