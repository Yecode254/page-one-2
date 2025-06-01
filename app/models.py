from sqlalchemy import Table,Column, Integer,Float, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
Base = declarative_base()

author_book = Table('author_book', Base.metadata,
    Column('author_id', Integer, ForeignKey('authors.id')),
    Column('book_id', Integer, ForeignKey('books.id'))
)
book_genre = Table('book_genre', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('genre_id', Integer, ForeignKey('genres.id'))
)

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
    authors = relationship('Author', secondary=author_book, back_populates='books')
    genres = relationship('Genre', secondary=book_genre, back_populates='books') 

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer,primary_key = True)
    name= Column(String, nullable=False)
    books = relationship('Book', secondary=author_book, back_populates='authors')
    


class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship('Book', secondary=book_genre, back_populates='genres')

class Review(Base):
    __tablename__ = 'reviews'
    id=Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('users.id'))
    book_id = Column(Integer,ForeignKey('books.id'))
    genre_id= Column(Integer,ForeignKey('genres.id'))
    rating = Column(Float)
    review = Column(String)

    

if __name__ == '__main__':
    pass
engine= create_engine('sqlite:///page_1.db')
Base.metadata.create_all(engine)