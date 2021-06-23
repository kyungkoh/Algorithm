#210623

def solution(dirs):
    answer = 1
    x,y = 0,0
    
    dic = set()
    
    
    for d in dirs :
        if d == 'L':
            nextx = x-1
            nexty = y
            if -5<=nextx<=5 and -5<=nexty<=5:
                dic.add((x,y,nextx,nexty))
                dic.add((nextx,nexty,x,y))
                x = nextx
                y = nexty
        elif d == 'R':
            nextx = x+1
            nexty = y
            if -5<=nextx<=5 and -5<=nexty<=5:
                dic.add((x,y,nextx,nexty))
                dic.add((nextx,nexty,x,y))
                x = nextx
                y = nexty
        elif d == 'U':
            nextx = x
            nexty =  y+1
            if -5<=nextx<=5 and -5<=nexty<=5:
                dic.add((x,y,nextx,nexty))
                dic.add((nextx,nexty,x,y))
                x = nextx
                y = nexty
        elif d == 'D':
            nextx = x
            nexty= y-1
            if -5<=nextx<=5 and -5<=nexty<=5:
                    #나중에 함수로 묶기
                dic.add((x,y,nextx,nexty))
                dic.add((nextx,nexty,x,y))
                x = nextx
                y = nexty
                    

    print(list(dic))
    
    #answer = len(dic)//2
    return answer