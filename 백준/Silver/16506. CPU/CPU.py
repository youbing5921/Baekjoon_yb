def binary_str(n, digit):
    n = int(n)
    n = bin(n)[2:]
    n = "0" * (digit - len(n)) + n
    return n

opcode_dic = {
    "ADD":     "0000",
    "ADDC":    "0000",
    "SUB":     "0001",
    "SUBC":    "0001",
    "MOV":     "0010",
    "MOVC":    "0010",
    "AND":     "0011",
    "ANDC":    "0011",
    "OR":      "0100",
    "ORC":     "0100",
    "NOT":     "0101",
    "MULT":    "0110",
    "MULTC":   "0110",
    "LSFTL":   "0111",
    "LSFTLC":  "0111",
    "LSFTR":   "1000",
    "LSFTRC":  "1000",
    "ASFTR":   "1001",
    "ASFTRC":  "1001",
    "RL":      "1010",
    "RLC":     "1010",
    "RR":      "1011",
    "RRC":     "1011"
}

n = int(input())
ans = ""

for i in range(n):
    assem = list(input().split())

    # 0~4
    ans += opcode_dic[assem[0]]
    if assem[0][-1] == "C":
        ans += "1"
    else:
        ans += "0"
    # 5
    ans += "0"
    # 6~8
    ans += binary_str(assem[1], 3)
    # 9~11
    ans += binary_str(assem[2], 3)
    # 12~15
    if ans[4] == "0":
        ans += binary_str(assem[3], 3) + "0"
    else:
        ans += binary_str(assem[3], 4)

    print(ans)
    ans = ""