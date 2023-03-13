# Stack Overflow clone

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



# **USING THE APP**

1. Home page

![HomePage](https://user-images.githubusercontent.com/92268035/224705488-635f3244-b476-4da9-8f2d-cb25fb9dc2b0.jpeg)

2. Log in

![Login](https://user-images.githubusercontent.com/92268035/224729328-de7488c4-86d0-4b46-a381-6e3e9a868d10.jpeg)

3. User profile

![Profile](https://user-images.githubusercontent.com/92268035/224705306-025636ba-7e86-495c-9504-d02b9cbdb41b.jpeg)

4. Post's List

![Posts](https://user-images.githubusercontent.com/92268035/224705599-d56ade2c-ce5f-40ca-b6ba-476c1486b630.jpeg)

5. Create new post

![Post](https://user-images.githubusercontent.com/92268035/224729325-de17bec9-ceb0-42fc-851c-0c3d8243b169.jpeg)

6. Chat rooms' list

![Chat](https://user-images.githubusercontent.com/92268035/224705652-819849dd-fff7-4901-a961-e68cb6f2b64c.jpeg)

7. Chat room

![Chatting](https://user-images.githubusercontent.com/92268035/224729314-ab7881b7-bdc7-4e6a-b26b-42dec1306677.jpeg)
