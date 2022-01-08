from flask import Flask, jsonify
from function import get_json_item
app = Flask(__name__)



@app.route("/<int:id>")
def page_search(id):
    return jsonify(get_json_item(id))


if __name__ == "__main__":
    app.run(debug=True)