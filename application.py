from flask import Flask, render_template, request, jsonify
import os
from tweet_processing import *

app = Flask(__name__, static_url_path='/static')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')
FILES_STATIC = os.path.join(APP_STATIC, 'files')


@app.route('/')
def asg1():
    return render_template('asg1.html')

@app.route('/assignment2')
def asg2():
    return render_template('asg2.html')

@app.route('/assignment3')
def asg3():
    return render_template('asg3.html')

@app.route('/assignment3_1')
def asg3_1():
    return render_template('asg3_1.html')






