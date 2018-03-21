# -*- coding: utf-8 -*-
"""
fahrToCelsius is function that converts the input temperature from degrees Fahrenheit
to degrees Celsius.
tempFahrenheit is input value of temperature in degrees Fahrenheit
convertedTemp is returned value of function that is value of temperature in degrees Celsius

Author: Pavel Zhuchkov - 21.03.2018
Modified by - None
"""

# Definition of the function which converts Fahrenheit to Celsius
def fahrToCelsius(tempFahrenheit):
	convertedTemp = (tempFahrenheit - 32) / 1.8
	return convertedTemp