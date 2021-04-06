import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

'''App's paths, functions helping to let the user "do CRUD":
Homepage with search bar,create recipes, retrieve, update, and delete recipes
list of categories returned to provide the dropdown category menu'''


@app.route('/')
def home():
    all_categories = list(mongo.db.categories.find())
    return render_template("index.html", categories=all_categories)

    # Host,Port and Debug set
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=False)
