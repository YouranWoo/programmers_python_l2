from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    orders = [list(ord) for ord in orders]
    
    order_dict = defaultdict(set)
    for i in range(len(orders)):
        for j in range(i+1, len(orders)):
            intersection = list(set(orders[i]) & set(orders[j])) # 교집합
            if len(intersection) >=2:
                for n in range(2, len(intersection)+1):
                    intersection_set = combinations(intersection, n) # 컴비네이션을 활용한 부분집합
                    for ins in intersection_set:
                        order_dict["".join(sorted(list(ins)))].add(i)
                        order_dict["".join(sorted(list(ins)))].add(j)

    answer = []
    for num in course:
        max_order = 0
        candi = []
        for menu in order_dict.keys():
            if len(menu) == num:
                if len(order_dict[menu]) > max_order:
                    max_order = len(order_dict[menu])
                    candi = [menu]
                elif len(order_dict[menu]) == max_order:
                    candi.append(menu)
        answer += candi
    return sorted(answer)