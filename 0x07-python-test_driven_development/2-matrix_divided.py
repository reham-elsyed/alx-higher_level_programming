#!/usr/bin/python3
def matrix_divided(matrix, div):
   if not isinstance(matrix, list) or len(matrix) == 0:
       raise TypeError("matrix must be a matrix (list of lists) " + "of integers/floats")
   for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " + "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " + "of integers/floats")
   if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
   if div == 0:
        raise ZeroDivisionError("division by zero")
   new_matrix = []
   for row in matrix:
        new_row = []
        for item in row:
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)
   return new_matrix
