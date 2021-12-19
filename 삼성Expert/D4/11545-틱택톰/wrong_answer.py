read = lambda: int(input())
readline = lambda: input().rstrip()

array = []

NOT_FINISHED = "Game has not completed"
O_WON = "O won"
X_WON = "X won"
DRAW = "Draw"

def check_winner(player):
    if player == "O":
        return O_WON
    if player == "X":
        return X_WON
    return "Error"

# 가로 탐색
def search_hori():
    hasEmpty = False
    for i in range(4):
        count = 1
        for j in range(1, 4):
            f_ele = array[i][0]
            pre = array[i][j - 1]
            curr = array[i][j]

            if curr == "." or f_ele == ".":
                hasEmpty = True
            if pre != "." and curr != "." and (pre == curr or pre == "T" or curr == "T"):
                count += 1
            if count == 4:
                if curr == "T":
                    return check_winner(f_ele)
                return check_winner(curr)
    if hasEmpty:
        return NOT_FINISHED
    return DRAW

# 세로 탐색
def search_verti():
    hasEmpty = False
    for i in range(4):
        count = 1
        for j in range(1, 4):
            f_ele = array[0][i]
            pre = array[j - 1][i]
            curr = array[j][i]

            if curr == '.' or f_ele == ".":
                hasEmpty = True
            if f_ele != "." and pre == curr or pre == "T" or curr == "T":
                count += 1
            if count == 4:
                if curr == "T":
                    return check_winner(f_ele)
                return check_winner(curr)
    if hasEmpty:
        return NOT_FINISHED
    return DRAW

# 대각선 탐색
def search_cross():
    # 오른쪽 왼쪽부터 오른쪽 아래로 탐색
    count = 1
    hasEmpty = False
    for i in range(1, 4):
        f_ele = array[0][0]
        pre = array[i - 1][i - 1]
        curr = array[i][i]

        if curr == "." or f_ele == ".":
            hasEmpty = True
        if pre != "." and curr != "." and pre == curr or pre == "T" or curr == "T":
            count += 1
        if count == 4:
            if curr == "T":
                return check_winner(f_ele)
            return check_winner(curr)
    # 왼쪽아래부터 오른쪽 위로 탐색
    count = 1
    for i in range(1, 4):
        f_ele = array[3][0]
        pre = array[3 - i + 1][i - 1]
        curr = array[3 - i][i]

        if curr == "." or f_ele == ".":
            hasEmpty = True
        if pre != "." and curr != "." and pre == curr or pre == "T" or curr == "T":
            count += 1
        if count == 4:
            if curr == "T":
                return check_winner(f_ele)
            return check_winner(curr)
    if hasEmpty:
        return NOT_FINISHED
    return DRAW

def solve(i):
    if i != 0:
        input()
    for _ in range(4):
        array.append(list(readline()))
    result = search_hori()
    if result == DRAW or result == NOT_FINISHED:
        result = search_verti()
    if result == DRAW or result == NOT_FINISHED:
        result = search_cross()
    return result
    # 세로 탐색
    # 대각선 탐색

# 출력부
for i in range(int(read())):
    print("#{} {}".format(i + 1, solve(i)))
    array = []