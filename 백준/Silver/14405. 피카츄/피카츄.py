a = input()
ans = "YES" # 조건을 달성하지 못하면 NO로 바뀜.

while a:
    if len(a) >= 3 and a[0:3] == "chu":
        a = a[3:]
    elif len(a) >= 2 and a[0:2] in ["pi", "ka"]:
        a = a[2:]
    else: # 피카츄가 발음할 수 없는 글자가 있는 경우
        ans = "NO"
        break

print(ans)