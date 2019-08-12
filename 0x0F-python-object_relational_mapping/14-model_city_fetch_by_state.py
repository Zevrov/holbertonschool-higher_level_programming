#!/usr/bin/python3


import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()

    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
