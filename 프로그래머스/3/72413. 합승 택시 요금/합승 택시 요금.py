from collections import defaultdict
import heapq
def solution(n, s, a, b, fares):
    answer = []
    # 1. 그래프 구현
    graph = defaultdict(list)
    for start, end, cost in fares:
        graph[start].append((cost, end))
        graph[end].append((cost, start))
    
    # 2. 다익스트라 함수 정의
    def dijkstra(start):
        costs = {}
        pq = []
        heapq.heappush(pq, (0, start))
        
        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            if cur_node not in costs:
                costs[cur_node] = cur_cost
                for cost, next_node in graph[cur_node]:
                    next_cost = cost + cur_cost
                    heapq.heappush(pq, (next_cost, next_node))
        
        return costs
    
    # 3. 경우의 수 계산 : 모든 지점들이 중간지점이라 생각하고 그 중간지점에서 다익스트라를 한 번 더 적용
    costs_s = dijkstra(s)
    for node in costs_s: # node가 중간지점
        costs_n = dijkstra(node) # 중간지점에서 다익스트라 적용
        s_n = costs_s[node]
        n_a = costs_n[a]
        n_b = costs_n[b]
        answer.append(s_n + n_a + n_b)
    
    return min(answer)