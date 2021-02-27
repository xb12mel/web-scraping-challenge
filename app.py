from flask import Flask, render_template, redirect, jsonify
# from flask_pymongo import PyMongo
# import scrape_mars import scrape_mars

#create instance of Flask app
app=Flask(__name__)


#create rout that renders index.html template
@app.route("/")
def echo():
    return render_template("index.html", text="Web Scrape Challenge")
# def index():
    

if __name__ == "__main__":
    app.run(debug=True)




# hemisphere_image_urls = [
#     {"title":"Cerberus", "img_url": cerberus},
#     {"title":"Schiaparelli", "img_url":schiaparelli},
#     {"title":"Surtis", "img_url":syrtis},
#     {"title":"Valles", "img_url":valles}
# ]
    