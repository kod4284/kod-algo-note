# 데이터의 개수 12개
arr = [1, 9, 3, 8, 4, 5, 5, 9, 10, 3, 4, 5]
# 데이터의 개수 12개랑 가장 가까운 2의 n승 수 6 의 2배로 배열 만들기
tree = [None] * 16 * 2

def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]

def get_sum(start, end, node, left, right):
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return get_sum(start, mid, node * 2, left, right) + get_sum(mid + 1, end, node * 2 + 1, left, right)

def update(start, end, node, idx, dif):
    if idx < start or end < idx:
        return
    tree[node] -= arr[idx]
    tree[node] += dif
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, idx, dif)
    update(mid + 1, end, node * 2 + 1, idx, dif)

init(0, 11, 1)
print(tree)
print(get_sum(0, 11, 1, 5, 11))
update(0, 11, 1, 5, 10)
print(get_sum(0, 11, 1, 5, 11))