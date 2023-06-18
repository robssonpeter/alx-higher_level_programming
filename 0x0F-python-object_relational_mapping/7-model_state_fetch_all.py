#!/usr/bin/python3

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

    results = session.query(State).all()
    for result in results:
        print(f"{result.id}: {result.name}")
