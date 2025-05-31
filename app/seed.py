from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Book, Author, Genre, Review

engine = create_engine('sqlite:///page_1.db')
Base.metadata.create_all(engine)  
Session = sessionmaker(bind= engine)
session = Session()


user1 = User(name= "Eddy Yego",age =19,email = "eddieyego273@gmail.com")
user2 = User(name= "Pennie Shigogodi",age =17,email = "shigogodi254@gmail.com")
user3 = User(name="Loice Joana",age=20,email="loice23@gmail.com")
user4 = User(name="Stacy Hoes",age=30,email="hoes35@gmail.com")
user5 = User(name="Elton John",age=33,email="john22@gmail.com")
user6 = User(name="Melvin Gal",age=40,email="gal78@gmail.com")
user7 = User(name="Lee San",age=18,email="san12@gmail.com")
user8 = User(name="Cobey Jona",age=22,email="cobey17@gmail.com")
user9 = User(name="Violah Gray",age=44,email="gray67@gmail.com")
user10 = User(name="Winston Chirchill",age=70,email="win24@gmail.com")
user11 = User(name="Diana Hills",age=58,email="hill17@gmail.com")
user12 = User(name="Still Tone",age=49,email="ton19@gmail.com")
user13 = User(name="Hyper Sing",age=33,email="sing90@gmail.com")
user14 = User(name="Rondo Hay",age=43,email="hay11@gmail.com")
user15 = User(name="Monkey.D.Luffy",age=21,email="luffy19@gmail.com")
user16 = User(name="Garp Still",age=68,email="still20@gmail.com")
user17 = User(name="Roronoa Zoro",age=63,email="zoro21@gmail.com")
user18 = User(name="Asta Yen",age=54,email="asta65@gmail.com")
user19 = User(name="Yuno Yen",age=28,email="yuno55@gmail.com")
user20= User(name="Crimson Slire",age=35,email="slire203@gmail.com")
user21 = User(name="San Goku",age=41,email="goku17@gmail.com")
user22 = User(name="Silvester Snow",age=26,email="snow212@gmail.com")
user23 = User(name="Dennis Chill",age=88,email="chill15@gmail.com")
user24 = User(name="Joana King",age=80,email="king190@gmail.com")
user25 = User(name="Ray Ring",age=24,email="ring77@gmail.com")

all_users=""

book1 = Book(title="The Night Circus",genre_id=1)
book2 = Book(title="The Silent Patient",genre_id=3)
book3 = Book(title="Project Hail Mary",genre_id=2)
book4 = Book(title="Where the Crawdads Sing",genre_id=4)
book5 = Book(title="Circe",genre_id=1)
book6 = Book(title="The Seven Husbands of Evelyn Hugo",genre_id=4)
book7 = Book(title="Atomic Habits",genre_id=5)
book8 = Book(title="The House in the Cerulean Sea",genre_id=1)
book9 = Book(title="Daisy Jones & The Six",genre_id=8)
book10 = Book(title="The Midnight Library",genre_id=6)
book11 = Book(title="Sunrise on the Reaping",genre_id=7)
book12 = Book(title="Never Flinch",genre_id=3)
book13 = Book(title="Parable of the Sower",genre_id=7)
book14 = Book(title="Kaleidoscope of Secrets",genre_id=9)
book15 = Book(title="The Missing Girl",genre_id=10)

all_books=""

author1 = Author(name="Erin Morgenstern",books=[book1])
author2 = Author(name="Alex Michaelides",books=[book2])
author3 = Author(name="Andy Weir",books=[book3])
author4 = Author(name="Delia Owens",books=[book4])
author5 = Author(name="Madeline Miller",books=[book5])
author6 = Author(name="Taylor Jenkins Reid",books=[book6,book9])
author7 = Author(name="James Clear",books=[book7])
author8 = Author(name="TJ Klune",books=[book8])
author9 = Author(name="Matt Haig",books=[book10])
author10 = Author(name="Suzanne Collins",books=[book11])
author11 = Author(name="Stephen King",books=[book12])
author12 = Author(name="Octavia Butler",books=[book13])
author13 = Author(name="Sandy Clement",books=[book14])
author14 = Author(name="Stacia Moffett",books=[book15])

all_authors =[]

