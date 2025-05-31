from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key = True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    email=Column(String)



class Book (Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key = True)
    title= Column(String, nullable=False)
    user_id = Column(Integer,ForeignKey('users.id'))
    genre_id = Column(Integer,ForeignKey('genres.id'))

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer,primary_key = True)
    name= Column(String, nullable=False)


class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Review(Base):
    __tablename__ = 'reviews'
    id=Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('users.id'))
    book_id = Column(Integer,ForeignKey('books.id'))
    genre_id= Column(Integer,ForeignKey('genres.id'))
    rating = Column(Integer)
    review = Column(String)

    

if __name__ == '__main__':
    pass
engine= create_engine('sqlite:///page_1.db')
Base.metadata.create_all(engine)