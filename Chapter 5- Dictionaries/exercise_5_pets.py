# -*- coding: utf-8 -*-
"""Exercise 5: Pets

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qxDDA3GASDb70wsCFg6W4xw7QMcol7W3
"""

#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about

#each pet

pets = []

pet = {
    "animal type": "Feline",
    "name": "Miko",
    "owner": "Rafael",
    "weight": 3,
    "eats": "anything",
}
pets.append(pet)

pet = {
    "animal type": "Tyrannosaurus rex",
    "name": "Barney",
    "owner": "HiT Entertainment",
    "weight": 62,
    "eats": "peanut butter and jelly sandwich with a glass of milk",
}
pets.append(pet)

pet = {
    "animal type": "Canine",
    "name": "Scooby Doo",
    "owner": "Shaggy",
    "weight": 31,
    "eats": "scooby snacks",
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))