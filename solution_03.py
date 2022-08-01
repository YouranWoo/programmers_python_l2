# https://school.programmers.co.kr/learn/courses/30/lessons/62048
# 멀쩡한 사각형

def solution(w,h):
    
    def gcd(a, b): # 최대공약수
        if b > a:
            a, b = b, a
        while b > 0:
            a, b = b, a % b
        return a
    
    def line(x, w, h):
        return h - (h * x) / w
    
    if w > h:
        w, h = h, w
    g = gcd(w, h)
    n = 0
    for i in range(1, int(w/g)):
        n += int(line(i, int(w/g), int(h/g)))
    mini = (w/g) * (h/g) - 2 * n
    
    return w * h - mini * g


# # 시간 초과 3개
# def solution(w,h):
    
#     def line(x, w, h):
#         return h - (h * x) / w
    
#     half_answer = 0
#     for i in range(1, w):
#         half_answer += int(line(i, w, h))
        
#     return 2 * half_answer


# 시간 초과 1개
# def solution(w,h):
    
#     def gcd(a, b): # 최대공약수
#         while b > 0:
#             a, b = b, a % b
#         return a
    
#     def line(x, w, h):
#         return h - (h * x) / w
    
#     g = gcd(w, h)
#     n = 0
#     for i in range(1, int(w/g)):
#         n += int(line(i, int(w/g), int(h/g)))
#     mini = (w/g) * (h/g) - 2 * n
    
#     return w * h - mini * g