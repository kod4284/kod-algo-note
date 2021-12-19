readline = lambda: list(map(int, input().split()))

N, M, K = readline()
stickers = []
sticker_sizes = []
# 노트북 생성
board = [[0] * M for _ in range(N)]
one_count = 0

def check_OOR(a, b):
    return a < 0 or a >= N or b < 0 or b >= M

def check_overlaped(a, b):
    return board[a][b] == 1

def rotate(n):
    for i, (r, c) in enumerate(stickers[n]):
        stickers[n][i][0] = c
        stickers[n][i][1] = -r + (sticker_sizes[n][0] - 1)
    sticker_sizes[n][0], sticker_sizes[n][1] = sticker_sizes[n][1], sticker_sizes[n][0]
    

def apply_sticker(i, j, n):
    global one_count 
    for r, c in stickers[n]:
        dr, dc = r + i, c + j
        board[dr][dc] = 1
    one_count += len(stickers[n])


# 스티커들 좌표로 저장
for k in range(K):
    R, C = readline()
    stickers.append([])
    sticker_sizes.append([R, C])
    for i in range(R):
        l = readline()
        for j in range(C):
            if l[j] == 1:
                stickers[k].append([i, j])

# 노트북에 오른쪽 위부터 붙일 수 있는지 탐색
for n, s in enumerate(stickers) :
    stop = False
    # 4 방향 체크
    for _ in range(4):
        if stop:
            break
        for i in range(N):
            if stop:
                break
            for j in range(M):
                if stop:
                    break
                count = 0
                for k in range(len(s)):
                    r, c = s[k][0], s[k][1]
                    dr = r + i
                    dc = c + j
                    if check_OOR(dr, dc) or check_overlaped(dr, dc):
                        break
                    count += 1
                    if count == len(s):
                        # 스티커 저장
                        apply_sticker(i, j, n)
                        stop = True
                        break
        rotate(n)

print(one_count)
