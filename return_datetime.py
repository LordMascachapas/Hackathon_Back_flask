from flask import Flask
from flask import jsonify
import json
import datetime
import time

app = Flask(__name__)


@app.route("/")
def init():
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%d/%m/%Y %H:%M:%S')
    dicc = {"data": timestamp}
    return jsonify(dicc)


# acceder a la ruta proporcionada por la terminal
if __name__ == "__main__":
    app.run(debug=True, port=5555)
