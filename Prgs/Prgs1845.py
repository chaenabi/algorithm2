# 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

# can take N마리 중 N/2마리 
# 예시
# [3, 1, 2, 3] 일 때 1번:1마리, 2번:1마리, 3번:2마리 존재.
# 4마리 중 2마리를 고르는 방법, 경우의 수
# 3 1
# 3 2
# 3 3
# 1 2
# 1 3
# 2 3
# 최대한 다양한 폰켓몬을 고르는 방법을 찾은 뒤 그때의 폰켓몬 수량을 리턴.
# def solution(nums):
#     answer = 0
#     map = {key: nums.count(key) for key in nums}
#     length = len(map)
#     if length % 2 == 0:
#         itercnt = length // 2
#     else:
#         itercnt = length // 2 + 1
#     keys = list(map.keys())
#     for _ in range(itercnt):
#         for key in keys:
#             if map[key] > 0:
#                map[key] -= 1
#                print(map)
#                answer += 1
#     return answer

# 첫번째 접근 시도 방식
# 해시 사용 또는 카운팅 배열 고려해볼 수 있지 않을까.
# 입력이 [3, 1, 2, 3] 일경우.
# key:value  --> [1:1, 2:1, 3:1]
# 한번씩 순회하며, 각요소의 value가 0이 될때까지 value를 -1, answer를 +1
# 각 순회횟수는 홀수의 경우 맵의 길이/2 + 1 
# 짝수의 경우 맵의 길이/2 만큼.

# 두번째 접근 시도
# 중복되지않는 폰켓몬 전체 갯수를 획득
# 획득가능한 폰켓몬의 갯수가 len / 2 보다 적다면? 예시 [1,1,1,1,1,2] -> len(6), unique(2) -> unique 리턴.
# 획득가능한 폰켓몬의 갯수가 len / 2 보다 많다면? len / 2 리턴.
def solution(nums):
    total_unique_phonecatmons = len(set(nums))
    max_select = len(nums) // 2  
    return min(max_select, total_unique_phonecatmons)


# 출력
result = solution([3, 1, 2, 3])
print(result) # 2