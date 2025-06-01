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
        user = session.query(User).filter_by(id=user_id).first()
        print(f"\nReviews by User: {user.name}\n{'-'*40}")
        for r in reviews:
            book = session.query(Book).filter_by(id=r.book_id).first()
            print(f" - {book.title}: Rated {r.rating}/5 - {r.review}")
        else:
            print("No reviews found or invalid user ID")
        
        session.close()

def list_books_by_genre(genre_name):
    session = Session()
    genre = session.query(Genre).filter_by(name=genre_name).first()

    if genre:
        books=genre.books
        print(f"\nBooks in the Genre '{genre_name}'\n{'-'*40}")
        for book in books:
            print(f" - {book.title}")
        else:
            print("No books found or invalid genre name.")

        session.close()

def list_all_books():
    session=Session()
    books=session.query(Book).all()

    if books:
        print(f"\nAll Books in Library\n{'-'*40}")
        for book in books:
            print(f"-{book.title} ( Book ID:{book.id})")
    else:
        print("No books found in the database!")
    
    session.close()

def list_all_users():
    session=Session()
    users=session.query(User).all()
        
    if users:
        print(f"\nAll Reviwers\n{'-'*40}")

        for user in users:
                print(f"-{user.name} (Reviewer's ID:{user.id})")
    else:
        print("No reviewers located")
        
    session.close()

def all_genres():
    session=Session()
    genres= session.query(Genre).all()

    if genres:
        print (f"\nAll Genres\n{'-'*40}")
        for genre in genres:
            print(f"-{genre.name} (Genre ID:{genre.id})")
    else:
        print ("Genre not available")
    session.close()

def create_book():
    session = Session()
    title = input("Enter book title")
    user_id = int(input("Enter reviewer's ID:"))

    new_book =Book(title=title,user_id = user_id)
    session.add(new_book)
    session.commit()
    print(f"Book '{title}' added sucessfully")
    session.close()

def delete_book():
    session = Session()
    title = input("Enter book title")
    user_id = int(input("Enter reviewer's ID:"))

    new_book =Book(title=title,user_id = user_id)
    session.delete(new_book)
    session.commit()
    print(f"Book '{title}' added sucessfully")
    session.close()



def main():
    while True:
        print("\nChoose an option:")
        print("1.list all books")
        print("2.List all Reviewers.")
        print("3.List reviews by Book ID")
        print("4.List reviews by Reviewer's ID")
        print("5.List all genres")
        print("6.List books by Genre")
        print("7.Add a Book")
        print("8.Delete a book")

    
    
        choice = input("Enter choice (1, 2, 3, 4, 5, 6, 7 or 8): ")

        if choice =='1':
            list_all_books()
        elif choice =='2':
            list_all_users()
        elif choice =='3':
            book_id = int(input("Enter Books ID: "))
            list_reviews_by_books(book_id)
        elif choice == '4':
            user_id = int(input("Enter User ID: "))
            list_reviews_by_users(user_id)
        elif choice == '5':
            all_genres()
        elif choice =='6':
            genre_name = input("Enter Genre Name: ")
            list_books_by_genre(genre_name)
        elif choice == '7':
            create_book()
        elif choice =='8':
            delete_book()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

