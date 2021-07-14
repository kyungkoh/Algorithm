#0715

def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
        else:
            bin_num = str(format(num,'b'))
            idx = bin_num.rfind('01')
            if idx == -1:
                bin_num = '10'+bin_num[1:]
                answer.append(int(bin_num,2))
            else:
                bin_num = bin_num[:idx]+'10'+bin_num[idx+2:]
                answer.append(int(bin_num,2))
    
    return answer