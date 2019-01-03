from  flask import Blueprint, jsonify, request, make_response
import datetime
from ..models.diaryEntries_model import DiaryEntry
from ..views.decorate_endpoint import protected


#create entries blueprint
entries = Blueprint('entries',__name__)


@entries.route("/entries", methods=["POST"])
@protected
def create_entry(user):
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
        return jsonify({'Message': 'Date is required'}), 400
    if not diaryEntryBody or diaryEntryBody == "":
        return jsonify({'Message': 'Field required: Please write someting'}), 400

    new_diary_entry = DiaryEntry(diaryTitle, date, diaryEntryBody, user['user_id'])
    new_diary_entry.create_entry()

    return jsonify({'Message': 'You have successfully created your entry'}), 201


@entries.route("/entries", methods=["GET"])
@protected
def fetch_entries(user):
    myEntries = []
    available_entries = DiaryEntry.fetch_all_entries(user['user_id'])

    if not available_entries or available_entries==type(None):
        return jsonify({"Message": "You have no entries", "entries":[]}), 200

    if len(available_entries) >= 1:
        for entry in available_entries:
            myEntries.append({"entry_id":entry[0],"diaryTitle":entry[1], "diaryEntryBody":entry[2],"date":str(entry[3]),"userId":entry[4]})
        return jsonify({
            "Message": "Successfully fetched entries",
            "entries": myEntries
        }), 200

#route for fetching single entry by id

@entries.route('entries/<int:entry_id>', methods=['GET'])
@protected
def get_single_entry(user,entry_id):
    """ Endpoint to fetch a single entry """
    entry = DiaryEntry.fetch_single_entry(user['user_id'],entry_id)
    if not entry or entry == type(None) :
        return jsonify({"Message": "Diary Entry Not Found"}), 200
    else:
        return jsonify({'entry': {"entry_id":entry[0],"diaryTitle":entry[1], "diaryEntryBody":entry[2],"date":str(entry[3]),"userId":entry[4]}}), 200

#route for modifying an entry
@entries.route("/entries/<int:entry_id>", methods=['PUT'])
@protected
def modify_entry(user,entry_id):
    """ Endpoint to modify a given entry"""
    available_entry = DiaryEntry.fetch_single_entry(user['user_id'],entry_id)
    if not available_entry or available_entry == type(None):
        return jsonify({"Message": "You have no entries to modify"}), 404

    if len(available_entry) >= 1:
        entry_data = request.get_json()
        diaryTitle = entry_data.get('diaryTitle')
        date = entry_data.get('date')
        diaryEntryBody = entry_data.get('diaryEntryBody')

        modified_entry = DiaryEntry(
                    diaryTitle, date, diaryEntryBody, user['user_id'])
        modified_entry.edit_entry(entry_id)
        return jsonify({
                "entry": modified_entry.__dict__,
                "Message": "You successfully modified your entry"
            }), 201

@entries.route("/entries/<int:entry_id>", methods=['DELETE'])
@protected
def delete_entry(user,entry_id):
    """ Endpoint to delete a given entry"""
    available_entry = DiaryEntry.fetch_single_entry(user['user_id'],entry_id)
    if not available_entry or available_entry == type(None):
        return jsonify({"Message": "You have no entries to delete"}), 404

    if len(available_entry) >= 1:
        # print(available_entry)
        DiaryEntry.delete_entry(entry_id)
        return jsonify({
                "Message": "You successfully deleted your entry"
            }), 200
