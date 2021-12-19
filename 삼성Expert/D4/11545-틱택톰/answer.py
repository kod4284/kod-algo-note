read = lambda: int(input())
readline = lambda: input().rstrip()

array = []

NOT_FINISHED = "Game has not completed"
O_WON = "O won"
X_WON = "X won"
DRAW = "Draw"

# 가로 세로 탐색
def check_hori_verti():
    for i in range(4):
        row = array[i]
        if '.' not in row and 'O' not in row:
            return X_WON
        if '.' not in row and 'X' not in row:
            return O_WON
        # 세로 체크 위한 list 생성
        col = [array[j][i] for j in range(4)]
        if '.' not in col and 'O' not in col:
            return X_WON
        if '.' not in col and 'X' not in col:
            return O_WON
    return NOT_FINISHED

# 대각선 탐색
def check_cross():
    # 좌 상단 -> 우 하단 방향으로 체크
    lRDown = [array[i][i] for i in range(4)]
    if '.' not in lRDown and 'O' not in lRDown:
        return X_WON
    if '.' not in lRDown and 'X' not in lRDown:
        return O_WON
    # 
    lRUp = [array[3 - i][i] for i in range(4)]
    if '.' not in lRUp and 'O' not in lRUp:
        return X_WON
    if '.' not in lRUp and 'X' not in lRUp:
        return O_WON
    return NOT_FINISHED

# . 을 포함하는지 아닌지 확인
def check_dot():
    for i in range(4):
        if '.' in array[i]:
            return NOT_FINISHED
    return DRAW

def solve(i):
    if i != 0:
        input()
    for _ in range(4):
        array.append(list(readline()))
    result = check_hori_verti()
    if result == NOT_FINISHED:
        result = check_cross()
    if result == NOT_FINISHED:
        result = check_dot()
    return result

# 출력부
for i in range(int(read())):
    print("#{} {}".format(i + 1, solve(i)))
    array = []