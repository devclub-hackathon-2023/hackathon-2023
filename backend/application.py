#this is a file, it's fun

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.get("/")
def hello_world():
    sample_dict = {"test": "123", "testing": "456"}
    sample_dict = json.dump(sample_dict)
    return sample_dict
