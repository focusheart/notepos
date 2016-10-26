# -*- coding: utf8 -*-

from flask import Flask
from flask import request
from flask import render_template
from flask import flash
from flask import jsonify

DEBUG = True
HOST = '0.0.0.0'
PORT = 51023
LP_PATH = '/dev/usb/lp0'


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('p.html')


@app.route('/p', methods=['GET','POST'])
def p():
    c = request.form.get('c')
    r = request.form.get('r')
    if c is None:
        c = request.args.get('c')
    if c is None:
        return render_template('p.html')

    c_encoded = c.encode('gbk')
    open(LP_PATH, 'w').write(c_encoded + '\n'*5)
    
    if r=='json':
        return jsonify({'success':True})
    else:
        return render_template('r.html')


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
