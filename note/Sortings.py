array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 선택정렬
# 가장 작은 데이터를 찾는 일이 코딩 테스트에서 잦으므로 소스코드에 익숙해질 필요있다
def selection_sort():
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

# 삽입정렬
# 보통의 상황에서는 퀵정렬보다 비효율적이나 거의 데이터가 정렬되어 있을때는 오히려 더 빠르다
def insertion_sort():
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            # 한 칸씩 왼쪽으로 이동
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

insertion_sort()
print(array)