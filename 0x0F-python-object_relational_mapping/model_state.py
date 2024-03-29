#!/usr/bin/python3
"""import libraries"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ class for states"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
