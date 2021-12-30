def solution(prices):
  answer = [0] * len(prices)
  for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
      if prices[i] <= prices[j]:
        answer[i] += 1
      else:
        answer[i] += 1
        break
  return answer

test_prices = [1,2,3,2,3] # return [4,3,1,1,0]
print(solution(test_prices))