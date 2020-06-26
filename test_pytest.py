# -*- coding: utf-8 -*-

from fonctions import *
import pytest
from bs4 import BeautifulSoup
#dans terminal
# C:\Users\Naomi\datascience\MINI_PROJET_RESTO>pytest test.py
def test_liens_annonces_paris():
    #given
    liens = ['https://www.century21.fr/annonces/achat-appartement/v-paris/s-0-/st-0-/b-0-/page-1/',
     'https://www.century21.fr/annonces/achat-appartement/v-paris/s-0-/st-0-/b-0-/page-2/',
     'https://www.century21.fr/annonces/achat-appartement/v-paris/s-0-/st-0-/b-0-/page-3/',
     'https://www.century21.fr/annonces/achat-appartement/v-paris/s-0-/st-0-/b-0-/page-4/',
     'https://www.century21.fr/annonces/achat-appartement/v-paris/s-0-/st-0-/b-0-/page-5/']
    #when
    result = liens_annonces_paris(5)
    #then
    assert result == liens

  
def test_scraping_by_annonce_century():       
    #given
    ann = '<li class="annonce margR0" id="derniereAnnonce"><script>google_tag_event("bien,vu_sur_listing,202_467_11481");</script><div class="contentAnnonce" data-template="n__bien__bloc__bien__liste" data-uid="1973843186" id="bien_1973843186"><div class="zone-photo-exclu"><a href="/trouver_logement/detail/1973843186/" onclick="google_tag_event("bien,clic_sur_listing,202_467_11481");return go_detail(this);"><div class="price tw-py-1 tw-text-xl tw-font-semibold tw-text-center">18 000 000€<span class="font20"></span></div><p class="pixM photoAnnonce tw-relative tw-flex tw-items-center tw-justify-center" onmouseover="popup_annonce("1973843186","202_467_11481",$(this));return false;"><img alt="Vente appartement - PARIS (75001) - 486.5 m² - 7 pièces" height="146" src="/imagesBien/202/467/c21_202_467_11481_9_3D6402A9-E84E-4A5D-98DA-433AA26D22E1.jpg" width="220"/></p></a></div><a class="tw-block" href="/trouver_logement/detail/1973843186/" onclick="google_tag_event("bien,clic_sur_listing,202_467_11481");return go_detail(this);"><h3 class="tw-text-xs tw-leading-none tw-my-1">PARIS <span class="tw-text-sm">75001</span></h3><div class="tw-flex tw-justify-between"><h4 class="tw-w-8/12 tw-text-c21-grey-medium tw-text-sm"> 55555 <br> 486,51 m² ,7 pièces</h4><div class="tw-w-4/12 tw-flex tw-flex-col tw-items-center tw-justify-between"><span class="icon-zoom-in2"></span><span class="tw-text-sm">Voir détail</span></div></div></a></div></li>'    
    annonce = BeautifulSoup(ann, "html.parser")
    arrondissement = []
    nb_pieces = []
    nb_chambres = []
    surface = []
    prix = []
    lien = []
    base_lien = "https://www.century21.fr"
    #when
    scraping_by_annonce_century(annonce,arrondissement,nb_pieces,nb_chambres,surface,prix,lien,base_lien)
    result = arrondissement
    #then      
    assert result==[1]
    
    
    
    

  
    
 