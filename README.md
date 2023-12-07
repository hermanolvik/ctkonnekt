# ctkonnekt

## Overview
ctkonnekt is a dynamic web application developed using Python Flask.

## Technology Stack
- **Python Flask:** Main framework for handling backend operations and routing.
- **Postgres Database:** Robust and scalable database for data storage.
- **SQLAlchemy:** ORM for managing and querying the database.
- **Flask-Login:** User authentication management.
- **Jinja2:** Templating engine for rendering HTML.
- **Bootstrap 5 & Font Awesome:** For responsive front-end design and icons.
- **Lottie:** Enhanced front-end styling with interactive animations.

## Development Process
The development of ctkonnekt was guided by the need for speed and reliability. Leveraging my experience from previous hobby projects, I selected a familiar technology stack that guaranteed a good balance of efficiency and quality. While I am exploring more advanced technologies like React for future projects, this application's tight deadline necessitated a more traditional and proven approach. Throughout the development, I utilized various online resources, including Google and ChatGPT, for development support and problem-solving.

## Running the Application
To get ctkonnekt up and running, follow these steps:

1. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Database Setup:**
    - Launch a Postgres database instance.
    - Configure the database connection in `config.py`.

3. **Initialize Database:**
   ```
   python init_db.py
   ```
   This will create the database schema and generate sample data.

4. **Start the Application:**
   ```
   python run.py
   ```
   This will start the Flask server and the application should be accessible on the designated port.
