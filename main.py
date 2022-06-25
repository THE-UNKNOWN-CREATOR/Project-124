from flask import Flask, jsonify, request


app = Flask(__name__)

contacts = [
    {
        "id": 1,
        "name": u"Name",
        "number": u"9012357890",
        "done": False
    }
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "Error",
            "message": "Please Provide The Data"
        }, 400)
    
    task = {
        "id": contacts[-1]["id"] + 1,
        "name": request.json["title"],
        "number": request.json.get("number", ""),
        "done": False
    }
    
    contacts.append(task)
    return jsonify({
        "status": "Success",
        "message": "Number added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": contacts
    })

if (__name__ == "__main__"):
    app.run(debug=True)