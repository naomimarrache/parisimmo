# -*- coding: utf-8 -*-

import folium
import pandas as pd
import json

import csv
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
#from matplotlib import cm
#import seaborn as sns



def map_prixmc_arrondissement():
    geo = json.load(open("arrondissements.geojson"))
    df = pd.read_csv('data.csv')
    prix = df[['prix_mc','arrondissement']].groupby('arrondissement').mean().round().sort_values(by='prix_mc', ascending=False)
    prix.reset_index(0, inplace=True)
    paris = folium.Map(location = [48.856578, 2.351828], zoom_start = 12)
    paris.choropleth(geo, key_on = "feature.properties.c_ar", data = df, columns = ["arrondissement", "prix_mc"],fill_color = "Spectral")
    return paris
