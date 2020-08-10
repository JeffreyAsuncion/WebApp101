# This is a step by step log of how to build this project

0:08:07 Lecture 1 - https://www.youtube.com/watch?v=LRL_lnOtyhI&feature=youtu.be
Lecture 1 - getting application structure organized
Lecture 2 - get data in the database
Lecture 3 - take data in database and train a model
Lecture 4 - we will deploy 

Lecture 1 - Objectives:
Student should be able to distinguish between front-end, back-end, database, and what tasks are appropriate for which
Student should be able to create a simple Python web application that exposes an API to URL endpoints

LECTURE 1
PART 1
1. Create a new repo on GitHub, then get it setup locally:
https://github.com/JeffreyAsuncion/WebApp101

2. in anaconda prompt 
git clone YOUR_REMOTE_ADDRESS
cd your-repo-name
code .

3. in VScode terminal - bash
conda deactivate
pipenv --python 3.7 #create pipfile

4. Installing package dependencies:
pipenv install Flask Flask-SQLAlchemy Flask-Migrate

5. Activate the virtual environment
pipenv shell

6. Client-Server Architecture 0:21:50 https://github.com/JeffreyAsuncion/lambda-ds-3-3/blob/master/notes/class-1.md

7. starter code https://flask.palletsprojects.com/en/1.1.x/quickstart/
# hello.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    x = 2 + 2
    return f"Hello World! {x}"

@app.route("/about")
def about():
    return "About me"

8. run it
Running a Flask App:

# Mac:
FLASK_APP=hello.py flask run

# Windows:
export FLASK_APP=hello.py # one-time thing, to set the env var
flask run

9. FLASK APPLICATION FACTORY PATTERN - official structure of a FLASK_APP
description 0:44:25 

10. Init file in "web_app" directory:

# web_app/__init__.py

from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)

11. Home routes: read up on 
https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/
https://flask.palletsprojects.com/en/1.1.x/blueprints/

# web_app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    x = 2 + 2
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    return "About me"

12. hello.py is not necessary anymore - Delete

13. Running the Flask App, after new "web_app" organizational structure in place:

# Mac:
FLASK_APP=web_app flask run

# Windows:
set FLASK_APP=web_app # one-time thing, to set the env var
flask run

or

export FLASK_APP=web_app # one-time thing, to set the env var
flask run

14. README.md

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


15. 1st commit 
git status
git add .
git commit -m 'msg 1'
git push origin master



#Part 2 1:07:28
CREATE API END POINT
... return json data
... return html pages
... connect app to db



16. Book routes:
... comment out the lasts two routes to focus on the first two
... we will use books (hard coded db) before connecting to db
...
... there is a function that returns something [json, html]
... with a route decorator
... which is on our Blueprint Object
...
... render_template() 
.....provides html and data parameter we want to project to the page
.....with the help of jinja

# web_app/routes/book_routes.py

from flask import Blueprint, jsonify, request, render_template #, flash, redirect

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_books():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    return jsonify(books)

@book_routes.route("/books")
def list_books_for_humans():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    return render_template("books.html", message="Here's some books", books=books)

