# https://school.programmers.co.kr/learn/courses/30/lessons/12949
# 행렬의 곱셈

def solution(arr1, arr2):
    
    answer = []
    len_row1, len_col1, len_col2 = len(arr1), len(arr1[0]), len(arr2[0])
    for i in range(len_row1):
        arr = []
        for k in range(len_col2):
            s = 0
            for j in range(len_col1):
                s += arr1[i][j]*arr2[j][k] 
            arr.append(s)
        answer.append(arr)
                
    return answer
