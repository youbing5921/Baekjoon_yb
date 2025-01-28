a = input()
aa = ""

for elt in a: 
    elt = ord(elt)
    if(elt < 97): # 대문자
        aa += chr(elt + 32)
    else:
        aa += chr(elt - 32)
print(aa)