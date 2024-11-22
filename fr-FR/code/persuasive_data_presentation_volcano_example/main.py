#!/bin/python3
from p5 import *
from random import randint

# Une visualisation des éruptions volcaniques depuis 2010

# En-têtes CSV : 0 Année, 1 Mois, 2 Jour, 3 Nom, 4 Emplacement, 5 Pays, 6 Latitude, 7 Longitude, 8 Altitude, 9 Type, 10 Statut

from xy import obt_xy_coords

couleurs = {}

# Dessiner le volcan sur la carte
def dessiner_volcan(couleur, x, y):
    fill(couleur)
    ellipse(x, y, 12, 12)


def preload():
    global carte
    carte = load_image('mercator.jpeg')


def setup():
    size(991, 768)
    image(
        carte,  # L'image à dessiner
        0,  # Le x du coin supérieur gauche
        0,  # Le y du coin supérieur gauche
        width,  # La largeur de l'image
        height  # La hauteur de l'image
    )
    charge_donnees('volcano-data.csv')
    dessine_donnees()


def charge_donnees(nom_fichier):
    # Créer un dictionnaire pour chaque site basé sur les données du fichier csv

    global eruptions_volcan

    eruptions_volcan = []

    with open(nom_fichier) as f:
        for ligne in f:
            info = ligne.split(',')
            dict_volcan = {
                'longitude': info[7],
                'latitude': info[6],
                'année': info[0],
                'région': info[5]
            }
            # Stocker le dictionnaire dans une liste
            eruptions_volcan.append(dict_volcan)


def dessine_donnees():
    no_stroke()

    valeur_bleu = 0
    # Utilise les données de latitude et de longueur pour calculer les coordonnées x y de la forme
    for eruption in eruptions_volcan:
        longitude = float(eruption['longitude'])
        latitude = float(eruption['latitude'])
        coords_region = obt_xy_coords(longitude, latitude)
        region_x = coords_region['x']
        region_y = coords_region['y']
        couleur = Color(255, 100, valeur_bleu) # Sélectionne une couleur aléatoire
        couleurs[couleur.hex] = eruption
        dessiner_volcan(couleur, region_x, region_y)
        valeur_bleu += 1


def mouse_pressed():
    # Place ici le code à exécuter lorsque la souris est cliquée
    couleur_pixel = Color(get(mouse_x, mouse_y)).hex
    if couleur_pixel in couleurs:
        faits = couleurs[couleur_pixel]
        print('Un volcan est entré en éruption en ' +
              faits['région'] + ' dans ' + faits['année'])
    else:
        print('Région non détectée')


run()
