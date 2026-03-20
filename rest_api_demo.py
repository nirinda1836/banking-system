from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    users.append(data)
    return jsonify(data)

@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.json
    return jsonify({"id": id, "data": data})

app.run(debug=True)