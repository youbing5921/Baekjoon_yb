lst = []
for _ in range(9):
    lst.append(int(input()))
total = sum(lst)
done = False
lst.sort()

for i in range(8):
    for j in range(i+1, 9):
        if(total - lst[i] - lst[j] == 100):
            lst.pop(j)
            lst.pop(i)
            done = True
            break
    if(done): break

print(*lst)