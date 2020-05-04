# Flask Boilerplate

A simple flask boiler plate with preconfigured the following packages:
1. Flask-Admin
2. Flask-SQLAlchemy
3. alembic
4. Flask-Security
5. Admin lte3

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Installation
Clone the repo
```
$ git clone https://github.com/nikoseystathiou/flask_boilerplate.git your-project-env
```
Initialize and activate a virtualenv:
```
$ python3 -m venv your-project-env
$ source my-project-env/bin/activate
```
Install the dependencies:
```
$ pip install -r requirements.txt
```
Create the .env file
```
$ cp env .env
```
Setup your database in the .env file
```
DB = driver://user:pass@localhost/dbname
```
Run the initial migration
```
$ flask db upgrade
```
Run the development server:
```
$ ./start.sh
```
