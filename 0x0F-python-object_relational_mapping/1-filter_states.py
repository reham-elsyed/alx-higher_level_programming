#!/usr/bin/python3
"""Module that list all states with n letter"""
import sys
import MySQLdb
import mysql.connector


if __name__ == "__main__":
    #Get MYSQL credentials frkm command line arguments
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()

    # Execute the SQL query to retreive all states by id
    c.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
