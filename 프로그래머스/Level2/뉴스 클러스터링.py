#0714
from collections import Counter
def solution(str1, str2):
    answer = 0
    
    str1 = str1.upper()
    str2 = str2.upper()
    
    arr1=[]
    arr2=[]
    plus = []
    same = []
    
    similiar = 0
    
    for i in range(len(str1)-1):
        temp = str1[i:i+2]
        if temp.isalpha():
            arr1.append(temp)
            
    for i in range(len(str2)-1):
        temp = str2[i:i+2]
        if temp.isalpha():
            arr2.append(temp)
    
    union = list((Counter(arr1)|Counter(arr2)).elements())
    intersection = list((Counter(arr1)&Counter(arr2)).elements())
    
    
    if len(union) == 0 :
        return 65536
    
    return int(len(intersection)/len(union)*65536)