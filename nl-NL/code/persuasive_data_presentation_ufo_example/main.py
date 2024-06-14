#!/bin/python3
from p5 import *

from xy import get_xy_coords

# Teken de UFO op de kaart
def draw_ufo(vorm, x, y):

    global fireball, circle, tri, light, disk, misc, cylinder
    fireball = Color(252, 186, 3)
    circle = Color(32, 201, 49)
    tri = Color(241, 245, 32)
    light = Color(247, 247, 245)
    disk = Color(189, 189, 172)
    misc = Color(255, 0, 0)
    cylinder = Color(73, 99, 230)

    if vorm == 'fireball':
        fill(fireball)
        ellipse(x, y, 15, 10)
    elif vorm == 'circle':
        fill(circle)
        ellipse(x, y, 8, 8)
    elif vorm == 'triangle':
        fill(tri)
        triangle(x-8, y-15, x, y, x+8, y-15)
    elif vorm == 'light':
        fill(light)
        ellipse(x, y, 15, 15)
    elif vorm == 'disk':
        fill(disk)
        ellipse(x, y, 20, 10)
    elif vorm== 'cylinder' or vorm == 'cigar':
        fill(cylinder)
        rect(x, y, 20, 10)
    else:
        fill(misc)
        ellipse(x, y, 10, 10)


def preload():
    wereldkaart
    kaart = load_image('mercator.jpeg')


def setup():

    size(991, 768)
    load_data ('ufo-sightings.csv')
    image(
        kaart, # De afbeelding om te tekenen
        0, # De x van de linkerbovenhoek
        0, # De y van de linkerbovenhoek
        breedte, # De breedte van de afbeelding
        hoogte # De hoogte van de afbeelding
    )
    draw_data()


def load_data(file_name):

    # Maak voor elke locatie een dictionary op basis van de gegevens in het csv-bestand

    wereldwijde ufo_waarnemingen

    ufo_waarnemingen = []

    with open(file_name) as f:
        for line in f:
            info = line.split(',')
            ufo_dict = {
                'datum': info[0],
                'tijd': info[1],
                'staat': info[2],
                'land': info[3],
                'vorm': info[4],
                'duur': info[5],
                'breedtegraad': info[6],
                'lengtegraad': info[7]
            }
            ufo_waarnemingen.append(ufo_dict) # Bewaar dictionary in een lijst


def draw_data():

    # Gebruik de breedte- en lengte-gegevens om de xy-coördinaten voor de vorm te berekenen

    for waarneming in ufo_waarnemingen:

        lengtegraad= float(waarneming['lengtegraad'])
        breedtegraad = float(waarneming['breedtegraad'])

        region_coords = get_xy_coords(lengtegraad, breedtegraad)

        regio_x = region_coords['x']
        regio_y = region_coords['y']

        vorm = waarneming['vorm']

        draw_ufo(vorm, regio_x, regio_y)


def mouse_pressed():

    # Geef een bericht weer, afhankelijk van welke vorm de gebruiker heeft ingedrukt

    pixel_colour = Color(get(mouse_x, mouse_y)).hex
    if pixel_colour == fireball.hex:
        print('Hier is een vuurbal-UFO gespot!')
    elif pixel_colour == circle.hex:
        print('Hier werd een cirkelvormige UFO gezien!')
    elif pixel_colour == tri.hex:
        print('Hier werd een driehoekige UFO gezien!')
    elif pixel_colour == light.hex:
        print('Een UFO van licht is hier gezien!')
    elif pixel_colour == disk.hex:
        print('Hier werd een schijfvormige UFO gezien!')
    elif pixel_colour == misc.hex:
        print('Hier werd een willekeurig gevormde UFO gespot!')
    elif pixel_colour == misc.hex:
        print('Hier werd een cilindervormige UFO gezien!')
    else:
        print('Er waren geen UFO-waarnemingen in dit gebied!')


run()
