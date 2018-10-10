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


@app.route('/check', methods=['POST'])
def sensitive_words_check():
    input = request.form.get('q')
    result, keywords = check(input, 'static/sensitive_words.txt')
    return jsonify(result='\n'.join(result), keywords='|'.join(keywords))


@app.route('/save', methods=['POST'])
def save_config():
    input = request.form.get('q')
    str2file(input, 'static/sensitive_words.txt')
    return jsonify(result='OK')


@app.route('/load')
def load():
    input = request.args.get('q')
    if input == 'yes':
        copyfile('static/default.txt', 'static/sensitive_words.txt')
        return jsonify(result='OK')
    return jsonify(result='0')

if __name__ == '__main__':
    app.run()
