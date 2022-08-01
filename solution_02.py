# https://school.programmers.co.kr/learn/courses/30/lessons/42888
# 오픈채팅방

def solution(record):
    id_list = {}
    for r in record:
        func = r.split(" ")[0]
        if func != "Leave":
            id_list[r.split(" ")[1]] = r.split(" ")[2]
    
    answer = []
    for r in record:
        func = r.split(" ")[0]
        if func == "Enter":
            answer.append("{}님이 들어왔습니다.".format(id_list[r.split(" ")[1]]))
        elif func == "Leave":
            answer.append("{}님이 나갔습니다.".format(id_list[r.split(" ")[1]]))
    return answer