@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    return jsonify({
        "message": "BOOK CREATED OK (TODO)",
        "book": dict(request.form)
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect(f"/books")

17. web_app/routes/book_routes.py
open web_app/routes/book_routes.py
begin to type html>down arrow>html:5>tab autofills
insert in <body>  </body>

<h2>Welcome to the Books Page</h2>

    <p>{{ message }}</p>

    {% if books %}
        <ul>
        {% for book in books %}
            <li>{{ book["title"] }}</li>
        {% endfor %}
        </ul>

    {% else %}
        <p>Books not found.</p>
    {% endif %}


18. in __init__.py file
connect book routes to our web app
or
tell our app about book routes

... from web_app.routes.book_routes import book_routes
...app.register_blueprint(book_routes)

19. test out new book route
export FLASK_APP=web_app
flask run
localhost:5000/books
...yay its shows our message var and books list
localhost:5000/books.json
...gives us json
20. git commit
git add .
git commit -m 'Use jinja to insert dyanmic contents in to the HTML page
git push origin master

21. back to book_routes.py
uncomment last two routes
... determine our ability to pass data to a web form 
... and do something with it. wow INPUT FOR A WEB PAGE
... and store in the database
TODO: how to navigate to /books/new

22. create NEW FORM web_app/templates/new_book.html
NEW FORM 
method POST
... SENT IN DICT in two keys "book_title", "author_name"
.....sent to server
/books/create
... flask request.form  collect data submitted to the form
.....TODO: store in database
<!-- web_app/templates/new_book.html -->

{% extends "layout.html" %}

{% block content %}

    <h1>New Book Page</h1>

    <p>Please fill out the form and submit to create a new book!</p>

    <form action="/books/create" method="POST">

        <label>Title:</label>
        <input type="text" name="book_title" placeholder="Book XYZ" value="Book XYZ">

        <label>Author:</label>
        <select name="author_name">
          <option value="A1">Author 1</option>
          <option value="A2">Author 2</option>
          <option value="A3">Author 3</option>
        </select>

        <button>Submit</button>
    </form>
{% endblock %}

@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():
    print("FORM DATA:", dict(request.form))

    # INSERT INTO books ...
    new_book = Book(title=request.form["book_title"], author_id=request.form["author_name"])
    db.session.add(new_book)
    db.session.commit()

    return jsonify({
        "message": "BOOK CREATED OK (TODO)",
        "book": dict(request.form)
    })
    # flash(f"Book '{new_book.title}' created successfully!", "success")
    # return redirect(f"/books")

22. Let's run it 1:39:51
export FLASK_APP=web_app
flask run
localhost:5000/books/new
book_title = "Unleash the Power Within", author_name = "A1"
returns
{"book":{"author_name":"A1","book_title":"Unleash the Power Within"},"message":"BOOK CREATED OK (TODO)"}

23. git commit -m 'New Book Form'

24. What we did so far
... Learned about http: request and response
... setup flask app and some examples routes 
... routes to get a response : text 
... routes to return more advanced responses : json data, html data
... with html pages we render those pages with content both : static and dynamic with jinja template language
... created pages to store data in the database
... created pages to fetch data from the database


25. Part 3 goals
... configure a local sqlite db
... setup a books table
... modify routes to store data in the database when we use our form : new book form
... /books.html or /books.json return results from the database

... html in the browser == FRONT END
... BACK END == what is happening behind the scenes
... connect app to the database

26. Flask-SQLAlchemy
https://github.com/pallets/flask-sqlalchemy/
https://flask-sqlalchemy.palletsprojects.com/en/2.x/
https://flask-migrate.readthedocs.io/en/latest/

ORM == Object Relational Map 

Flask-SQLAlchemy gives use database access in an Object Class 
Flask-Migrate help us create and drop databases in the command line

Defining database model class(es):

# web_app/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    author_id = db.Column(db.String(128))

    def __repr__(self):
        return f"<Book {self.id} {self.title}>"
    
def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON

    Param: database_records (a list of db.Model instances)

    Example: parse_records(User.query.all())

    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records


27. update __init__.py file
... configure database and tell our app to know about it
... migrate the database


In Software development model refers to 
... the class to interact with database

TO CONFIGURE THE DATABASE
add to __init__.py

from web_app.models import db, migrate

DATABASE_URL = "sqlite:///web_app_101.db" # using relative filepath
#DATABASE_URL = "sqlite:////Users/Username/Desktop/your-repo-name/web_app_99.db" # using absolute filepath on Mac (recommended)
#DATABASE_URL = "sqlite:///C:\\Users\\Username\\Desktop\\your-repo-name\\web_app_99.db" # using absolute filepath on Windows (recommended) h/t: https://stackoverflow.com/a/19262231/670433


TO LET THE APP KNOW ABOUT THE DATABASE
add to __init__.py def create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)



28. COMMANDS TO MIGRATE THE DATABASE add to README.md

Creating and migrating the database:

# Windows users can omit the "FLASK_APP=web_app" part...

FLASK_APP=web_app flask db init #> generates app/migrations dir

# run both when changing the schema:
FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=web_app flask db upgrade #> creates the specified tables



29. TRY TO CONNECT TO DB WITH TABLEPLUS USING RELATIVE FILE PATH
... connect
after migrate
... creates table


30. root directory add .gitignore
# ignore local database stuff:
migrations/
*.db

31. git commit -m 'Setup local database'


32. add to 
@book_routes.route("/books/create", methods=["POST"])
def create_book():@routebook/create

    # INSERT INTO books ...
    new_book = Book(title=request.form["book_title"], author_id=request.form["author_name"])
    db.session.add(new_book)
    db.session.commit()


33. add to
@book_routes.route("/books")
def list_books_for_humans():

    # this replaces the hard coded dictionary books={}
    # SELECT * FROM books
    book_records = Book.query.all()
    print(book_records)

    # additional func from mike r. to present books
    books = parse_records(book_records)  # converts to dict OPTIONALLY



34. add to book_routes.py
from web_app.models import Book, db, parse_records



35. flask run # check the app
http://127.0.0.1:5000/
http://127.0.0.1:5000/about 
http://127.0.0.1:5000/books/new # insert
http://127.0.0.1:5000/books # select from db



36. git commit -m 'lecture 1 objectives completed'




LECTURE #2 - https://www.youtube.com/watch?v=KzMsdjvye3E&feature=youtu.be
Objectives:
Student should be able to connect to the Twitter API and query for tweets by various parameters
Student should be able to connect to Basilica API and retrieve and manipulate embeddings for given entities


1. Installing package dependencies:
conda deactivate
pipenv install python-dotenv requests basilica tweepy
pipenv shell



2. study for Sprint Challenge
Part 0 (Bonus / SC Hint)
If you're working with an API that doesn't provide its own Python package interface, 
one option is to use the requests package to directly issue HTTP requests to the given API.

Using the requests package to issue HTTP requests:

https://github.com/psf/requests
https://requests.readthedocs.io/en/master/
https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json
https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/requests.md
A simple example API to get started with (can use API KEY "abc123"):

https://www.alphavantage.co/
https://www.alphavantage.co/documentation/#daily


3. Basilica API - Word2Vec https://www.basilica.ai/quickstart/python/
reason we are using Basilica 
to analyze our tweets so we can build predictive model

create
web_app.services.basilica_services.py

import basilica
sentences = [
    "This is a sentence!",
    "This is a similar sentence!",
    "I don't think this sentence is very similar at all...",
]
with basilica.Connection('29644820-0fb3-5c6f-bc91-4081ab51bd20') as c:
    embeddings = list(c.embed_sentences(sentences))
print(embeddings)
[[0.8556405305862427, ...], ...]



4. Refactoring code to fix purpose

'29644820-0fb3-5c6f-bc91-4081ab51bd20' looks like the api key
API_KEY = '29644820-0fb3-5c6f-bc91-4081ab51bd20' #TODO: use env var

web_app.services.basilica_services.py

import basilica
from basilica import Connection

API_KEY = '29644820-0fb3-5c6f-bc91-4081ab51bd20' #TODO: use env var

sentences = [
    "This is a sentence!",
    "This is a similar sentence!",
    "I don't think this sentence is very similar at all...",
]

connection =  Connection(API_KEY)
print("CONNECTION", type(connection))

embeddings = list(connection.embed_sentences(sentences))
print(embeddings)

breakpoint() # ADD A BREAKPOINT TO SEE WHAT OTHER METHODS ARE AVAILABLE



5. python web_app/services/basilica_service.py # with breakpoint

dir(connection)
embedding = connection.embed_sentence("Hello World!!!")
type(embedding) # <class 'list'>
type(embedding[0]) # <class 'float'>
len(embedding) # 768

6. add environment variables
web_app/services/basilica_service.py
import os
from dotenv import load_dotenv


.env
API_KEY = '29644820-0fb3-5c6f-bc91-4081ab51bd20'



7. restructure  web_app/services/basilica_service.py
to make connection available for other files

import basilica
from basilica import Connection
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")

# could use a function here to return our connection
# could use a class
connection = Connection(API_KEY)
print("CONNECTION", type(connection))

if __name__ == '__main__':

    sentences = [
        "This is a sentence!",
        "This is a similar sentence!",
        "I don't think this sentence is very similar at all...",
    ]

    embeddings = list(connection.embed_sentences(sentences))
    print(embeddings)

    embedding = connection.embed_sentence("Hello World!!!")
    print(type(embedding)) # <class 'list'>
    print(type(embedding[0])) # <class 'float'>
    print(len(embedding)) # 768


8. git commit -m 'Basilica Service'
... have shown ability to use the basilica API


9. Lecture 2 Part 2 - Twitter API 0:45:20
user info
user lastest tweets

https://developer.twitter.com/en/docs
http://docs.tweepy.org/en/latest/getting_started.html # python pkg api to access twitter api
# tweepy # getting started


create web_app/service/twitter_service.py

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user("s2t2")


10. log into developer.twitter.com     gmail account login?
get API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
regenerate if necessary

# these are not just made up creditials 
TWITTER_API_KEY = 'so5ySdP7lbARylG'
TWITTER_API_SECRET_KEY = '6V6uDCq5O7mDxaMeOn4Xp3nwy83'
TWITTER_ACCESS_TOKEN = '128648prkud9knC9iyKJJhMXC'
TWITTER_ACCESS_TOKEN_SECRET = 'dLvOqVBj7D9NUIcwYlsaTVWr'



11. rewriting file
web_app/service/twitter_service.py


import tweepy
from tweepy import OAuthHandler, API #add 
import os #add
from dotenv import load_dotenv #add

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET_KEY")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = API(auth)
print("API CLIENT", api)

user = api.get_user("s2t2")
print("TWITTER USER:", type(user))

breakpoint() # to see what is going on with this data


12.  python web_app/services/twitter_service.py # with breakpoint

dir(api)
from pprint import pprint
pprint(dir(api)) # formatted better list
user # print user
pprint(user._json)
#### check API REFERENCE in tweety.org how to get tweets

user = api.get_user("s2t2")
type(user) #> <class 'tweepy.models.User'>
user.id
user.screen_name
user.name

tweets = api.user_timeline("s2t2", tweet_mode="extended") #> <class 'tweepy.models.ResultSet'>
type(tweets) #> <class 'tweepy.models.Status'>

tweet = tweets[0]
dir(tweets[0])
pprint(tweets[0]._json)
tweet.id
tweet.full_text 


13. .env  : always in the root directory 
store all your twitter creds and basilica


14. restructure  web_app/services/twitter_service.py
web_app/services/twitter_service.py

import tweepy
from tweepy import OAuthHandler, API 
import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET_KEY")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# could use a function here to return our api client
# could use a class

auth = OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print("API AUTH: ", auth)

api = API(auth)
print("API CLIENT", api)

if __name__ == "__main__":

    user = api.get_user("s2t2")
    print("TWITTER USER:", type(user)) #> <class 'tweepy.models.User'>
    print(user.id)
    print(user.screen_name)
    print(user.name)

    tweets = api.user_timeline("s2t2", tweet_mode="extended") #> <class 'tweepy.models.ResultSet'>
    print("TWEETS", type(tweets)) #> <class 'tweepy.models.Status'>

    tweet = tweets[0]
    print(tweet.id)
    print(tweet.full_text)


15. git commit -m 'Twitter Service'






Lecture 2 Part 3 1:19:45
we want
... for a given twitter user, fetch info about that user and store in db
... fetch all their recent tweets and store them in the db
... for all their coresponding tweets get all the embedding 
... store embedding for each tweet

set up views and routes to perform these actions

1. Twitter Routes (Iteration 3, storing users and tweets and embeddings in the database):

# web_app/routes/twitter_routes.py

from flask import Blueprint, render_template, jsonify
from web_app.models import db, User, Tweet, parse_records
from web_app.services.twitter_service import api as twitter_api_client
#from web_app.services.basilica_service import basilica_api_client

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user(screen_name=None):
    print(screen_name)

    # FETCHING DATA FROM THE TWITTER API
    twitter_user = api.get_user(screen_name)
    tweets = api.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    print("TWEETS COUNT:", len(tweets))
    #return jsonify({"user": user._json, "tweets": [s._json for s in statuses]})

    # STORING TWITTER DATA IN THE DATABASE   #SIMILAR TO /BOOKS/CREATE
    # get existing user from the db or initialize a new one:
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count
    db.session.add(db_user)
    db.session.commit()
   # #return "OK"
   # #breakpoint()


   # all_tweet_texts = [status.full_text for status in statuses]
   # embeddings = list(basilica_api.embed_sentences(all_tweet_texts, model="twitter"))
   # print("NUMBER OF EMBEDDINGS", len(embeddings))

   ## TODO: explore using the zip() function maybe...
   # counter = 0
   # for status in statuses:
   #     print(status.full_text)
   #     print("----")
   #     #print(dir(status))
   #     # get existing tweet from the db or initialize a new one:
   #     db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
   #     db_tweet.user_id = status.author.id # or db_user.id
   #     db_tweet.full_text = status.full_text
   #     #embedding = basilica_client.embed_sentence(status.full_text, model="twitter") # todo: prefer to make a single request to basilica with all the tweet texts, instead of a request per tweet
   #     embedding = embeddings[counter]
   #     print(len(embeddings))
   #     db_tweet.embedding = embeddings
   #     db.session.add(db_tweet)
   #     counter+=1
   # db.session.commit()
   # #breakpoint()
   return "OK"
   # #return render_template("user.html", user=db_user, tweets=statuses) # tweets=db_tweets



2. CREATE User and Tweet in web_app/model.py

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    screen_name = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String)
    location = db.Column(db.String)
    followers_count = db.Column(db.Integer)
    #latest_tweet_id = db.Column(db.BigInteger)

