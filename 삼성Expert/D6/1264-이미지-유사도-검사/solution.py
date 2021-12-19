def solve():
    N = int(input())
    X = input()
    Y = input()
    board = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if X[i - 1] == Y[j - 1]:
                board[i][j] = board[i - 1][j - 1] + 1
            else:
                board[i][j] = max(board[i][j - 1], board[i - 1][j])
    return board[N][N] / N * 100
            

if __name__ == "__main__":
    TC = int(input())
    for i in range(1, TC + 1):
        print("#{} {:.2f}".format(i, solve()))