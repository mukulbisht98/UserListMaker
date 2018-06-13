# import CRUD Operations from Lesson 1 ##
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Users

# Create session and connect to DB ##
engine = create_engine('sqlite:///users.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
b = raw_input("enter name : ")
newEntry = Users(name = b)
session.add(newEntry)
session.commit()
session.query(Users).all()
