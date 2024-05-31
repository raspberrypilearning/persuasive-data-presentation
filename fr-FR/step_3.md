## Construire et tester - Dessiner ou construire un graphique

Il est maintenant temps de réaliser ton projet de visualisation de données.

![Une capture d'écran du projet d'expédition ISS. Il y a une illustration de l'ISS avec trois drapeaux en haut. L’un des drapeaux est russe, l’un est pour les États-Unis d’Amérique, l’autre pour le Royaume-Uni.](images/iss-project.PNG)

Pour réussir un projet de programmation, tu dois utiliser les compétences de **décomposition** pour décomposer le problème en parties plus petites et plus faciles à gérer. Cela signifie que tu dois prendre chaque partie à la fois et la faire fonctionner avant de passer à la partie suivante.

**Astuce :** teste ton code après chaque nouvelle section pour qu'il soit plus facile de trouver et de corriger de nouvelles erreurs.

--- collapse ---
---
title: Exemple de décomposition
---

Ton idée nécessite qu'un dessin apparaisse à l'écran en fonction des données contenues dans un fichier texte ou csv ? Si c'est le cas, tu peux décomposer ce problème de la manière suivante :

1. Écrit le code pour dessiner une forme ou charger une image
2. Fais apparaître l'image au centre de l'écran pour la tester
3. Charge les données requises depuis le fichier texte ou csv
4. `print()` les données dont tu as besoin pour l'emplacement de l'image pour vérifier que le code fonctionne
5. Utilise les données pour placer l'image au bon endroit

--- /collapse ---

Pense aux étapes que tu devras suivre pour réussir ton projet. Auras-tu besoin d’afficher un graphique ou une image ? De quelles compétences auras-tu besoin pour y parvenir ?

--- task ---

Tu as acquis des compétences vraiment utiles. Voici un rappel pour t'aider à réaliser ta visualisation de données :

### Formes et images

[[[p5-coordinates]]]

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-python-quad]]]

--- collapse ---

---
title: Utiliser les caractères emoji
---

Tu peux utiliser des caractères emoji dans la fonction p5 text() pour utiliser un emoji pour représenter ton joueur.

Voici un exemple :

--- code ---
---
language: python filename: main.py line_numbers: line_number_start:
line_highlights:
---
def setup(): size(400, 400) text_align(CENTER, TOP)  # Position around the centre

def draw_emoji(emoji, size):  # snake text_size(size)  # controls the size of the emoji text(emoji, 200, 200)

--- /code ---

--- /collapse ---

[[[processing-translation]]]

[[[processing-rotation]]]


--- collapse ---
---
title: Placer une forme en fonction de la latitude et de la longitude
---

Le fichier `xy.py` est disponible dans tous les projets de démarrage. Ce fichier prendra les données **longitude** et **latitude** de ton fichier **CSV** et renverra les coordonnées d'une forme à placer sur une image.

L'exemple de code ci-dessous montre les données `longitude` et `latitude` accessibles à partir du dictionnaire. Il transmet ensuite ces données comme arguments dans la fonction `obt_xy_coords` qui renvoie ensuite les coordonnées.

--- code ---
---
language: python filename: line_numbers: false line_number_start: 1
line_highlights: 10-12
---
def draw_data():

  no_stroke()

  # Use the lat and long data to calculate the x y coords for the shape

  i = 255

  for eruption in volcano_eruptions: longitude = float(eruption['longitude']) latitude = float(eruption['latitude']) region_coords = get_xy_coords(longitude, latitude)  # return coordinates to place map pin region_x = region_coords['x'] region_y = region_coords['y'] colour = Color(i, 255, 255) colours[colour.hex] = eruption draw_volcano(colour, region_x, region_y) i -= 2 --- /code ---

--- /collapse ---

### Couleurs et effets

[[[generic-theory-simple-colours]]]

--- collapse ---

---
title: Couleur en p5
---

La fonction p5 Color() attend trois nombres : un pour le rouge, le vert et le bleu.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 1
---
blue = Color(50, 70, 206)  # Red = 50, Green = 70, Blue = 206

--- /code ---

--- /collapse ---

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

--- collapse ---
---
title: Modifier la valeur d'une couleur d'épingle de carte
---
Cet exemple modifie la valeur du rouge à chaque fois que le code place une épingle :

**N'oublie pas** de définir également un dictionnaire de `couleurs` dans la partie principale de ton code, généralement vers le haut.

--- code ---
---
language: python filename: line_numbers: false line_number_start:
line_highlights: 1, 9, 17-20
---
colours = {}

