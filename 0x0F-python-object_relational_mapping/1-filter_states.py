#!/usr/bin/python3
"""filter dem boys"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1],
                               passwd=argv[2],
                               db=argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY \
                  states.id ASC")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    databaseb.close()
