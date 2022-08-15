# https://school.programmers.co.kr/learn/courses/30/lessons/17677
# 뉴스 클러스터링

def solution(str1, str2):
    # 다중집합 원소 생성
    str1_list = []
    str2_list = []
    
    for i in range(len(str1)-1):
        st = str1[i]+str1[i+1]
        if st.isalpha():
            str1_list.append(st.lower())
    for i in range(len(str2)-1):
        st = str2[i]+str2[i+1]
        if st.isalpha():
            str2_list.append(st.lower())
    
    if (not str1_list) and (not str2_list):
        return 1 * 65536
    
    # (다중집합) 자카드 유사도 구하기    
    answer = 0
    intersection = list(set(str1_list) & set(str2_list))
    union = list(set(str1_list) | set(str2_list))
    
    hap = 0
    kyo = 0
    for ele in union:
        hap += max(str1_list.count(ele), str2_list.count(ele))
        if ele in intersection:
            kyo += min(str1_list.count(ele), str2_list.count(ele))
    
    return int((kyo / hap) * 65536)