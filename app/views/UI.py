from flask import Blueprint, render_template


#create blue print
UI = Blueprint('UI',__name__)

@UI.route('/', methods=['GET','POST'])
@UI.route('/index.html', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@UI.route('/signup.html', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@UI.route('/welcome.html', methods=['GET'])
def home():
    return render_template('welcome.html')
