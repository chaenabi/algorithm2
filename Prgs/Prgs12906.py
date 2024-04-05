# 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    result = []
    for num in arr:
        if not result or result[-1] != num: 
            result.append(num)
    return result

# 출력
result = solution([1,1,3,3,0,1,1])
print(result) # [1,3,0,1]