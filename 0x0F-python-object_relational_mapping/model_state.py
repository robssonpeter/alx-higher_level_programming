#!/usr/bin/python3
import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

""" Class Definition for State"""


class State(Base):
    """ Representing a state """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"<State(id={self.id}, name='{self.name}')>"
