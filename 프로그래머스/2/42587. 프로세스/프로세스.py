from collections import deque

def solution(priorities, location):
    q = deque([(p, i) for i, p in enumerate(priorities)])
    order = 0

    while q:
        pri, idx = q.popleft()

        if any(pri < other for other, _ in q):
            q.append((pri, idx))
        else:
            order += 1
            if idx == location:
                return order