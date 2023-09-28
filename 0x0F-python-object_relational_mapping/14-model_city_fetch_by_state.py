#!/usr/bin/python3
<<<<<<< HEAD
"""import libraries"""

from model_city import Base, City
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sys import argv


def main():
    engine = create_engine('mysql://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    conn = engine.connect()
<<<<<<< HEAD
    out = conn.execute(text("SELECT * FROM cities"))
    for i in out:
        print(i)
=======
    # Session = sessionmaker(bind=engine)
    # session = Session()

    # out = session.query(City).all()
    # for i in out:
    #     print(i)
    out = conn.execute(text("SELECT * FROM states"))
    for i in out:
        print("{}: {}".format(i[0], i[1]))
>>>>>>> 8471a57e3477eda38ae4ca078b9a3a025bf16069


if __name__ == "__main__":
    main()
