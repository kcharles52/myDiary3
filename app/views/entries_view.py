from  flask import Blueprint, jsonify, request, make_response
import datetime
from ..models.diaryEntries_model import DiaryEntry
from ..views.decorate_endpoint import protected


#create entries blueprint
entries = Blueprint('entries',__name__)


@entries.route("/entries", methods=["POST"])
@protected
def create_entry(user_id):
    """ Endpoint to create a diary entry given the entry data """
    # get request data
    diary_entry_data = request.get_json()

    #check if entry data is not empty
    if not diary_entry_data:
        return jsonify({"message": "Enter data in all fields"}), 400

    diaryTitle = diary_entry_data.get('diaryTitle')
    date = str(diary_entry_data.get('date')).strip()
    diaryEntryBody = diary_entry_data.get('diaryEntryBody')

    # validate request data
    if not diaryTitle or diaryTitle == "" or diaryTitle == type(int):
        return jsonify({'Message': 'Title is required'}), 400
    if not date or date == "":
        return jsonify({'Message': 'date is required'}), 400
    if not diaryEntryBody or diaryEntryBody == "":
        return jsonify({'Message': 'Field required: Please write someting'}), 400

    new_diary_entry = DiaryEntry(diaryTitle, date, diaryEntryBody, user_id) # review user id
    new_diary_entry.create_entry()

    return jsonify({'Message': 'You have successfully created your entry'}), 201


@entries.route("/entries", methods=["GET"])
@protected
def fetch_entries(user_id):
    myEntries = []
    available_entries = DiaryEntry.fetch_all_entries(user_id)

    if not available_entries or len(available_entries) < 1:
        return jsonify({"Message": "You have no entries"}), 404

    if len(available_entries) >= 1:
        for entry in available_entries:
            myEntries.append(entry)
        return jsonify({
            "Message": "Successfully fetched entries",
            "entries": myEntries
        }), 200

#route for fetching single entry by id
@entries.route('entries/<int:entry_id>', methods=['GET'])
@protected
def get_single_entry(entry_id):
    """ Endpoint to fetch a single entry """
    available_entry = DiaryEntry.fetch_single_entry(entry_id) 
    if len(available_entry) < 1:
        return jsonify({"Message": "Diary Entry Not Found"}), 404
    else:
        return jsonify({'entry': available_entry}), 200
