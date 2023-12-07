# ctkonnekt

## Overview
ctkonnekt is a simple forum-style web application developed using Python Flask. It allows users to create posts, comment on them, and engage with a community through a user-friendly interface. It follows a monolithic architecture where both server-side operations and client-facing interfaces are managed within a single unified codebase, as opposed to microservices or a decoupled architecture.

## Technology stack
- **Python Flask:** Main framework for handling backend operations and routing.
- **PostgreSQL:** Database for data storage.
- **SQLAlchemy:** ORM for managing and querying the database.
- **Flask-Login:** User authentication management.
- **Jinja2:** Templating engine for rendering HTML.
- **Bootstrap 5 & Font Awesome:** For responsive front-end design and icons.

## The one-week development process
The development of ctkonnekt was guided by the need for speed and reliability. Leveraging my experience from previous hobby projects, I selected a familiar technology stack that guaranteed a good balance of efficiency and quality. While I am exploring more advanced technologies like React for future projects, the tight deadline had me choose a more familiar approach. Throughout the development, I utilized various online resources, including Google and ChatGPT, for development support and problem-solving.

## Running the application
To get ctkonnekt up and running, follow these steps:

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Database setup:**
    - Launch a Postgres database instance.
    - Configure the database connection in `config.py`.

3. **Initialize database:**
   ```
   python init_db.py
   ```
   This will create the database schema and generate sample data.

4. **Start the application:**
   ```
   python run.py
   ```
   This will start the Flask server and the application should be accessible on the designated port.
