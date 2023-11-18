#!/usr/bin/python3
""" joss what """

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, nullable=False primary_key=True)
    name =  Column(String(128), nullable=False)
