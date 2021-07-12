#0713 

def solution(cacheSize, cities):
    answer = 0
    
    cache = []
    CITY = []
    
    for i in cities:
        CITY.append(i.upper())
        
    
    for city in CITY:
        if city not in cache:
            # cache miss
            if len(cache) < cacheSize:
                cache.append(city)
                answer+=5
            else:
                if cacheSize == 0 : 
                    answer+=5
                else:
                    cache.pop(0)
                    cache.append(city)
                    answer+=5
        #cache hit
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer+=1
            
    
    return answer