class Tweet(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey("user.id")) # relationship between User and Tweet
    full_text = db.Column(db.String(500))
    embedding = db.Column(db.PickleType)

    user = db.relationship("User", backref=db.backref("tweets", lazy=True))
    #this makes theses available == automatic joins
    # Tweet.user  and   User.tweets

def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON

    Param: database_records (a list of db.Model instances)

    Example: parse_records(User.query.all())

    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records


3. for web_app/models.py

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    screen_name = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String)
    location = db.Column(db.String)
    followers_count = db.Column(db.Integer)
    #latest_tweet_id = db.Column(db.BigInteger)

class Tweet(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey("user.id")) # relationship between User and Tweet
    full_text = db.Column(db.Unicode(500))
    embedding = db.Column(db.PickleType)

    user = db.relationship("User", backref=db.backref("tweets", lazy=True))
    #this makes theses available == automatic joins
    # Tweet.user  and   User.tweets



4.  web_app/routes/twitter_routes/def fetch_user

    # STORING TWITTER DATA IN THE DATABASE

    # get existing user from the db OR initialize a new one:
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)

    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count
    db.session.add(db_user)
    db.session.commit()
    return "OK, got it dude!"
    #breakpoint()


5. migrate the database : creates tables(migrate) and commits(upgrade) them
flask db migrate #> creates the db (with "alembic_version" table)
flask db upgrade #> creates the specified tables

