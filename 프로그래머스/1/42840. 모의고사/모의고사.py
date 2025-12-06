def solution(answers):
    answer = []
    one = list(range(1, 6))
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1 = cnt2 = cnt3 = 0
    
    for i, a in enumerate(answers):
        if one[i%5] == a:
            cnt1 += 1
        if two[i%8] == a:
            cnt2 += 1
        if three[i%10] == a:
            cnt3 += 1
    
    cnt = [cnt1, cnt2, cnt3]
    maxCnt = max(cnt)
    for i, c in enumerate(cnt):
        if c == maxCnt:
            answer.append(i+1)
    
    return answer