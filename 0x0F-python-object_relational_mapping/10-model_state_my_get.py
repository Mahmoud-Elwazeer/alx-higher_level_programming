#!/usr/bin/python3
"""import libraries"""
from model_state import Base, State
from sqlalchemy import create_engine, text
from sys import argv


def main():
    engine = create_engine('mysql://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    conn = engine.connect()
    out = conn.execute(text("SELECT * FROM states WHERE name = :name"), name=argv[4])
    row = out.fetchall()
    if row:
        print(row[0][0])
    else:
        print("Not found")


if __name__ == "__main__":
    main()
