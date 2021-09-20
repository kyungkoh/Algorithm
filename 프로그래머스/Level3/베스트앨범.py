#0920 
#defaultdictionary, sort


from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    plays_in_genres = defaultdict(int)
    song_in_genres = defaultdict(list)
    
    for i in range(len(genres)):
        plays_in_genres[genres[i]] += plays[i]
        song_in_genres[genres[i]].append((i,plays[i]))
    
    print(plays_in_genres)
    plays_in_genres = sorted(plays_in_genres.items(),key = lambda x:x[1], reverse = True)
    
    for i in song_in_genres:
        song_in_genres[i] = sorted(song_in_genres[i], key = lambda x:x[1],reverse = True)[:2]
    
    print(song_in_genres)
    
    while len(plays_in_genres) > 0:
        genre = plays_in_genres.pop(0)
        for t in song_in_genres:
            if t == genre[0]:
                if len(song_in_genres[t])>1:
                    answer.append(song_in_genres[t][0][0])
                    answer.append(song_in_genres[t][1][0])
                else:
                    answer.append(song_in_genres[t][0][0])
    
    #print(plays_in_genres)
    
    return answer