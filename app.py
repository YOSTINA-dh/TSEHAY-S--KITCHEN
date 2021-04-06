# Import installed libraries and components to the Python file
import os
import os
from os import path
import re
from flask import Flask, render_template, redirect, request, url_for
if path.exists("env.py"):
    import env

# Define the app, and set the MONGO_URI secret key
app = Flask(__name__)

@app.route('/')
def home():
    all_categories = list(mongo.db.categories.find())
    return render_template("index.html", categories=all_categories)

    # Host,Port and Debug set
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=False)