def draw_data():

  no_stroke()

  # Use the lat and long data to calculate the x y coords for the shape

  red = 255

  for eruption in volcano_eruptions: longitude = float(eruption['longitude']) latitude = float(eruption['latitude']) region_coords = get_xy_coords(longitude, latitude) region_x = region_coords['x'] region_y = region_coords['y'] colour = Color(red, 0, 0) colours[colour.hex] = eruption draw_volcano(colour, region_x, region_y) red -= 2 --- /code ---



--- /collapse ---

--- collapse ---
---
title: Changer la valeur de plusieurs couleurs d'épingles de carte
---

Cet exemple modifie les valeurs du rouge, du vert et du bleu à chaque fois que le code place une épingle :

**N'oublie pas** de définir également un dictionnaire de `couleurs` dans la partie principale de ton code, généralement vers le haut.

--- code ---
---
language: python filename: line_numbers: false line_number_start:
line_highlights: 1, 9-11, 19-24
---
colours = {}

def draw_data():

    no_stroke()
    
    # Use the lat and long data to calculate the x y coords for the shape
    
    red = 255
    green = 0
    blue = 255
    
    for eruption in volcano_eruptions:
        longitude = float(eruption['longitude'])
        latitude = float(eruption['latitude'])
        region_coords = get_xy_coords(longitude, latitude)
        region_x = region_coords['x']
        region_y = region_coords['y']
        colour = Color(red, green, blue)
        colours[colour.hex] = eruption
        draw_volcano(colour, region_x, region_y)
        red -= 1  # Change the red value
        green += 1  # Change the green value
        blue -= 1  # Change the blue value
--- /code ---

--- /collapse ---

--- collapse ---
---
titre: Choisir des couleurs aléatoires pour tes épingles de carte
---

Au début de ton code, avec tes autres imports, tu devras importer `randint` depuis la bibliothèque `random`.

Tu devras également définir un dictionnaire `couleurs` dans la partie principale de ton code. Ceci est généralement placé sous tes déclarations d'importation.

Tu peux alors choisir une couleur aléatoire pour les couleurs de ta région, à chaque fois autour de la boucle for. Il y a une petite chance que deux couleurs ou plus finissent par être les mêmes, mais c'est une très petite chance.

**Attention :** choisir des couleurs aléatoires signifie que tes épingles changeront de couleur à chaque boucle.

--- code ---
---
language: python filename: line_numbers: false line_number_start:
line_highlights: 1, 3, 17-19
---
from random import randint

colours = {}

def draw_data():

  no_stroke()

  # Use the lat and long data to calculate the x y coords for the shape

  for eruption in volcano_eruptions: longitude = float(eruption['longitude']) latitude = float(eruption['latitude']) region_coords = get_xy_coords(longitude, latitude) region_x = region_coords['x'] region_y = region_coords['y'] colour = Color(randint(0,255), randint(0,255), randint(0,255))  # Select a random colour colours[colour.hex] = eruption draw_volcano(colour, region_x, region_y) --- /code ---


--- /collapse ---

--- collapse ---
---
title: Définir les couleurs d’arrière-plan au démarrage de ton programme
---

Définis une nouvelle fonction appelée `dessine_arriere_plan()` et crée un appel à celle-ci dans `draw():`, après un appel à `no_stroke()`.

--- code ---
---
language: python filename: main.py - draw_background() line_numbers: false line_number_start: 1
line_highlights: 1-4
---
def draw_background(colour): # Background colour fill(colour) rect(0, 0, 400, 400)

--- /code ---

Puis crée un appel avec `draw()`:

--- code ---
---
language: python filename: main.py - draw() line_numbers: false line_number_start: 1
line_highlights: 8
---
def draw():

    red = Color(255,0,0)
    green = Color(0,255,0)
    blue = Color(0,0,255)
    
    no_stroke()
    draw_background(red)

--- /code ---

Si tu veux que ton arrière-plan inclue plus de couleurs, tu devras ajouter plus de paramètres.

--- code ---
---
language: python filename: main.py - draw_background() line_numbers: false line_number_start: 1
line_highlights: 1, 6-7
---
def draw_background(green, blue):

    # Background colour
    fill(blue)
    rect(0, 0, 400, 200)
    fill(green)
    rect(0, 200, 400, 200)

--- /code ---

Puis crée un appel avec `draw()`:

--- code ---
---
language: python filename: main.py - draw() line_numbers: false line_number_start: 1
line_highlights: 7-8
---
def draw():

    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    blue = Color(0, 0, 255)
    
    no_stroke()
    draw_background(green, blue)

