# -*- coding: utf-8 -*-
"""
The script converts input temperature data list in degrees Fahrenheit to degrees Celsius
and further classifies him to the different temperature classes (0 - cold,
1 - slippery, 2 - comfortable, 3 - warm) and then counts number of zeros, ones,
twos, and threes in the tempClasses list.
tempClasses is temperature data list that is imported from data.py file.
The script uses functions that is imported from functions.py.

Author: Pavel Zhuchkov - 21.03.2018
"""

# Import data and functions
import functions as func
import data

# Create an empty list for storing of temperature classes
tempClasses = []

# Convert input temperature data list in degrees Fahrenheit to degrees Celsius
# and classify him to the different temperature classes
for tempFahr in data.tempData:
    tempCelsius = func.fahrToCelsius(tempFahr)
    tempClass = func.tempClassifier(tempCelsius)
    tempClasses.append(tempClass)

# Count the number of zeros, ones, twos, and threes in the tempClasses list
count0 = tempClasses.count(0)
count1 = tempClasses.count(1)
count2 = tempClasses.count(2)
count3 = tempClasses.count(3)

# Print the number of zeros, ones, twos, and threes in the tempClasses list
print('Сlass 0 occurs',count0,'times\nClass 1 occurs',count1,'times\nClass 2 occurs',count2,'times\nClass 3 occurs',count3,'times')
    
    








