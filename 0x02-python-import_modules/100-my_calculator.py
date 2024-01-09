#!/usr/bin/python3
if __name__ = "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    a_cast = int(sys.argv[1])
    b_cast =int(sys.argv[3])
    s = sys.argv[2]

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit 1
    else:
        if s == '+':
            print("{:d} '+' {:d} = {:d}.format(a_cast, b_cast, add(a_cast, b_cast))")
        elif s == '_':
            print("{:d} '_' {:d} = {:d}.format(a_cast, , b_cast, sub(a_cast, b_cast))")
        elif s == '*':
            print("{:d} '*' {:d} = {:d}.format(a_cast, b_cast, mul(a_cast, b_cast))")
        elif s == '/':
            print("{:d} '/' {:d} = {:d}.format(a_cast, b_cast, div(a_cast, b_cast))")
        else:
             print("Unknown operator. Available operators: +, -, * and /")
            sys.exit 1
