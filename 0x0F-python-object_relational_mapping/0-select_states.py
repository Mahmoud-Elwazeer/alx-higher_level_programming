#!/usr/bin/python3

import sys
import MySQLdb


def main():
    dbconnect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    cusrsor = dbconnect.cursor()

    states = "SELECT * FROM states"
    
    try:
        cursor.execute(states)
        readlist = cursor.fetchall()
        for i in readlist:
            print(i)
            print(1)
    except:
        print("Error")
    finally:
        dbconnect.close()



if __name__ == '__main__':
    if len(sys.argv) == 4:
        main()
