#!/usr/bin/python3
if __name__ = "__main__":
    from calculator_1 import add, sub, mul, div
    a_cast = int(sys.argv[1])
    b_cast =int(sys.argv[2])
    operator =['+', '_', '*', '/']
    if len(sys.argv) > 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit 1
    else:
        if s not in operator:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        if s == '+':
            print("{:d} {} {:d} = {:d}.format(a_cast, s.operator, b_cast, add(a, b))")
        elif s == '_':
            print("{:d} {} {:d} = {:d}.format(a_cast, s.operator, b_cast, sub(a, b))")
        elif s == '*':
            print("{:d} {} {:d} = {:d}.format(a_cast, s.operator, b_cast, mul(a, b))")
        elif s == '/':
            print("{:d} {} {:d} = {:d}.format(a_cast, s.operator, b_cast, div(a, b))")
