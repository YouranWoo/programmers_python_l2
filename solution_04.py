# https://school.programmers.co.kr/learn/courses/30/lessons/12899
# 124 나라의 숫자

def solution(n):
    answer = ''
    d = 3
    
    while n > 0:
        n , mod = divmod(n, d)
        if mod == 1:
            answer = "1" + answer
        elif mod == 2:
            answer = "2" + answer
        else: # mod == 0
            n -= 1
            answer = "4" + answer    
        
    return answer