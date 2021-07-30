#0731
#Counter 복습을 해도 까먹네.. 꾸준히 반복 할 것!

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for i in course:
        temp = []
        for j in orders:
            combi = combinations(sorted(j),i)
            temp += combi
        counter = Counter(temp)
        print(counter)
        if len(counter) !=0 and max(counter.values())>1:
            answer+=[ ''.join(x) for x in counter if counter[x] == max(counter.values())]
            
    return sorted(answer)