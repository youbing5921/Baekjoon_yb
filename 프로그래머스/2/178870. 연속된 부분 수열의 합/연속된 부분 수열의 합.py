def solution(sequence, k):
    answer = []
    i = j = len(sequence) - 1
    sum = sequence[i]
    
    while i >= 0:
        if sum == k:
            if sequence[i] == sequence[j]:  
                while i > 0 and sequence[i-1] == sequence[i]:
                    i -= 1
                    j -= 1
            break
        elif sum > k:
            sum -= sequence[j]
            j -= 1
        else:
            i -= 1
            sum += sequence[i]
    
    answer = [i, j]
    return answer