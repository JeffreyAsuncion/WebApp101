# WebApp101
Web App - Flask Python


## Installation

Download the repo and navigate there from the command line:

```sh
git clone https://github.com/JeffreyAsuncion/WebApp101.git
cd WebApp101
```



## Setup

Setup and activate a virtual environment:
```sh
pipenv install 
pipenv shell
```

Setup the database:

'''sh
# Windows users can omit the "FLASK_APP=web_app" part...

FLASK_APP=web_app

flask db init #> generates app/migrations dir

# run both when changing the schema:
flask db migrate #> creates the db (with "alembic_version" table)
flask db upgrade #> creates the specified tables
'''

## Usage

```sh
export FLASK_APP=web_app
flask run
```

lecture 2 ___  1:37:26

example of flask run
>>> from web_app.routes.twitter_routes import fetch_user
>>> fetch_user('s2t2')
s2t2
'OK, got it dude!'
>>>
