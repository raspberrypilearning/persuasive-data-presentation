#!/bin/python3
from p5 import *
from random import randint

# A visualisation of volcano erruptions since 2010

# CSV Headings: 0 Year, 1 Month, 2 Day, 3 Name, 4 Location, 5 Country, 6 Latitude, 7 Longitude, 8 Elevation, 9 Type, 10 Status

from xy import get_xy_coords

colours = {}

# Draw the volcano on the map
def draw_volcano(colour, x, y):
    fill(colour)
    ellipse(x, y, 12, 12)


def preload():
    global map
    map = load_image('mercator.jpeg')


def setup():
    size(991, 768)
    image(
        map,  # The image to draw
        0,  # The x of the top-left corner
        0,  # The y of the top-left corner
        width,  # The width of the image
        height  # The height of the image
    )
    load_data('volcano-data.csv')
    draw_data()


def load_data(file_name):
    # Create a dictionary for each siting based on the data in the csv file

    global volcano_eruptions

    volcano_eruptions = []

    with open(file_name) as f:
        for line in f:
            info = line.split(',')
            volcano_dict = {
                'longitude': info[7],
                'latitude': info[6],
                'year': info[0],
                'region': info[5]
            }
            # Store dictionary in a list
            volcano_eruptions.append(volcano_dict)


def draw_data():
    no_stroke()

    blue_value = 0
    # Use the lat and long data to calculate the x y coords for the shape
    for eruption in volcano_eruptions:
        longitude = float(eruption['longitude'])
        latitude = float(eruption['latitude'])
        region_coords = get_xy_coords(longitude, latitude)
        region_x = region_coords['x']
        region_y = region_coords['y']
        colour = Color(255, 100, blue_value)  # Select a random colour
        colours[colour.hex] = eruption
        draw_volcano(colour, region_x, region_y)
        blue_value += 1


def mouse_pressed():
    # Put code to run when the mouse is pressed here
    pixel_colour = Color(get(mouse_x, mouse_y)).hex
    if pixel_colour in colours:
        facts = colours[pixel_colour]
        print('A volcano erupted in ' +
              facts['region'] + ' in ' + facts['year'])
    else:
        print('Region not detected')


run()
