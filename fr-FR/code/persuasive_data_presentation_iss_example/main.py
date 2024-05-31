#!/bin/python3
from p5 import *


def preload():
    global iss, drapeau_be, drapeau_ca, drapeau_fr, drapeau_uk, drapeau_gm, drapeau_it, drapeau_jp
    global drapeau_pb, drapeau_ru, drapeau_us
    iss = load_image('iss.jpg')
    drapeau_be = load_image('be.jpg')
    drapeau_ca = load_image('ca.jpg')
    drapeau_fr = load_image('fr.jpg')
    drapeau_uk = load_image('gb.jpg')
    drapeau_gm = load_image('gm.jpg')
    drapeau_it = load_image('it.jpg')
    drapeau_jp = load_image('jp.jpg')
    drapeau_pb = load_image('ne.jpg')
    drapeau_ru = load_image('ru.jpg')
    drapeau_us = load_image('us.jpg')


def setup():
    size(400, 400)
    charge_donnees('iss-expedition-data.csv')

    date = (expedition_date(expedition_choisie))
    astronautes = (expedition_astronauts(expedition_choisie))
    pays = (expedition_pays(expedition_choisie))

    print('Expédition : ' + expedition_choisie)
    print('Date de lancement de la mission : ' + date + '\n')
    print('Astronautes :')
    for astronaute in astronautes:
        print(astronaute)

    print('\nPays représentés :')
    for contree in pays:
        print(contree)


def charge_donnees(nom_fichier):

    # Créer un dictionnaire pour chaque site basé sur les données du fichier csv

    global expeditions

    expeditions = []

    with open(nom_fichier) as f:
        for ligne in f:
            info = ligne.split('\n')
            info = info.split(',')
            expedition_dict = {
                'numéro d\'expédition': info[0],
                'pays représenté': info[1],
                'astronaute': info[2],
                'date de lancement de la mission': info[3]
            }
            expeditions.append(expedition_dict) # Stocker le dictionnaire dans une liste


def expedition_date(nombre):

    for expedition in expeditions:
        if expedition['numéro d\'expédition'] == nombre:
            date = expedition['date de lancement de la mission']

    return date


def expedition_astronautes(nombre):

    astronautes = []

    for expedition in expeditions:
        if expedition['numéro d\'expédition'] == nombre:
            astronaute = expedition['astronaute']
            astronautes.append(astronaute)

    return astronautes


def expedition_pays(nombre):

    pays = []

    for expedition in expeditions:
        if expedition['numéro d\'expédition'] == nombre:
            contree = expedition['pays représenté']
            if contree not in pays:
                pays.append(contree)

    return pays


def draw():

    f_width = 60
    f_height = 35

    positions_drapeau = [[45, 145], [130, 60], [210, 310], [300, 220], [300, 70]]

    pays_dict = {
        'États-Unis d\'Amérique': drapeau_us,
        'Russie': drapeau_ru,
        'Pays-Bas': drapeau_pb,
        'Japon': drapeau_jp,
        'Italie': drapeau_it,
        'Allemagne': drapeau_gm,
        'Royaume-Uni': drapeau_uk,
        'France': drapeau_fr,
        'Canada': drapeau_ca,
        'Belgique': drapeau_be
    }

    image(iss, 0, 0, width, height)

    pays = expedition_pays (expedition_choisie)

    nbr_pays = len(pays)

    for x in range(nbr_pays):
        drapeau = pays[x]
        image_drapeau = pays_dict[drapeau]
        image(image_drapeau, positions_drapeau[x][0],
              positions_drapeau[x][1], f_width, f_height)


print('Choisis une expédition ISS. Entre un nombre de 1 à 65 :')
expedition_choisie = input()

run()
