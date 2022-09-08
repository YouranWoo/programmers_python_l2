# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 올바른 괄호

def solution(s):
    answer = True
    # "("의 수와 ")"의 수가 같아야 함
    # 현재 상태에서 "(" 의 수가 ")"의 수보다 많아야 함
    left = 0
    right = 0
    for br in s:
        if br == "(":
            left += 1
        else: # br == ")"
            right += 1
        if right > left:
            answer = False
            break
    if left != right:
        answer = False
    
    return answer