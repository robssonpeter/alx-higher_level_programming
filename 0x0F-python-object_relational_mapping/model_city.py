#!/usr/bin/python3
""" Class Definition for city"""

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State

Base = declarative_base()


class City(Base):
    """ Representing a city 
    __tablename__ (str): The table to be used
    id (sqlalchemy.Integer): the id the auto increments
    name (sqlalchemy.String): name of the city
    state_id (integer): id of the state 
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable = False)
