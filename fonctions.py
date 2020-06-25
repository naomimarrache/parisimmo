
"""
def lien_par_arrondissement(lien_annonces_paris):
    for i in range(1,21):
        base_url = 'https://www.pap.fr/annonce/vente-appartements-paris-'
        base_url_part2 = "g377"
        if i == 1:
            lien_annonces_paris.append('https://www.pap.fr/annonce/vente-appartements-paris-1er-g37768')
        else:
            lien_annonces_paris.append(base_url+str(i)+'e-'+base_url_part2+str(67+i))

"""


from os import listdir
from os.path import isfile, join
import os
import glob
import pandas as pd
from fonctions import *
import csv 
from bs4 import BeautifulSoup

from selenium import webdriver



def scraping_by_annonce(annonce, nb_pieces, prix, arrondissement, lien, nb_chambres, surface):
    if annonce.find_all('li')[-1].text.split()[1] != "m2":
        #
        print('e')
    else:
        if annonce.find('span',{'class':'h1'}).text.split()[1][0] == '(':
            #
            print('e')
        else:
            base_lien_annonce = 'https://www.pap.fr'
            nb_pieces.append(int(annonce.find('ul',{'class':'item-tags'}).find_all('li')[0].text.split()[0]))
            prix.append(int(annonce.find('span',{'class':'item-price'}).text.split()[0].replace('.','')))    
            arrondissement.append(int(annonce.find('span',{'class':'h1'}).text.split()[1].replace('E','').replace('r','')))
            lien.append(base_lien_annonce + annonce.find('a',{'class':'item-title'})['href'])
            #if int(annonce.find('ul',{'class':'item-tags'}).find_all('li')[0].text.split()[0]) == 1:
            if annonce.find('ul',{'class':'item-tags'}).find_all('li')[1].text.split()[1] == 'm2':
                nb_chambres.append(0)
                surface.append(int(annonce.find('ul',{'class':'item-tags'}).find_all('li')[1].text.split()[0]))
            else:
                nb_chambres.append(int(annonce.find('ul',{'class':'item-tags'}).find_all('li')[1].text.split()[0]))
                surface.append(int(annonce.find('ul',{'class':'item-tags'}).find_all('li')[2].text.split()[0]))
 

def liens_annonces_paris(nb_pages):
    liens = []
    base_lien = 'https://www.century21.fr/annonces/achat-appartement/v-paris/s-0-/st-0-/b-0-/'
    for page in range(1,nb_pages+1):
        lien = base_lien + 'page-'+str(page)+'/'
        liens.append(lien)
    return liens



def scraping_by_annonce_century(annonce,arrondissement,nb_pieces,nb_chambres,surface,prix,lien,base_lien):
    if annonce.find('a',{'class':'tw-block'}) != None:
        arrondissement.append(int(annonce.find('span',{'class':'tw-text-sm'}).text.replace('750','')))
        nb_pieces.append(annonce.find('h4',{'class':'tw-w-8/12 tw-text-c21-grey-medium tw-text-sm'}).text.split()[-2])
        nb_chambres.append(None)
        surface.append(int(annonce.find('h4',{'class':'tw-w-8/12 tw-text-c21-grey-medium tw-text-sm'}).text.split()[-5].split(',')[0]))
        prix.append(int(annonce.find('div',{'class':'price tw-py-1 tw-text-xl tw-font-semibold tw-text-center'}).text.replace('\n','').replace('€','').strip().replace(' ','')))
        lien.append(base_lien + annonce.find('div',{'class':'zone-photo-exclu'}).find('a')["href"])
        



def load_data_by_page_orpi(link,driver,arrondissement,prix,info,nb_pieces,surface, lien):
    #response = requests.get(link)
    #soup = BeautifulSoup(response.text, 'html.parser')
    class_arrondissement = "u-mt-sm"
    class_info='u-link-unstyled c-overlay__link'
    class_prix='u-text-md u-color-primary'
    class_link_appart='u-link-unstyled c-overlay__link'
    
    base_lien_annonce = 'https://www.orpi.com'

    driver.get(link)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    div_appart = soup.find_all('li',{'class':'o-grid__col u-flex u-flex-column'})
    for div in div_appart:
        #nb_review.append(div.find('span', {'class':class_nb_review}).text)
        if div.find('div', {'class':class_arrondissement}) is not None:
            arrondissement.append(int(div.find('div',attrs={'class':'c-box__inner c-box__inner--sm'}).find('p', attrs={'class':class_arrondissement }).text.split()[1]))
            prix.append(int(div.find('strong', attrs={'class':class_prix}).text.replace('€','').replace(' ','')))
            info.append(div.find('a',attrs={'class':class_info}).text)
            nb_pieces.append(int(div.find('a',attrs={'class':class_info}).text.split()[1]))
            surface.append(int(div.find('a',attrs={'class':class_info}).text.split()[3]))
            lien.append(base_lien_annonce +div.find('a', attrs={'class':class_link_appart})['href'])
       




                       
def fichiers_csv():
    fichier_csv=[]
    fichiers = [f for f in listdir('csv') if isfile(join('csv', f))]
    for fichier in fichiers:
        fichier_csv.append('csv/'+fichier)
    return fichier_csv





def df_aggregate_csv(fichiers_csv):
    frames=[]
    for fichier in fichiers_csv:
        dfr=pd.read_csv(fichier)
        frames.append(dfr) 
    result=pd.concat(frames)
    result.to_csv('data.csv')
    
    #return result










