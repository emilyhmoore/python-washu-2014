import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker
#Some info about sqlalchemy

print sqlalchemy.__version__
#Connect to the local database, can use :memory: to just try it out in memory

engine = sqlalchemy.create_engine('sqlite:///mydatabase.db')
Base = declarative_base()
#Define some schemas

class Player(Base):
	__tablename__ = 'players'
#Have an ID column because player attributes (name, etc) are not unique
	id = Column(Integer, primary_key=True)
	name = Column(String)
	number = Column(Integer)
	team_id = Column(Integer, ForeignKey("teams.id"))
	def __init__(self, name, number, team=None):
		self.name = name
		self.number = number
		self.team = team
	def __repr__(self):
		return "<Player('%s', '%s)>" % (self.name, self.number)

class Team(Base):
	__tablename__ = "teams"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	players = relationship("Player", backref="team")
	def __init__(self, name):
		self.name = name
	def __repr__(self):
		return "<team('%s')>" % (self.name)

# First time create tables
Base.metadata.create_all(engine)
#See structure of players table:
Player.__table__ 