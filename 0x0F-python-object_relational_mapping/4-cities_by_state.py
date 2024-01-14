#!/usr/bin/python3
"""
    A script that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    connection = MySQLdb.connect(host='localhost', port=3306,
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])

    cur = connection.cursor()
    quary = "SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id"
    cur.execute(quary)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    connection.close()
