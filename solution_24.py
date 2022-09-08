# https://school.programmers.co.kr/learn/courses/30/lessons/12945
# 피보나치 수

def solution(n):
    answer = 0
    
    fn_2 = 0
    fn_1 = 1
    for i in range(2, n+1):
        fn = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = fn
    
    return fn % 1234567