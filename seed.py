from faker import Faker
from models import db, User, Product
from app import app

fake = Faker()

with app.app_context():
    # Delete all data from tables
    db.session.query(Product).delete()
    db.session.query(User).delete()
    db.session.commit()

    users = []

    # Seed Users
    for _ in range(10):
        user = User(
            name=fake.name(),
            email=fake.unique.email()
        )
        db.session.add(user)
        users.append(user)

    db.session.commit()  # Commit users so they have IDs

    # Seed Products
    for _ in range(100):
        product = Product(
            name=fake.word().capitalize(),
            description=fake.sentence(nb_words=10),
            price=fake.random_int(min=100, max=10000),
            category=fake.random_element(elements=['electronics', 'clothing', 'books', 'beauty', 'furniture']),
            stock=fake.random_int(min=1, max=100),
            image=fake.image_url(width=200, height=200),
            user_id=fake.random_element(users).id
        )
        db.session.add(product)

    db.session.commit()
    
