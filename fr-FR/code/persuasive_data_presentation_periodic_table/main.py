#!/bin/python3
from p5 import *
from random import randint

pt_dict = {}
pt_dict_groupe = {}
pt_dict_periode = {}

# Mets le code à exécuter une seule fois ici
def setup():
    global carte
    charge_donnees_pt('pt.csv')
    config_coords()
    size(1024, 576)
    carte = load_image('pt.png')


def config_coords():

    for i in range(18):
        pt_dict_groupe[i + 1] = {}
        pt_dict_groupe[i + 1]['min_x'] = 25 + (i * 54)
        pt_dict_groupe[i + 1]['max_x'] = 25 + (i * 54) + 55

    for i in range(9):
        pt_dict_periode[i + 1] = {}
        pt_dict_periode[i + 1]['min_y'] = 35 + (i * 54)
        pt_dict_periode[i + 1]['max_y'] = 35 + (i * 54) + 55

# Mets le code à exécuter à chaque image ici
def draw():
    image(
        carte,  # L'image à dessiner
        0,  # Le x du coin supérieur gauche
        0,  # Le y du coin supérieur gauche
        width,  # La largeur de l'image
        height  # La hauteur de l'image
    )

# Place ici le code à exécuter lorsque la souris est cliquée
def mouse_pressed():
    x_coord = mouse.x
    y_coord = mouse.y
    if y_coord > 415:
        x_coord -= 30

    for x in pt_dict_groupe:
        if pt_dict_groupe[x]['min_x'] <= x_coord <= pt_dict_groupe[x]['max_x']:
            groupe = x
    for y in pt_dict_periode:
        if pt_dict_periode[y]['min_y'] <= y_coord <= pt_dict_periode[y]['max_y']:
            periode = y
    for element in pt_dict:
        if pt_dict[element]['groupe'] == groupe and pt_dict[element]['periode'] == periode:
            print(pt_dict[element]['nom'], 'is a', pt_dict[element]
                  ['apparance'], 'and is a', pt_dict[element]['phase'])


def charge_donnees_pt(nom_fichier):
    with open(nom_fichier) as f:
        for ligne in f:
            info = ligne.strip().split(',')
            pt_dict[int(info[0])] = {
                'nom': info[1],
                'periode': int(info[7]),
                'groupe': int(info[8]),
                'phase': info[9],
                'apparance': info[28]
            }


run()
