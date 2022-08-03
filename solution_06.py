# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 더 맵게

import heapq

def solution(scv, K):
    l = len(scv)
    heapq.heapify(scv)
    answer = 0
    while len(scv) >= 2: #조건 확인
        if scv[0] < K:
            min1 = heapq.heappop(scv)
            min2 = heapq.heappop(scv)
            heapq.heappush(scv, min1 + 2*min2)
            answer += 1
            if answer == l-1 and scv[0] < K:
                return -1
        else: #scv[0] >= K
            break

    return answer


# refernce 
# python heapq : https://littlefoxdiary.tistory.com/3