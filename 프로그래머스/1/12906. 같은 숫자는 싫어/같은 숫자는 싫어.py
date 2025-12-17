def solution(arr):
    answer = [arr[0]]
    curr = arr[0]
    for elt in arr[1:]:
        if curr != elt:
            answer.append(elt)
            curr = elt
    return answer