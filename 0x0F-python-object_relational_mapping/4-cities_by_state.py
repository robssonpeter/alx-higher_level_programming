#!/usr/bin/python3
""" script to list cities with their states """

if __name__ == "__main__":
    import MySQLdb
    import sys

    stmt = """
            SELECT cities.id, cities.name, states.name
            INNER JOIN states
            ON states.id = cities.state_id
            """
    arg = sys.argv
    connection = MySQLdb.connect('localhost', arg[1], arg[2], arg[3])
    cursor = connection.cursor()
    cursor.execute()
    results = cursor.fetchall()
    for result in results:
        print(result)
