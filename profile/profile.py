from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/dev"
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
mongo = PyMongo(app)
db = mongo.db

@app.route("/profile")
def get_user_profile():
    users = db.user.find()
    property_list = []
    for user in users:
        item = {
            "Id": str(user["_id"]),
            "Property": str(user["name"]),
            "Value": user["value"]
        }
        property_list.append(item)
    return jsonify(
        profile = property_list
    )

@app.route("/profile/add", methods=["POST"])
def add_property():
    data = request.get_json(force=True)
    property = db.user.find_one({"name": data["name"]})
    if property:
        message = "Property already exist!"
    else:
        db.user.insert_one({"name": data["name"], "value": data["value"]})
        message="User profile property added successfully!"
    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)