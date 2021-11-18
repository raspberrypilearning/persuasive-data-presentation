## Expand and test - User interaction

Now its time to add some user interaction to your data visualisation!

![A screenshot of the ISS expedition project. The user is asked to input which crew expedition number they would like to explore.](images/user-interaction.PNG)

--- task ---

Look at the [ISS expedition project](https://trinket.io/python/822033c5b6){:target="_blank"} project. It asks the user to choose an ISS expedition to explore. The user enters a number and then this number is used to:
+ access the relevant data for that expedition
+ draw flags on the ISS based on the data
+ display the relevant expedition data as output for the user

**Could your project do something similar?**

Look at the [UFO tracker](https://trinket.io/python/cb376de667){:target="_blank"} project. This project allows the user to click on the different shapes that are displayed on the map. When the user clicks on an object, a message is shown to say the **type** of UFO that was spotted in that location. 

**Could you use this idea to help you add user interaction to your project?**

Explore the [World Happiness Index](https://trinket.io/python/0507433548){:target="_blank"} project. This asks the user to choose what type of data is displayed to them in a graph.

**Could you give your user options about the type of data they want to see?**

Think about your own project and the data that you want your users to be able to explore. Draw inspiration from the example projects and **think about how your project could interact with the user**. 

--- /task ---

--- task ---

Add user interaction to your project. Here is a reminder of some of the skills that you might need to do this:

--- collapse ---
---
title: Interaction with the mouse
---

You can create a `mouse_pressed()` function to work with the **p5** library. It allows a task to be carried out when the mouse is pressed. 

The code below detect the colour of the pixel that has been clicked by the mouse:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
pixel_colour = color(get(mouse_x, mouse_y))

--- /code ---

This piece of code can be used with a selection (`if`) statement to make something happen based on the pixel colour. 

An example of this happening can be seen in the **UFO sightings** project:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 101
line_highlights: 
---
def mouse_pressed():
  
  # Display a message depending on what shape the user has pressed
  
  pixel_colour = color(get(mouse_x, mouse_y))
  if pixel_colour == fireball:
    print('A fireball UFO was spotted here!')
  elif pixel_colour == circle:
    print('A circle shaped UFO was spotted here!')
  elif pixel_colour == tri:
    print('A triangle shaped UFO was spotted here!')
  elif pixel_colour == light:
    print('A UFO made of light was spotted here!')
  elif pixel_colour == disk:
    print('A disk shaped UFO was spotted here!')
  elif pixel_colour == misc:
    print('A random shaped UFO was spotted here!')
  elif pixel_colour == cylinder:
    print('A cylinder shaped UFO was spotted here!')
  else:
    print('There were no UFO sightings in this area!')

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Interaction based on user input
---

A good way to interact with your user is to ask them a question. Their response can then be held in a variable and used to display the requested data. If you want your question to happen before a map, chart or drawing is displayed then you need to make sure that this is one of the first piece of code that runs. 

Common places to ask a user question:
+ in the main part of your code (not inside a function)
+ in a `main()` function
+ in the `setup()` function (if using p5)

Here is the code for asking a question that was used in the **Happiness index project**:

--- code ---
---
language: python
filename: main.py - main()
line_numbers: true
line_number_start: 15
line_highlights: 4-6
---
def main():
  print('World Happiness Index Data 2019')
  
  choice = input('What would you like to see? \n1. How happy are countries overall? \n2. How much does national wealth matter? \n3. How well does your country look after the disadvantaged? \n4.How generous are people? \n5. How fair and honest are people? \n6. How much freedom do you have? \nChoice:')
  
--- /code ---

--- /collapse ---

--- /task ---



mouse pressed options

user input options




--- save ---
