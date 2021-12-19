read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

INF = int(1e9)
n, m = readline()
start = read()

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
distance = [INF] * (n + 1)

for i in range(1, m + 1):
    a, b, c = readline()
    graph[a].append((b, c))

def get_smallest_node_idx():
    min_value = INF
    idx = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i
    return idx

def dijkstra(start):
    distance[start] = 0
    visited[start] = 1
    for i in graph[start]:
        distance[i[0]] = i[1]
    for _ in range(n - 1):
        now = get_smallest_node_idx()
        visited[now] = 1
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    print(distance[i])
        
    