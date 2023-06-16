#!/usr/bin/python3
""" Python script to list all the states from database """

if __name__ == "__main__":
    import MySQLdb
    import sys

    args = sys.argv
    connection = MySQLdb.connect("localhost", args[1], args[2], args[3])
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    results = cursor.fetchall()
    for result in results:
        print(result)
