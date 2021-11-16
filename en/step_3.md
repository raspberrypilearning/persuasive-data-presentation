## Build and test

Now it's time to make your data visualisation project.

![A screenshot of the ISS expedition project. There is an illustration of the ISS with three flags on top. One flag is Russian, one is for the United States of America and the other is for the United Kingdom.](images/iss-project.PNG)

In order to be successful with a programming project, you need to use **decomposition** skills to break the problem down into smaller, more manageable parts. This means you should take each part at a time and get it working before moving on to the next part. 

**Tip:** Test your code after each new section to make it easier to find and fix new errors. 

--- collapse ---
---
title: Example decomposition
---

Does your idea require a drawing to appear on the screen based on data in a text file? If so, you can break this problem down in the following way:

1. Write the code for drawing a shape or loading an image
2. Make the image appear in the centre of the screen to test it
3. Load the required data from the text file
4. `print()` the data that you need for the image location to check that the code works
5. Use the data to place the image in the correct location

--- /collapse ---

Think about the steps that you will need to take in order to be successful in your project. Will you need to display a chart or an image? What skills will you need to make that happen?

![A screenshot of the maritime piracy project. A map shows the locations of piracy events that have taken place in 2020, each is represented by a blue dot.](images/piracy-map.PNG)

--- task ---

You have built up some really useful skills. Here is a reminder to help you make your data visualisation:

### Shapes and images

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-add-image]]]

### Colours and effects

[[[generic-theory-simple-colours]]]

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

### Loading data from text files

--- collapse ---
---
title: Load data into a variable
---

To write the **entire contents** of a text file into a **variable**, you can use the following code:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
my_text_file = ''

with open('filename.csv') as f:
  for line in f:
      my_text_file += line

print(my_text_file)
--- /code ---

This can be a useful code snippet if you are working with very small text files and you don't intend to perform many actions on the loaded data. For example, you might want to just display the contents of the text file. 

--- /collapse ---

--- collapse ---
---
title: Load data into a list
---



--- /collapse --- 

--- collapse ---
---
title: Load data into a list of dictionaries
---



--- /collapse ---

--- collapse ---
---
title: Load data into a list of lists
---



--- /collapse ---


### Accessing data from list and dictionaries

--- collapse ---
---
title: Access data from a list
---



--- /collapse ---

--- collapse ---
---
title: Access data from a 2D list
---



--- /collapse ---

--- collapse ---
---
title: Access data from a dictionary
---



--- /collapse ---

--- collapse ---
---
title: Access data from a list of dictionaries
---



--- /collapse ---

--- /task ---



--- save ---
