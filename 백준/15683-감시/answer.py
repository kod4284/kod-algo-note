# Time complexity: 20971520 (4*8)*(8)+(64)*(4^8) {upd 함수 호출 갯수--5번 cctv 8개}, {upd 함수안의 while 최대 반복횟수 max(N, M)}, {0 개수 세기}, {cctv 방향 모든 조합 개수}
import sys
readline = lambda: list(map(int, sys.stdin.readline().split()))

N, M = readline()
board1 = []
board2 = [[0] * M for _ in range(N)]
cctv_cords = []
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
zero_count = 0

def check_OOR(r, c):
    return r < 0 or r >= N or c < 0 or c >= M

def upd(r, c, dir):
    dir %= 4
    while(True):
        r += DIR[dir][0]
        c += DIR[dir][1]
        if check_OOR(r, c) or board2[r][c] == 6:
            return 
        if board2[r][c] != 0:
            continue
        board2[r][c] = 7

def print_board2():
    for i in range(N):
        for j in range(M):
            print(board2[i][j], end=" ")
        print()
    print()

# 초기화
for _ in range(N):
    board1.append(readline())

# 0 개수 세기 cctv 위치 확인
for i in range(N):
    for j in range(M):
        if board1[i][j] == 0:
            zero_count += 1
        elif board1[i][j] not in [0, 6]:
            cctv_cords.append((i, j))

# CCTV 방향의 모든 조합
for i in range(1<<(2*len(cctv_cords))):
    # board1 board2로 deepcopy
    for x in range(N):
        for y in range(M):
            board2[x][y] = board1[x][y]
    brute = i
    for r, c in cctv_cords:
        direction = brute % 4 # CCTV 방향
        brute //= 4
        cctv = board1[r][c]
        if cctv == 1:
            upd(r, c, direction)
        elif cctv == 2:
            upd(r, c, direction)
            upd(r, c, direction + 2)
        elif cctv == 3:
            upd(r, c, direction)
            upd(r, c, direction + 1)
        elif cctv == 4:
            upd(r, c, direction)
            upd(r, c, direction + 1)
            upd(r, c, direction + 2)
        elif cctv == 5:
            upd(r, c, direction)
            upd(r, c, direction + 1)
            upd(r, c, direction + 2)
            upd(r, c, direction + 3)
    count = 0
    # 0 개수 세기
    for r in range(N):
        for c in range(M):
            if board2[r][c] == 0:
                count += 1
    zero_count = min(zero_count, count)
print(zero_count)