--- /code ---

--- /collapse ---

### Charger des données à partir de fichiers texte

--- collapse ---
---
title: Charger des données dans une variable
---

Pour écrire le **contenu entier** d'un fichier texte dans une **variable**, tu peux utiliser le code suivant :

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start:
line_highlights:
---
my_text_file = ''  # Initialises the variable so that it can be added to

with open('filename.csv') as f:  # Opens the file temporarily for line in f:  # Loops through each line in the file my_text_file += line  # Adds the line to the current contents of the variable

--- /code ---

Cela peut être un extrait de code utile si tu travailles avec de très petits fichiers texte et que tu n'as pas l'intention d'effectuer beaucoup d'actions sur les données chargées. Par exemple, tu voudrais juste afficher le contenu du fichier texte.

--- /collapse ---

--- collapse ---
---
title: Charger les données dans une seule liste
---
Pour écrire **chaque ligne** d'un fichier texte en tant qu'élément **distinct** dans une liste, tu peux utiliser le code suivant :

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start:
line_highlights:
---
my_text_file = []  # Initialises the list so that data can be appended (added) to it

with open('filename.csv') as f:  # Opens the file temporarily for line in f:  # Loops through each line in the file my_text_file.append(line)  # Adds each line as an item in the list --- /code ---

Cela peut être utile si ton fichier texte ne contient qu'**un** élément de données sur **chaque ligne**. Par exemple, il peut s'agir d'une liste de noms de joueurs pour un jeu.

--- /collapse ---

--- collapse ---
---
title: Charger les données dans une liste de listes (une liste 2D)
---
Une liste de listes est souvent appelée liste 2D. Lorsque les données sont stockées dans un fichier CSV, chaque élément d'une ligne (rangée) est séparé par une virgule `,`.

![Une capture d'écran d'un fichier texte. Le fichier texte contient des données sur les éruptions volcaniques. Chaque ligne de données a une date, la longitude, la latitude et l'emplacement de l'éruption du volcan.](images/text-file.PNG)

Tu peux utiliser cette virgule pour créer une liste des éléments pour chaque ligne. Un extrait de code pour cela peut être vu ci-dessous à **ligne 5** :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 1
line_highlights: 5
---
my_text_file = []

with open('filename.csv') as f: for line in f: info = line.split(',')  # Split each item separated by a comma into a list

print(info)

--- /code ---

Si tu exécutes le code ci-dessus, il affichera **la dernière ligne** du fichier CSV sous forme de liste. En effet, pour chaque ligne, la liste `info` a été recréée. Elle n'a pas été ajoutée.

```
['29/12/2020', '6.4', '2.733333333', 'Autour de 94nm au sud de Brass\n']
```

Pour stocker **toutes** les données, tu peux créer une **liste de listes** !

Le code ci-dessous utilise le même code que ci-dessus mais maintenant il **ajoute** la liste `info` à la liste `mon_fichier_texte` à la **ligne 6**. Cela signifie que tu peux maintenant stocker toutes les données du fichier CSV.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 1
line_highlights: 6
---
my_text_file = []

with open('filename.csv') as f: for line in f: info = line.split(',') my_text_file.append(info)  # Add the info list to the my_text_file list

print(my_text_file)

--- /code ---

Les listes 2D sont très utiles pour stocker et parcourir de grandes quantités de données. Cependant, tu dois être très au courant de **ce qui** est stocké et **où** est stocké.

--- /collapse ---

--- collapse ---
---
title: Charger des données dans une liste de dictionnaires
---
Chaque ligne (ligne) d'un fichier CSV peut être stockée dans un **dictionnaire**. Le fichier CSV ci-dessous contient des données sur les éruptions volcaniques ayant eu lieu depuis 2010. Chaque ligne est une nouvelle éruption. Chaque éruption contient des informations sur la date, la longitude, la latitude et l'emplacement, ainsi que d'autres éléments.

![Une capture d'écran d'un fichier texte. Le fichier texte contient des données sur les éruptions volcaniques. Chaque ligne de données a une date, la longitude, la latitude et l'emplacement de l'éruption du volcan.](images/text-file.PNG)

Si ces données étaient stockées dans une liste 2D, tu aurais alors besoin de connaître les valeurs `d'index` des données pour y accéder. Avec un **dictionnaire**, tu as juste besoin de connaître la `clé`. C'est le mot clé utilisé pour représenter les données conservées pour chaque événement. Dans cet exemple, les clés sont `date`, `longitude`, `latitude`et `emplacement`.

