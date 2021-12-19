import heapq

read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

INF = int(1e9)
n, m = readline()
start = read()

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(1, m + 1):
    a, b, c = readline()
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    print(distance[i])
        
    