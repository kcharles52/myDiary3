[![Build Status](https://travis-ci.org/kcharles52/myDiary3.svg?branch=develop)](https://travis-ci.org/kcharles52/myDiary3)[![Coverage Status](https://coveralls.io/repos/github/kcharles52/myDiary3/badge.svg?branch=develop)](https://coveralls.io/github/kcharles52/myDiary3?branch=develop)[![Maintainability](https://api.codeclimate.com/v1/badges/8b6db8a4e63923bfaa4c/maintainability)](https://codeclimate.com/github/kcharles52/myDiary3/maintainability)
# My Diary Application
This is an online application that helps users to record their memories.

## Prerequists
You must have the following installed on your computer
* Git - This is a version control system
* Python - This is a programming languange
* Postman - This an application used to send different types of requests to an application program interface (API)
* Postgres - This is a database management software

## How to setup the project
### For linux and Mac operating system follow the following steps

* clone the repository onto your computer with the command
    >`$git clone https://github.com/kcharles52/mydiary3`
* change to the directory that contains the cloned copy of the project
    >`$cd mydiary3`
* Create a virtual environment
  > `$python3 -m venv env`
* Activate the virtual environment
  > `$source myenv/bin/activate`
* Install dependencies in the virtual environment
  > `$pip install -r requirements.txt`

##  How to Run the application
* Use this command to run the application
  > `$python3 run.py`
* View a sample endpoint in postman at http://127.0.0.1:5000/api/v1/auth/signup

## Testing frame work
* nosetests - This is a python testing framework

## How to run the tests
* use the following command to run tests
  > `$nosetests --with-coverage`


## Endpoints
HTTP Method|End point |Action        |Note
-----------------|---------------------------|--------------|--------------
POST | /api/v1/auth/signup | Register a user|
POST | /api/v1/auth/login | Login a user|
GET| /api/v1/entries   | Fetch all entries for a user
GET | /api/v1/entry/<entry_Id> | Fetch the details of an entry for a user |
POST | /api/v1/entry | Add an entry|
PUT | /api/v1/entries/<entry_id>/ | Modify a diary entry|An entry can only be modified on the same day it was created.
DELETE | /api/v1/entries/<entry_id>/ | Delete a diary entry|An entry can only be modified on the same day it was created.



## Author
[Kato Charles](https://github.com/kcharles52)