6. test - flask run
localhost:5000/users/s2t2/fetch # > OK, got it dude!
check tablePlus for user table and tweet table

7. flask shell - example
$ flask shell
>>> from web_app.routes.twitter_routes import fetch_user
>>> fetch_user('s2t2') #note screen_name is a string must pass a string
s2t2
TWEETS COUNT: 150


8. twitter_routes.py
cleaned up file 

from web_app.services.basilica_service import connection as basilica_api_client

db.session.commit()
return "OK tweet"



9. test - flask run
localhost:5000/users/s2t2/fetch # > OK, got it dude!
### this takes a while ITS TOO SLOW..


10. git commit -m "Storing users and tweets in the db"
git add . 
git commit -m "Storing users and tweets in the db"
git push origin master



11.  

    # STORING TWITTER DATA IN THE DATABASE
    all_tweet_texts = [status.full_text for status in tweets]
    embeddings = list(basilica_api_client.embed_sentences(all_tweet_texts, model="twitter"))
    print("NUMBER OF EMBEDDINGS", len(embeddings))
    
    for index, status in enumerate(tweets):
        print(index)
        print(status.full_text)
        print("----")

        # embedding = basilica_api_client.embed_sentence(status.full_text, model="twitter") # todo: prefer to make a single request to basilica with all the tweet texts, instead of a request per tweet
        # print(len(embedding))
        embedding = embeddings[index]

        # get existing tweet from the db or initialize a new one:
        db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)

        db_tweet.user_id = status.author.id # or db_user.id
        db_tweet.full_text = status.full_text
        db_tweet.embedding = embedding
        db.session.add(db_tweet)
        
    db.session.commit()
    return "OK tweet"


