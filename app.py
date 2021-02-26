from flask import Flask, render_template, redirect, url_for, request

# from flask_pymongo import PyMongo
# import scrape_mars import scrape_mars

#create instance of Flask app
app=Flask(__name__)

# hemisphere_image_urls = [
#     {"title":"Cerberus", "img_url": cerberus},
#     {"title":"Schiaparelli", "img_url":schiaparelli},
#     {"title":"Surtis", "img_url":syrtis},
#     {"title":"Valles", "img_url":valles}
# ]

#create rout that renders index.html template
@app.route("/")

def index():
    return render_template("index.html", hemisphere_image_urls=hemisphere_image_urls)





    if __name__ == "__main__":
        app.run(debug=True)




    