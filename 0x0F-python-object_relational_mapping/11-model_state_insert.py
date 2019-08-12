#!/usr/bin/python3


import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new = State(name='Louisiana')

    new = State(name='Louisiana')
    session.add(new)
    session.commit()
    session.close()

    Murica = session.query(State).filter(State.name == 'Louisiana').one()

    print(Murica.id)
