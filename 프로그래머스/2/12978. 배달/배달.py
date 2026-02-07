from collections import defaultdict
import heapq

def solution(N, road, K):
    graph = defaultdict(list)

    # 1. 그래프 생성
    for start, end, cost in road:
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    # 2. 다익스트라
    costs = {}
    pq = []
    heapq.heappush(pq, (0, 1))  # (cost, node)

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if cur_node not in costs:
            costs[cur_node] = cur_cost

            for next_node, cost in graph[cur_node]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_node))

    # 3. 결과 계산
    answer = 0
    for node in range(1, N + 1):
        if node in costs and costs[node] <= K:
            answer += 1

    return answer