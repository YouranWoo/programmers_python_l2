# https://school.programmers.co.kr/learn/courses/30/lessons/81302?language=python3
# 거리두기 확인하기

#맨허튼 거리 : abs(x1-x2) + abs(y1-y2) 
from itertools import combinations

def solution(places):
    answer = []
    for place in places:
        answer_part = 1
        place_list = [list(line) for line in place]
        # P 위치 기록
        p_loc = []
        for i in range(5):
            for j in range(5):
                if place_list[i][j] == "P":
                    p_loc.append((i, j))
        # P 사이 거리두기 확인
        for (p1_loc, p2_loc) in combinations(p_loc, 2):
            if abs(p1_loc[0]-p2_loc[0]) + abs(p1_loc[1]-p2_loc[1]) == 1:
                answer_part = 0
                break
            elif (abs(p1_loc[0]-p2_loc[0]) == 1) and (abs(p1_loc[1]-p2_loc[1]) == 1):
                if not (place_list[p1_loc[0]][p2_loc[1]] == "X" and place_list[p2_loc[0]][p1_loc[1]] == "X"):
                    answer_part = 0
                    break
            elif (abs(p1_loc[0]-p2_loc[0]) == 2) and (abs(p1_loc[1]-p2_loc[1]) == 0):
                if not place_list[int((p1_loc[0]+p2_loc[0])/2)][p2_loc[1]] == "X":
                    answer_part = 0
                    break
            elif (abs(p1_loc[0]-p2_loc[0]) == 0) and (abs(p1_loc[1]-p2_loc[1]) == 2):
                if not place_list[p2_loc[0]][int((p1_loc[1]+p2_loc[1])/2)] == "X":
                    answer_part = 0
                    break
        answer.append(answer_part)
        
    return answer