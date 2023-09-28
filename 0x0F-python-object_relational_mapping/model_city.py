#!/usr/bin/python3
"""import libraries"""
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import State, Base


class City(Base):
    """ class for states"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer)
