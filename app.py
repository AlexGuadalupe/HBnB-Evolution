from flask import Flask
from api.user_api import user_blueprint
from api.amenities_api import amenities_blueprint
from api.review_api import review_blueprint
from api.places_api import places_blueprint
from api.countries_cities_api import countries_cities_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint)
app.register_blueprint(amenities_blueprint)
app.register_blueprint(review_blueprint)
app.register_blueprint(places_blueprint)
app.register_blueprint(countries_cities_blueprint)

if __name__ == '__main__':
    app.run()
