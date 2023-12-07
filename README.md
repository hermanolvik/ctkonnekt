# ctkonnekt
<img width="800" alt="Screenshot 2023-12-08 at 00 10 31" src="https://github.com/hermanolvik/ctkonnekt/assets/72079200/23803465-e7f1-4511-80bc-4c2864cdd6f3">

## Overview
ctkonnekt is a simple forum-style web application developed using Python Flask. It allows users to create posts, comment on them, and engage with a community through a user-friendly interface. It follows a monolithic architecture where both server-side operations and client-facing interfaces are managed within a single unified codebase, as opposed to microservices or a decoupled architecture.

## Technology stack
- **Python Flask:** Main framework for handling backend operations and routing.
- **PostgreSQL:** Database for data storage.
- **SQLAlchemy:** ORM for managing and querying the database.
- **Flask-Login:** User authentication management.
- **Jinja2:** Templating engine for rendering HTML.
- **Bootstrap 5 & Font Awesome:** For responsive front-end design and icons.

## The week-long project time frame
given the one-week deadline, the development of ctkonnekt was guided by the need for speed and reliability. Leveraging my experience from previous hobby projects, I selected a familiar technology stack that guaranteed a good balance of efficiency and quality. While I am exploring more advanced technologies like React for future projects, the tight deadline had me choose a more familiar approach. Throughout the development, I utilized various online resources, including Google and ChatGPT, for development support and problem-solving.

### Actual time spent on the case

backend development: 10 hrs, frontend development: 8 hrs, documentation and everything else: 2 hrs

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


# Video

A screen recording demonstrating some functionalities of the application

link: https://drive.google.com/file/d/1O6rLfLhk0FFAe6QmbgNzaMlK85vr_nsr/view?usp=sharing

Time stamps:

0:07 - view all posts [view_all]

0:15 - like post [like_post<post_id>]

0:19 - sort posts [sort_post()]

0:33 - view post [view_post<post_id>]

0:42 - add comment [add_comment<post_id>]

0:46 - edit comment [edit_comment<comment_id>]
