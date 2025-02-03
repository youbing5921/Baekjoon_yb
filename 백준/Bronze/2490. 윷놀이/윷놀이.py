for _ in range(3):
    lst = list(map(int, input().split()))
    a = sum(lst)
    if a > 2: # 도, 모
        if a == 3: # 도
            print("A")
        else: # 모
            print("E")
    else:
        if a == 2: # 개
            print("B")
        elif a == 1: # 걸
            print("C")
        else: # 윷
            print("D")