#!/bin/python3
from math import radians, pi, log, tan


def convert_bre_leng(breedtegraad, lengtegraad, kaart_breedte, kaart_hoogte):

    false_easting = 180
    straal = kaart_breedte / (2 * pi)
    breedtegraad = radians(breedtegraad)
    lengtegraad = radians (lengtegraad + false_easting)

    x_coord = lengtegraad * straal

    y_afst_van_evenaar = straal * log(tan(pi / 4 + breedtegraad / 2))
    y_coord = kaart_hoogte / 2 - y_afst_van_evenaar

    coördinaten = {'x': x_coord, 'y': y_coord}

    return coördinaten


def get_xy_coords(lengtegraad, breedtegraad, kaart_breedte=991, kaart_hoogte=768):

    coördinaten = None

    coördinaten = convert_bre_leng(breedtegraad, lengtegraad, kaartbreedte, kaarthoogte)
    return coördinaten
