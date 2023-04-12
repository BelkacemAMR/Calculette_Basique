import sys

def calculator(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            print("input error")
            return
        return a / b
    elif operator == "%":
        return a % b
    elif operator == "^":
        return a ** b
    else:
        print("input error")
        return

if len(sys.argv) != 4:
    print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")
    sys.exit()

try:
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    result = calculator(a, operator, b)
    if result is not None:
        print(result)
except ValueError:
    print("input error")