Le code ci-dessous montre une **liste de dictionnaires** créés pour le contenu d'un fichier CSV :

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
volcano_eruptions = []  # Initialise the list to store the eruptions

with open(file_name) as f: for line in f: info = line.split(',')  # Split the line into a list volcano_dict = { # Create a dictionary for the event 'date': info[0], 'longitude': info[1], 'latitude': info[2], 'location': info[3] } volcano_eruptions.append(volcano_dict)  # Store dictionary in a list

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Supprimer le \n
---
Quand tu regardes un fichier texte dans sa forme brute, il n'y a pas de `\n` à la fin de chaque ligne. Cependant, lorsque tu charges chaque ligne d'un fichier texte, tu verras qu'un `\n` apparaît. En effet, `\n` signifie **ajouter une nouvelle ligne**. Sans cela, toutes les lignes de texte seraient sur une seule et très longue ligne.

Cela n'est pas utile lorsque tu veux utiliser les données dans ton programme.

Pour supprimer le `\n` tu peux utiliser la méthode `strip()`. Cela supprime tout ce que tu écris entre parenthèses des données.

Tu peux voir un exemple de ceci utilisé à la **ligne 3** ci-dessous :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 1
line_highlights: 3
---
with open(file_name) as f: for line in f:  # For each line in the text file info = line.strip('\n')  # Strip away the \n info = info.split(',')

--- /code ---


--- /collapse ---

### Accéder aux données des listes et dictionnaires

[[[generic-python-list-index]]]

--- collapse ---
---
title: Accéder aux données d'un dictionnaire
---

Un dictionnaire a été créé pour stocker les observations d'ovnis :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start:
line_highlights:
---

    ufo_dict = {
        'date': '12-1-2020',
        'time': '13:55',
        'state': 'TX',
        'country': 'United States of America'
    }

--- /code ---

Les données sont stockées dans un dictionnaire à l'aide d'une **clé**, qui est l'étiquette ou le mot-clé des données.

Les **clés** de ce dictionnaire sont :
+ Date
+ Heure
+ État
+ Pays

Si tu voulais connaître la **date** de l'observation d'ovni, tu utiliserais cet extrait de code :

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start:
line_highlights:
---
ufo_dict['date']

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Accéder aux données à partir d’une liste de dictionnaires
---

Lorsque tu crées une liste de dictionnaires, tu peux parcourir la liste pour rechercher et utiliser les données dont tu as besoin.

### Exemple 1 – expéditions ISS

Voici un exemple de code utilisé pour trouver la date d'une expédition vers l'ISS :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 1
line_highlights:
---
for expedition in expeditions:  # Loop through all of the expedition dictionaries in the expeditions list

    if expedition['expedition number'] == 3:  # Check if the expedition number is equal to 3
        date = expedition['mission launch date']  # If true, store the matching mission launch date

--- /code ---

Remarque comment le code `expedition['numéro d'expédition']` a été utilisé pour accéder aux données du dictionnaire.

`expedition` est utilisé comme espace réservé temporaire pour parcourir la liste. À chaque itération, `expedition` contient le dictionnaire d'expédition **actuel**. La **clé** est alors nommée dans les crochets pour accéder aux données.

### Exemple 2 - Observations d'ovnis

Voici un autre exemple qui a été utilisé pour trouver les valeurs de latitude et de longitude pour les observations d'ovnis.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 1
line_highlights:
---
for sighting in ufo_sightings:  # Loop through all of the sighting dictionaries in the ufo_sightings list

    longitude = float(sighting['longitude'])  # Store the longitude data
    latitude = float(sighting['latitude'])  # Store the latitude data
--- /code ---

Tu peux voir le même schéma se produire avec cet exemple que dans le premier exemple. La boucle parcourt la liste des dictionnaires. Pour chaque boucle, `observation` est utilisée comme espace réservé temporaire pour le dictionnaire. La **clé** est ensuite utilisée pour accéder aux données de latitude et de longitude requises.

Dans ce cas, `float()` a également été utilisé car les données devaient être stockées sous forme de nombre décimal.

--- /collapse ---

### Afficher des graphiques

[[[pygal-library]]]

--- /task ---

--- task ---

**Test :** montre ton projet à quelqu'un d'autre pour avoir son avis.
+ Si tu crées des graphiques, es-tu satisfait du type de graphique que tu as affiché et des données que tu as utilisées ?
+ Si tu ajoutes des dessins sur une carte, es-tu satisfait des formes que tu as choisies ?
+ Si tu crées un autre type de visualisation, pourrait-on l'améliorer d'une manière ou d'une autre ?

