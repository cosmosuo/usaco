N, M = [int(w) for w in input().strip().split()]
cows = [int(w) for w in input().strip().split()]
candies = [int(w) for w in input().strip().split()] 

def eat(cowHeight, candyHeight, candyBase):
    if cowHeight > candyBase:
            if cowHeight < candyHeight:
                 return cowHeight - candyBase
            else:
                 return candyHeight - candyBase
    else:
        return 0
        
for i in range(M):
    candyBase = 0
    candyHeight = candies[i]
    for j in range(N):
        cowHeight = cows[j]
        amountEaten = eat(cowHeight, candyHeight, candyBase)
            
        cows[j] += amountEaten
        candyBase += amountEaten
        if candyBase >= candyHeight:
            break

for cow in cows:
    print(cow)
