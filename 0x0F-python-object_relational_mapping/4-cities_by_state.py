#!/usr/bin/python3
""" Methoc to print cities in states"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id")

    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
