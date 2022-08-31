# https://school.programmers.co.kr/learn/courses/30/lessons/67257
# 수식 최대화


from itertools import permutations
import re

def solution(expression):
    
    def compute(num1, num2, compute_sign):
        num1, num2 = int(float(num1)), int(float(num2))
        if compute_sign == "+":
            return num1 + num2
        elif compute_sign == "-":
            return num1 - num2
        elif compute_sign == "*":
            return num1 * num2

    numbers = re.split('[+,\-,*]', expression)
    operators = re.split('[0-9]+', expression)[1:-1]
    operator_set = list(set(operators))
    numops = []
    for i in range(len(numbers)):
        numops.append(int(numbers[i]))
        if i < len(operators):
            numops.append(operators[i])
    
    answer = 0
    for ops in permutations(operator_set, len(operator_set)):
        for_compute = numops[:]
        for op in ops:
            while op in for_compute and len(for_compute) > 1:
                idx = for_compute.index(op)
                new_num = compute(for_compute[idx-1], for_compute[idx+1], for_compute[idx])     
                del for_compute[idx+1]
                del for_compute[idx]
                del for_compute[idx-1]
                for_compute.insert(idx-1, new_num)
        if abs(for_compute[0]) > answer :
            answer = abs(for_compute[0])
            
    return answer