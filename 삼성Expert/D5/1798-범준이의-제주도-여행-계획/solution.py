read = lambda: int(input())
readline = lambda: list(map(int, input().split()))
readlineSTR = lambda: list(map(lambda arg: arg[1] if arg[0] == 0 else int(arg[1]), enumerate(input().split())))

def dfs(t, day, satis, path, cur_p):
    global answer, visited, N, M, dis, info, hotel_indice

    can_go_next = False
    for i in range(2, N + 1):
        if i in hotel_indice or visited[i]:
            continue
        sum_t = t + info[i][1] + dis[cur_p][i]
        if sum_t <= 540:
            can_go_next = True
            visited[i] = True
            new_path = path + " {}".format(i)
            new_satis = satis + info[i][2]
            dfs(sum_t, day, new_satis, new_path, i)
            visited[i] = False
    if not can_go_next:
        if day > 1:
            for i in hotel_indice:
                sum_t = t + dis[cur_p][i]
                if sum_t <= 540:
                    new_path = path + " {}".format(i)
                    dfs(0, day - 1, satis, new_path, i)
        else:
            if t + dis[cur_p][1] <= 540 and answer[0] < satis:
                new_path = path + " 1"
                answer[0] = satis
                answer[1] = new_path

def solve():
    global answer, dis, info, visited, N, M, hotel_indice
    N, M = readline()
    dis = [[0] * (N + 1) for _ in range(N + 1)]
    info = [-1]
    visited = [False] * (N + 1)
    hotel_indice = []
    answer = [0, ""]
    
    for i in range(1, N):
        data = readline()
        for j, x in enumerate(data, i + 1):
            dis[i][j] = dis[j][i] = x 

    for i in range(1, N + 1):
        line = readlineSTR()
        if line[0] == "H":
            hotel_indice.append(i)
        if len(line) == 1:
            line += [0, 0]
        info.append(line)
    
    dfs(0, M, 0, "", 1)

    return str(answer[0]) + answer[1]
        
        

TC = read()
for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))