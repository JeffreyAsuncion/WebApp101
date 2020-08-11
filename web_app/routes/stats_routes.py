# POST /predict  
# web_app/routes/stats_routes.py

from flask import Blueprint, request, jsonify, render_template
from sklearn.linear_model import LogisticRegression
from web_app.models import User, Tweet
# from web_app.services.basilica_service import basilica_api_client

stats_routes = Blueprint("stats_routes", __name__)

@stats_routes.route("/predict", methods=["POST"])
def predict():
    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form)) #> {'screen_name_a': 'elonmusk', 'screen_name_b': 's2t2', 'tweet_text': 'Example tweet text here'}
    screen_name_a = request.form["screen_name_a"]
    screen_name_b = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]

    print("-----------------")
    print("FETCHING TWEETS FROM THE DATABASE...")
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
    # get the embeddings (from database)
    user_a = User.query.filter_by(screen_name=screen_name_a).first()
    user_b = User.query.filter_by(screen_name=screen_name_b).first()

    user_a_tweets = user_a.tweets
    user_b_tweets = user_b.tweets
    print("FETCHED TWEETS", len(user_a_tweets), len(user_b_tweets))

    print("-----------------")
    print("TRAINING THE MODEL...")
    
    # classifier = LogisticRegression()
    # # X values / inputs: embeddings
    # # Y values / labels: screen_names
    # embeddings = []
    # labels = []
    # classifier.fit(embeddings, labels)


    print("-----------------")
    print("MAKING A PREDICTION...")

    # TODO
    
    return render_template("prediction_results.html",
        screen_name_a=screen_name_a,
        screen_name_b=screen_name_b,
        tweet_text=tweet_text,
        screen_name_most_likely="TODO" #result[0]
    )