stmts = list(input().split())
basic = stmts.pop(0) # 기본 변수명

for i in range(len(stmts)):
    ans = basic
    stmt = stmts[i]
    stmt = stmt[:-1] # 쉼표 혹은 세미콜론 제거

    while stmt:
        # 변수 선언문을 역순으로 접근한다.
        if stmt[-1].isalpha(): # 종료 조건 : 변수 이름이 나왔을 때
            ans += " " + stmt + ";"
            stmt = ""
        elif stmt[-1] == "]": # 배열인 경우
            ans += "[]"
            stmt = stmt[:-2]
        else: # 포인터와 참조인 경우
            ans += stmt[-1]
            stmt = stmt[:-1]
    print(ans)