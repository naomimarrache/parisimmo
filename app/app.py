# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for, flash, redirect
import time

import folium

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


@app.route('/test_map')
def test_map():
    start_coords = (46.9540700, 142.7360300)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    folium_map.save('templates/map.html')
    return render_template('test_map.html')
    

def pred(r):
    return 'negative'

if __name__ == '__main__':
	app.run(debug=True)

