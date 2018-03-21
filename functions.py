# -*- coding: utf-8 -*-
"""
fahrToCelsius is the function that converts the input temperature from degrees Fahrenheit
to degrees Celsius.
tempFahrenheit is input value of temperature in degrees Fahrenheit.
convertedTemp is returned value of the function that is value of temperature in degrees Celsius.

tempClassifier is the function that classifies temperature into 4 different classes (0,1,2,3).
tempCelsius is input value of temperature in degrees Celsius.
The fuction returns value of class (0 - cold, 1 - slippery, 2 - comfortable, 3 - warm)

Author: Pavel Zhuchkov - 21.03.2018
Modified by - None
"""

# Definition of the function that converts Fahrenheit to Celsius
def fahrToCelsius(tempFahrenheit):
	convertedTemp = (tempFahrenheit - 32) / 1.8
	return convertedTemp
 
 # Definition of the function that classifies temperature into 4 different classes
def tempClassifier(tempCelsius):
    if tempCelsius < -2:
        return 0
    elif tempCelsius >= -2 and tempCelsius <= 2:
        return 1
    elif tempCelsius > 2 and tempCelsius <= 15:
        return 2
    else:
        return 3