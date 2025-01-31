# import sys
# sys.stdin = open("TextFile1.txt", "r")

line = input()
result = 0
vowel = ["a", "e", "i", "o", "u"]

while line != "#":
    line = line.lower()
    for elt in line:
        if elt in vowel:
            result += 1
    print(result)
    result = 0
    line = input()
    