# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 기능 개발

from collections import deque 

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses and speeds:
        # 1 day
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
        num = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            num += 1
        if num > 0 :
            answer.append(num)
    
    return answer