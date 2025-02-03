res = []

for i in range(1, 6):
    agent = input()
    len_agent = len(agent)
    for j in range(len_agent - 2):
        if agent[j] == "F" and agent[j+1] == "B" and agent[j+2] == "I":
            res.append(i)
            break

if res != []:
    print(*res)
else:
    print("HE GOT AWAY!")