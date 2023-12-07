from flask_bcrypt import Bcrypt
from app.models import User, Post, Comment
from datetime import datetime, timedelta
import random

# Initialize Bcrypt for user creation
bcrypt = Bcrypt()


def create_sample_users():
    users = [
        User(email="olvik@chalmers.se", password=bcrypt.generate_password_hash("123456789").decode('utf-8'), first_name="Herman", family_name="Olvik"),
        User(email="musk@chalmers.se", password=bcrypt.generate_password_hash("123456789").decode('utf-8'), first_name="Elon", family_name="Musk"),
        User(email="abba@chalmers.se", password=bcrypt.generate_password_hash("123456789").decode('utf-8'), first_name="Agnetha", family_name="Fältskog"),
        User(email="gunilla@chalmers.se", password=bcrypt.generate_password_hash("123456789").decode('utf-8'), first_name="Gunilla", family_name="Persson"),
        User(email="zlatan@chalmers.se", password=bcrypt.generate_password_hash("123456789").decode('utf-8'), first_name="Zlatan", family_name="Ibrahimović"),
        User(email="glen@chalmers.se", password=bcrypt.generate_password_hash("123456789").decode('utf-8'), first_name="Glenn", family_name="Hysén"),
    ]
    return users


def create_sample_posts(users):
    sample_titles = ["Studietips för tentaperioden", "Campusaktiviteter denna vecka", "Exjobbsmöjligheter inom AI", "Vet du var hajen lärde sig att simma?"]
    sample_contents = [
        "Hej allihopa! Har ni några bra studietips för kommande tentaperioden?",
        "Vilka aktiviteter händer på campus denna vecka? Någon som vill hänga med?",
        "Jag letar efter exjobb inom AI och maskininlärning. Några tips eller företag att rekommendera?",
        "På haj-school"
    ]
    posts = []

    for i in range(len(sample_titles)):
        post = Post(
            title=sample_titles[i],
            content=sample_contents[i],
            date_posted=datetime.utcnow() - timedelta(days=i),
            user_id=random.choice(users).id
        )
        posts.append(post)

    return posts


def create_sample_comments(users, posts):
    sample_comments = [
        "Bra fråga, jag skulle också vilja veta mer om detta.",
        "Tack för informationen!",
        "Intressant ämne, jag har några tankar om det.",
        "Jag kommer definitivt att kolla in det!"
    ]
    comments = []

    for post in posts:
        for _ in range(random.randint(1, 3)):  # Each post gets 1 to 3 comments
            comment = Comment(
                content=random.choice(sample_comments),
                date_posted=datetime.utcnow(),
                user_id=random.choice(users).id,
                post_id=post.id
            )
            comments.append(comment)

    return comments


def distribute_likes(users, posts, db):
    for post in posts:
        likers_set = set()  # To keep track of users who have already liked this post
        for _ in range(random.randint(1, 5)):  # Each post gets 1 to 5 likes
            liker = random.choice(users)
            if liker.id not in likers_set:  # Check if this user has already liked this post
                likers_set.add(liker.id)
                post.likers.append(liker)

    db.session.commit()


def generate_data(db):
    # Create sample data
    users = create_sample_users()

    # Add users to database and commit
    for user in users:
        db.session.add(user)
    db.session.commit()

    # Now create posts and comments since users are committed and have IDs
    posts = create_sample_posts(users)
    for post in posts:
        db.session.add(post)
    db.session.commit()

    comments = create_sample_comments(users, posts)
    for comment in comments:
        db.session.add(comment)
    db.session.commit()

    # Distribute likes among posts
    distribute_likes(users, posts, db)
