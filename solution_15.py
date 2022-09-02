# https://school.programmers.co.kr/learn/courses/30/lessons/64065
# 튜플

def solution(s):
    s_list = [x.replace("{","").replace("}", "").split(",") for x in s.split("},{")]
    s_list.sort(key=lambda x : len(x))
    
    answer = []
    for lst in s_list:
        for n in lst:
            if int(n) not in answer:
                answer.append(int(n))
    
    return tuple(answer)