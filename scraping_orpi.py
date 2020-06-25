#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:08:57 2020
@author: salomelamartinie
"""


import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from math import *
from fonctions import * 



orpi_link = "https://www.orpi.com/recherche/buy?transaction=buy&resultUrl=&realEstateTypes%5B0%5D=maison&realEstateTypes%5B1%5D=appartement&locations%5B0%5D%5Bvalue%5D=paris-metropole&locations%5B0%5D%5Blabel%5D=Paris&agency=&minSurface=&maxSurface=&newBuild=&oldBuild=&minPrice=&maxPrice=&sort=date-down&layoutType=mixte&nbBedrooms=&page=&minLotSurface=&maxLotSurface=&minStoryLocation=&maxStoryLocation="
#class_page_number = "lemon--div__373c0__1mboc border-color--default__373c0__3-ifU text-align--center__373c0__2n2yQ"
#response = requests.get(orpi_link)


driver = webdriver.Firefox()
driver.get(orpi_link)


soup = BeautifulSoup(driver.page_source, 'html.parser')

anonce=soup.find_all('article')

class_arrondissement = "u-mt-sm"
class_prix_m2=''
class_nmb_piece=''
class_info='u-link-unstyled c-overlay__link'
class_prix='u-text-md u-color-primary'
class_link_appart='u-link-unstyled c-overlay__link'





all_appart_links = []
all_appart_links.append(orpi_link)


## en plus  
numbre_article = int(soup.find('strong',attrs={'class':'u-color-primary u-h4'}).find('span').text.split()[0])
nombre_page = ceil(numbre_article/12)

### en plus 
for i in range(2,nombre_page+2): 
  all_appart_links.append('https://www.orpi.com/recherche/buy?transaction=buy&resultUrl=&realEstateTypes%5B0%5D=maison&realEstateTypes%5B1%5D=appartement&locations%5B0%5D%5Bvalue%5D=paris-metropole&locations%5B0%5D%5Blabel%5D=Paris&agency=&minSurface=&maxSurface=&newBuild=&oldBuild=&minPrice=&maxPrice=&sort=date-down&layoutType=mixte&nbBedrooms=&page=' + str(i-1) + 'minLotSurface=&maxLotSurface=&minStoryLocation=&maxStoryLocation=#')
  
  

arrondissement = []
nb_pieces = []
surface = []
prix = []
lien = []
info=[]

link_appart=[]

base_lien_annonce = 'https://www.orpi.com'


for link in all_appart_links:
    load_data_by_page_orpi(link,driver,arrondissement,prix,info,nb_pieces,surface, lien)
    print(link)


 

data = {'arrondissement':arrondissement,
        'nb_pieces':nb_pieces,
        'nb_chambres':[None]*len(surface),
        'surface':surface,
        'prix':prix,
        'lien':lien}


df_orpi = pd.DataFrame(data)


prix_mc = []
for index_df in range(df_orpi.shape[0]):
    prix_mc.append(df_orpi[index_df-1:index_df].prix/df_orpi[index_df-1:index_df].surface)
    
    
df_orpi['prix_mc'] = df_orpi['prix']/df_orpi['surface']

#suppression des doublons
df2 = df_orpi.copy()
df2 = df2.drop_duplicates(subset=['lien'], keep=False)

df2.to_csv('csv/orpi2.csv', header=True, index=False) 

