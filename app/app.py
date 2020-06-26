# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for, flash, redirect
import time
from fonctions_app import map_prixmc_arrondissement
import seaborn as sns
import folium
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    name = "nao"
    return render_template('home.html', name=name)
    
@app.route('/test',methods = ['POST'])
def test():
    result = request.form
    arrondissement = result['arrondissement']
    nombre = result['nombre']
    return render_template('test.html', arrondissement=arrondissement, nombre=nombre)


@app.route('/test_piechart')
def test_piechart():
    df = pd.read_csv("data.csv") 
    #pie_chart = df["arrondissement"].value_counts(normalize=True).plot(kind='pie',figsize=(10,6))
    df = pd.read_csv("data.csv")
    df_tracer = df[['prix_mc','arrondissement']].groupby('arrondissement').mean().round().sort_values(by='prix_mc', ascending=False)
    df_tracer.reset_index(0, inplace=True)
    df_tracer.head()
    plt.figure(figsize=(10,6))
    sns.barplot(x=df_tracer['arrondissement'], y=df_tracer['prix_mc'], palette="Blues_r")
    plt.tight_layout()
    return render_template('test_piechart.html',pie_chart=plt.show())

@app.route('/test_hist') 
def test_hist():
    df = pd.read_csv("data.csv") 
    color = cm.inferno_r(np.linspace(.3, .8, 30))
    plt.figure(figsize=(10,8))
    df.arrondissement.value_counts().plot(kind='barh',color=color)
    plt.xlabel("Nombre d'annonce")
    plt.ylabel("Arrondissement")
    plt.title("Nombre d'annonce par arrondissement")
    return render_template('test_hist.html',hist=plt.show())
        


@app.route('/test_map')
def test_map():
    folium_map = map_prixmc_arrondissement()
    folium_map.save('templates/map.html')
    return render_template('test_map.html')



 
    
def fonction_front_end(arrondissement,nombre_annonce):
    df=pd.read_csv('data.csv')
    df2=df.copy()
    df2 = df2[ df2.arrondissement == arrondissement]
    df2=df2.sort_values(by=['prix_mc'],ascending=True)
    return df2.head(nombre_annonce)

    



def function_tracer(var1,var2):
    df = pd.read_csv("data.csv")
    df_tracer = df[[var1,var2]].groupby(var2).mean().round().sort_values(by=var1, ascending=False)
    df_tracer.reset_index(0, inplace=True)
    df_tracer.head()
    plt.figure(figsize=(10,6))
    sns.barplot(x=df_tracer[var2], y=df_tracer[var1], palette="Blues_r")
    plt.tight_layout()
    


if __name__ == '__main__':
	app.run(debug=True)

