# 스택에 있는 게 본인보다 작거나 같으면 스택에 추가
# 스택에 있는 게 본인보다 크면 주식이 떨어지는 거니까 그 가격이 있던 인덱스 자리에 (지금까지의 시간(현재인덱스) - 그 가격의 인덱스)를 저장
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = [] # [(가격, 인덱스)]
    
    for i, p in enumerate(prices):
        if not stack or stack[-1][0] <= p: # 스택에 넣기
            stack.append((p, i))
        else: # 스택에서 빼기
            while stack:
                prev_p, prev_i = stack.pop()
                if prev_p > p:
                    answer[prev_i] = i - prev_i
                else:
                    stack.append((prev_p, prev_i))
                    break
            stack.append((p, i))
    
    while stack:
        p, i = stack.pop()
        answer[i] = n - i - 1
        
    return answer