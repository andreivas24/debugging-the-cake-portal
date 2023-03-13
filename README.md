Stack Overflow clone

Steps to follow for running the project locally

First, clone the repository to your local machine:

    git clone https://github.com/andreivas24/debugging_cake_portal.git

Install the requirements:

    pip install -r requirements.txt

Create the database:

    python manage.py makemigrations cake_user tag posts user_profile comment chats like notifications && python manage.py migrate

Finally, run the development server:

    python manage.py runserver

The project will be available at **127.0.0.1:8000**


`#RRGGBB`
**USING THE APP**

1. Home page

![HomePage](https://user-images.githubusercontent.com/92268035/224705488-635f3244-b476-4da9-8f2d-cb25fb9dc2b0.jpeg)

2. User profile

![Profile](https://user-images.githubusercontent.com/92268035/224705306-025636ba-7e86-495c-9504-d02b9cbdb41b.jpeg)

3. Post's List

![Posts](https://user-images.githubusercontent.com/92268035/224705599-d56ade2c-ce5f-40ca-b6ba-476c1486b630.jpeg)

4. Chat rooms

![Chat](https://user-images.githubusercontent.com/92268035/224705652-819849dd-fff7-4901-a961-e68cb6f2b64c.jpeg)


