#!/bin/python3
from p5 import *

from xy import obt_xy_coords

# Dessiner l'OVNI sur la carte
def dessine_ovni(forme, x, y):

    global boule_de_feu, cercle, tri, lumiere, disque, divers, cylindre
    boule_de_feu = Color(252, 186, 3)
    cercle = Color(32, 201, 49)
    tri = Color(241, 245, 32)
    lumiere = Color(247, 247, 245)
    disque = Color(189, 189, 172)
    divers = Color(255, 0, 0)
    cylindre = Color(73, 99, 230)

    if forme == 'boule_de_feu':
        fill(boule_de_feu)
        ellipse(x, y, 15, 10)
    elif forme == 'cercle':
        fill(cercle)
        ellipse(x, y, 8, 8)
    elif forme == 'triangle':
        fill(tri)
        triangle(x-8, y-15, x, y, x+8, y-15)
    elif forme == 'lumiere':
        fill(lumiere)
        ellipse(x, y, 15, 15)
    elif forme == 'disque':
        fill(disque)
        ellipse(x, y, 20, 10)
    elif forme == 'cylindre' or forme == 'cigare':
        fill(cylindre)
        rect(x, y, 20, 10)
    else:
        fill(divers)
        ellipse(x, y, 10, 10)


def prechargement():
    global carte
    carte = load_image('mercator.jpeg')


def setup():

    size(991, 768)
    charge_donnees('ufo-sightings.csv')
    image(
        carte,  # L'image à dessiner
        0,  # Le x du coin supérieur gauche
        0,  # Le y du coin supérieur gauche
        width,  # La largeur de l'image
        height  # La hauteur de l'image
    )
    dessine_donnees()


def charge_donnees(nom_fichier):

    # Créer un dictionnaire pour chaque site basé sur les données du fichier csv

    global observations_ovni

    observations_ovni = []

    with open(nom_fichier) as f:
        for ligne in f:
            info = ligne.split(',')
            dict_ovni = {
                'date': info[0],
                'heure': info[1],
                'état': info[2],
                'pays': info[3],
                'forme': info[4],
                'durée': info[5],
                'latitude': info[6],
                'longitude': info[7]
            }
            observations_ovni.append(dict_ovni) # Stocker le dictionnaire dans une liste


def dessine_donnees():

    # Utilise les données de latitude et de longueur pour calculer les coordonnées x y de la forme

    for observation in observations_ovni:

        longitude = float(observation['longitude'])
        latitude = float(observation['latitude'])

        region_coords = obt_xy_coords(longitude, latitude)

        region_x = coords_region['x']
        region_y = coords_region['y']

        forme = observation['forme']

        dessine_ovni(formes, region_x, region_y)


def mouse_pressed():

    # Affiche un message en fonction de la forme sur laquelle l'utilisateur a appuyé

    couleur_pixel = Color(get(mouse_x, mouse_y)).hex
    if couleur_pixel == boule_de_feu.hex:
        print('Un OVNI boule de feu a été repéré ici !')
    if couleur_pixel == cercle.hex:
        print('Un OVNI en forme de cercle a été repéré ici !')
    if couleur_pixel == tri.hex:
        print('Un OVNI en forme de triangle a été repéré ici !')
    if couleur_pixel == lumiere.hex:
        print('Un OVNI fait de lumière a été repéré ici !')
    if couleur_pixel == disque.hex:
        print('Un OVNI en forme de disque a été repéré ici !')
    if couleur_pixel == divers.hex:
        print('Un OVNI de forme aléatoire a été repéré ici !')
    if couleur_pixel == cylindre.hex:
        print('Un OVNI en forme de cylindre a été repéré ici !')
    else:
        print('Il n\'y a eu aucune observation d\'OVNI dans cette zone !')


run()
