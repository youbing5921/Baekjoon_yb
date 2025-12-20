import math

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    day = [0] * n # 각 기능이 완료되는데 걸리는 일자
    work = 0
    
    for i in range(n): # day 사전 계산
        day[i] = math.ceil((100 - progresses[i]) / speeds[i])
    
    while len(day) > 0:
        d = day.pop(0)
        work = 1
        while len(day) > 0 and d >= day[0]:
            day.pop(0)
            work += 1
        answer.append(work)
    
    return answer