#!/usr/bin/python3
def pascal_triangle(n):
    """Method to print pascal triangle"""
    mylist =[]
    if numrows <= 0:
        print(mylist)
    else:
        for row in range(n):
            new_row = []
            for col in range(row + 1):
                if col == 0 or col == row:
                    new_row.append(1)
                else:
                    if row - 1 >= 0 and col - 1 >= 0 and row - 1 < len(mylist) and col < len(mylist[row - 1]):
                        val = mylist[row - 1][col - 1] + mylist[row - 1][col]
                        new_row.append(val)
            mylist.append(new_row)
