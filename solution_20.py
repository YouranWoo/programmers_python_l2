# https://school.programmers.co.kr/learn/courses/30/lessons/70129
# 이진 변환 반복하기

def solution(s): 
    num_trans = 0
    num_zeros = 0
    while s != "1":
        new_s = s.replace("0", "")
        num_zeros += len(s) - len(new_s)
        s = bin(len(new_s))[2:]
        num_trans += 1
        
    return [num_trans, num_zeros]