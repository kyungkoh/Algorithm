#0902 
#정규 표현식 & 구현문제 
#String으로 풀려고 했엇는데, 어림도 없는 짓이었다.. 정규 표현식 어려워.. 

import re

def solution(word, pages):
    answer = 0
    
    word = word.lower()
    
    webpage = []
    webpageName = []
    webpageGraph = {}
    
    for page in pages: 
        url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
        basicScore = 0
        for f in re.findall(r'[a-zA-Z]+',page.lower()):
            if f == word:
                basicScore+=1
        exiosLink = re.findall('<a href="(https://[\S]*)"',page)
        
        for link in exiosLink:
            if link not in webpageGraph.keys():
                webpageGraph[link] = [url]
            else:
                webpageGraph[link].append(url)
        
        webpageName.append(url)
        webpage.append([url,basicScore,len(exiosLink)]) # 내가 가진 외부 링크 수
    
    maxValue = 0
    result = 0 
    
    for i in range(len(webpage)):
        url = webpage[i][0]
        score = webpage[i][1]
        
        if url in webpageGraph.keys():
            for link in webpageGraph[url]:
                a,b,c = webpage[webpageName.index(link)]
                score += (b/c)
    
        if maxValue < score:
            maxValue = score
            result = i
        
    return result