import math

def is_float(num):
    try:
        a = int(num)
        return True
    except:
        return False

n = int(input())
operation = []
operator = []
length = 0

while length < n:
    a = input()
    if (is_float(a)):
        a = int(a)
        if(len(operator) and (operator[-1] == "*" or operator[-1] == "/")):
            b = operation.pop()
            op = operator.pop()
            if(op == "*"):
                a = b * a
            else:
                a = b // a
        operation.append(a)
        length += 1
    else:
        operator.append(a)

while(len(operator)):
    a = operation.pop(0)
    b = operation.pop(0)
    op = operator.pop(0)
    if (op == "+"):
        operation.insert(0, a + b)
    else:
        operation.insert(0, a - b)
    

print(int(operation[0]))