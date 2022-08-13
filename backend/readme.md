# Setup for Server(Django_Project)
## after cloning the Repo

1. install python3-pip python3-dev and Gunicorn on the server

2. install and active the virtual environment

3. install all the dependencies on the on the requirements.txt
    `Django==4.1`
    `asgiref==3.5.2`
    `dj-database-url==1.0.0`
    `django-crispy-forms==1.14.0`
    `gunicorn==20.1.0`
    `Pillow==9.2.0`
    `psycopg2==2.9.3`
    `sqlparse==0.4.2`
    `tzdata==2022.2`
    `whitenoise==6.2.0`
    `django-heroku==0.3.1`

## the rest should be server based setups...thanks



# Setup for Local-testing 

## after cloning the Repo

1. Run `python manage.py setup` to install all requirements and create a virtual environment. Follow the output instructions to activate the virtual environment.(`env\scripts\activate`)


2. Run `pip install -r requirements.txt`. This runs the migrations

3. Import dummy data to sqlite DB
 
- `python manage.py loaddata data.json`

4. Run Makemigrations and migrate command

- `python manage.py makemigrations`

- `python manage.py migrate`

5. Startup server with the command:

- `python manage.py runserver`

