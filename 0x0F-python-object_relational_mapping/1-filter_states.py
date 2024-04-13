#!/usr/bin/python3
"""Module that list all states with n letter"""
import sys
import MySQLdb
import mysql.connector

if __name__ == "__main__":
    #Get MYSQL credentials frkm command line arguments
    # Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Execute the SQL query to retreive all states by id
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
