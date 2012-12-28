from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
engine = create_engine("postgresql+pg8000://postgres:master@localhost/cherrypy", echo=True)
Session.configure(bind=engine)
Base = declarative_base()

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	username = Column(String)
	fullname = Column(String)
	password = Column(String)

	def __init__(self, username, fullname, password):
		self.username = username
		self.fullname = fullname
		self.password = password
		
Base.metadata.create_all(engine)