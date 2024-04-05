# 체육복
# https://school.programmers.co.kr/learn/courses/30/lessons/42862
# python 

# 체육복 도난. 여벌 체육복이 있는 학생이 체육복 대여 가능.
# 단, 바로 앞 혹은 뒤 번호의 학생에게만 체육복을 빌려줄 수 있음.
# 전체 학생 수 n
# 체육복 도난당한 학생들의 번호가 담긴 배열 lost
# 여벌 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
# 체육수업을 들을 수 있는 학생의 최댓값을 return

# 제한 사항
# 전체 학생 수는 2 ~ 30
# 도난당한 학생 수는 1 ~ n, 중복 없음
# 여벌 체육복 학생 수는 1 ~ n, 중복 없음
# 여벌 체육복 학생이 도난당한 경우도 있음
# 여벌 체육복 학생은 체육복을 하나만 도난당했다고 가정한다. 
# 단, 남은 체육복이 없어서 체육복을 빌려줄 수 없음.

# 입출력 예
# n = 5, lost = [2, 4], reserve = [1, 3, 5] -> 5
# n = 5, lost = [2, 4], reserve = [3] -> 4

# 첫번째 접근방법
# n 만큼의 배열 a 생성, array.fill(1). 
# lost 만큼 돌면서 lost 값에 해당하는 a 배열의 인덱스 값을 0으로 만든다. 
# 그뒤 reserve 만큼 돌면서, reserver값에 해당하는 a배열의 인덱스 값을 2로 변경한다.

# 주의할점. 여별 체육복을 가져온 학생이 도난당했다는 사실은, 
# lost [1, 3] reserve [3, 4, 5] 일수도 있다는 말.
# 합칠때 lost에도 있고 reserve에도 있는 숫자는 1로 기록해야한다.
# 먼저 lost를 순회하면서 reserve에 해당 값이 있는지 확인하자. 있다면, 
# 리스트에 따로 기록해둔뒤, reserve만큼 돌때 해당 리스트를 뒤져서 1로 변경한다.
# 그뒤 리스트에서는 값을 제거한다.
# 합친 배열 a을 0 ~ N 순회하며 2을 만날때마다 이전 인덱스에 해당하는 값이 0이면 1로 변경 및 해당 인덱스 값 2를 1로 변경
# 이전 인덱스에 해당하는 값이 1이면 다음 인덱스에 해당하는 값이 0인지 확인, 0이면 그 값을 1로 변경, 해당인덱스 값 2를 1로 변경.

# 주의할점2: ArrayOutOfIndex
# 그 뒤에 a 배열을 순회하며 1인 값을 카운팅한뒤 그 카운팅값을 리턴한다.

def solution(n, lost, reserve):
    a = [1] * (n + 1) # 0번째 인덱스를 사용하지 않을 것임
    stset = set(lost) & set(reserve)  # 도난당하고 여벌이 있는 학생 목록

    for e in lost:
        a[e] = 0
    for e in reserve:
        if e not in stset:
            a[e] = 2
        else:
            a[e] = 1

    for i in range(1, len(a)):
        if a[i] == 2:
            if i > 1 and a[i - 1] == 0:
                a[i - 1] = 1
                a[i] = 1
            elif i < len(a) - 1 and a[i] == 2 and a[i + 1] == 0:
                a[i + 1] = 1
                a[i] = 1

    return a.count(1) + a.count(2) - 1  # 0번째 인덱스 제외를 위한 -1
  
print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))