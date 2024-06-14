#!/bin/python3
from p5 import *


def preload():
    global iss, be_vlag, ca_vlag, fr_vlag, uk_vlag, gm_vlag, it_vlag, jp_vlag
    global ne_vlag, ru_vlag, us_vlag
    iss = load_image('iss.jpg')
    be_vlag = load_image('be.jpg')
    ca_vlag = load_image('ca.jpg')
    fr_vlag = load_image('fr.jpg')
    uk_vlag = load_image('gb.jpg')
    gm_vlag = load_image('gm.jpg')
    it_vlag = load_image('it.jpg')
    jp_vlag = load_image('jp.jpg')
    ne_vlag = load_image('ne.jpg')
    ru_vlag = load_image('ru.jpg')
    us_vlag = load_image('us.jpg')


def setup():
    size(400, 400)
    load_data ('iss-expedition-data.csv')

    datum = (expeditie_datum(gekozen_expeditie))
    astronauten = (expeditie_astronauten(gekozen_expeditie))
    landen = (expeditielanden(gekozen_expeditie))

    print('Expeditie: ' + gekozen_expeditie)
    print('Lanceringsdatum missie: ' + datum + '\n')
    print('Astronauten:')
    for astronaut in astronauten:
        print(astronaut)

    print('\nVertegenwoordigde landen:')
    for land in landen:
        print(land)


def load_data(file_name):

    # Maak voor elke locatie een dictionary op basis van de gegevens in het csv-bestand

    global expedities

    expedities = []

    with open(file_name) as f:
        for line in f:
            info = line.strip('\n')
            info = info.split(',')
            expeditie_dict = {
                'expeditienummer': info[0],
                'vertegenwoordigend land': info[1],
                'astronaut': info[2],
                'lanceringsdatum missie': info[3]
            }
            expedities.append(expedition_dict) # Bewaar dictionary in een lijst


def expeditie_datum(number):

    for expeditie in expedities:
        if expeditie['expeditienummer'] == number:
            datum = expeditie['lanceringsdatum missie']

    return datum


def expeditie_astronauten(number):

    astronauten = []

    for expeditie in expedities:
        if expeditie['expeditienummer'] == number:
            astronaut = expeditie['astronaut']
            astronauten.append(astronaut)

    return astronauten


def expeditie_landen(number):

    landen = []

    for expeditie in expedities:
        if expeditie['expeditienummer'] == number:
            land = expeditie['vertegenwoordigend land']
            if land not in landen:
                landen.append(land)

    return landen


def draw():

    v_breedte = 60
    v_hoogte = 35

    vlag_posities = [[45, 145], [130, 60], [210, 310], [300, 220], [300, 70]]

    land_dict = {
        'Verenigde Staten van Amerika': us_vlag,
        'Rusland': ru_vlag,
        'Nederland': ne_vlag,
        'Japan': jp_vlag,
        'Italië': it_vlag,
        'Duitsland': gm_vlag,
        'Verenigd Koninkrijk': uk_vlag,
        'Frankrijk': fr_vlag,
        'Canada': ca_vlag,
        'België': be_vlag
    }

    image(iss, 0, 0, breedte, hoogte)

    landen = expeditielanden(gekozen_expeditie)

    aantal_landen = len(landen)

    for x in range(aantal_landen):
        vlag = landen[x]
        vlag_image = land_dict[vlag]
        image(vlag_image, vlag_posities[x][0],
              vlag_posities[x][1], v_breedte, v_hoogte)


print('Kies een ISS-expeditie. Voer een getal in van 1 tot 65:')
gekozen_expeditie = input()

run()
