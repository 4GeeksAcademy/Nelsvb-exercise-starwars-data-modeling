import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True )
    username = Column(String(25), nullable=False)
    firstname = Column(String(15), nullable=False)
    lastname = Column(String(25), nullable=False)
    email = Column(String(35), nullable=False)
    password = Column(String(15), nullable=False)
    subscription_date = Column(String(25), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    gender = Column(String(25), nullable=False)
    species = Column(String(25), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    climate = Column(String(25), nullable=False)
    terrain = Column(String(30), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id= Column(Integer, ForeignKey('planet.id'))

    user = relationship(User)
    character = relationship(Character)
    planet = relationship(Planet)




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print('Diagrama realizado con éxito!!! Revisa el archivo diagram.png.')
except Exception as e:
    print('Hubo un problema al generar el diagrama')
    raise e
