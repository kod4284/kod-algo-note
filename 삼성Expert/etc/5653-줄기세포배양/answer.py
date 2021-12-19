read = lambda: list(map(int, input().split()))
readline = lambda: input().rstrip()
 
# 1000x1000 배열(배양용기)의 적당한 가운데 지정하기 위한 OFFSET
OFFSET = 500
# 죽은 세포
DEAD = -1
# 세포가 분열할 수 있는 빈 셀
NOTHING = 0
# 살아있는 세포
CELL = 1
 
def solve():
  div_t =[[] for i in range(301)]
  dead_t = [[] for i in range(301)]
  # 1000x1000 빈 배열(배양용기) 선언
  board = [ [NOTHING] * 1000 for i in range(1000) ]
  # N: 세로, M: 가로, K: 배양시간
  N, M, K = read()
  for i in range(N):
    arr = read()
    for j in range(M):
      life = arr[j]
      # 입력이 0이면 넘기기
      if life == NOTHING:
        continue
      # 입력이 0이 아니면 세포 위치에 기록
      board[i + OFFSET][j + OFFSET] = CELL
      # 세포가 분열하는 시간 테이블에 셀의 위치와 생명력을 넣음
      div_t[life + 1].append([life, i + OFFSET, j + OFFSET])
      # 세포가 죽을 시간 테이블에 셀의 위치만 넣음
      dead_t[2 * life].append([i + OFFSET, j + OFFSET])
 
  for t in range(1, K + 1):
    # 내림 차순으로 sorting됨
    div_t[t].sort(reverse=True)
    for life, r, c in div_t[t]:
      # 상하좌우 위치참조
      for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        R = r + dr 
        C = c + dc
        # 셀이 비었으면 그자리에 세포분열
        if board[R][C] == NOTHING:
          board[R][C] = CELL
          # 세포가 분열하는 시간 테이블에 세포의 생명력과 위치 기록
          if t + life + 1 <= K:
            div_t[t + life + 1].append([life, R, C])
          # 세포가 죽을 시간 테이블에 세포위치 기록
          if t + 2 * life <= K:
            dead_t[t + 2 * life].append([R, C])
 
    # 죽은세포 배양용기에 기록
    for r, c in dead_t[t]:
      board[r][c] = DEAD 
 
  ans = 0
 
  # 배양용기 모든 셀 참조하면서 살아있는 세포 카운트
  for i in board:
    for j in i:
      if j == CELL:
        ans += 1
  return ans 
 
# 출력 부
for case in range(int(readline())):
  print("#{} {}".format(case + 1, solve()))