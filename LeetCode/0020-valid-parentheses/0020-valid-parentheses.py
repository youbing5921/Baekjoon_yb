class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openB = ['(', '{', '[']
        closeB = [')', '}', ']']
        for elt in s:
            for idx, c in enumerate(closeB): # 닫는 괄호인지 확인
                if elt == c:
                    # 그전에 여는 괄호가 없었거나, 맞는 여는 괄호가 아니면 false
                    if len(stack) == 0 or stack.pop() != openB[idx]:
                        return False
                    break
            else: # 여는 괄호이면 스택에 추가
                stack.append(elt)
        return len(stack) == 0