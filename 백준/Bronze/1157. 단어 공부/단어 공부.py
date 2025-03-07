dictionary = {}
ans = []
maximum = 0

n = input().upper()

for elt in n:
    if elt not in dictionary:
        dictionary[elt] = 1
    else:
        dictionary[elt] += 1

for k, v in dictionary.items():
    if maximum < v:
        ans = [k]
        maximum = v
    elif maximum == v:
        ans.append(k)

if len(ans) == 1:
    print(ans[0])
else:
    print("?")