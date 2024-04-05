# 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# 접두어 찾기.
# phone_book 목록을 순회하며 (0 ~ size - 1), 
# phone_book에 있는 다른 요소와 비교. 
# 앞에서부터 비교하려면 ... 119, 11999 와 같이 만들어야 할듯 (정렬)
# 효율성을 테스트하는 부분이 있는데... startswith를 써도 될지 잘 모르겠음. startswith -> O(NM) 걸릴듯.
def solution(phone_book):
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book) - 1):
      if phone_book[i + 1].startswith(phone_book[i]):
        return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))