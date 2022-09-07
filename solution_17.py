# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 전화번호 목록

def solution(phone_book):
    answer = True
    phone_book.sort()
    for n1, n2 in zip(phone_book, phone_book[1:]):
        if n1 == n2[:len(n1)]:
            answer = False
            break
    return answer