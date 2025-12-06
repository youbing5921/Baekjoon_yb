def solution(sizes):
    answer = 0
    max_w = max_h = 0
    for elt in sizes:
        w = elt[0]
        h = elt[1]
        if w < h: # 항상 가로가 더 길게 회전
            w, h = h, w
        if w > max_w:
            max_w = w
        if h > max_h:
            max_h = h
    answer = max_w * max_h
    return answer