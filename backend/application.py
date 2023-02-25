#this is a file, it's fun

from flask import Flask, request, jsonify
import json
import fileIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/")
def hello_world():
    sample_dict = {"test": "123", "testing": "456"}
    sample_dict = json.dumps(sample_dict)
    return sample_dict

@app.post("/api/account/create_account")
def create_account():
    username = request.get_json()["username"]
    password = request.get_json()["password"]
    user_dict = {"username": username, "pass": password}
    user_dict = fileIO.create_file(json.dumps(user_dict))
    user_dict = json.loads(user_dict)
    return user_dict["userID"] # should be a cookie

@app.post('/api/account/login')
def login():
    username = request.get_json()["username"]
    password = request.get_json()["password"]
    user_dict = {"username": username, "pass": password}
    user_dict = json.dumps(user_dict)
    user_file = fileIO.read_file(user_dict)
    if(user_file == -1):
        return "Error, user not instantiated"
    user_dict = json.loads(user_file)
    if password == user_dict["pass"]:
        return user_file # should be a cookie
    else:
        return "Error, user password did not match"
@app.post("/api/todo/")
def add_todo():
    username = request

