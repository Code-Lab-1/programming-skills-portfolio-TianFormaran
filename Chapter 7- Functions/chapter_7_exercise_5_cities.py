# -*- coding: utf-8 -*-
"""Chapter 7 Exercise 5: Cities

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Re9MyWoee0W_QhOEnro9ToblxFMydgHv
"""

#Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence,

#such as Reykjavik is in Iceland. Give the parameter for the country a default value.

#Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city, country="Philippines"):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('Manila')
describe_city("Washington D.C", "United States")
describe_city("Davao")