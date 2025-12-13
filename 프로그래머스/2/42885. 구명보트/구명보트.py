def solution(people, limit):
    answer = 0
    people.sort()
    l = 0
    r = len(people) - 1
    weight = 0
    
    while l <= r:
        weight += people[r]
        if weight + people[l] <= limit:
            l += 1
        weight = 0
        r -= 1
        answer += 1
            
    return answer