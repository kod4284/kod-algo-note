import heapq
from itertools import combinations, permutations

readline = lambda: list(map(int, input().split()))

N = int(input())
board = []
abil = [[0] * N for _ in range(N)]

for i in range(N):
    board.append(readline())

for i in range(N):
    for j in range(N):
        sumv = 0
        sumv += board[i][j]
        sumv += board[j][i]
        abil[i][j] = abil[i][j] = sumv

cases = list(combinations(range(N), N // 2))


half = len(cases) // 2
a = cases[0:half]
b = list(reversed(cases[half:]))

def cal(a, b):
    suma = 0
    sumb = 0
    for f, s in combinations(list(a), 2):
        suma += abil[f][s]
    for f, s in combinations(list(b), 2):
        sumb += abil[f][s]
    return abs(suma - sumb)

ans = []

for i in range(len(a)):
    heapq.heappush(ans, cal(a[i], b[i]))

def print_arr(arr):
    for i in arr:
        print(i)
    print()
print(heapq.heappop(ans))
