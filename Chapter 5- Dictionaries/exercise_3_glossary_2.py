# -*- coding: utf-8 -*-
"""Exercise 3: Glossary 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qxDDA3GASDb70wsCFg6W4xw7QMcol7W3
"""

#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms

#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

#will add to glossary: key, loop, comment, boolean, value

coding_glossary = {
    "Python": "Python is a high-level, general-purpose programming language.",
    "Variable": "A Python variable is a symbolic name that is a reference or pointer to an object.",
    "Float": "Float is a method that returns a floating-point number for a provided number or string.",
    "Program": "A program si a set of instructions that a computer uses to perform a specifc action",
    "Dictionary": "A Python dictionary is a data type that stores an unordered collection of data values.",
    "Key": "keys in Python are used to retrieve all of the keys from the dictionary",
    "Loop": "Looping means repeating something over and over until a particular condition is satisfied.",
    "Comment": "Comments in Python are identified with a hash symbol, #, and extend to the end of the line.",
    "Boolean": "Represents one of the two values i.e. True or False",
    "Value": "values is an inbuilt method in Python programming language that returns a view object.",
    }

for word, definition in coding_glossary.items():
    print("\n" + word.title() + ": " + definition)