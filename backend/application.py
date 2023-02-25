#this is a file, it's fun

from flask import Flask, request, jsonify
import json
import fileIO

app = Flask(__name__)

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
    fileIO.create_file(json.dumps(user_dict))
    return "woohoo this thing is working"

@app.get("/api/account/login")
def login():
    pass

