#!/usr/bin/python3
if __name__ = "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    a_cast = int(sys.argv[1])
    b_cast =int(sys.argv[3])
    s = sys.argv[2]

    if len(sys.argv) > 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit 1
    else:
        if s == '+':
            print("{:d} {} {:d} = {:d}.format(a_cast, s.operator, b_cast, add(a_cast, b_cast))")
        elif s == '_':
            print("{:d} {} {:d} = {:d}.format(a_cast, s.operator, b_cast, sub(a_cast, b_cast))")
        elif s == '*':
            print("{:d} {} {:d} = {:d}.format(a_cast, s.operator, b_cast, mul(a_cast, b_cast))")
        elif s == '/':
            print("{:d} {} {:d} = {:d}.format(a_cast, s.operator, b_cast, div(a_cast, b_cast))")
        else:
             print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
