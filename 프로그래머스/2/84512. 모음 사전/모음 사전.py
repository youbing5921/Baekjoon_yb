def solution(word):
    answer = 0
    
    def backtracking(cur_word):
        nonlocal answer
        if cur_word == word: # 단어를 찾음
            return True
        if len(cur_word) == 5: # 단어를 찾지 못하고 5칸이 다 참
            return False

        for elt in ["A", "E", "I", "O", "U"]:
            answer += 1
            if backtracking(cur_word + elt): # 단어를 찾으면 상위로 전달해서 종료시킴.
                return True
        
    backtracking("")
    return answer