#!/usr/bin/python3
""" Lists the of a state with a given name from db """

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine, Integer, String
    from sqlalchemy.orm import sessionmaker, declarative_base
    from model_state import Base, State

    args = sys.argv
    command = f"mysql://{args[1]}:{args[2]}@localhost:3306/{args[3]}"
    engine = create_engine(command)
    Session = sessionmaker(bind=engine)
    session = Session()

    model = State()
    model.name = "Louisiana"

    session.add(model)
    saved = session.commit()

    print(model.id)
