from flask import Flask
from api.user_api import user_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run()
