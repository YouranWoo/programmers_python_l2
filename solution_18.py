# https://school.programmers.co.kr/learn/courses/30/lessons/12939
# 최댓값과 최솟값

def solution(s):
    s_list = [int(n) for n in s.split(" ")]
    s_list.sort()
    return "{} {}".format(str(s_list[0]), str(s_list[-1]))