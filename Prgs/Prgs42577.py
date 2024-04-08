# 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# 접두어 찾기.
# phone_book 목록을 순회하며 (0 ~ size - 1), 
# phone_book에 있는 다른 요소와 비교. 
# 앞에서부터 비교하려면 ... 119, 11999 와 같이 만들어야 할듯 (정렬)
# 효율성을 테스트하는 부분이 있는데... startswith를 써도 될지 잘 모르겠음. startswith -> O(NM) 걸릴듯.
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
      if phone_book[i + 1].startswith(phone_book[i]):
        return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))

def solution2(phone_book):
  map = dict(zip(phone_book, range(len(phone_book))))
  for i in range(len(phone_book)):
     for j in range(len(phone_book[i])):
        if map.get(phone_book[i][0:j]) != None:
           return False
  return True

print(solution2(["119", "97674223", "1195524421"])) # expect false
print(solution2(["123","456","789"])) # expect true
print(solution2(["12","123","1235","567","88"])) # expect false

def solution3(phone_book):
  hset = set(phone_book)
  for i in range(len(phone_book)):
     for j in range(len(phone_book[i])):
        if phone_book[i][0:j] in hset:
           return False
  return True

print(solution3(["119", "97674223", "1195524421"])) # expect false
print(solution3(["123","456","789"])) # expect true
print(solution3(["12","123","1235","567","88"])) # expect false