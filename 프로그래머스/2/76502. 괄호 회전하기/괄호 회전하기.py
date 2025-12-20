def solution(s):
    def check(s):
        stack = []
        for ss in s:
            if ss in ['[', '(', '{']:
                stack.append(ss)
            else:
                if len(stack) == 0:
                    return False
                if ss == ']' and stack.pop() != '[':
                        return False
                if ss == ')' and stack.pop() != '(':
                        return False
                if ss == '}' and stack.pop() != '{':
                        return False
                
        return len(stack) == 0

    answer = 0
    n = len(s)
    s = list(s)
    if n % 2: # n이 홀수면 항상 성립 X
        return 0
    
    for i in range(n):
        if check(s):
            answer += 1
        s.append(s.pop(0))
        
    return answer

