# https://school.programmers.co.kr/learn/courses/30/lessons/131127
# 할인 행사

from collections import Counter

def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9): # (len(discount)-10) + 1
        discount_dict = dict(Counter(discount[i:i+10]))
        flag = True
        for j in range(len(want)):
            if not (want[j] in discount_dict.keys() and discount_dict[want[j]] >= number[j]):
                flag = False
                break
        if flag == True: 
            answer += 1
    return answer