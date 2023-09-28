#!/usr/bin/python3
"""import libraries"""
from model_city import Base, City
from sqlalchemy import create_engine, text
from sys import argv


def main():
    engine = create_engine('mysql://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    conn = engine.connect()
    out = conn.execute(text("SELECT * FROM cities"))
    for i in out:
        print(i)


if __name__ == "__main__":
    main()