--- /task ---

--- task ---

**Débogage :** tu pourrais trouver des bogues dans ton projet que tu dois corriger. Voici quelques bogues courants.

--- collapse ---
---
title: Le message "index out of range" (index hors de portée) s'affiche en permanence
---

Le message d'erreur `index out of range` fait généralement référence à ton code essayant d'accéder à un **élément** dans une **liste** qui n'existe pas.

Si ta liste est liée à un fichier texte :
+ Vérifie que ton fichier texte n'a pas de ligne vide en bas
+ Vérifie que les lignes dans ton fichier texte ont toutes la même quantité d'éléments (ce n'est pas toujours nécessaire mais dans ce cas, cela pourrait causer un problème)

--- /collapse ---

--- collapse ---
---
title: Les données ne sont pas tracées sur ma carte comme prévu
---

Un fichier a été créé pour t'aider dans cette tâche, il s'appelle `xy.py`. Il s'agit d'un fichier supplémentaire dans les projets de démarrage où les données **latitude** et **longitude** ont été incluses dans le fichier CSV.

Le code de ce fichier peut être consulté ci-dessous :

--- code ---
---
language: python filename: xy.py line_numbers: true line_number_start: 1
line_highlights:
---
from math import radians, pi, log, tan

def convert_lat_long(latitude, longitude, map_width, map_height):

    false_easting = 180
    radius = map_width / (2 * pi)
    latitude = radians(latitude)
    longitude = radians(longitude + false_easting)
    
    x_coord = longitude * radius
    
    y_dist_from_equator = radius * log(tan(pi / 4 + latitude / 2))
    y_coord = map_height / 2 - y_dist_from_equator
    
    coords = {'x': x_coord, 'y': y_coord}
    
    return coords


def get_xy_coords(longitude, latitude, map_width=991, map_height=768):

    coords = None
    
    coords = convert_lat_long(latitude, longitude, map_width, map_height)
    return coords

--- /code ---

Ce code prend les données **longitude** et **latitude**, effectue certaines tâches puis renvoie les coordonnées x et y pour placer le dessin au bon endroit.

Si tu utilises ce fichier :
+ Vérifie que tu l'as importé en haut de ton programme principal. Il doit être indiqué `from xy import obt_xy_coords`.
+ Vérifie que tu transmets les données **longitude** et **latitude** dans le bon ordre. Ton appel de fonction devrait être similaire à ceci : `obt_xy_coords(longitude, latitude)`.
+ Vérifie que les données de longitude et de latitude ont été converties au type de données **float** . Ton code devrait ressembler à ceci : `longitude = float(observation['longitude'])`.

--- /collapse ---

--- collapse ---
---
title: Quelque chose n'est "pas défini" (not defined)
---

C'est une erreur courante. Cela signifie généralement qu'une variable, un dictionnaire ou une liste est en train d'être consultée ou modifiée avant qu'elle n'ait été définie.

Par exemple, tu peux utiliser ce code pour ajouter un élément à une liste :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 1
line_highlights:
---
state = 'TX'

ufo_data.append(state) --- /code ---

Cette ligne de code provoquera un message d'erreur car la liste `ufo_data` n'a pas encore été définie. Pour corriger cette erreur, tu dois ajouter une ligne de code qui définit la liste.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 1
line_highlights: 1
---
ufo_data = []

state = 'TX'

ufo_data.append(state)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Mon graphique ne s'affiche pas
---

Vérifie que tu as inclus le code pour afficher le graphique à l'écran :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 1
line_highlights:
---
chart.render()

--- /code ---

Tu devras peut-être également vérifier que tu convertis des valeurs numériques en `float()` pour les nombres décimaux ou `int()` pour les nombres entiers dans ton code.

--- /collapse ---

Tu pourrais trouver un bogue qui n'est pas répertorié ici. Peux-tu trouver un moyen de le corriger ?

**Astuce :** trouve l'exemple de projet qui ressemble le plus au tien et étudie attentivement le code qui a été utilisé pour le faire fonctionner. Cela peut t'aider à repérer des choses que tu pourrais avoir manquées dans ton propre programme.

Nous aimerions connaître tes bogues et la façon dont tu les as résolus. Utilise le bouton Envoyer un commentaire au bas de cette page si tu as trouvé un bogue différent dans ton projet.

--- /task ---


--- save ---
