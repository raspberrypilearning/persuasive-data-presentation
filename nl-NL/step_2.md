## Jouw idee

Gebruik deze stap om je gegevens weergave te plannen. Je kunt het plannen door erover na te denken, te knutselen, te tekenen of te schrijven, of hoe je maar wilt!

![Drie screenshots van voorbeeldprojecten. De eerste toont het ISS met drie vlaggen eraan toegevoegd. De tweede afbeelding toont een grafiek met gegevens van het Happiness Index-project. De derde toont gegevens over UFO-waarnemingen in het Verenigd Koninkrijk.](images/project-examples.png)

### Waarom maak je jouw data visualisatie?

--- task ---

Denk na over het **doel** van de datavisualisatie die je maakt. Er zijn **acht** datasets waaruit je kunt kiezen. Als startproject **of** kun je je eigen dataset vinden over een onderwerp dat je graag onder de aandacht van anderen wilt brengen.

Gebruik een dataset die belangrijk is voor jou. De datasets in de startersprojecten zijn:
+ ISS-expedities
+ Vulkaan uitbarstingen
+ UFO-tracker
+ World Happiness Index
+ Kenmerken van hondenrassen
+ Cafeïnehoudende dranken
+ Bechdel testscores
+ Pokemon-kaartgegevens

--- collapse ---

---
title: Ideeën voor de visualisatie van jouw gegevens
---

Het **doel** van je gegevensvisualisatie kan zijn:

+ Toon de verschillende **expedities** die hebben plaatsgevonden op het **ISS**
+ Laat de **meest intelligente hond** rassen zien
+ Classificeer de verschillende soorten **UFO-waarnemingen** en waar deze zich meestal bevinden
+ Toon gebieden over de hele wereld waar **vulkaanuitbarstingen** hebben plaatsgevonden
+ Ontdek de gebieden over de hele wereld die de **beste plekken zijn om te wonen** (volgens de happiness index)
+ Toon de krachtigste **Pokemon** karakters
+ Analyseer het **cafeïnegehalte van** in populaire drankjes
+ Ontdek de **films** met de beste **Bechdel Test-scores** (dit is een dataset die onderzoekt hoe vrouwen in films worden weergegeven)

--- /collapse ---

