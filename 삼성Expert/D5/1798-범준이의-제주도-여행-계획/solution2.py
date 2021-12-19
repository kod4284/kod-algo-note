def dfs(day, time, satis, v):
    chk = False
    for i, (m, s) in points.items():
        if visited[i]:
            continue
        if time - m - distance[v][i] >= 10:
            chk = True
            path.append(i)
            visited[i] = 1
            dfs(day, time - m - distance[v][i], satis + s, i)
            path.pop()
            visited[i] = 0
    if not chk:
        if day > 1:
            for i in hotels:
                if distance[v][i] <= time:
                    path.append(i)
                    dfs(day - 1, 540, satis, i)
                    path.pop()
        else:
            if time >= distance[v][airport] and ans[0] < satis:
                ans[0] = satis
                ans[1] = path[1:] + [airport]
 
 
T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    distance = [[0] * (N + 1) for _ in range(N + 1)]
    hotels = []
    points = {}
    visited = [0] * (N + 1)
    ans = [0, []]
 
    for i in range(1, N):
        data = list(map(int, input().split()))
        for j, x in enumerate(data, i + 1):
            distance[i][j] = distance[j][i] = x
 
    for i in range(1, N + 1):
        data = input()
        if data[0] == 'P':
            points[i] = list(map(int, data.split()[1:]))
        elif data[0] == 'H':
            hotels.append(i)
        else:
            airport = i
 
    path = [airport]
    dfs(M, 540, 0, airport)
    print('#{} {}'.format(test_case + 1, ans[0]), *ans[1])