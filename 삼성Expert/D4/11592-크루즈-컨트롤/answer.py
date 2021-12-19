#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
read = lambda: list(map(int, input().split()))
result = []

# TC: 테스트 케이스
# D, N: 종로거리, 말 수
# K, S: 말 위치, 말 속도

def solve():
    TC = int(input())
    for _ in range(TC):
        D, N = read()
        array = []
        for _ in range(N):
            K, S = read()
            array.append((D - K)/ S)
        value = '{0:.7f}'.format(D / max(array))
        array = []
        result.append(value)
solve()

# 출력부
for i, r in enumerate(result, start=1):
    print("#{} {}".format(i, r))
