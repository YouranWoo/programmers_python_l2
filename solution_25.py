# https://school.programmers.co.kr/learn/courses/30/lessons/12911
# 다음 큰 숫자


def solution(n):
    n_zero = bin(n)[2:].count("1")
    while True:
        n += 1
        if n_zero == bin(n)[2:].count("1"):
            answer = int(bin(n)[2:], 2)
            break
    
    return answer