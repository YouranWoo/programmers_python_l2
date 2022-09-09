# https://school.programmers.co.kr/learn/courses/30/lessons/92341
# 주차 요금 계산

from collections import defaultdict
import math

def solution(fees, records):
    
    def time_com(str_time):
        hh, mm = map(int, str_time.split(":"))
        return hh * 60 + mm
    
    base_time, base_fee, per_time, per_fee = fees
    
    records_by_car = defaultdict(list)
    for record in records:
        records_by_car[record.split(" ")[1]].append(record)
    
    answer = []
    for car in records_by_car.keys():
        car_fee = [car]
        sum_time = 0
        
        if records_by_car[car][-1][-2:] == "IN": # 마지막 출차 기록이 없는 경우
            records_by_car[car].append("23:59 {} OUT".format(car))
        
        # 누적 시간 계산
        for i in range(int(len(records_by_car[car])/2)): 
            sum_time += time_com(records_by_car[car][2*i+1].split(" ")[0]) - time_com(records_by_car[car][2*i].split(" ")[0])
        
        # 요금 계산
        total_fee = 0
        if sum_time - base_time > 0:
            total_fee += base_fee 
            total_fee += math.ceil((sum_time - base_time) / per_time) * per_fee
        else:
            total_fee += base_fee
        car_fee.append(total_fee)
        answer.append(car_fee)

    return [record[1] for record in sorted(answer, key=lambda x:x[0])]