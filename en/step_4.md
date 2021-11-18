## Expand and test - User interaction

Now its time to add some user interaction to your data visualisation!

![A screenshot of the ISS expedition project. The user is asked to input which crew expedition number they would like to explore.](images/user-interaction.PNG)

--- task ---

Look at the [**ISS expedition project**](https://trinket.io/python/822033c5b6){:target="_blank"} project. It asks the user to choose an ISS expedition to explore. The user enters a number and then this number is used to:
+ access the relevant data for that expedition
+ draw flags on the ISS based on the data
+ display the relevant expedition data as output for the user

Could your project do something similar?

Look at the [**UFO tracker**](https://trinket.io/python/cb376de667){:target="_blank"} project. This project allows the user to click on the different shapes that are displayed on the map. When the user clicks on an object, a message is shown to say the **type** of UFO that was spotted in that location. 

Could you use this idea to help you add user interaction to your project?

Explore the [**World Happiness Index**](https://trinket.io/python/0507433548){:target="_blank"} project. This asks the user to choose what type of data is displayed to them in a graph.

Could you give your user options about the type of data they want to see?

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

--- task ---

**Test:** Run your code and make sure that it does what you expect when the user enters their choice. If your program has multiple options then make sure that you test that **each** option works as expected. 

Finally, ask another person to take a look at your program and provide any feedback on the user interaction element. 

--- /task ---

--- task ---

**Debug:** Below are some potential bugs that might occur when working with user interaction:

--- collapse ---
---
title: The question doesn't appear when the program runs
---
Check that your question and `input()` function have been placed in the correct part of your program. This is typically:
+ in the main part of your code (not inside a function)
+ in a `main()` function
+ in the `setup()` function (if using p5)

--- /collapse ---

--- collapse ---
---
title: Nothing happens when the user enters a number
---

The `input()` function is designed to take whatever a user types and return it as **string**. This means that in your **conditions**, you need to also use string values. You might have a condition that looks like this:

```
if choice == 1:
```
This is checking for the **integer** value: 1 and not the **string** value: 1. To fix this, you can add apostrophes `'` to either side of your number. 

```
if choice == '1':
```

--- /collapse ---

--- collapse ---
---
title: It is not displaying the correct data when I click the mouse
---

The `mouse_pressed()` function that you have created is designed to check the **pixel colour** that has been clicked on the screen. If you have two or more objects that are the same colour then your program will display the data for the first condition in the sequence that is true. 

If you would like your program to display different data for each item that the user clicks then they must all be a **different colour**. You can see an example of how to code this for all of your data points here:

--- code ---
---
language: python
filename: main.py - draw_data()
line_numbers: true
line_number_start: 1
line_highlights: 11
---
def draw_data():
  red_value = 255

  for region in region_list:
    region_name = region['name']
    region_coords = get_region_coords(region_name)
    region_x = region_coords['x']
    region_y = region_coords['y']
    region_colour = color(red_value, 0, 0)
    draw_pin(region_x, region_y, region_colour)
    red_value -= 1

--- /code ---

**Notice** that the colour is originally set to `red_value = 255` this is the most amount of red that you can use. After each data point is draw, the value of `red_value` is reduced by `1`. This ensures that each data point is a different colour. 

--- /collapse ---

--- /task ---




--- save ---
