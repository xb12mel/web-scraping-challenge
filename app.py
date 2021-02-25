from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import  scrape_assignment import scrape_assignment

app=Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:2017/mars_mission'
mongo = PyMongo(app)
@app.route('/')
def index():
    posts = mongo.db.posts.find()
    return render_template("index.html", mars= )

@app.route('/scrape')
def scrape_mars():
    mars_mission = mongo.db.mars_mission
    data = scrape_mars.scrape()


if __name__ == "__main__":
    app.run(debug=True)