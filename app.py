from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from profile_svc import access, register
from task_svc import task
import os
import socket

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/dev"
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
mongo = PyMongo(app)
db = mongo.db


@app.route("/")
def index():
    hostname = socket.gethostname()
    return jsonify(
        message="Welcome to the personal tasks app! I am running inside {} pod!".format(hostname)
    )

###### calling the user tasks through API ######

@app.route("/tasks")
def get_all_tasks():
    tasks = task.gettasks()
    return tasks

@app.route("/task/add", methods=["POST"])
def create_task():
    data = request.get_json(force=True)
    message = task.addtask(data)
    return jsonify(
        message=message
    )

@app.route("/task/<id>", methods=["PUT"])
def update_task(id):
    data = request.get_json(force=True)
    message = task.updatetask(id, data)
    return jsonify(
        message=message
    )

@app.route("/task/<id>", methods=["DELETE"])
def delete_task(id):
    message = task.deletetask(id)
    return jsonify(
        message=message
    )

###### calling the user profile through API ######

@app.route("/profile/add", methods=["POST"])
def add_property():
    data = request.get_json(force=True)
    message = register.addproperty(data)
    return message

@app.route("/profile")
def get_profile():
    profile = access.getprofile()
    return profile

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
