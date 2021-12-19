from collections import deque
from copy import deepcopy
readline = lambda: list(map(int, input().split()))

N, M = readline()
arr = []
cctvs = []
zero_count = 0

for _ in range(N):
    arr.append(readline())

direction = {
    1: [[0, 1]],
    2: [[0, -1], [0, 1]],
    3: [[-1, 0], [0, 1]], 
    4: [[0, -1], [1, 0], [0, 1]],
    5: [(-1, 0), (0, 1), (1, 0), (0, -1)],
}

rotation_count = {
    1: 4,
    2: 2,
    3: 4,
    4: 4,
    5: 1
}

def rotate(kind):
    if kind == 5:
        return
    for i in range(len(direction[kind])):
        direction[kind][i][0], direction[kind][i][1] = direction[kind][i][1], -direction[kind][i][0]

def check_safe_range(r, c):
    if (r >= 0 and r < N) and (c >= 0 and c < M):
        return True 
    else:
        return False

def print_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()
    print()


# CCTV 종류 및 좌표 찾아서 저장
for i in range(N):
    for j in range(M):
        if arr[i][j] >= 1 and arr[i][j] <= 5:
            cctvs.append((i, j, arr[i][j]))
        elif arr[i][j] == 0:
            zero_count += 1

for x, y, kind in cctvs:
    counter = []
    maps = []
    for _ in range(rotation_count[kind]):
        copied_arr = deepcopy(arr)
        cnt = 0
        for i in range(len(direction[kind])):
            r, c = direction[kind][i][0], direction[kind][i][1]
            dr, dc = x + r, y + c
            queue = deque([])
            if check_safe_range(dr, dc):
                queue.append(arr[dr][dc])
            while queue:
                v = queue.popleft()
                if v == "#":
                    dr, dc = dr + r, dc + c
                    if check_safe_range(dr, dc):
                        queue.append(arr[dr][dc]) 
                elif v == 6:
                    break
                elif v == 0:
                    copied_arr[dr][dc] = "#"
                    cnt += 1
                    dr, dc = dr + r, dc + c
                    if check_safe_range(dr, dc):
                        queue.append(arr[dr][dc])
                elif v >= 1 and v <= 5:
                    if check_safe_range(dr + r, dc + c):
                        dr, dc = dr + r, dc + c
                        queue.append(arr[dr][dc])
        counter.append(cnt)
        maps.append(copied_arr)
        rotate(kind)
    final_count = max(counter)
    arr = maps[counter.index(final_count)]
    print(zero_count, "-", final_count, "=", end=" ")
    zero_count -= final_count
    print(zero_count)
    print_arr(arr)

print(zero_count)