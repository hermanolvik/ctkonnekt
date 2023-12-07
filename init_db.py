from app import create_app, db
from app.util.generate_sample_data import generate_data

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Generate and add sample data to the database
    generate_data(db)
