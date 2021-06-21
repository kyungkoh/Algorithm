def solution(record):
    answer = []
    usr = {}
    
    for msg in record : 
        if msg.split(' ')[0] == 'Enter' or msg.split(' ')[0] == 'Change':
            usr[msg.split(' ')[1]] = msg.split(' ')[2]
            
    for msg in record : 
        if msg.split(' ')[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(usr[msg.split(' ')[1]]))
        elif msg.split(' ')[0] == 'Leave': 
            answer.append("{}님이 나갔습니다.".format(usr[msg.split(' ')[1]]))
            
    
    return answer