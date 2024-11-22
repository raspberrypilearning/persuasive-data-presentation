#!/bin/python3

# En-têtes de données : 0 Nom de la race, 1 Type, 2 Prix moyen (en dollars américains), 3 Score d'intelligence, 4 Score de popularité aux États-Unis 2017

from pygal import *

with open('dog_breed_characteristics.csv') as f:
    donnees = f.read()
    lignes = donnees.splitlines()

choix = 0


def main():

    choix = input(
        'Analyse des chiens jouets. Que veux-tu voir ? \n1. Prix moyen, \n2. Popularité, \n3. Intelligence, \nChoix :')

    if choix == '1':
        graphique = Bar(width=600, height=400,
                    title=' 🐶 Prix moyen des chiens jouets par race 🐶 ')
        for ligne in lignes:
            info = ligne.split(',')
            NomRace = info[0]
            Type = info[1]
            PrixMoy = info[2]
            Intelligence = info[3]
            Popularite = info[4]
            if Type == 'Jouet':
                graphique.add(NomRace, float(PrixMoy))
        graphique.render()

    if choix == '2':
        graphique = Pie(width=600, height=400,
                    title=' 🐶 Prix moyen des chiens jouets par race 🐶 ')
        for ligne in lignes:
            info = ligne.split(',')
            NomRace = info[0]
            Type = info[1]
            PrixMoy = info[2]
            Intelligence = info[3]
            Popularite = info[4]
            if Type == 'Jouet':
                graphique.add(NomRace, float(Popularite))
        graphique.render()

    if choix == '3':
        graphique = Bar(width=600, height=400,
                    title='🐶 Intelligence des chiens jouets par race 🐶')
        for ligne in lignes:
            info = ligne.split(',')
            NomRace = info[0]
            Type = info[1]
            PrixMoy = info[2]
            Intelligence = info[3]
            Popularite = info[4]
            if Type == 'Jouet':
                graphique.add(NomRace, float(Intelligence))
        graphique.render()
    main()


main()
