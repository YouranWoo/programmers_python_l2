# https://school.programmers.co.kr/learn/courses/30/lessons/42747
# H-Index

def solution(citations):
    answer = 0
    for i in range(len(citations), -1, -1):
        if i <= len([p for p in citations if p >= i]) and i >= len([p for p in citations if p > i]):
            answer = i
            break    
    
    return answer