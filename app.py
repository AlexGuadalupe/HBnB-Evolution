from flask import Flask
from api.user_api import user_blueprint
from api.amenities_api import amenities_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint)
app.register_blueprint(amenities_blueprint)

if __name__ == '__main__':
    app.run(host='localhost', port=8081, debug=True)
