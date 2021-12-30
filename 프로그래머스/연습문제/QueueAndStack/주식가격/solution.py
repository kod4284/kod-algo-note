def solution(prices):
  answer = []
  for i, v in enumerate(prices):
    for j in range(i + 1, len(prices)):
      if v > prices[j]:
        answer.append(j - i)
        break
    else:
      answer.append(len(prices) - i - 1)
  return answer

test_prices = [1,2,3,2,3] # return [4,3,1,1,0]
print(solution(test_prices))