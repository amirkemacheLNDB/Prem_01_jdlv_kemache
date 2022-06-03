# -*- coding: utf-8 -*-
"""

"""

from os import listdir
from os.path import isfile, join
import random
import time
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from jdlv_data import *
from jdlv_model import *
from jdlv_outils import *

def clean_grid (grid):
    for i in range (default_grid_size):
        for j in range (default_grid_size):
            grid.cases [i][j]['s'] = death_status
            grid.cases [i][j]['c'] = death_color
    return grid

def make_flamme (grid, i, j, color):
    grid = clean_grid (grid)
    cases = grid.cases



    cases[i+180][j+9]['s']=life_status
    cases[i+180][j+9]['c'] = 'red'
    cases[i+181][j+9]['s']=life_status
    cases[i+181][j+9]['c'] = 'red'
    cases[i+182][j+10]['s']=life_status
    cases[i+182][j+10]['c'] = 'red'
    cases[i+183][j+7]['s']=life_status
    cases[i+183][j+7]['c'] = 'red'
    cases[i+183][j+10]['s']=life_status
    cases[i+183][j+10]['c'] = 'red'
    cases[i+184][j+7]['s']=life_status
    cases[i+184][j+7]['c'] = 'red'
    cases[i+184][j+10]['s']=life_status
    cases[i+184][j+10]['c'] = 'red'
    cases[i+185][j+7]['s']=life_status
    cases[i+185][j+7]['c'] = 'red'
    cases[i+185][j+8]['s']=life_status
    cases[i+185][j+8]['c'] = 'red'
    cases[i+185][j+9]['s']=life_status
    cases[i+185][j+9]['c'] = 'red'
    cases[i+185][j+10]['s']=life_status
    cases[i+185][j+10]['c'] = 'yellow'
    cases[i+185][j+11]['s']=life_status
    cases[i+185][j+11]['c'] = 'red'
    cases[i+186][j+7]['s']=life_status
    cases[i+186][j+7]['c'] = 'red'
    cases[i+186][j+8]['s']=life_status
    cases[i+186][j+8]['c'] = 'yellow'
    cases[i+186][j+9]['s']=life_status
    cases[i+186][j+9]['c'] = 'yellow'
    cases[i+186][j+10]['s']=life_status
    cases[i+186][j+10]['c'] = 'yellow'
    cases[i+186][j+11]['s']=life_status
    cases[i+186][j+11]['c'] = 'red'
    cases[i+187][j+8]['s']=life_status
    cases[i+187][j+8]['c'] = 'red'
    cases[i+187][j+9]['s']=life_status
    cases[i+187][j+9]['c'] = 'yellow'
    cases[i+187][j+10]['s']=life_status
    cases[i+187][j+10]['c'] = 'yellow'
    cases[i+187][j+11]['s']=life_status
    cases[i+187][j+11]['c'] = 'yellow'
    cases[i+187][j+12]['s']=life_status
    cases[i+187][j+12]['c'] = 'red'
    cases[i+188][j+5]['s']=life_status
    cases[i+188][j+5]['c'] = 'red'
    cases[i+188][j+8]['s']=life_status
    cases[i+188][j+8]['c'] = 'red'
    cases[i+188][j+9]['s']=life_status
    cases[i+188][j+9]['c'] = 'yellow'
    cases[i+188][j+10]['s']=life_status
    cases[i+188][j+10]['c'] = 'yellow'
    cases[i+188][j+11]['s']=life_status
    cases[i+188][j+11]['c'] = 'yellow'
    cases[i+188][j+12]['s']=life_status
    cases[i+188][j+12]['c'] = 'yellow'
    cases[i+188][j+13]['s']=life_status
    cases[i+188][j+13]['c'] = 'red'
    cases[i+189][j+5]['s']=life_status
    cases[i+189][j+5]['c'] = 'red'
    cases[i+189][j+8]['s']=life_status
    cases[i+189][j+8]['c'] = 'red'
    cases[i+189][j+9]['s']=life_status
    cases[i+189][j+9]['c'] = 'yellow'
    cases[i+189][j+10]['s']=life_status
    cases[i+189][j+10]['c'] = 'yellow'
    cases[i+189][j+11]['s']=life_status
    cases[i+189][j+11]['c'] = 'yellow'
    cases[i+189][j+12]['s']=life_status
    cases[i+189][j+12]['c'] = 'yellow'
    cases[i+189][j+13]['s']=life_status
    cases[i+189][j+13]['c'] = 'red'
    cases[i+190][j+5]['s']=life_status
    cases[i+190][j+5]['c'] = 'red'
    cases[i+190][j+8]['s']=life_status
    cases[i+190][j+8]['c'] = 'red'
    cases[i+190][j+9]['s']=life_status
    cases[i+190][j+9]['c'] = 'yellow'
    cases[i+190][j+10]['s']=life_status
    cases[i+190][j+10]['c'] = 'yellow'
    cases[i+190][j+11]['s']=life_status
    cases[i+190][j+11]['c'] = 'yellow'
    cases[i+190][j+12]['s']=life_status
    cases[i+190][j+12]['c'] = 'yellow'
    cases[i+190][j+13]['s']=life_status
    cases[i+190][j+13]['c'] = 'red'
    cases[i+191][j+4]['s']=life_status
    cases[i+191][j+4]['c'] = 'red'
    cases[i+191][j+5]['s']=life_status
    cases[i+191][j+5]['c'] = 'red'
    cases[i+191][j+7]['s']=life_status
    cases[i+191][j+7]['c'] = 'red'
    cases[i+191][j+8]['s']=life_status
    cases[i+191][j+8]['c'] = 'yellow'
    cases[i+191][j+9]['s']=life_status
    cases[i+191][j+9]['c'] = 'yellow'
    cases[i+191][j+10]['s']=life_status
    cases[i+191][j+10]['c'] = 'yellow'
    cases[i+191][j+11]['s']=life_status
    cases[i+191][j+11]['c'] = 'yellow'
    cases[i+191][j+12]['s']=life_status
    cases[i+191][j+12]['c'] = 'red'
    cases[i+192][j+3]['s']=life_status
    cases[i+192][j+3]['c'] = 'red'
    cases[i+192][j+4]['s']=life_status
    cases[i+192][j+4]['c'] = 'yellow'
    cases[i+192][j+5]['s']=life_status
    cases[i+192][j+5]['c'] = 'red'
    cases[i+192][j+7]['s']=life_status
    cases[i+192][j+7]['c'] = 'red'
    cases[i+192][j+8]['s']=life_status
    cases[i+192][j+8]['c'] = 'yellow'
    cases[i+192][j+9]['s']=life_status
    cases[i+192][j+9]['c'] = 'yellow'
    cases[i+192][j+10]['s']=life_status
    cases[i+192][j+10]['c'] = 'yellow'
    cases[i+192][j+11]['s']=life_status
    cases[i+192][j+11]['c'] = 'yellow'
    cases[i+192][j+12]['s']=life_status
    cases[i+192][j+12]['c'] = 'yellow'
    cases[i+192][j+13]['s']=life_status
    cases[i+192][j+13]['c'] = 'red'
    cases[i+193][j+3]['s']=life_status
    cases[i+193][j+3]['c'] = 'red'
    cases[i+193][j+4]['s']=life_status
    cases[i+193][j+4]['c'] = 'yellow'
    cases[i+193][j+5]['s']=life_status
    cases[i+193][j+5]['c'] = 'yellow'
    cases[i+193][j+6]['s']=life_status
    cases[i+193][j+6]['c'] = 'red'
    cases[i+193][j+7]['s']=life_status
    cases[i+193][j+7]['c'] = 'yellow'
    cases[i+193][j+8]['s']=life_status
    cases[i+193][j+8]['c'] = 'yellow'
    cases[i+193][j+9]['s']=life_status
    cases[i+193][j+9]['c'] = 'yellow'
    cases[i+193][j+10]['s']=life_status
    cases[i+193][j+10]['c'] = 'yellow'
    cases[i+193][j+11]['s']=life_status
    cases[i+193][j+11]['c'] = 'yellow'
    cases[i+193][j+12]['s']=life_status
    cases[i+193][j+12]['c'] = 'yellow'
    cases[i+193][j+13]['s']=life_status
    cases[i+193][j+13]['c'] = 'red'
    cases[i+194][j+2]['s']=life_status
    cases[i+194][j+2]['c'] = 'red'
    cases[i+194][j+3]['s']=life_status
    cases[i+194][j+3]['c'] = 'yellow'
    cases[i+194][j+4]['s']=life_status
    cases[i+194][j+4]['c'] = 'yellow'
    cases[i+194][j+5]['s']=life_status
    cases[i+194][j+5]['c'] = 'yellow'
    cases[i+194][j+6]['s']=life_status
    cases[i+194][j+6]['c'] = 'yellow'
    cases[i+194][j+7]['s']=life_status
    cases[i+194][j+7]['c'] = 'yellow'
    cases[i+194][j+8]['s']=life_status
    cases[i+194][j+8]['c'] = 'yellow'
    cases[i+194][j+9]['s']=life_status
    cases[i+194][j+9]['c'] = 'yellow'
    cases[i+194][j+10]['s']=life_status
    cases[i+194][j+10]['c'] = 'yellow'
    cases[i+194][j+11]['s']=life_status
    cases[i+194][j+11]['c'] = 'yellow'
    cases[i+194][j+12]['s']=life_status
    cases[i+194][j+12]['c'] = 'yellow'
    cases[i+194][j+13]['s']=life_status
    cases[i+194][j+13]['c'] = 'yellow'
    cases[i+194][j+14]['s']=life_status
    cases[i+194][j+14]['c'] = 'red'
    cases[i+195][j+2]['s']=life_status
    cases[i+195][j+2]['c'] = 'red'
    cases[i+195][j+3]['s']=life_status
    cases[i+195][j+3]['c'] = 'yellow'
    cases[i+195][j+4]['s']=life_status
    cases[i+195][j+4]['c'] = 'yellow'
    cases[i+195][j+5]['s']=life_status
    cases[i+195][j+5]['c'] = 'yellow'
    cases[i+195][j+6]['s']=life_status
    cases[i+195][j+6]['c'] = 'yellow'
    cases[i+195][j+7]['s']=life_status
    cases[i+195][j+7]['c'] = 'yellow'
    cases[i+195][j+8]['s']=life_status
    cases[i+195][j+8]['c'] = 'yellow'
    cases[i+195][j+9]['s']=life_status
    cases[i+195][j+9]['c'] = 'yellow'
    cases[i+195][j+10]['s']=life_status
    cases[i+195][j+10]['c'] = 'yellow'
    cases[i+195][j+11]['s']=life_status
    cases[i+195][j+11]['c'] = 'yellow'
    cases[i+195][j+12]['s']=life_status
    cases[i+195][j+12]['c'] = 'yellow'
    cases[i+195][j+13]['s']=life_status
    cases[i+195][j+13]['c'] = 'yellow'
    cases[i+195][j+14]['s']=life_status
    cases[i+195][j+14]['c'] = 'yellow'
    cases[i+195][j+15]['s']=life_status
    cases[i+195][j+15]['c'] = 'red'
    cases[i+196][j+2]['s']=life_status
    cases[i+196][j+2]['c'] = 'red'
    cases[i+196][j+3]['s']=life_status
    cases[i+196][j+3]['c'] = 'yellow'
    cases[i+196][j+4]['s']=life_status
    cases[i+196][j+4]['c'] = 'yellow'
    cases[i+196][j+5]['s']=life_status
    cases[i+196][j+5]['c'] = 'yellow'
    cases[i+196][j+6]['s']=life_status
    cases[i+196][j+6]['c'] = 'yellow'
    cases[i+196][j+7]['s']=life_status
    cases[i+196][j+7]['c'] = 'yellow'
    cases[i+196][j+8]['s']=life_status
    cases[i+196][j+8]['c'] = 'yellow'
    cases[i+196][j+9]['s']=life_status
    cases[i+196][j+9]['c'] = 'yellow'
    cases[i+196][j+10]['s']=life_status
    cases[i+196][j+10]['c'] = 'yellow'
    cases[i+196][j+11]['s']=life_status
    cases[i+196][j+11]['c'] = 'yellow'
    cases[i+196][j+12]['s']=life_status
    cases[i+196][j+12]['c'] = 'yellow'
    cases[i+196][j+13]['s']=life_status
    cases[i+196][j+13]['c'] = 'yellow'
    cases[i+196][j+14]['s']=life_status
    cases[i+196][j+14]['c'] = 'yellow'
    cases[i+196][j+15]['s']=life_status
    cases[i+196][j+15]['c'] = 'red'
    cases[i+197][j+3]['s']=life_status
    cases[i+197][j+3]['c'] = 'red'
    cases[i+197][j+4]['s']=life_status
    cases[i+197][j+4]['c'] = 'yellow'
    cases[i+197][j+5]['s']=life_status
    cases[i+197][j+5]['c'] = 'yellow'
    cases[i+197][j+6]['s']=life_status
    cases[i+197][j+6]['c'] = 'yellow'
    cases[i+197][j+7]['s']=life_status
    cases[i+197][j+7]['c'] = 'yellow'
    cases[i+197][j+8]['s']=life_status
    cases[i+197][j+8]['c'] = 'yellow'
    cases[i+197][j+9]['s']=life_status
    cases[i+197][j+9]['c'] = 'yellow'
    cases[i+197][j+10]['s']=life_status
    cases[i+197][j+10]['c'] = 'yellow'
    cases[i+197][j+11]['s']=life_status
    cases[i+197][j+11]['c'] = 'yellow'
    cases[i+197][j+12]['s']=life_status
    cases[i+197][j+12]['c'] = 'yellow'
    cases[i+197][j+13]['s']=life_status
    cases[i+197][j+13]['c'] = 'yellow'
    cases[i+197][j+14]['s']=life_status
    cases[i+197][j+14]['c'] = 'red'
    cases[i+198][j+4]['s']=life_status
    cases[i+198][j+4]['c'] = 'red'
    cases[i+198][j+5]['s']=life_status
    cases[i+198][j+5]['c'] = 'yellow'
    cases[i+198][j+6]['s']=life_status
    cases[i+198][j+6]['c'] = 'yellow'
    cases[i+198][j+7]['s']=life_status
    cases[i+198][j+7]['c'] = 'yellow'
    cases[i+198][j+8]['s']=life_status
    cases[i+198][j+8]['c'] = 'yellow'
    cases[i+198][j+9]['s']=life_status
    cases[i+198][j+9]['c'] = 'yellow'
    cases[i+198][j+10]['s']=life_status
    cases[i+198][j+10]['c'] = 'yellow'
    cases[i+198][j+11]['s']=life_status
    cases[i+198][j+11]['c'] = 'yellow'
    cases[i+198][j+12]['s']=life_status
    cases[i+198][j+12]['c'] = 'yellow'
    cases[i+198][j+13]['s']=life_status
    cases[i+198][j+13]['c'] = 'yellow'
    cases[i+198][j+14]['s']=life_status
    cases[i+198][j+14]['c'] = 'red'
    cases[i+199][j+5]['s']=life_status
    cases[i+199][j+5]['c'] = 'red'
    cases[i+199][j+6]['s']=life_status
    cases[i+199][j+6]['c'] = 'red'
    cases[i+199][j+7]['s']=life_status
    cases[i+199][j+7]['c'] = 'red'
    cases[i+199][j+8]['s']=life_status
    cases[i+199][j+8]['c'] = 'red'
    cases[i+199][j+9]['s']=life_status
    cases[i+199][j+9]['c'] = 'red'
    cases[i+199][j+10]['s']=life_status
    cases[i+199][j+10]['c'] = 'red'
    cases[i+199][j+11]['s']=life_status
    cases[i+199][j+11]['c'] = 'red'
    cases[i+199][j+12]['s']=life_status
    cases[i+199][j+12]['c'] = 'red'
    cases[i+199][j+13]['s']=life_status
    cases[i+199][j+13]['c'] = 'red'
    return grid


