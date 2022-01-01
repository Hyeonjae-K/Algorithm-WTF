from flask import Flask, render_template, url_for, redirect, request, jsonify
from threading import Thread
import uuid

from calculators import compareExpressions, measureFunction

app = Flask(__name__)
g_results = {}


@app.route('/')
def index():
    return redirect(url_for('exps'))


@app.route('/exps', methods=['GET', 'POST'])
def exps():
    if request.method == 'POST':
        data = request.form['content']
        key = uuid.uuid4().hex
        g_results[key] = {'is_finish': False,
                          'is_valid': False, 'result': None}
        Thread(target=compareExpressions, args=(g_results, data, key)).start()
        return jsonify(key)
    return render_template('views/exps.html')


@app.route('/func', methods=['GET', 'POST'])
def func():
    if request.method == 'POST':
        data = request.form['content']
        key = uuid.uuid4().hex
        g_results[key] = {'is_finish': False,
                          'is_valid': False, 'result': None}
        Thread(target=measureFunction, args=(g_results, data, key)).start()
        return jsonify(key)
    return render_template('views/func.html')


@app.route('/results/<string:key>', methods=['GET'])
def get_result(key):
    return g_results[key]
