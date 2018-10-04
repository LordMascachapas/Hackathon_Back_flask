from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)


@app.route("/")
def init():
    with open("templates_and_src/data.json", "r") as j_file:
        dicc = json.load(j_file)
    return jsonify(dicc)


# acceder a la ruta proporcionada por la terminal
if __name__ == "__main__":
    app.run(debug=True, port=5555)
