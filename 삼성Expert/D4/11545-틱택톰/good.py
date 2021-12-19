def check():
    # 가로 판단
    for i in range(4):
        if '.' not in arr[i] and 'O' not in arr[i]:
            return 'X won'
        if '.' not in arr[i] and 'X' not in arr[i]:
            return 'O won'
         
        # 세로 판단을 위한 리스트 생성
        col = [arr[j][i] for j in range(4)]
        if '.' not in col and 'O' not in col:
            return 'X won'
        if '.' not in col and 'X' not in col:
            return 'O won'
  
    # 우상단 대각선 판단
    rUp = [arr[i][i] for i in range(4)]
    if '.' not in rUp and 'O' not in rUp:
        return 'X won'
    elif '.' not in rUp and 'X' not in rUp:
        return 'O won'
     
    # 좌상단 대각선 판단
    lUP = [arr[i][3-i] for i in range(4)]
    if '.' not in lUP and 'O' not in lUP:
        return 'X won'
    elif '.' not in lUP and 'X' not in lUP:
        return 'O won'
  
    # 그밖의 경우.
    for i in range(4):
        for j in range(4):
            if arr[i][j] == '.':
                return 'Game has not completed'
  
    return 'Draw'
 
N = int(input())
for T in range(N):
    arr = [list(input()) for _ in range(4)]
    if T < N-1:
        _ = input()
         
    print(f'#{T+1} {check()}')
 
 
# T의 숫자를 고려해서 코딩해야 하는 줄 알았으나. 
# 문제에 T는 최대 1개로 설정. 
# 즉, T의 숫자를 별도로 카운트 하지 않아도 됨.