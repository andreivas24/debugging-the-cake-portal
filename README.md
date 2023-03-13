Debugger web app for the team at Luminess.

Steps to follow for running the project locally

First, clone the repository to your local machine:

    git clone https://github.com/thedanoprean/debugging_cake_portal.git

Install the requirements:

    pip install -r requirements.txt

Create the database:

    python manage.py makemigrations cake_user tag posts user_profile comment chats like notifications && python manage.py migrate

Finally, run the development server:

    python manage.py runserver

The project will be available at **127.0.0.1:8000**
