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


#lien_1a10 = "https://www.pap.fr/annonce/achat-vente-appartement-paris-1er-g37768g37769g37770g37771g37772g37773g37774g37775g37776g37777"
#lien_11a20 = "https://www.pap.fr/annonce/vente-appartements-paris-11e-g37778g37779g37780g37781g37782g37783g37784g37785g37786g37787"
lien_annonces_paris = []
lien_1a5 = 'https://www.pap.fr/annonce/achat-vente-appartement-paris-1er-g37768g37769g37770g37771g37772'
lien_6a10 = 'https://www.pap.fr/annonce/achat-vente-appartement-paris-6e-g37773g37774g37775g37776g37777'
lien_11a15 = 'https://www.pap.fr/annonce/achat-vente-appartement-paris-11e-g37778g37779g37780g37781g37782'
lien_16a20 = 'https://www.pap.fr/annonce/achat-vente-appartement-paris-16e-g37783g37784g37785g37786g37787'
lien_annonces_paris = [lien_1a5,lien_6a10,lien_11a15, lien_16a20]
#lien_par_arrondissement(lien_annonces_paris)
#lien_annonces_paris = [lien_1a10, lien_11a20]


base_lien_annonce = 'https://www.pap.fr'
    
arrondissement = []
nb_pieces = []
nb_chambres = []
surface = []
prix = []
lien = []


for lien_annonces in lien_annonces_paris:
    driver = webdriver.Firefox()
    driver.get(lien_annonces)

    for i in range(23):
        target = driver.find_element_by_link_text('Plan du site')
        target.location_once_scrolled_into_view
        time.sleep(3)
        page_source  = driver.page_source
        
    page_source  = driver.page_source
    soup = BeautifulSoup(page_source,'html.parser')
    #soup = BeautifulSoup(driver.page_source,'html.parser')
    annonces = soup.find_all('div',{'class':'item-body'})
    
    for annonce in annonces:
        if annonce.find('ul',{'class':'item-tags'}).find_all('li') is not None:
             try:
                if annonce.find('span',{'class':'h1'}).text.split()[0] == 'Paris':
                    if annonce.find('span',{'class':'h1'}).text.strip() != 'Paris':
                        scraping_by_annonce(annonce, nb_pieces, prix, arrondissement, lien, nb_chambres, surface)
             except IndexError:
                print("e")


data = {'arrondissement':arrondissement,
        'nb_pieces':nb_pieces,
        'nb_chambres':nb_chambres,
        'surface':surface,
        'prix':prix,
        'lien':lien
        }

df = pd.DataFrame(data)
#en faisant la commande suivante on voit bien que ça ne suffit pas, pas assez d'annonces pour chauqe arrondissemnt
#il faudra scrapper chaque arrondissment puis supprimer les doublons dans la base
print(df.arrondissement.value_counts())
###############################################
####            INTERP!RETATION       #########
###############################################

#Si jamais je trouve une bonne affaire pour des arrondissemnt où il n'y à pas beaucoup d'offre, je devrais penser à la saisir.

prix_mc = []
for index_df in range(df.shape[0]):
    prix_mc.append(df[index_df-1:index_df].prix/df[index_df-1:index_df].surface)
    
    
df['prix_mc'] = df['prix']/df['surface']




print(df.loc[df['prix_mc'].idxmax(), 'arrondissement'])


df.loc[df['surface']==1].lien




df2 = df.copy()
df2 = df2.drop_duplicates(subset=['lien'], keep=False)

df2.to_csv('csv/pap.csv', header=True, index=False) 


