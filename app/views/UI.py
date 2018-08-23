from flask import Blueprint, render_template


#create blue print
UI = Blueprint('UI',__name__)

@UI.route('/' )
def index():
    return render_template('index.html')
