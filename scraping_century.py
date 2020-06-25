# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 19:30:06 2020

@author: Naomi
"""


from fonctions import *
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import requests


lien_century = 'https://www.century21.fr/annonces/achat-appartement/v-paris/s-0-/st-0-/b-0-/page-1/'
r = requests.get(lien_century) 
soup = BeautifulSoup(r.content, 'html.parser') 


nb_annonce_par_page = 28
nb_annonce = int(soup.find('h2',{'class':'titreSeparation titreSeparation txtA_plusplus'}).text.strip().replace('\n','').split()[0])
nb_pages = int(round(nb_annonce/nb_annonce_par_page,0))


arrondissement = []
nb_pieces = []
nb_chambres = []
surface = []
prix = []
lien = []
base_lien = "https://www.century21.fr"
liens_annonces_paris = liens_annonces_paris(nb_pages)


for link in liens_annonces_paris:
    #link = liens_annonces_paris[0]
    r = requests.get(link) 
    soup = BeautifulSoup(r.content, 'html.parser') 
    ul_annonces = soup.find('ul',{'class':'annoncesListeBien'})
    annonces = ul_annonces.find_all('li',{'class':'annonce'})
    for annonce in annonces:
        scraping_by_annonce_century(annonce,arrondissement,nb_pieces,nb_chambres,surface,prix,lien,base_lien)
    


data = {'arrondissement':arrondissement,
        'nb_pieces':nb_pieces,
        'nb_chambres':nb_chambres,
        'surface':surface,
        'prix':prix,
        'lien':lien
        }

df = pd.DataFrame(data)
print(df.arrondissement.value_counts())

prix_mc = []
for index_df in range(df.shape[0]):
    prix_mc.append(df[index_df-1:index_df].prix/df[index_df-1:index_df].surface)
    
    
df['prix_mc'] = df['prix']/df['surface']
print(df.loc[df['prix_mc'].idxmax(), 'arrondissement'])
df.loc[df['surface']==1].lien

df2 = df.copy()
df2 = df2.drop_duplicates(subset=['lien'], keep=False)

df2.to_csv('csv/century.csv', header=True, index=False) 

