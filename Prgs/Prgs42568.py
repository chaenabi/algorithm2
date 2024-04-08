# 의상
# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# python

# 코니 -> 매일 다른 옷을 조합하여 입는다.

# 코니가 가진 옷이 다음과 같을때:
# 얼굴	동그란 안경, 검정 선글라스
# 상의	파란색 티셔츠
# 하의	청바지
# 겉옷	긴 코트

# 1일차에 동그란 안경을 꼈다면 2일차에는 다른 옷을 입어야 한다.

# 첫번째 접근방법
# 조합 가능한 최대 경우의 수를 리턴해야하는 것으로 보임. 즉 모든 옷을 다 입지 않을 수도 있는 것으로 보임.
# 어짜피 옷 하나만 바꾸면 되기 때문에 겹치는 옷의 종류는 별로 안 중요할듯... 
# 조합의 공식은 n! / r!(n - r)! , n은 value 총 갯수, r은 1 ~ value 갯수

# 위에서 든 예시로 계산하면...
# n = 5 = 동그란 안경 + 검정 선글라스 + 파란색 티셔츠 + 청바지 + 긴 코트 
# r = 1 ~ n
# 계산하면.. answer = (5! / 1!(5 - 1)!) + (5! / 2!(5 - 2)!) + (5! / 3!(5 - 3)!) + (5! / 4!(5 - 4)!) + (5! / 5!(5 - 5)!)
# 의상의 종류가 최대 30개 일수 있으므로 factorial 직접 구현하면 효율성에서 터지겠지만 일단 정답부터 맞추는 걸로.
# clothes의 길이 = n

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def solution(clothes):
  n = len(clothes)
  answer = 0
  for r in range(1, n):
    answer += combination(n, r)
  return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))

# 첫번째 접근방법 실패.
# [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
# 일때 최대 조합은 3이 나와야해서 안됨.. 

# 두번째 접근방법
# 해시맵으로 접근.
# 즉 key: [value, value] 형태로. key는 의상종류 . value는 의상명. 굳이 string 형태로 저장할 필요는 없겠지만.. 
# 총 조합의 수는 [value.count()] * [value.count()] * [value.count()] 단, 각 value.count()에 + 1을 해서 해당 옷종류를 안입는 경우를 추가.
# 코니는 최소 한 개의 의상을 입기 떄문에 안입는 경우, 즉 공집합을 제외해야함 (-1)
def solution2(clothes):
    map = {}
    for cloth in clothes:
        if cloth[1] in map:
            map[cloth[1]] += 1
        else:
            map[cloth[1]] = 1
    cnt = 1
    for key in map:
        cnt *= (map[key] + 1)
    return cnt - 1

print(solution2([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution2([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))

def solution3(clothes):
    map = {}
    for [name, kind] in clothes:
        if kind in map:
            map[name] += 1
        else:
            map[name] = 1
    cnt = 1
    for key in map:
        cnt *= (map[key] + 1)
    return cnt - 1

print(solution3([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution3([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))