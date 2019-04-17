from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    mars_dict = mongo.db.mars_dict.find_one()
    print(mars_dict)
    return render_template("index.html", mars_info=mars_dict)


@app.route("/scrape")
def scraper():
    mars_dict = mongo.db.mars_dict
    mars_data = mission_to_mars.scrape()
    mars_dict.update({}, mars_data, upsert=True)
    return redirect("/", code=302)



app.run(debug=True)
