# 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

# 입력: 
# progresses: 각 작업의 진도 목록 
# speeds:     각 작업의 개발 속도 목록

# 출력:
# 배포시마다 배포 가능한 수량을 매번 기록한 목록

# 첫번째 접근 방법
# 해시맵 사용
# map = zip(progresses, speeds)
# map을 순회하며 대응하는 speeds를 합산
# 100 이상인 progresses를 발견할 경우 0번째 인덱스부터 100이상인 다른 요소가 더 있는지 검사
# 100이 아닌 요소가 앞 인덱스에 있을 경우 무시
# 모두 100이면 100인 모든 요소를 맵에서 제거. 이 단계의 제거 횟수를 카운팅하여 answer 목록에 추가
# 순회하는 동안 map이 동적으로 변할 수 있기 때문에 좋지 않은 방법인듯 잘못생각했음

# 두번째 접근 방법
# 일단 progress들이 전부 100 이상이 될때까지 전부 다 더한다음 걸린 시간을 체킹하면 되지 않을까?
# 예를들면... 
# progresses가 [93, 30, 55]이고 
# speeds가     [ 1, 30,  5]일때,
# 모든 prgoresses가 100이상이 되었을 때 걸린 시간을 나타내면 다음과 같을 것임
# takenTime =  [ 7,  3,  9] # takenTime은 걸린 시간

# 또한
# progresses가 [95, 90, 99, 99, 80, 99]이고,
# speeds가     [ 1,  1,  1,  1,  1,  1]일때,
# takenTime =  [ 5, 10,  1,  1, 20,  1]

# takenTime을 순회하며,
# 이전 값이 뒷 값보다 크거나 같으면 계속해서 카운트, 조건에서 벗어나는 순간 이 카운트 값을 answer 목록에 기록하고 
# 카운트를 초기화.
import Math

assert [-((100 - p) / -s) for (p, s) in zip([95, 3, 10], [1, 5, 7])] == [7, 3, 9]


# [3,1,1,4,2] => 3
# [1,2,3] => 1ㅇ
[1,2,3,4,5][1:] = [2,3,4,5]


def solution(progresses, speeds):
  answer = []
  taken_times = [-((100 - p) / -s) for (p, s) in zip(progresses, speeds)] # 
  
  def go(taken_times):
    if not taken_times:
      return []

    first = taken_times[0]
    cnt = 1
    for i in taken_times[1:]:
      if first < i:
        break
      cnt += 1

    return [cnt] + go(taken_times[cnt:])
  
  return go(taken_times)

  # # 모든 작업을 배포한다
  
  # while taken_times:
  #   # 가능한 최대 숫자의 작업을 배포한다

  #   # 배포간으한 작업의 숫자(cnt)를 구한다
  #   first = taken_times[0]
  #   cnt = 1
  #   for i in taken_times[1:]:
  #     if first < i:
  #       break
  #     cnt += 1
      
  #   # 실제 배포한다
  #   answer.append(cnt) 
  #   # 배포한 값은 제거한다
  #   # taken_times.splice(0, cnt)
  #   taken_times = taken_times[cnt:]

  # return answer

  # cnt = 1
  # j = 0
  # for i in range(1, len(taken_times)):
  #   if taken_times[j] >= taken_times[i]:
  #     cnt += 1
  #   else: 
  #     j = i
  #     answer.append(cnt)
  #     cnt = 1

  # answer.append(cnt)
print(solution([93, 30, 55], [1, 30, 5])) # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) # [1, 3, 2]
print(solution([95, 95, 95, 95], [4, 3, 2, 1])) #  [2, 1, 1]
print(solution([98, 99, 97, 98], [1, 1, 1, 1])) # [2, 2]
print(solution([1, 95, 95, 95], [99, 1, 1, 1])) # [1, 3]
print(solution([90, 90], [10, 9])) # [1, 1]

# 반례에서 실패.
print(solution([90, 98, 97, 96, 98], [1, 1, 1, 1, 1])) # asis: [2,1,2] tobe: [5] 
# taken_time: [10, 2, 3, 4, 2]

# 두번째 접근 방식으로도 풀릴 거 같긴한데, 현재는 성공 케이스보다 실패 케이스가 많고 당장 떠오르는 해결책이 없음.