12. git commit -m 'More Performant approach'
git add . 
git commit -m 'More Performant approach'
git push origin master



13.  2:05:00 question about a visual of the web_app





Lecture 3 - Part 1  https://www.youtube.com/watch?v=z4Vm1gqsCOI&feature=youtu.be
Objectives
Run and report simple online analysis of data from the user or an API
Run a more complicated offline model, and serialize the results for online use

1. install libraries
$ pipenv install scikit-learn



2. create web_app/iris_classifier.py

#web_app/iris_classifier.py
import os
import pickle

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression # for example

MODEL_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "models", "latest_model.pkl")

def train_and_save_model():
    print("TRAINING THE MODEL...")
    X, y = load_iris(return_X_y=True)
    #print(type(X), X.shape) #> <class 'numpy.ndarray'> (150, 4)
    #print(type(y), y.shape) #> <class 'numpy.ndarray'> (150,)
    classifier = LogisticRegression() # for example
    classifier.fit(X, y)

    print("SAVING THE MODEL...")
    with open(MODEL_FILEPATH, "wb") as model_file:
        pickle.dump(classifier, model_file)

    return classifier

def load_model():
    print("LOADING THE MODEL...")
    with open(MODEL_FILEPATH, "rb") as model_file:
        saved_model = pickle.load(model_file)
    return saved_model

