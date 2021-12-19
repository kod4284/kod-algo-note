from copy import deepcopy
read = lambda: int(input())
readline = lambda: list(map(int, input().split()))


N = read()
board = []

def mergable(arr, dir):
    global N
    if dir in [0, 1]:
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] == arr[i - 1]:
                arr[i] += arr[i - 1]
                arr[i - 1] = 0
        arr = list(filter(lambda x: x!=0, arr))
        for _ in range(N - len(arr)):
            arr.insert(0, 0)
        return arr
    elif dir in [2, 3]:
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                arr[i] += arr[i + 1]
                arr[i + 1] = 0
        arr = list(filter(lambda x: x!=0, arr))
        for _ in range(N - len(arr)):
            arr.append(0)
        return arr


def shift(board, dir):
    if dir in [0, 2]:
        for i in range(N):
            arr = list(filter(lambda x: x!=0, board[i]))
            arr = mergable(arr, dir)
            for j in range(N):
                board[i][j] = arr[j]
    elif dir in [1, 3]:
        arr_s = []
        # 어레이 수평으로 만들기
        for i in range(N):
            temp_arr=[]
            for j in range(N):
                tg = board[j][i]
                if (tg != 0):
                    temp_arr.append(tg)
            arr_s.append(temp_arr)
        for i in range(N):
            arr_f = mergable(arr_s[i], dir)
            for j in range(N):
                board[j][i] = arr_f[j]

for _ in range(N):
    board.append(readline())

max_value = 0
for i in range(1<<(2 * 5)):
    temp_board = deepcopy(board)
    brute = i
    for _ in range(5):
        dir = brute % 4
        brute //= 4
        shift(temp_board, dir)
    maxi = 0
    for b in temp_board:
        maxi = max(maxi, max(b))
    max_value = max(maxi, max_value)

print(max_value)
    
