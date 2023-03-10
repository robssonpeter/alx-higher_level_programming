#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys

    arguments = sys.argv
    if len(arguments) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(arguments[1])
    b = int(arguments[3])
    operator = arguments[2]
    result = 1

    if operator == '+':
        result = calc.add(a, b)
    elif operator == '-':
        result = calc.sub(a, b)
    elif operator == '*':
        result = calc.mul(a, b)
    elif operator == '/':
        result = calc.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print(f"{a} {operator} {b} = {result}")
    sys.exit(0)
