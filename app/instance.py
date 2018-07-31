#imports
from flask import Flask
from .views.users_auth import users
from .views.entries_view import entries

#create flask application
app = Flask(__name__)

#Add blueprints to the flask application instance
app.register_blueprint(users)
app.register_blueprint(entries)