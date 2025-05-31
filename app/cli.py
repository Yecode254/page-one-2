from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Review, Book, User, Genre

DATABASE_URL = "sqlite:///page_1.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def list_reviews_by_books(book_id):
    session = Session()
    reviews = session.query(Review).filter_by(book_id=book_id).all()

    if reviews:
        book =session.query(Book).filter_by(id=book_id).first()
        print(f"\nReview for Book: {book.title}\n{'-'*40}")
        for r in reviews:
            user = session.query(User).filter_by(id=r.user_id).first()
            print(f" - {user.name} rated it {r.rating}/5: {r.review}")
        avg_rating = sum(r.rating for r in reviews) / len(reviews)
        print(f"\nAverage Rating: {avg_rating:.1f}/5\n{'-'*40}")
    else:
        print("No reviews found or invalid book ID.")
    
    session.close()

def list_reviews_by_users(user_id):
    session= Session()
    reviews= session.query(Review).filter_by(user_id=user_id).all()

    if reviews:
        user= session.query(User)(id=user_id).first()
        print(f"\nReviews by User: {user.name}\n{'-'*40}")
        for r in reviews:
            book = session.query(Book).filter_by(id=r.book_id).first()
            print(f" - {book.title}: Rated {r.rating}/5 - {r.review}")
        else:
            print("No reviews found or invalid user ID")
        
        session.close()

def 
