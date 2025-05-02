#!/bin/python3

# Gegevens rubrieken: 0 Rasnaam, 1 Type, 2 Gemiddelde prijs (Amerikaanse dollars), 3 Intelligentiescore, 4 Populariteitsscore VS 2017

from pygal import *

with open('dog_breed_characteristics.csv') als f:
    data = f.read()
    lines = data.splitlines()

keuze = 0


def main():

    keuze = input(
        'Analyseren van kleine honden. Wat zou je willen zien? \n1. Gemiddelde prijs, \n2. Populariteit, \n3. Intelligentie, \nKeuze:')

    if keuze == '1':
        chart = Bar(width=600, height=400,
                    title=' 🐶 Gemiddelde prijs van kleine honden per ras 🐶 ')
        for line in lines:
            info = line.split(',')
            Rasnaam = info[0]
            Type = info[1]
            GemPrijs = info[2]
            Intelligentie = info[3]
            Populariteit = info[4]
            if Type == 'Toy':
                chart.add(RasNaam, float(GemPrijs))
        chart.render()

    if keuze == '2':
        chart = Pie(width=600, height=400,
                    title=' 🐶 Populariteit van kleine honden per ras 🐶 ')
        for line in lines:
            info = line.split(',')
            RasNaam = info[0]
            Type = info[1]
            GemPrijs = info[2]
            Intelligentie = info[3]
            Populariteit = info[4]
            if Type == 'Toy':
                chart.add(RasNaam, float(Populariteit))
        chart.render()

    if keuze == '3':
        chart = Bar(width=600, height=400,
                    title='🐶 Intelligentie van kleine honden per ras 🐶')
        for line in lines:
            info = line.split(',')
            RasNaam = info[0]
            Type = info[1]
            GemPrijs = info[2]
            Intelligentie = info[3]
            Populariteit = info[4]
            if Type == 'Toy':
                chart.add(RasNaam, float(Intelligentie))
        chart.render()
    main()


main()
