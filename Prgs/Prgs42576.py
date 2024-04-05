# 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# 주의점: 동명이인
# 첫번째 접근법: 해시맵 사용: {key:value} -> {participant.name: participant.size}
# completion에서 완주한 선수를 발견할 때마다 value--
# value가 1이상인 선수를 해시맵에서 검색 후 리턴 
def solution(participant, completion):
     map = { key: participant.count(key) for key in participant}
     for (r) in completion:
         if map[r] > 0:
             map[r] -= 1
     print(map)
    
     for nc in map:
         if map[nc] != 0:
             answer = nc
     return answer
# 효율성 시간 초과
# map 을 만드는데 필요한 시간 O(N^2) 
# completion 탐색시간 O(M)
# map 탐색시간 O(L)
# 토탈: O(N^2 + M + L)

# 두번째 접근법:
# 두 목록을 모두 정렬하고 하나씩 비교.
# 다른게 발견되는 순간 완주못한것으로 판단가능, 다른 것을 리턴
# 또는 "단 한 명의 선수를 제외하고는" -> 이라고 했으므로 마지막 선수 리턴
def solution2(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]

    return participant[-1]
# 왜 효율성 통과?
# O(N log N)을 보장하는 sort
# 비교 


# 출력
result = solution2(["leo", "kiki", "eden"], ["eden", "kiki"])
print(result) # "leo"

# zip 활용
def solution3(participant, completion):
    participant.sort()
    completion.sort()
    
    for c, p in zip(completion, participant):
        if c != p:
            return p
    return participant[-1]

result = solution3(["leo", "kiki", "eden"], ["eden", "kiki"])
print(result) # "leo"