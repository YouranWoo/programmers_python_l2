# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 구명보트

def solution(people, limit):
    
    people.sort()
    answer = len(people)
    start = 0
    end = len(people) - 1
    while start < end:
        if people[start] + people[end] <= limit:
            answer -= 1
            start += 1
            end -= 1
        else: # people[start] + people[end] > limit
            end -= 1

    return answer