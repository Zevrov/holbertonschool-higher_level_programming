#!/usr/bin/python3
"""list all states available"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    database = MySQLdb.connect(port=3306,
                               host='localhost',
                               charset='utf8',
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])
    curs = database.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    database.close()
