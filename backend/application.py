#this is a file, it's fun

from flask import Flask, request, jsonify
import json
import fileIO
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

USER_DIRECTORY = "./users/"

@app.get("/")
def hello_world():
    sample_dict = {"test": "123", "testing": "456"}
    sample_dict = json.dumps(sample_dict)
    return sample_dict

# @app.post("/api/account/create_account")
def create_account():
    username = request.get_json()["username"]
    password = request.get_json()["password"]
    user_dict = {"username": username, "pass": password}
    user_dict = fileIO.create_file(json.dumps(user_dict))
    user_dict = json.loads(user_dict)
    return json.dumps(user_dict) # should be a cookie

@app.post('/api/account/login')
def login():
    username = request.get_json()["username"]
    password = request.get_json()["password"]
    if (username != '') and ( password != ''):
        user_dict = {"username": username, "pass": password}
        user_dict = json.dumps(user_dict)
        user_file = fileIO.read_file(user_dict)
        if(user_file == -1):
            data = create_account()
        user_dict = json.loads(user_file)
        if password == user_dict["pass"]:
            data =  user_file
        else:
            errDict = {"ERROR": "password no worky"}
            data = json.dumps(errDict)
    else:
        errDict = {"ERROR": "you gave me some bad stuff"}
        data = errDict
        
    resp = json.loads(data)
    if(resp["ERROR"]):
        response = app.response_class(response= data, status=403, mimetype = 'application/json')
    else:
        response = app.response_class(response= data, status=200, mimetype = 'application/json')

    return response

@app.post('/api/add_todo')
def add_todo():
    userID = request.get_json()["userID"]
    find_username_by_id();
    # username = find_username_by_id()
    taskname = request.get_json()["taskname"]
    # fileIO.create_file() # no username found yet
    return "it worked!"

def find_username_by_id():
    if os.path.exists(USER_DIRECTORY):
        for file in (os.listdir(USER_DIRECTORY)):
            userID_to_compare = fileIO.read_file(file)
            userID_to_compare = json.loads(userID_to_compare)
    else:
        os.makedirs(USER_DIRECTORY)
    # for file in os.listdir(USER_DIRECTORY):
