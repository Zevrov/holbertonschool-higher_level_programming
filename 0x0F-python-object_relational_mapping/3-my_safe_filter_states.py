#!/usr/bin/python3


import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1],
                               passwd=argv[2],
                               db=argv[3])
    curs = database.cursor()
    curs.execute("SELECT * FROM states WHERE name\
                  LIKE %s ORDER BY states.id\
                  ASC", [argv[4]])
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    database.close()
