from itertools import combinations
import heapq
readline = lambda: list(map(int, input().split()))

N, M = readline()

board = [[-1] * N]
homes = []
chickens = []


for _ in range(N):
    board.append([-1] + readline())

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if board[i][j] == 1:
            homes.append((i, j))
        elif board[i][j] == 2:
            chickens.append((i, j))

all_cases = combinations(chickens, M)

cases = []
for case in all_cases:
    m = []
    for home in homes:
        que = []
        for chicken in case:
            cr, cc = chicken
            hr, hc = home
            length = abs(hr - cr) + abs(hc - cc)
            heapq.heappush(que, length)
        m.append(heapq.heappop(que))
    heapq.heappush(cases, sum(m))
print(cases[0])
