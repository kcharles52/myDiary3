from flask import Blueprint, render_template
from ..views.decorate_endpoint import protected


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
@protected
def home(user):
    return render_template('welcome.html')


@UI.route('/addEntry.html', methods=['GET','POST'])
@protected
def addEntry(user):
    return render_template('addEntry.html')

@UI.route('/diaryentries.html', methods=['GET'])
@protected
def FetchEntries(user):
    return render_template('diaryentries.html')


@UI.route('/diaryentry.html/<int:id>', methods=['GET'])
@protected
def FetchEntry(user,id):
    entryId = id
    return render_template('diaryentry.html', id=entryId)
