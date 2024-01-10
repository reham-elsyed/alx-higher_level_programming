#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    lookup = [
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V',5),
            ('IV',4),
            ('I', 1),
            ]
    res = 0
    i = 0
    while i < len(roman_string):
        for l, n in lookup:
            if roman_string[i:i+len(l)] == l:
                res += n
                i += len(l)
                break
        else:
            return 0
    return res
