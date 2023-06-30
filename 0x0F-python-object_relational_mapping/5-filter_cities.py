#!/usr/bin/python3
""" script to list cities with their states """

if __name__ == "__main__":
    import MySQLdb
    import sys

    stmt = """
            SELECT cities.id, cities.name, states.name
            FROM cities JOIN states ON states.id = cities.state_id
            WHERE states.name = %s"""
    arg = sys.argv
    connection = MySQLdb.connect('localhost', arg[1], arg[2], arg[3])
    cursor = connection.cursor()
    cursor.execute(stmt, (arg[4],))
    results = cursor.fetchall()
    length = len(results)
    index = 0
    if length == 0:
        print()
    for result in results:
        if index < length - 1:
            print(result[1], end=", ")
        else:
            print(result[1])
        index += 1
