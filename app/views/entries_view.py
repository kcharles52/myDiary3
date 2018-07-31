from  flask import Blueprint, jsonify, request, make_response
import datetime

from ..models.diaryEntries_model import DiaryEntry

#create entries blueprint
entries = Blueprint('entries',__name__)


