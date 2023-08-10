#!/usr/bin/python3
""" Class Definition for State"""

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String

Base = declarative_base()



class State(Base):
    """ Representing a state
    __tablename__ (str): The table to be used
    id (sqlalchemy.Integer): the id the auto increments
    name (sqlalchemy.String): name of the state
    """

    __tablename__ = 'states'


    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    """cities = relationship('City', back_populates='state')"""

    def __repr__(self):
        return f"<State(id={self.id}, name='{self.name}')>"
