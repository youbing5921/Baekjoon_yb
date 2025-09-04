'''
현재 선택이 다음 선택에 영향을 미치는 경우 백트래킹으로 해결
다른 백트래킹 문제와 달리 탈출 조건이 return이 아닌 exit(0)인 이유
  : return을 사용하게 되면 현재 재귀 함수만 종료됨.
    -> 이전 단계의 재귀로 돌아가서 다른 경우를 탐색함.
    -> 지금 문제는 성립하는 경우 하나를 찾으면 프로그램을 끝내야 하므로 exit(0) 사용
'''

from collections import deque

graph = [list(map(int, input().split())) for _ in range(9)]
blanks = deque()

# 스도쿠에 빈칸이 있는 (행, 열)을 blanks에 저장
for row in range(9):
    for col in range(9):
        if graph[row][col] == 0: # 빈칸이면 추가
            blanks.append((row, col))

def backTracking(cnt):
    global graph

    if cnt == len(blanks): # 종료 조건 : 빈칸을 다 채운 경우
        for row in graph:
            print(*row)
        exit(0)
    
    row, col = blanks[cnt]
    for i in range(1, 10):
        if check(i, row, col): # (row, col) 위치에 숫자 i를 넣어도 되면
            graph[row][col] = i
            backTracking(cnt+1) # 그 다음 빈칸 해결
            graph[row][col] = 0 # 변경사항 복구

def check(num, row, col):
    # 행 조사
    if num in graph[row]:
        return False
    
    # 열 조사
    for roww in graph:
        if roww[col] == num:
            return False
        
    # 33 블럭 조사
    checkRow = (row // 3) * 3
    checkCol = (col // 3) * 3

    for roww in graph[checkRow : checkRow+3]:
        for elt in roww[checkCol : checkCol+3]:
            if elt == num:
                return False

    # 조사 결과 문제 없음.
    return True

backTracking(0)