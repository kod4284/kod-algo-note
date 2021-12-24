read = lambda: int(input())
readline = lambda: list(input().split())

# # ans 1
# def solution(phone_book):
#   phone_list = sorted(phone_book) # 문자열 정렬
#   for p1, p2 in zip(phone_list, phone_list[1:]): # 맨 마지막은 비교 필요 X
#     if p2.startswith(p1):
#       return False
#   return True

# ans 2
def solution(phone_book):
  phone_dict = {}
  for phone in phone_book:
    phone_dict[phone] = True
  for phone in phone_book:
    prefix = ""
    for number in phone:
      prefix += number
      if prefix in phone_dict and prefix != phone:
        return False
  return True

TC = read()
for i in range(1, TC + 1):
  print("#{} {}".format(i, solution(readline())))
