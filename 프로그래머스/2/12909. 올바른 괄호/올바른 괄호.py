def solution(s):
    answer = True
    stack = []
    for elt in s:
        if elt == '(':
            stack.append('(')
        else:
            if len(stack) == 0: # 맞는 열린 괄호가 없는 경우
                return False
            else:
                stack.pop()
    
    return len(stack) == 0