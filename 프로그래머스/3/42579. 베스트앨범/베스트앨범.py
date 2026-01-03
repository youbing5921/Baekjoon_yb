def solution(genres, plays):
    answer = []
    play = {} # genres : sum(plays)
    dic = {} # genres : [(plays[i], i)]
    # 장르별로 (plays, idx) 저장
    for i, g in enumerate(genres):
        if g in dic: # 이미 저장된 장르이면
            play[g] += plays[i]
            dic[g].append((plays[i], i))
        else: # 처음 저장하는 장르이면
            play[g] = plays[i]
            dic[g] = [(plays[i], i)]

    # 값 기준 키 내림차순 정렬
    keys = [k for k, v in sorted(play.items(), key=lambda x: x[1], reverse=True)]
    for k in keys: # 장르별로 많이 재생된 노래 먼저 수록
        playlist = dic[k]
        playlist.sort(key=lambda x: (-x[0], x[1]))
        answer.extend([i for _, i in playlist[:2]])
        
    return answer