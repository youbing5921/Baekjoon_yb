n = int(input())
ans = n # 그룹 단어가 아닌 경우 차감

for _ in range(n):
    array = [] # 나온 알파벳들 저장
    string = list(input())
    while string:
        elt = string.pop()
        if elt not in array: # 처음 나온 알파벳이면
            array.append(elt)
            while string and elt == string[-1]:
                string.pop()
        else: # 이미 앞에서 나온 알파벳이면
            ans -= 1
            break
print(ans)