def make_fil(grid, i, j, color):
    grid = clean_grid (grid)
    cases = grid.cases

    cases[i+199][j+16]['s']=life_status
    cases[i+199][j+16]['c'] = 'red'
    cases[i+198][j+17]['s']=life_status
    cases[i+198][j+17]['c'] = 'red'
    cases[i+197][j+17]['s']=life_status
    cases[i+197][j+17]['c'] = 'red'
    cases[i+197][j+18]['s']=life_status
    cases[i+197][j+18]['c'] = 'yellow'
    cases[i+198][j+18]['s']=life_status
    cases[i+198][j+18]['c'] = 'yellow'
    cases[i+199][j+17]['s']=life_status
    cases[i+199][j+17]['c'] = 'yellow'
    cases[i+198][j+18]['s']=life_status
    cases[i+198][j+18]['c'] = 'yellow'
    cases[i+199][j+18]['s']=life_status
    cases[i+199][j+18]['c'] = 'yellow'

    cases[i+198][j+19]['s']=life_status
    cases[i+198][j+19]['c'] = 'yellow'
    cases[i+199][j+19]['s']=life_status
    cases[i+199][j+19]['c'] = 'yellow'
    cases[i+197][j+19]['s']=life_status
    cases[i+197][j+19]['c'] = 'yellow'
    cases[i+198][j+19]['s']=life_status
    cases[i+198][j+19]['c'] = 'yellow'
    cases[i+196][j+18]['s']=life_status
    cases[i+196][j+18]['c'] = 'red'
    cases[i+196][j+19]['s']=life_status
    cases[i+196][j+19]['c'] = 'red'

    cases[i+195][j+20]['s']=life_status
    cases[i+195][j+20]['c'] = 'red'
    cases[i+196][j+21]['s']=life_status
    cases[i+196][j+21]['c'] = 'red'
    return grid


