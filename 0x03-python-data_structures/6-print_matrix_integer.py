#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    print("matrix = [", end="")
    for i in matrix:
        print("\n [", end="")
        for j in i:
            print("{:d}, ".format(j), end="")
        print("],")
    print("")
