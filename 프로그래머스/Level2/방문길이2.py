#210623_2

def solution(dirs):
    answer = 1
    x,y = 0,0
    command = {'U':(0,1), 'D': (0,-1), 'L':(-1,0), 'R':(1,0)}
    dic = set()
    
    
    for d in dirs :
        nextx, nexty = x+command[d][0], y+command[d][1]
        if -5<=nextx<=5 and -5<=nexty<=5:
            dic.add((nextx,nexty,x,y))
            dic.add((x,y,nextx,nexty))
            x,y = nextx,nexty
            
                    

    #print(list(dic))
    answer = len(dic)//2
    return answer