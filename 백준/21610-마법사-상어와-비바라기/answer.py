from copy import deepcopy
readline = lambda: list(map(int, input().split()))

N, M = readline()
cloud_cord = [[N, 1], [N, 2], [N - 1, 1], [N - 1, 2]]
basket = []
visited = []
move = []
DIRECTION = {
    1: (0, -1),
    2: (-1, -1),
    3: (-1, 0),
    4: (-1, 1),
    5: (0, 1),
    6: (1, 1),
    7: (1, 0),
    8: (1, -1)
}
CROSS_CORD = [(-1, 1),(1, 1),(1, -1),(-1, -1)]

def make_cloud_entirely():
    global cloud_cord
    new_cloud_cord = []
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if basket[i][j] >= 2 and not visited[i][j]:
                basket[i][j] -= 2
                new_cloud_cord.append([i, j])
            if visited[i][j]:
                visited[i][j] = False
    cloud_cord = deepcopy(new_cloud_cord)

def cast_water_copy_bug():
    for r, c in cloud_cord:
        for cr, cc in CROSS_CORD:
            dr = r + cr
            dc = c + cc
            # 범위 넘어가면 skip
            if dr < 1 or dr > N or dc < 1 or dc > N:
                continue
            # 해당 바구니에 물이없으면 스킵
            if basket[dr][dc] == 0:
                continue
            basket[r][c] += 1
    

def rain():
    # 비내리기 1증가
    for r, c in cloud_cord:
        basket[r][c] += 1
    

def move_cloud(dir, mov):
    # 구름 입력 방향으로 이동
    for cord in cloud_cord:
        cord[0] += DIRECTION[dir][0] * mov
        cord[1] += DIRECTION[dir][1] * mov
        # print("r:",cord[0], "c:", cord[1])
        cord[0] %= N
        cord[1] %= N
        if cord[0] == 0:
            cord[0] = N
        if cord[1] == 0:
            cord[1] = N
        visited[cord[0]][cord[1]] = True
    

def sum_water():
    count = 0
    for i in basket:
        count += sum(i)
    return count

def init():
    # 초기화
    basket.append([0] * (N + 1))
    visited.append([False] * (N + 1))
    for _ in range(N):
        data = readline()
        # 첫번째 자리 인덱스 1을 맞춰 주기 위한 0
        basket.append([0, *data])
        visited.append([False] * (N + 1))
    for _ in range(M):
        dir, mov = readline()
        move.append((dir, mov))
    
# 출력부
init()
for dir, mov in move:
    move_cloud(dir, mov)
    rain()
    cast_water_copy_bug()
    make_cloud_entirely()
print(sum_water())