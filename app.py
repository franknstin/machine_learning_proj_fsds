from zlib import MAX_WBITS
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def index():
    return "created CI CD pipeline"


if __name__ == '__main__':
    app.run(debug=True)
