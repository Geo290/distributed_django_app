# Django app build over a layered architecture

- This app was built in Django, a Python framework for web development.
- If you haven't work with Django or python before there are some steps you must follow to run this app:

    1 Install Python by downloading it from its official website.
    2 Create a Folder where the project will be nested.
    3 Open a terminal an run the following comands:
        -> py -m ensurepip --upgrade
        -> pip install -r requirements.txt
    4 Next you must go to crud/settings.py read the header and follow the instructions
    5 Return to the terminal and run the following commands:
        -> python manage.py makemigrations
        -> python manage.py migrate
        -> python manage.py runserver 0.0.0.0:8000
    6 The server will be running.