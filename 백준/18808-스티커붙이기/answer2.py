from copy import deepcopy
readline = lambda: list(map(int, input().split()))

N, M, K = readline()
global sticker
global R, C
note = [[0] * M for _ in range(N)]

def rotate():
    global R, C, sticker
    temp = deepcopy(sticker)
    sticker = [[0] * R for _ in range(C)]
    for i in range(C):
        for j in range(R):
            sticker[i][j] = temp[R - 1 - j][i]
    R, C = C, R 

def attachable(r, c):
    global R, C, note, sticker
    # 만약 스티커가 노트북에 이미 붙여져있는 스티커랑 겹칠경우
    for i in range(R):
        for j in range(C):
            if note[r + i][c + j] == 1 and sticker[i][j] == 1:
                return False
    # 스티커 노트북에 붙이기
    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1:
                note[r + i][c + j] = 1
    return True

for _ in range(K):
    R, C = readline()
    sticker = []
    # 스티커 초기화
    for _ in range(R):
        sticker.append(readline())
    # 스티커 붙이기 시뮬레이션 시작
    for _ in range(4):
        stop = False
        for i in range(N - R + 1):
            if stop: break
            for j in range(M - C + 1):
                if attachable(i, j):
                    stop = True
                    break
        if stop: break
        rotate()
# 스티커 개수 세기
cnt = 0
for i in range(N):
    for j in range(M):
        if note[i][j] == 1:
            cnt += 1
print(cnt)