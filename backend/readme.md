# Setup for Local-testing 
## after cloning the Repo

1. Run `python manage.py setup` to install all requirements and create a virtual environment. Follow the output instructions to activate the virtual environment.

- Windows `env\scripts\activate`

- Linux - `source env/scripts/activate`


2. install the dependencies using the command:

- `pip install -r requirements.txt`
 
3. Import dummy data to sqlite DB
 
- `python manage.py loaddata data.json`

4. Run Makemigrations and migrate command

- `python manage.py makemigrations`

- `python manage.py migrate`

5. Startup server with the command:

- `python manage.py runserver`



# Setup for Server (Django_Project)
## after cloning the Repo

1. install python3-pip python3-dev and Gunicorn on the server

2. install and active the virtual environment

3. install all the dependencies in requirements.txt

- `pip install -r requirements.txt`

## the rest should be server based setups...thanks