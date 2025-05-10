s = input()
vowel = ['a', 'e', 'i', 'o', 'u']

while s != "end":
    cond1 = False
    cond2 = True
    cond3 = True
    for idx, elt in enumerate(s):
        if elt in vowel:
            cond1 = True
        
        if idx < len(s) - 2:
            if elt in vowel and s[idx+1] in vowel and s[idx+2] in vowel:
                cond2 = False
                break
            elif elt not in vowel and s[idx+1] not in vowel and s[idx+2] not in vowel:
                cond2 = False
                break

        if elt not in ['e', 'o'] and idx < len(s) -  1 and s[idx+1] == elt:
            cond3 = False
            break
    
    if cond1 and cond2 and cond3:
        print("<%s> is acceptable." % s)
    else:
        print("<%s> is not acceptable." % s)
    
    s = input()
            

