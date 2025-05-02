#!/bin/python3
from math import radians, pi, log, tan


def convert_bre_leng(breedtegraad, lengtegraad, kaartbreedte, kaarthoogte):

    false_easting = 180
    straal = kaartbreedte / (2 * pi)
    breedtegraad = radians(breedtegraad)
    lengtegraad = radians (lengtegraad + false_easting)

    x_coord = lengtegraad * straal

    y_afst_van_evenaar = straal * log(tan(pi / 4 + breedtegraad / 2))
    y_coord = kaart_hoogte / 2 - y_afst_van_evenaar

    coordinaten = {'x': x_coord, 'y': y_coord}

    return coordinaten


def get_xy_coords(lengtegraad, breedtegraad, kaartbreedte=991, kaarthoogte=768):

    coordinaten = None

    coordinaten = convert_bre_leng(breedtegraad, lengtegraad, kaartbreedte, kaarthoogte)
    return coordinaten