def apply_game_of_life_rules (grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases 
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, int(len (cases)/2)):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            nbre_alive_voisins = count_alive_voisins (voisins)
            if nbre_alive_voisins == 3:
                next_cases [i] [j] = revive_case (next_cases [i] [j],"red")
            elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    for i in range (int(len (cases)/2 +1), len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            nbre_alive_voisins = count_alive_voisins (voisins)
            if nbre_alive_voisins == 3:
                next_cases [i] [j] = revive_case (next_cases [i] [j],"red")
            elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid





def apply_rules (grid, compteur):
    next_grid = grid
    time.sleep (0.2) 
    if -1 < compteur < 100:
        next_grid = make_conway_flamme(next_grid, 0, compteur, 'black')
    if 101 < compteur < 200:
        next_grid = make_fil_artifice(next_grid, compteur, 0, 'black')
    
    if 78 < compteur<90:
        next_grid = make_fil_artifice(next_grid, compteur *(-1), 0, 'black')              
    else:

        time.sleep (0.5)
        next_grid = apply_game_of_life_rules (next_grid)
    return next_grid


def apply_rules (grid, compteur):
    if compteur % 11 == 0:
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_conway (grid, 4, compteur + 4, 'black')
    else:
        print ("COMPTEUR % 11 is NOT 0")
        time.sleep (0.1)

        if compteur > 80:
            next_grid = apply_game_of_life_rules (grid)
        else:
            next_grid = apply_game_of_life_rules (grid)
    return next_grid
