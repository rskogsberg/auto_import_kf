import os

from flask import Flask, render_template, request
from flask_dropzone import Dropzone
from compute import xls_to_csv

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Relative path of directory for uploaded files
UPLOAD_DIR = 'S:/Departments/Analytics/Chemical Analytics/Richard/kf_import_csv'

ALLOWED_EXTENSIONS = set(['xls'])

app.config['UPLOAD_FOLDER'] = UPLOAD_DIR

if not os.path.isdir(UPLOAD_DIR):
    os.mkdir(UPLOAD_DIR)

app.config.update(
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_CUSTOM=True,
    DROPZONE_ALLOWED_FILE_TYPE='.xls',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=30,
    DROPZONE_UPLOAD_ON_CLICK=True
)

dropzone = Dropzone(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        for key, f in request.files.items():
            if key.startswith('file'):
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
                csv = xls_to_csv(f.filename)
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)