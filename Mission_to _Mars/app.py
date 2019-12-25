from flask_pymongo import PyMongo
import mission_to_mars
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_mars"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    news = mongo.db.news.find_one()
    images = mongo.db.images.find_one()
    twitter = mongo.db.twitter.find_one()
    facts = mongo.db.facts.find_one()
    hemisphere = mongo.db.hemisphere.find_one()
    return render_template("index.html", news=news, images=images, twitter=twitter, facts=facts, hemisphere=hemisphere)


@app.route("/scrape")
def scraper():
    news = mongo.db.news
    news_data = mission_to_mars.scrape_news()
    news.update({}, news_data, upsert=True)

    images = mongo.db.images
    images_data = mission_to_mars.scrape_images()
    images.update({}, images_data, upsert=True)

    twitter = mongo.db.twitter
    twitter_data = mission_to_mars.scrape_twitter()
    twitter.update({}, twitter_data, upsert=True)

    hemisphere = mongo.db.hemisphere
    hemisphere_data = mission_to_mars.scrape_hemispheres()
    hemisphere.update({}, hemisphere_data, upsert=True)

    facts = mongo.db.facts
    facts_data = mission_to_mars.scrape_facts()
    facts.update({}, facts_data, upsert=True)

    return redirect("/", code=302)
    # return jsonify(news_data, images_data, twitter_data, hemisphere_data, facts_data)


if __name__ == "__main__":
    app.run(debug=True)
