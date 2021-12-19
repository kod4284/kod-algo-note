from itertools import product
from collections import defaultdict
readline = lambda: list(map(int, input().split()))

N = int(input())
board = []
for _ in range(N):
    board.append(readline())

def check_OOR(r, c):
    return r < 0 or c < 0 or r >= N or c >= N

# 좌우 내려갈때 다리 체크
def check_ROCX(r, c):
    return 0 <= r < N and (c >= N or c < 0)

def cal_five(r, c, d1, d2):
    cnt = 0
    dic = defaultdict(set)
    # 북서
    for i in range(d1 + 1):
        dr, dc = r + i, c - i
        if check_ROCX(dr, dc):
            dic[dr].add(0)
            continue
        if check_OOR(dr, dc):
            continue
        dic[dr].add(dc)
    print(dic)
    # 서남
    for i in range(d2 + 1):
        dr, dc = r + d1 + i, c - d1 + i
        if check_OOR(dr, dc):
            continue
        dic[dr].add(dc)
    print(dic)
    # 북동
    for i in range(d2 + 1):
        dr, dc = r + i, c + i
        if check_ROCX(dr, dc):
            dic[dr].add(N - 1)
            continue
        if check_OOR(dr, dc):
            continue
        dic[dr].add(dc)
    print(dic)
    # 동남
    for i in range(d1 + 1):
        dr, dc = r + d2+ i, c + d2 - i
        if check_OOR(dr, dc):
            continue
        dic[dr].add(dc)
    print(dic)
    sumv = 0
    for i in range(r, r + d1 + d2 + 1):
        if check_OOR(i, 0):
            continue
        block = list(dic[i])
        if i == r:
            first = r
            print(i, block[0])
            sumv += board[i][block[0]]
            continue
        elif i == r + d1 + d2:
            print(i, block[0])
            sumv += board[i][block[0]]
            continue
        if len(block) == 1:
            block.append(first)
            block.sort()
        for k in range(block[0], block[1] + 1):
            print(i, k)
            sumv += board[i][k]
    return sumv


print(cal_five(3, 5, 1, 1))

# for i in range(N):
#     cases = list(filter(lambda x: x[0] + x[1] <= N - i, product(range(N - i + 1), range(N - i + 1))))
#     for j in range(N):
#         print()

