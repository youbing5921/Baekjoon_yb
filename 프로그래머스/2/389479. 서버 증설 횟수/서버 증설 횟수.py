'''
리스트를 사용해서 증설된 서버의 지속시간을 표현
이용자 수가 (증설된 서버의 수 + 1) * m 이상이면 증설 필요
-> ceil(이용자수 / m)을 하면 필요한 서버의 수가 나옴
증설 횟수 = answer
현재 증설된 서버의 수 = server
'''        
def solution(players, m, k):
    answer = 0
    n = len(players)
    server = [0] * n
    
    for time in range(n):
        p = players[time]
        s = server[time]
        if p >= (s+1) * m: # 서버 증설 필요
            need = p // m - s
            answer += need
            for kk in range(k):
                if time + kk < n:
                    server[time+kk] += need
                else:
                    break
            
    return answer