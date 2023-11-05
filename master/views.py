#!/usr/bin/env python3
""""""
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os


load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = os.environ.get('UPLOAD_FOLDER')


@app.route('/', methods=['GET'], strict_slashes=False)
def landing():
    """"""

    return render_template('landing.html')

