#!/bin/python3
from p5 import *
from random import randint

pt_dict = {}
pt_dict_group = {}
pt_dict_period = {}

# Zet de code om eenmalig uit te voeren hier onder
def setup():
    wereldkaart
    load_pt_data('pt.csv')
    setup_coords()
    size(1024, 576)
    kaart = load_image('pt.png')


def setup_coords():

    for i in range(18):
        pt_dict_group[i + 1] = {}
        pt_dict_group[i + 1]['min_x'] = 25 + (i * 54)
        pt_dict_group[i + 1]['max_x'] = 25 + (i * 54) + 55

    for i in range(9):
        pt_dict_period[i + 1] = {}
        pt_dict_period[i + 1]['min_y'] = 35 + (i * 54)
        pt_dict_period[i + 1]['max_y'] = 35 + (i * 54) + 55

# Zet hier code om bij elk frame uit te voeren
def draw():
    image(
        kaart, # De afbeelding om te tekenen
        0, # De x van de linkerbovenhoek
        0, # De y van de linker bovenhoek
        breedte, # De breedte van de afbeelding
        hoogte # De hoogte van de afbeelding
    )

# Zet code die moet worden uitgevoerd wanneer de muis wordt ingedrukt hier
def mouse_pressed():
    x_coord = mouse.x
    y_coord = mouse.y
    if y_coord > 415:
        x_coord -= 30

    for x in pt_dict_group:
        if pt_dict_group[x]['min_x'] <= x_coord <= pt_dict_group[x]['max_x']:
            group = x
    for y in pt_dict_period:
        if pt_dict_period[y]['min_y'] <= y_coord <= pt_dict_period[y]['max_y']:
            period = y
    for element in pt_dict:
        if pt_dict[element]['groep'] == group and pt_dict[element]['periode'] == period:
            print(pt_dict[element]['naam'], 'is een', pt_dict[element]
                  ['uiterlijk'], 'en is een', pt_dict[element]['fase'])


def load_pt_data(file_name):
    with open(file_name) as f:
        for line in f:
            info = line.strip().split(',')
            pt_dict[int(info[0])] = {
                'naam': info[1],
                'periode': int(info[7]),
                'groep': int(info[8]),
                'fase': info[9],
                'uiterlijk': info[28]
            }


run()
