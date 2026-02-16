'''
가장 많은 던전을 돌려면 최소 필요 피로도가 높고, 소모 피로도가 낮은 던전을 우선으로 돌아야 함.
-> (실패) 지역 최적 선택이 전체 최적을 보장하지 않기 때문에 그리디가 실패합니다.
-> DFS + 백트래킹으로 모든 순서를 탐색해야 함.
'''
# def solution(k, dungeons):
#     answer = 0
#     dungeons.sort(key=lambda x: (-x[0], x[1]))
#     for d in dungeons:
#         if k >= d[0]: # 현재 피로도보다 최소 피로도가 높으면 탐험 가능
#             k -= d[1]
#             answer += 1
#     return answer

def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
    
    def dfs(cur_k, ans):
        nonlocal answer
        answer = max(answer, ans)
        
        for i, d in enumerate(dungeons):
            if not visited[i] and cur_k >= d[0]: # 아직 방문을 안한 던전이고 탐험할 수 있으면
                visited[i] = True
                dfs(cur_k-d[1], ans+1)
                visited[i] = False
    
    dfs(k, answer)
    return answer