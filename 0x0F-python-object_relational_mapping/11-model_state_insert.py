#!/usr/bin/python3
""" inserter in a state """

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisana')
    session.add(new_state)
    new_instance = session.query(State).filter_by(name='Louisana').first()
    session.commit()    
    print(new_instance.id)
    session.close()
