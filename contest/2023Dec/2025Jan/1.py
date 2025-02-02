import sys
sys.stdin = open('1.in')

def solve(N, sky, A, B):
    res = 0
    if A == 0 and B == 0:
        for i in range(N):
            for j in range(N):
                if sky[p_i][p_j] == 'G' or sky[p_i][p_j] == 'B':
                    res += 1
        return res
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            p_i = i - B
            p_j = j - A
            if sky[i][j] == 'G':
                res += 1
                if p_i < 0 or p_j < 0:
                    continue
                elif sky[p_i][p_j] == 'G':
                    sky[p_i][p_j] = 'W'
                elif sky[p_i][p_j] == 'B':
                    sky[p_i][p_j] = 'G'
            elif sky[i][j] == 'B':
                res += 2
                if p_i < 0 or p_j < 0:
                    return -1
                elif sky[p_i][p_j] == 'W':
                    return -1
                elif sky[p_i][p_j] == 'G':
                    sky[p_i][p_j] = 'W'
                elif sky[p_i][p_j] == 'B':
                    sky[p_i][p_j] = 'G'

    return res

T = int(input().strip())

for _ in range(T):
    N, A, B = [int(e) for e in input().strip().split()]
    sky = []
    for i in range(N):
        line = input().strip()
        sky.append(list(line))
    print(solve(N, sky, A, B))