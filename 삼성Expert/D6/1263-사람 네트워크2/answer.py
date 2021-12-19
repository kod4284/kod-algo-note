readline = lambda: list(map(int, input().split()))

TC = int(input())
INF = int(1e9)

def solve():
    temp = readline()
    N = temp[0]
    board = [[INF] * (N + 1)]
    idx = 0
    for i in range(1, N + 1):
        board.append([INF])
        for j in range(1, N + 1):
            idx += 1
            if temp[idx] == 0 and i != j:
                board[i].append(INF)
            else:
                board[i].append(temp[idx])
    # 플로이드 워셜
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                board[a][b] = min(board[a][b], board[a][k] + board[k][b])
    # 최솟값 구하기
    min_value = INF
    for i in range(1, N + 1):
        min_value = min(min_value, sum(board[i][1:]))
    return min_value

for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))