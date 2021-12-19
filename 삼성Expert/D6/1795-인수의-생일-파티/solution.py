import heapq

read = lambda: int(input())
readline = lambda: list(map(int, input().split()))
INF = int(1e9)

def dijkstra(start, graph, distance, X):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if start != X and now == X:
            break
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def solve():
    N, M, X = readline()
    graph = [[] for _ in range(N + 1)]
    distance = [[INF] * (N + 1) for _ in range(N + 1)]
    sum_board = [0] * (N + 1)
    for _ in range(M):
        x, y, c = readline()
        graph[x].append((y, c))

    for i in range(1, N + 1):
        dijkstra(i, graph, distance[i], X)
    for i in range(1, N + 1):
        sum_board[i] += distance[i][X]
    for i, v in enumerate(distance[X]):
        sum_board[i] += v
    return max(sum_board[1:])

TC = read()
for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))