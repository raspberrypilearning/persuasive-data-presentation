#!/bin/python3
from p5 import *
from random import randint

# Een visualisatie van vulkaanuitbarstingen sinds 2010

# CSV labels: 0 Jaar, 1 Maand, 2 Dag, 3 Naam, 4 Locatie, 5 Land, 6 Breedtegraad, 7 Lengtegraad, 8 Hoogte, 9 Type, 10 Status

from xy import get_xy_coords

kleuren = {}

# Teken de vulkaan op de kaart
def teken_vulkaan(kleur, x, y):
    fill(kleur)
    ellipse(x, y, 12, 12)


def preload():
    wereldkaart
    kaart = load_image('mercator.jpeg')


def setup():
    size(991, 768)
    image(
        kaart, # De afbeelding om te tekenen
        0, # De x van de linkerbovenhoek
        0, # De y van de linkerbovenhoek
        breedte, # De breedte van de afbeelding
        hoogte # De hoogte van de afbeelding
    )
    load_data ('volcano-data.csv')
    draw_data()


def load_data(file_name):
    # Maak voor elke waarneming een dictionary op basis van de gegevens in het csv-bestand

    wereldwijde vulkaan_uitbarstingen

    vulkaan_uitbarstingen = []

    with open(file_name) as f:
        for line in f:
            info = line.split(',')
            vulkaan_dict = {
                'lengtegraad': info[7],
                'breedtegraad': info[6],
                'jaar': info[0],
                'regio': info[5]
            }
            # Bewaar dictionary in een lijst
            vulkaan_uitbarstingen.append(vulkaan_dict)


def draw_data():
    no_stroke()

    blauw_waarde = 0
    # Gebruik de breedte- en lengte-gegevens om de xy-coördinaten voor de vorm te berekenen
    for uitbarsting in vulkaan_uitbarstingen:
        lengtegraad= float(uitbarsting['lengtegraad'])
        breedtegraad = float(uitbarsting['breedtegraad'])
        region_coords = get_xy_coords(lengtegraad, breedtegraad)
        regio_x = region_coords['x']
        regio_y = region_coords['y']
        kleur = Color(255, 100, blauw_waarde) # Selecteer een willekeurige kleur
        kleuren[kleur.hex] = uitbarsting
        draw_vulkaan(kleur, regio_x, regio_y)
        blauw_waarde += 1


def mouse_pressed():
    # Zet code die moet worden uitgevoerd wanneer de muis wordt ingedrukt hier
    pixel_kleur = Color(get(mouse_x, mouse_y)).hex
    if pixel_kleur in kleuren:
        feiten = kleuren[pixel_kleur]
        print('Er barstte een vulkaan uit in ' +
              feiten['regio'] + ' in ' + feiten['jaar'])
    else:
        print('Regio niet gedetecteerd')


run()
