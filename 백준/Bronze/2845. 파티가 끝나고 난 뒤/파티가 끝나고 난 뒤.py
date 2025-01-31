l, p = map(int, input().split())
arti = list(map(int, input().split()))

num = l * p
for elt in arti:
    print(elt - num, end=" ")