genre1=Genre(name="Fantasy",books=[book1,book8,book5])
genre2=Genre(name="Science Fiction",books=[book3])
genre3=Genre(name="Psychological Thriller",books=[book2,book12])
genre4=Genre(name="Historical Fiction",books=[book4,book6])
genre5=Genre(name="Self-Help",books=[book7])
genre6=Genre(name="Philosophical Fiction",books=[book10])
genre7=Genre(name="Dystopian Fiction",books=[book11,book13])
genre8=Genre(name="Contemporary Fiction",books=[book9])
genre9=Genre(name="Suspense/Mystery",books=[book14])
genre10=Genre(name="Drama",books=[book15])

all_genres=[]

review1=Review(user_id=1,book_id=1,genre_id=1,rating=4.1,
               review="A mesmerizing tale of a magical competition between two illusionists, set in a mysterious circus that only appears at night. The writing is enchanting, and the world-building is breathtaking.")
review2=Review(user_id=7,book_id=2,genre_id=3,rating=4.3,
               review="A gripping psychological thriller about a woman who stops speaking after committing a shocking crime. Twists and turns keep you hooked until the final reveal.")
review3=Review(user_id=10,book_id=3,genre_id=2,rating=4.5,
               review="A thrilling space adventure where a lone astronaut must save humanity. Packed with humor, science, and heartwarming moments.")
review4=Review(user_id=17,book_id=4,genre_id=4,rating=4.2,
               review="A beautifully written novel blending mystery and nature, following a girl who grows up isolated in the marshlands and becomes entangled in a murder case.")
review5=Review(user_id=12,book_id=5,genre_id=1,rating=4.4,
               review="A stunning retelling of the life of Circe, the sorceress from Greek mythology. The novel explores themes of power, independence, and transformation.")
review6=Review(user_id=8,book_id=6,genre_id=4,rating=4.5,
               review="A glamorous and emotional story about a Hollywood icon revealing her life secrets. A captivating read filled with drama and romance.")
review7=Review(user_id=20,book_id=7,genre_id=5,rating=4.6,
               review="A practical guide to building good habits and breaking bad ones. James Clear provides actionable strategies backed by psychology and neuroscience.")
review8=Review(user_id=16,book_id=8,genre_id=1,rating=4.6,
               review="A heartwarming fantasy about a caseworker who evaluates magical children. A feel-good story about acceptance, love, and finding family in unexpected places.")
review9=Review(user_id=14,book_id=9,genre_id=8,rating=4.2,
               review="A unique novel written in an interview format, following the rise and fall of a fictional rock band. The characters feel incredibly real, making it an immersive experience.")
review10=Review(user_id=9,book_id=10,genre_id=6,rating=4.1,
               review="A thought-provoking novel about a woman who explores alternate versions of her life through a magical library. A deep and inspiring read about regrets and second chances.")
review11=Review(user_id=13,book_id=11,genre_id=7,rating=4.0,
               review="A highly anticipated prequel to The Hunger Games, exploring Haymitch Abernathy’s role in the brutal 50th Hunger Games.")
review12=Review(user_id=19,book_id=12,genre_id=3,rating=4.1,
               review="Stephen King’s latest novel delivers dark crime and psychological intrigue, keeping readers on edge.")
review13=Review(user_id=21,book_id=13,genre_id=7,rating=4.3,
               review="Octavia Butler’s classic dystopian novel remains more relevant than ever, exploring survival in a collapsing society.")
review14=Review(user_id=15,book_id=14,genre_id=9,rating=4.0,
               review="A gripping thriller packed with twists and secrets that unravel in unexpected ways.")
review15=Review(user_id=22,book_id=15,genre_id=10,rating=4.1,
               review="A poignant tale of loss and resilience, exploring the emotional journey of a missing child’s family.")

all_reviews=[]
session.add_all([user1,user2,user3,user4,user5,user6,user7,user8,user9,user10,user11,user12
                 ,user13,user14,user15,user16,user17,user18,user19,user20,user21,user22,user23,user24,user25
                 ,book1,book2,book3,book4,book5,book6,book7,book8,book9,book10,book11,book12,book13,book14,book15
                 ,author1,author2,author3,author4,author5,author6,author7,author8,author9,author10,author11,author12,author13,author14
                 ,genre1,genre2,genre3,genre4,genre5,genre6,genre7,genre8,genre9,genre10
                 ,review1,review2,review3,review4,review5,review6,review7,review8,review9,review10,review11,review12,review13,review14,review15])
session.commit()
print ("seed data added successfully!!!")