# https://school.programmers.co.kr/learn/courses/30/lessons/49994
# 방문 길이

def solution(dirs):
    
    dir_dict = {"U":[0,1], "D":[0,-1], "R":[1, 0], "L":[-1, 0]}
    
    start = [0,0]
    routes = [] # routes의 원소 예시 : [[0, 0], [-1, 0]]
    for d in dirs:
        x, y = start[0] + dir_dict[d][0], start[1] + dir_dict[d][1]
        if  -5 <= x and x <= 5 and  -5 <= y and y <= 5:
            if sorted([start, [x, y]]) not in routes:
                routes.append(sorted([start, [x, y]]))
            start = [x, y]
    
    return len(routes)