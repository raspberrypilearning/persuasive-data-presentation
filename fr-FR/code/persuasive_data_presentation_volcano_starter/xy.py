#!/bin/python3
from math import radians, pi, log, tan


def convert_lat_long(latitude, longitude, largeur_carte, hauteur_carte):

    fausse_ordonnee = 180
    rayon = largeur_carte / (2 * pi)
    latitude = radians(latitude)
    longitude = radians(longitude + fausse_ordonnee)

    x_coord = longitude * rayon

    y_dist_depuis_equateur = rayon * log(tan(pi / 4 + latitude / 2))
    y_coord = hauteur_carte / 2 - y_dist_depuis_equateur

    coords = {'x': x_coord, 'y': y_coord}

    return coords


def obt_xy_coords(longitude, latitude, largeur_carte=991, hauteur_carte=768):

    coords = None

    coords = convert_lat_long(latitude, longitude, largeur_carte, hauteur_carte)
    return coords
