#!/usr/bin/python3
"""
    A script that lists all cities states from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    connection = MySQLdb.connect(host='localhost', port=3306,
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])

    cur = connection.cursor()
    arg = sys.argv[4]
    cur.execute('SELECT cities.name \
                FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name = %(name)s', {'name': arg})

    rows = cur.fetchall()
    list_cities = [item for city in rows for item in city]
    print(", ".join(list_cities))

    cur.close()
    connection.close()
