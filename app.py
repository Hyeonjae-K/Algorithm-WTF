import threading
from random import getrandbits
from flask import Flask, render_template, url_for, redirect, request, jsonify

import global_var
from calculators import exps_comp_cal, func_time_comp_cal

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('exps'))


@app.route('/exps', methods=['GET', 'POST'])
def exps():
    if request.method == 'POST':
        data = request.form['content']
        hash = getrandbits(128)
        global_var.exps_results[hash] = False
        threading.Thread(target=exps_comp_cal, args=(data, hash))
        print(jsonify(hash))
        return jsonify(hash)
    return render_template('views/exps.html', report=True)


@app.route('/func', methods=['GET', 'POST'])
def func():
    if request.method == 'POST':
        data = '\n'.join([x for x in request.form['content'].split(
            '\n') if 'print(' not in x])
        report = func_time_comp_cal(data)
        return render_template('views/func.html', report=report, data=data)
    return render_template('views/func.html', report=True)


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        return {'method': 'POST'}
    return 'test'
