from flask import Flask
from flask import flash
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


@app.route('/')
def root():
    return render_template('record.html', name=None)


@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return "<h1></h1>"


@app.route('/save-record', methods=['GET', 'POST'])
def save_record():
    if request.method == "GET":
        return app.secret_key

    # check if the post request has the file part
    if 'file' not in request.files:
        flash("what happened to the file?")
        redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash("what happened to the filename?")
        redirect(request.url)

    filename = "testfile.mp3"
    file.save("files/"+filename)
    return redirect(request.url)


def run():
    app.run(host="127.0.0.1", port=7000, debug=True)
