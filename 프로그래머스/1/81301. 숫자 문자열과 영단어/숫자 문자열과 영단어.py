def solution(s):
    answer = ""
    dic = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    
    idx = 0
    word = ""
    while idx < len(s):
        if "0" <= s[idx] <= "9": # 숫자이면 바로 저장
            answer += s[idx]
        else:
            word += s[idx]
            if word in dic:
                answer += str(dic[word])
                word = ""
        idx += 1

    return int(answer)