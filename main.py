#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from shutil import copyfile
from lib import check, str2file

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name='root')


@app.route('/setting')
def setting():
    return render_template('index.html', name='setting')


@app.route('/check')
def sensitive_words_check():
    input = request.args.get('q', 0, type=str)
    result = check(input, 'static/sensitive_words.txt')
    return jsonify(result=result)


@app.route('/save')
def save_config():
    input = request.args.get('q', 0, type=str)
    str2file(input, 'static/sensitive_words.txt')
    return jsonify(result='OK')


@app.route('/load')
def load():
    input = request.args.get('q', 0, type=str)
    if input == 'yes':
        copyfile('static/default.txt', 'static/sensitive_words.txt')
        return jsonify(result='OK')
    return jsonify(result='0')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
