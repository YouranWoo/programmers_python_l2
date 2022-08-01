# https://school.programmers.co.kr/learn/courses/30/lessons/60057
# 문자열 압축

def solution(s):
    length = len(s)
    answer = length
    
    for i in range(1, length+1):
        cut_list = []
        for j in range(length//i+1):
            if j < length//i:
                cut_list.append(s[i*j:i*(j+1)])
            elif j == length//i and length%i != 0:
                cut_list.append(s[i*j:i*j+length%i])
        
        short = ""
        num = 0
        for i in range(len(cut_list)):
            if i==len(cut_list)-1 or cut_list[i] != cut_list[i+1]:
                num += 1
                if num > 1:
                    short += str(num)
                short += cut_list[i]
                num = 0
            else: #cut_list[i] == cut_list[i+1]
                num += 1

        if len(short) < answer:
            answer = len(short)
            
    return answer