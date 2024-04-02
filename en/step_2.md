## Your idea

Use this step to plan your data visualisation. You can plan by just thinking, tinkering, drawing or writing, or however you like!

![Three screenshots of example projects. The first is showing the ISS with three flags attached. The second image shows a chart of data from the Happiness Index project. The third shows data points on the UK showing UFO sightings.](images/project-examples.png)

### Why are you making your data visualisation?

--- task ---

Think about the **purpose** of the data visualisation you are creating. There are **eight** datasets to choose from as starter projects **or** you can find your own data set on a topic that you would like to highlight to others. 

Use a dataset that is important to you. The datasets in the starter projects are:
+ ISS expeditions 
+ Volcanic eruptions
+ UFO tracker
+ World happiness index
+ Dog breed characteristics
+ Caffeinated drinks
+ Bechdel Test scores
+ Pokemon card data

--- collapse ---

---
title: Ideas for your data visualisation
---

The **purpose** of your data visualisation could be to:

+ Show the different **expeditions** that have taken place on the **ISS**
+ Demonstrate the **most intelligent dog** breeds 
+ Classify the different types of **UFO sightings** and where they are mostly located
+ Show areas around the world that have experienced **volcanic eruptions**
+ Discover the areas around the world that are the **best places to live** (according to the happiness index)
+ Show the most powerful **pokemon** characters
+ Analyse the **caffeine** levels in popular drinks 
+ Find out the **movies** that have the best **Bechdel Test scores** (this is a data set that looks into how women are represented in movies)

--- /collapse ---

Or you can choose your own, a good place to explore other data sets is [Kaggle](https://www.kaggle.com/datasets){:target="_blank"}. 

**Tip:** If you are going to use your own data set and want to place shapes on a world map then you will need to have data that contains the **longitude** and **latitude** locations for the items that you wish to display. 

--- /task ---

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 10px; border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px; margin-bottom: 27px;">In <span style="color: #0faeb0">1854</span>, the physician John Snow believed that the the outbreak of <span style="color: #0faeb0">cholera</span> in the Soho area of London was being caused by a contaminated water supply — contrary to the commonly held belief that cholera was caused by 'bad air' in the area. To help prove his theory, Snow mapped the deaths from cholera in the area. The map clearly showed the deaths were centred around Broad Street and residents there were getting their water from the pump on this street. By visualising the data in this way, he was able to convince the local council to disable the water pump. It was widely recognised that this visualisation helped to save many lives.
</div>
<div>
![A snippet of John Snow's cholera map showing infections in red.](images/john-snow-map.png){:width="200px"}
</div>
</div>


### Who is it for?

--- task ---

Think about who you will make your data visualisation for (your **audience**).

What is the **significance** of your visualisation? Does it highlight something specific about the world around us?

Will the colours, shapes, images, or charts mean **something special** to you or your audience?

Sharing your data visualisation is a great way to express something about yourself, your interests, or your culture.

--- /task ---

### Get started

--- task ---

Select the correct **starter project** for your chosen data visualisation. The Raspberry Pi code editor will open in a new window. Make sure you are **logged in** and click **Save** to save a copy to your projects.

The **ISS expedition** [starter project](https://editor.raspberrypi.org/en/projects/data-iss-starter){:target="_blank"}.

The **Volcanic eruptions** [starter project](https://editor.raspberrypi.org/en/projects/data-volcano-starter){:target="_blank"}.

The **UFO tracker** [starter project](https://editor.raspberrypi.org/en/projects/data-ufo-starter){:target="_blank"}.

The **World happiness index** [starter project](https://editor.raspberrypi.org/en/projects/data-happiness-starter){:target="_blank"}.

The **Dog breed characteristics** [starter project](https://editor.raspberrypi.org/en/projects/data-dogs-starter){:target="_blank"}.

The **Caffeinated drinks** [starter project](https://editor.raspberrypi.org/en/projects/data-caffeine-starter){:target="_blank"}.

The **Bechdel Test scores** [starter project](https://editor.raspberrypi.org/en/projects/data-bechdel-starter){:target="_blank"}.

The **Pokemon card data** [starter project](https://editor.raspberrypi.org/en/projects/data-cards-starter){:target="_blank"}.

**Using your own data set**

If you are using your own data set then you will need to use the blank [starter project](https://editor.raspberrypi.org/en/projects/data-blank-starter){:target="_blank"}. You will also need to **add** in your own data set. 

--- collapse ---
---
title: Add your own data set
---

Once you have found your own data set you will need to **download** it as a CSV file. 

You should then **open** the file and check it for missing or unusual data.

**Tip 1:** It is a good idea to delete a **whole row** of data if it has sections that are blank. This will help to prevent problems with your code later on. 

**Tip 2:** Look carefully at the data in your CSV file. Can you see any unusual symbols where text should be? If so, you might want to also delete these rows. Another option is to delete the symbols as long as that doesn't change the meaning of the data. 

**Tip 3:** If your data has lots of extra columns that you aren't going to use for your visualisation then it is a good idea to delete them. This will make it easier to navigate and access your data from your code. 

Once you are satisfied that your data is looking good, it is time to add it to your project. Here's how:

1. Make sure that you have saved your CSV file as a CSV file. If you have been editing it in spreadsheet software then you might have to change the file type to CSV **before** pressing save.
2. Find the location of your CSV file. It will most likely be in your downloads folder if you downloaded it from a site like Kaggle.
3. Open the file with notepad (right-click on the file and choose **Open with** > **Notepad**).
4. Delete the header (top) row of data as you will not need this for your program.
5. Scroll to the bottom of your file and check that there isn't a blank space at the bottom. If there is, delete it.
7. Go to your project in the Code Editor.
8. Click on `+ Add file` button.
9. Give it a sensible name (e.g. `mydata.csv`) and then click `Add file` to confirm.
10. Copy all the data from notepad (Select All > Copy) and then paste it into your new file in your project.

--- /collapse ---

--- /task ---

### Set up your project

--- task ---

### Add in your import statements and starter code

--- collapse ---
---
title: Use p5 to draw shapes, maps, and images
---

If you are going to be drawing shapes using `p5` then you will need to include the import statement at the top of your code. 

The import statement imports **all** of the code from the `p5`.

To use p5, you will also need to create two functions and to include the `run()` function call. 

**Function one**

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 1-7
---
from p5 import *

def setup():  # Runs once at the start 
    size(400, 400)  # Choose the size of your canvas

def draw():  # Runs every frame

run()

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Use xy to place data on a map
---

If your CSV file includes longitude and latitude data, then you can use this to place objects on a world map. The file `xy.py` has been created to allow you to convert the latitude and longitude data to xy coordinates that can be used in your program. 

To use the `xy.py` file, you will need the following import statement at the top of your code:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 
---
from xy import get_xy_coords

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Use pygal to create charts
---

If your project requires you to create graphs and charts then you will need to use **pygal**. The following line of code imports **pygal** into your program:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 
---
from pygal import *
--- /code ---

The import statement imports **all** of the code from the pygal library.

--- /collapse ---

--- /task ---

--- save ---
