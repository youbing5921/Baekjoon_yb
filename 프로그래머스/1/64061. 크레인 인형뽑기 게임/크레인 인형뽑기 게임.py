from collections import deque

def solution(board, moves):
    answer = 0 # 터진 인형의 개수
    board = [list(row) for row in zip(*board)] # 전치 행렬로 전환
    n = len(board)
    dq = deque()
    for i in moves:
        for idx, elt in enumerate(board[i-1]):
            if elt != 0:
                board[i-1][idx] = 0
                
                if len(dq) > 0 and dq[-1] == elt: # 터지기
                    dq.pop()
                    answer += 1
                else: # 큐에 넣기
                    dq.append(elt)
                
                break
                
    return answer * 2