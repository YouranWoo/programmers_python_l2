# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 위장

from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(int)
    for clth in clothes: 
        clothes_dict[clth[1]] += 1

    for i in list(clothes_dict.values()):
        answer *= i+1
    
    return answer-1