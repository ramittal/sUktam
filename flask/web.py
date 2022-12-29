import random

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request

from flask_session import Session
from pathlib import Path

UPLOAD_FOLDER = 'files'
app = Flask(__name__)
sess = Session()

app.config['SECRET_KEY'] = 'secretsecret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SESSION_TYPE'] = 'filesystem'
sess.init_app(app)


@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return '<h1></h1>'


@app.route('/get_random_line', methods=['GET'])
def get_random_line():
    path = Path(__file__).parent.parent.__str__() + "\\reference_files.txt"
    lines = open(path, encoding="UTF-8").readlines()[1:]
    return random.choice(lines)


@app.route('/')
def root():
    return render_template('record.html', name=None)


@app.route('/save-record', methods=['GET', 'POST'])
def save_record():
    if request.method == "GET":
        return ""

    if request.method == "POST":
        # check if the post request has the file part
        if 'file' not in request.files:
            print("what happened to the file?")
            redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            print("what happened to the filename?")
            redirect(request.url)

        path = Path(__file__).parent.__str__() + "\\files\\testfile.mp3";
        file.save(path)

        return redirect(request.url)


def run():
    app.run(host="127.0.0.1", port=7000, debug=True)
