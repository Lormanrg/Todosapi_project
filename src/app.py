from flask import Flask, request, jsonify

app = Flask(__name__)

todolist= [
    {
        "done": True,
        "label": "Sample Todo 1"
    },
    {
        "done": True,
        "label": "Sample Todo 2"
    }
]

@app.route("/todos", methods= ["GET"])
def get_todos():
    if request.method == "GET":
        return jsonify(todolist), 200



 
@app.route("/todos_add", methods=["POST"])
def addtask():
    if request.method == "POST":
        body = request.json
        if body.get("label") is None:
            return jsonify("Message: Wrong property"), 400
        if body.get("done") is None:
            return jsonify("Message: Wrong property"), 400
        todolist.append(body)
        return todolist, 201

# @app.route("/todos", methods=["PUT"])

@app.route("/todos_delete/<int:position>", methods=["POST"])
def todos_delete(position=None):
    todolist.pop(position)
    return jsonify(todolist),201
      
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3001", debug=True)