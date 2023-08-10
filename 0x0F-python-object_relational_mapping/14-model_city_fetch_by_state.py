#!/usr/bin/python3
""" The script to search for cities """


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, join
import sys

if __name__ == "__main__":
    from model_city import City
    from model_state import State
    args = sys.argv
    engine_text = f"mysql://{args[1]}:{args[2]}@localhost:3306/{args[3]}"
    engine = create_engine(engine_text)

    Session = sessionmaker(bind=engine)
    session = Session()
    """ query = session.query(State.name, City.id, City.name).join(City)
    query = query.order_by(City.id) """
    query = session.query(City, State).join(State, State.id == City.state_id)
    """ results = query.all() """

    for city, state in query:
        string = f"{state.name}: ({city.id}) {city.name}"
        print(string)
