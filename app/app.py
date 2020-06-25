# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for, flash, redirect
import time

app = Flask(__name__)

@app.route('/')
def home():
    name = "nao"
    return render_template('home.html', name=name)

@app.route('/test',methods = ['POST'])
def test():
    result = request.form
    r = result['review']
    #prediction = "positive"
    prediction = pred(r)
    return render_template('test.html', review=r, prediction=prediction, langue=r)


def pred(r):
    return 'negative'

if __name__ == '__main__':
	app.run(debug=True)

