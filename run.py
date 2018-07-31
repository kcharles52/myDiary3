from flask import Flask
from config import app_configuration


def create_app(mode):
    """This method is used to create a flask application with the specified mode"""
    app = Flask(__name__)

    app.config.from_pyfile('config.py')
    app.config.from_object(app_configuration[mode])

    return app


app = create_app("development")


if __name__ == "__main__":
    app.run()