Of je kunt je eigen datasets kiezen. Een goede plek om andere datasets te verkennen is [Kaggle](https://www.kaggle.com/datasets){:target="_blank"}.

**Tip:** Als je je eigen data set gaat gebruiken en je wil vormen op een wereldkaart plaatsen dan heb je data nodig die de **lengtegraad** en **breedtegraad** locaties bevatten van de dingen die je wil laten zien.

--- /task ---

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 10px; border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px; margin-bottom: 27px;">In <span style="color: #0faeb0">1854</span> dacht de arts John Snow dat de uitbraak van <span style="color: #0faeb0">cholera</span> in het Soho-gebied van Londen werd veroorzaakt door een vervuilde watervoorziening – het tegendeel tot de algemeen aanvaarde opvatting dat cholera werd veroorzaakt door 'slechte lucht' in het gebied. Om zijn theorie te helpen bewijzen, bracht Snow de sterfgevallen als gevolg van cholera in het gebied in kaart. Op de kaart was duidelijk te zien dat de sterfgevallen zich concentreerden rond Broad Street en dat de bewoners daar hun water haalden uit de pomp in deze straat. Door de gegevens op deze manier weer te geven kon hij de gemeente ervan overtuigen de waterpomp uit te schakelen. Het werd algemeen erkend dat deze visualisatie heeft bijgedragen aan het redden van vele levens.
</div>
<div>
![Een fragment van de cholera kaart van John Snow die infecties in rood laat zien.](images/john-snow-map.png){:width="200px"}
</div>
</div>

### Voor wie is het?

--- task ---

Bedenk voor wie je de weergave gaat maken (je **publiek**).

Wat is de **betekenis** van je weergave? Benadrukt het iets specifieks over de wereld om ons heen?

Zullen de kleuren, vormen, afbeeldingen of manier waarop het patroon wordt herhaald **iets speciaals** voor jou of je publiek betekenen?

Het delen van je data weergave is een geweldige manier om iets over jezelf, je interesses of je cultuur uit te drukken.

--- /task ---

### Aan de slag

--- task ---

Selecteer het juiste **startersproject** voor de door jou gekozen data weergave. De Raspberry Pi code-editor wordt geopend in een nieuw tabblad. Zorg ervoor dat je **ingelogd bent** en klik op **Save** om een kopie in je projecten op te slaan.

Het **ISS-expeditie** [startproject](https://editor.raspberrypi.org/en/projects/data-iss-starter){:target="_blank"}.

Het **Vulkaanuitbarstingen** [startproject](https://editor.raspberrypi.org/en/projects/data-volcano-starter){:target="_blank"}.

Het **UFO-tracker** [startproject](https://editor.raspberrypi.org/en/projects/data-ufo-starter){:target="_blank"}.

Het **World happiness index** [startproject](https://editor.raspberrypi.org/en/projects/data-happiness-starter){:target="_blank"}.

Het **Kenmerken van hondenrassen** [startproject](https://editor.raspberrypi.org/en/projects/data-dogs-starter){:target="_blank"}.

Het **Cafeïnehoudende dranken** [startproject](https://editor.raspberrypi.org/en/projects/data-caffeine-starter){:target="_blank"}.

Het **Bechdel Test scores** [startproject](https://editor.raspberrypi.org/en/projects/data-bechdel-starter){:target="_ blank"}.

De **Pokemon-kaartgegevens** [startproject](https://editor.raspberrypi.org/en/projects/data-cards-starter){:target="_blank"}.

**Je eigen dataset gebruiken**

Als je je eigen dataset gebruikt, dan moet je het lege [startproject](https://editor.raspberrypi.org/en/projects/data-blank-starter){:target="_ blank"} gebruiken. Je zult ook **gegevens** moeten toevoegen aan je eigen dataset.

--- collapse ---
---
title: Voeg je eigen dataset toe
---

Zodra je jouw eigen dataset hebt gevonden, moet je deze **downloaden** als CSV-bestand.

Vervolgens moet je het bestand **openen** en controleren op ontbrekende of ongebruikelijke gegevens.

**Tip 1:** Het is een goed idee om een **hele rij** met gegevens te verwijderen als deze secties bevat die leeg zijn. Dit helpt later problemen met je code te voorkomen.

**Tip 2:** Kijk goed naar de gegevens in je CSV-bestand. Zie jij ongebruikelijke symbolen waar tekst zou moeten staan? Zo ja, dan kun je ook deze rijen verwijderen. Een andere optie is om de symbolen te verwijderen, zolang dat de betekenis van de gegevens niet verandert.

**Tip 3:** Als jouw gegevens veel extra kolommen bevatten die je niet gaat gebruiken voor je weergave, dan is het een goed idee om ze te verwijderen. Dit zal het makkelijker maken om te navigeren en toegang te krijgen tot je gegevens vanuit je code.

Zodra je tevreden bent dat je gegevens er goed uitzien, is het tijd om ze toe te voegen aan je project. Zo werkt het:

1. Zorg ervoor dat je je CSV-bestand hebt opgeslagen als CSV-bestand. Als je het in spreadsheetsoftware hebt bewerkt, moet je mogelijk het bestandstype wijzigen in CSV **voordat** je op Opslaan drukt.
2. Zoek de locatie van je CSV-bestand. Het staat waarschijnlijk in je download-map als je het hebt gedownload van een site als Kaggle.
3. Open het bestand met Notepad (klik met de rechtermuisknop op het bestand en kies **Openen met** > **Notepad**).
4. Verwijder de kopregel (bovenste) met gegevens, aangezien je deze niet nodig hebt voor jouw programma.
5. Scroll naar de onderkant van het bestand en controleer of er geen lege ruimte is onderaan. Als dit het geval is, verwijder het dan.
7. Ga naar je project in de Code Editor.
8. Klik op de knop `+ Add file`.
9. Geef het een zinvolle naam (bijvoorbeeld `mijndata.csv`) en klik vervolgens op `Add file` om te bevestigen.
10. Kopieer alle gegevens uit Notepad (Select All > Copy) en plak deze vervolgens in je nieuwe bestand in je project.

--- /collapse ---

--- /task ---

### Stel je project in

--- task ---

### Voeg je importopdrachten en begincode toe

--- collapse ---
---
title: Gebruik p5 om vormen, kaarten en afbeeldingen te tekenen
---

Als je vormen gaat tekenen met `p5`, dan moet je de importinstructie bovenaan je code opnemen.

De importinstructie importeert **alles** van de code uit de `p5`.

Om p5 te gebruiken, moet je ook twee functies maken en de functie aanroep `run()` toevoegen.

**Functie één**

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 1-7
---
from p5 import *

def setup():  # Runs once at the start size(400, 400)  # Choose the size of your canvas

def draw():  # Runs every frame

run()

--- /code ---

--- /collapse ---

--- collapse ---
---
titel: Gebruik xy om gegevens op een kaart te plaatsen
---

Als je CSV-bestand lengte- en breedtegraad gegevens bevat, kun je dit gebruiken om objecten op een wereldkaart te plaatsen. Het bestand `xy.py` is gemaakt om je de breedtegraad en lengtegraad data te laten converteren naar xy coördinaten die kunnen worden gebruikt in je programma.

Om het bestand `xy.py` te gebruiken, heb je de volgende importinstructie bovenaan je code nodig:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
from xy import get_xy_coords

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Gebruik pygal om grafieken te maken
---

Als je project grafieken heeft dan moet je **pygal** gebruiken. De volgende regel code importeert **pygal** in je programma:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
from pygal import * --- /code ---

De importinstructie importeert **alle** code uit de pygal-bibliotheek.

--- /collapse ---

--- /task ---

--- save ---
