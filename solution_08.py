# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 짝지어 제거하기

from collections import deque

def solution(s):
    str_li = list(s) # s.split() 아님!! 
    stack = deque()
    answer = 1 #성공
    
    for s in str_li:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
        
    if stack:
       answer = 0
    return answer