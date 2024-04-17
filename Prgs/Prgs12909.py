# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909


def solution(s): # s: "()()", "(())()" 등의 input 값 주입
  stack = Stack() # 파이썬은 별도의 스택을 구현하고 있지 않으므로 직접 구현한다. 

  for e in s: # 괄호 문자열 순회. (, ), (, ) 순으로 반복됨
    if (e == '('): # 열린괄호면 스택에 추가 
      stack.add(e)
    else: # 닫힌괄호면 스택에서 제거
      if (stack.size() < 1): 
        return False # 닫힌 괄호가 더 많으면 짝짓는것이 실패했다는 말이므로 False 반환
      else: # 열린괄호가 하나라도 있을때만 제거
        stack.remove()

  return stack.size() < 1 # ((( 와 같이 남아있으면 짝짓기 실패했으므로 False, size가 0이면 짝지어졌으므로 True 리턴

class Stack():
  def __init__(self):
    self.arr = []
    self.pointer = 0

  def add(self, s):
    self.arr.append(s)
    self.pointer += 1 # size를 찾기 위한 pointer 변경

  def remove(self):
    self.arr.pop()
    self.pointer -= 1
  
  def size(self):
    return len(self.arr)

  def __repr__(self):
      return f"{self.arr}"

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))