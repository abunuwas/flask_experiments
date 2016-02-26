from sqlalchemy import Column, Integer, String
from flask_experiments.database import Base

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	username = Column(String(50))
	email = Column(String(120), unique=True)

	def __init__(self, username=None, email=None):
		self.name = name
		self.mail = email

	def __repr__(self):
		return '<User {}>'.format(self.name)

