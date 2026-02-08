from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))

    INF = 10**9
    intensity = [INF] * (n + 1)

    gates = set(gates)
    summits = set(summits)

    pq = []

    # 1️⃣ 모든 gate를 시작점으로
    for g in gates:
        intensity[g] = 0
        heapq.heappush(pq, (0, g))

    # 2️⃣ 다익스트라
    while pq:
        cur_intensity, node = heapq.heappop(pq)

        if cur_intensity > intensity[node]:
            continue

        # summit에 도착하면 확장 X
        if node in summits:
            continue

        for next_node, cost in graph[node]:
            new_intensity = max(cur_intensity, cost)
            if new_intensity < intensity[next_node]:
                intensity[next_node] = new_intensity
                heapq.heappush(pq, (new_intensity, next_node))

    # 3️⃣ summit 중 최소 intensity 선택
    answer = [0, INF]
    for s in sorted(summits):
        if intensity[s] < answer[1]:
            answer = [s, intensity[s]]

    return answer

'''
from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    answer = []
    
    graph = defaultdict(list)
    for start, end, cost in paths:
        graph[start].append((cost, end))
        graph[end].append((cost, start))
    
    def dijkstra(start):
        costs = {}
        pq = []
        heapq.heappush(pq, (0, start))
        
        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            if cur_node not in costs:
                costs[cur_node] = cur_cost
                if cur_node not in gates:
                    for cost, next_node in graph[cur_node]:
                        next_cost = max(cost, cur_cost)
                        heapq.heappush(pq, (next_cost, next_node))
    
        return costs
    
    for s in summits:
        costs_s = dijkstra(s)
        for g in gates:
            i = costs_s[g]
            heapq.heappush(answer, (i, s))
    
    i, s = heapq.heappop(answer)
    return [s, i]
'''