# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 가장 큰 수

def solution(numbers):
    sorted_numbers = sorted([str(n) for n in numbers], key = lambda x : 3*x, reverse=True)
    return str(int("".join(sorted_numbers)))

# 아이디어 참고