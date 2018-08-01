#imports
from flask import Flask
from .views.users_auth import users
from .views.entries_view import entries
import db

db_instance = db.DatabaseConnection()
db_instance.create_table_users()
db_instance.create_table_entries()



#create flask application
app = Flask(__name__)

#Add blueprints to the flask application instance
app.register_blueprint(users, url_prefix='/api/v1/auth')
app.register_blueprint(entries, url_prefix='/api/v1')
