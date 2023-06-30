#!/usr/bin/python3
""" The script to search for cities """

from model_city import City
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    args = sys.argv
    engine_text = f"mysql://{args[1]}:{args[2]}@localhost:3306/{args[3]}"
    engine = create_engine(engine_text)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State.name, City.id, City.name).join(City)
    query = query.order_by(City.id)
    results = query.all()
    for result in results:
        print(result)
