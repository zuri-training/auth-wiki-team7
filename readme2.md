# auth-wiki-team7
It is a userfriendly webapp that has a library of authentication code examples. Any Developer can register in this platform to view and download different authentication code examples, and also make community interactions.

# Setup

1. Run `python manage.py setup` to install all requirements and create a virtual environment. Make sure you are in the backend directory. Follow the output instructions to activate the virtual environment.

2. Run `python manage.py update`. This runs the migrations

3. Import dummy data to sqlite DB
 
- `python manage.py loaddata data.json`
  
4. Create a different admin account and Start Local Server:
 
- `python manage.py createsuperuser`
- `python manage.py runserver`

## To Contribute
[Follow the contribution guide](../README.md#contribution-guide)

Any contributions you make are **greatly appreciated**.