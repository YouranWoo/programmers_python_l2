# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# 귤 고르기

from collections import Counter

def solution(n, tangerine):
    counter = Counter(tangerine)
    counter_list = sorted([(k, counter[k]) for k in counter.keys()], key=lambda x:-x[1])
    
    answer = 0
    s = 0
    for (k, v) in counter_list:
        s += v
        answer += 1
        if s >= n:
            break
    
    return answer