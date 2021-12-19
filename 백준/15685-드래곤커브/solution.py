read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

board = [[0] * 120 for _ in range(120)]
dgcs = []
dgcvs = []

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def make_dg_curve(x, y, d, g):
    cords = []
    start_p = (y, x)
    cords.append(start_p)
    end_p = (y + dr[d], x + dc[d])
    # 0세대 만들기
    cords.append(end_p)
    if g < 1:
        return cords
    for _ in range(g):
        new_points = []
        for r, c in cords:
            # 90도 시계방향 돌리기
            rotated_p = (c, -r)
            if r == start_p[0] and c == start_p[1]:
                new_end_p = rotated_p
            elif r == end_p[0] and c == end_p[1]:
                attached_p = rotated_p
            new_points.append(rotated_p)
        sx = end_p[0] - attached_p[0]
        sy = end_p[1] - attached_p[1]
        shift_p = (sx, sy)
        # 붙이기
        for r, c in new_points:
            cords.append((r + shift_p[0], c + shift_p[1]))
        end_p = (new_end_p[0] + shift_p[0], new_end_p[1] + shift_p[1])
    return cords

N = read()
for _ in range(N):
    dgcs.append(readline())

for x, y, d, g in dgcs:
    dgcvs.append(make_dg_curve(x, y, d, g))
for cvs in dgcvs:
    for r, c in cvs:
        board[r][c] = 1

CHECK_DIR = [(0, 0), (0, 1), (1, 0), (1, 1)]
def check_squares():
    total = 0
    for i in range(100):
        for j in range(100):
            cnt = 0
            for r, c in CHECK_DIR:
                if board[i + r][j + c] == 1:
                    cnt += 1
            if cnt == 4:
                total += 1
    return total
                
print(check_squares())
