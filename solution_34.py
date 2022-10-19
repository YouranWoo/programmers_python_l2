# https://school.programmers.co.kr/learn/courses/30/lessons/42839s
# 소수 찾기

from itertools import permutations
import math

def solution(numbers):
    
    def is_prime(x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    
    number_list = list(numbers)
    prime_numbers = []
    check_numbers = []
    for i in range(1, len(number_list)+1):
        for nums in permutations(number_list, i):
            x = int("".join(nums))
            if x > 1 and x not in check_numbers and is_prime(x):
                check_numbers.append(x)
                prime_numbers.append(x)
                
    return len(prime_numbers)