if __name__ == "__main__":

    train_and_save_model()

    exit()  #run section by section


    clf = load_model()
    print("CLASSIFIER:", clf)

    X, y = load_iris(return_X_y=True) # just to have some data to use when predicting
    inputs = X[:2, :]
    print(type(inputs), inputs)

    result = clf.predict(inputs)
    print("RESULT:", result)


3. create root/models folder


4. $ python web_app/iris_classifier.py
TRAINING THE MODEL...
C:\Users\jeffr\.virtualenvs\WebApp101-hdUGlVey\lib\site-packages\sklearn\linear_model\_logistic.py:762: ConvergenceWarning: lbfgs failed to converge (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

Increase the number of iterations (max_iter) or scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
  n_iter_i = _check_optimize_result(
SAVING THE MODEL...



5. check out root/model/lastest_model.pkl 
this is a binary file
this is not encryption
this is just a saved version


6. modify  root/model/lastest_model.pkl

if __name__ == "__main__":
    # train_and_save_model()
    # exit() # run section by section


    clf = load_model()
    print("CLASSIFIER:", clf)

    X, y = load_iris(return_X_y=True) # just to have some data to use when predicting
    inputs = X[:2, :]
    print(type(inputs), inputs)

    result = clf.predict(inputs)
    print("RESULT:", result)



7. $ python web_app/iris_classifier.py
LOADING THE MODEL...
CLASSIFIER: LogisticRegression()
<class 'numpy.ndarray'> [[5.1 3.5 1.4 0.2]
 [4.9 3.  1.4 0.2]]
RESULT: [0 0]

... it loaded the pikled model
... and made a prediction


8. pretrain model VS train on the fly               0:30:45
do you have to train for each set of ppl you compare tweets
yes!!!




9.  36:56  talking about build  


10. git commit -m "trained a model and save pkl"
Demonstrate how to save a pretrained model




LECTURE 3 PART 2    0:49:57

1. create 
<!-- web_app/templates/prediction_form.html -->


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <h2>Prediction Time</h2>

    <p>Use the form below to predict which user is more likely to say a given tweet...</p>

    <form action="/predict" method="POST">

        <!-- TODO: Instead of hard-coding these drop-down menu options, dynamically populate them based on user records from the database -->
        <label>Twitter User A:</label>
        <select name="screen_name_a">
            <option value="elonmusk" selected="true">@elonmusk</option>
            <option value="justinbieber">@justinbieber</option>
            <option value="s2t2">@s2t2</option>
        </select>
        <br>

        <!-- TODO: Instead of hard-coding these drop-down menu options, dynamically populate them based on user records from the database -->
        <label>Twitter User B:</label>
        <select name="screen_name_b">
            <option value="elonmusk">@elonmusk</option>
            <option value="justinbieber" selected="true">@justinbieber</option>
            <option value="s2t2">@s2t2</option>
          </select>
        <br>

        <label>Tweet Text:</label>
        <input type="text" name="tweet_text" placeholder="Tesla Model S production facility is great" value="Tesla Model S production facility is great">
        <br>

        <button>Submit</button>
    </form>


</body>
</html>


2. Let's make the prediction_form.html our homepage

goto home_routes.py
and change "index" to hello

@home_routes.route("/hello") ### change from "/" to "/hello"
def hello():  ####  change "index" to "hello"
    x = 2 + 2
    return f"Hello World! {x}"



3. setup new HOME PAGE in home_routes.py
from flask import Blueprint, render_template

@home_routes.route("/")
def index():
    return render_template("prediction_form.html")



4. create web_app/routes/stats_routes.py
# web_app/routes/stats_routes.py

from flask import Blueprint, request, jsonify, render_template
#from sklearn.linear_model import LogisticRegression # for example
#from web_app.models import User, Tweet
#from web_app.services.basilica_service import basilica_api_client

stats_routes = Blueprint("stats_routes", __name__)

@stats_routes.route("/predict", methods=["POST"])
def predict():
    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form)) 
    #> {'screen_name_a': 'elonmusk', 'screen_name_b': 's2t2', 'tweet_text': 'Example tweet text here'}
    screen_name_a = request.form["screen_name_a"]
    screen_name_b = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]

    print("-----------------")
    print("FETCHING TWEETS FROM THE DATABASE...")
   
    #TODO

    print("-----------------")
    print("TRAINING THE MODEL...")
    

    print("-----------------")
    print("MAKING A PREDICTION...")

    # TODO
    
    return render_template("prediction_results.html",
        screen_name_a=screen_name_a,
        screen_name_b=screen_name_b,
        tweet_text=tweet_text,
        screen_name_most_likely="TODO" #result[0]
    )

#TODO REGISTER new stats_routes.py ROUTE IN __init__.py



5. create predicition_result.html file

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>Results!</h2>

    <p>Between '@{{ screen_name_a }}' and '@{{ screen_name_b }}',
        the user who is most likely to say '{{ tweet_text }}'
        is '@{{ screen_name_most_likely }}'
    </p>
</body>
</html>


#TODO REGISTER new stats_routes.py ROUTE IN __init__.py



6. goto to __init__.py and import the 
from web_app.routes.stats_routes import stats_routes ############### Add this

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(stats_routes)    ######################## Add this
    return app



7. flask run
in prediction form type in "pizza hut is great"
next page is prediction result page with prediction == TODO

Yay! its working. without model

