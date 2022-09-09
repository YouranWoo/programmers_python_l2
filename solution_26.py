# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 카펫

def solution(brown, yellow):
    
    total = brown + yellow
    answer = []
    for i in range(3, brown):
        if (total % i == 0) and ((i-2) * (int(total/i)-2) == yellow):
            answer.append(i)
            answer.append(int(total/i))
            break
    
    return sorted(answer, reverse=True)