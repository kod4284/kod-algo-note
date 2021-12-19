import math

readline = lambda: list(map(int, input().split()))
N = int(input())

# 초기화
arr = []
sand_sum = 0
t_cord = [N // 2, N // 2]
for _ in range(N):
    arr.append(readline())

# (r, c, 비율)
scattered = [
    [-1, 0, 0.07],
    [1, 0, 0.07],
    [2, 0, 0.02],
    [-2, 0, 0.02],
    [-1, -1, 0.1],
    [1, -1, 0.1],
    [-1, 1, 0.01],
    [1, 1, 0.01],
    [0, -2, 0.05],
]

# 좌 -> 하 -> 우 -> 상
direction = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

# +90도 회전
def rotate():
    for i in range(len(scattered)):
        scattered[i][0], scattered[i][1] = -scattered[i][1], scattered[i][0]

def scatter(r, c, direction):
    global sand_sum
    temp_sand = 0
    for i, j, rate in scattered:
        dr, dc = r + i, c + j
        target_sand = math.trunc(arr[r][c] * rate)
        temp_sand += target_sand
        if dr < 0 or dr >= N or dc < 0 or dc >= N:
            sand_sum += target_sand
        else:
            arr[dr][dc] += target_sand
    # alpha sand 계산
    alpha_sand = arr[r][c] - temp_sand
    # alpha cord 
    dr, dc = r + direction[0], c + direction[1]
    if dr >= 0 and dr < N and dc >= 0 and dc < N:
        arr[dr][dc] += alpha_sand
    else:
        sand_sum += alpha_sand
    # 기존위치 모래 비우기
    arr[r][c] = 0

# 토네이도 돌기
move, count = 1, 0
for i in range(2*N - 1):
    # 방향전환
    r, c = direction[i % 4]
    # 토네이도 이동
    for _ in range(move):
        t_cord[0] += r
        t_cord[1] += c
        # 흩어진 모래 계산
        scatter(t_cord[0], t_cord[1], (r, c))
    count += 1
    rotate()
    # 2번 이동하면 움직이는 거리 1증가
    if count == 2 and i < (2*N - 3):
        move += 1
        count = 0

print(sand_sum)