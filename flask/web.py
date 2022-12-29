import os
import random
from pathlib import Path

from flask import Flask, flash, send_from_directory
from flask import redirect
from flask import render_template
from flask import request
from flask_session import Session

UPLOAD_FOLDER = 'files'
app = Flask(__name__)
sess = Session()

app.config['SECRET_KEY'] = 'secretsecret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SESSION_TYPE'] = 'filesystem'
sess.init_app(app)
_path = Path(__file__).parent.__str__() + "\\files"
if not os.path.exists(_path):
    os.mkdir(_path)


# Dummy response to satisfy website if it does get request to .../favicon.ico
@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return '<h1></h1>'


# Navigation to url will generate random choice and return to HTML
@app.route('/get_random_line', methods=['GET'])
def get_random_line():
    path = Path(__file__).parent.parent.__str__() + "\\reference_files.txt"
    lines = open(path, encoding="UTF-8").readlines()[1:]

    return random.choice(lines)


# Home page, render the "record.html" template
@app.route('/')
def home():
    return render_template('record.html', name=None)


# Navigation will create GET request for website and POST request for audio data as mp3 file
@app.route('/save-record', methods=['GET', 'POST'])
def save_record():
    flash("saving")
    if request.method == "POST":
        # Sanity check on file existence
        if 'file' not in request.files:
            flash("Sorry! File not found!")
            redirect(request.url)

        file = request.files['file']

        # Sanity check that file is named correctly
        if file.filename == '':
            flash("Sorry! File name is empty!")
            redirect(request.url)

        # save file in hosts dir
        path = Path(__file__).parent.__str__() + "\\files\\testfile.mp3"
        file.save(path)

        return "<h1>Success!</h1>"

    # TODO: add scoring capability and return score
    if request.method == "GET":
        return ""


@app.route('/get_random_audio/<audio_id>/', methods=['GET'])
def get_random_audio(audio_id):
    path = Path(__file__).parent.parent.__str__() + "\\hackathon_data"
    audio_id = audio_id + ".wav"
    for file in os.listdir(path):
        if file.endswith(audio_id):
            with open(path + "\\" + file, "rb") as f:
                print(audio_id)
                print(path)
                return send_from_directory(
                    directory=path,
                    path=audio_id)
    return None


def run():
    app.run(host="127.0.0.1", port=7000, debug=True)
