#!/usr/bin/python3
""" Python script to list all the states starting with N from database """

if __name__ == "__main__":
    import MySQLdb
    import sys

    args = sys.argv
    connection = MySQLdb.connect("localhost", args[1], args[2], args[3])
    cursor = connection.cursor()
    stmnt = f"SELECT id, name FROM states WHERE name = {args[4]} ORDER BY id ASC"
    cursor.execute(stmnt)
    results = cursor.fetchall()
    for result in results:
        print(result)
