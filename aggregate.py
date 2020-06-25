#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 20:48:06 2020

@author: salomelamartinie
"""
from fonctions import *



###########   AGGREATE DATA FROM DIFFERENT ################

df_aggregate_csv(fichiers_csv())




######### COPY DU FICHIER CREER DANS APP POUR LA PARTIE FRONT ##########

import shutil

filePath = shutil.copy('data.csv', 'app/data.csv')