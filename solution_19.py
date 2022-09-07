# https://school.programmers.co.kr/learn/courses/30/lessons/12951
# JadenCase 문자열 만들기

def solution(s):
    s_list = [ss[0].upper() + ss[1:].lower() if len(ss) > 1 else ss.upper() for ss in s.split(" ")]
    return " ".join(s_list)