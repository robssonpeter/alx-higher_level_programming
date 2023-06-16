#!/usr/bin/python3
""" Python script to list all the states from database """

if __name__ == "__main__":
    import MySQLdb
    import sys

    connection = MySQLdb.connect(host="locahost", user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    results = cursor.fetchall()
    for result in results:
        print(result)
