# -*- coding: utf-8 -*-
"""Exercise 2: Glossary

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qxDDA3GASDb70wsCFg6W4xw7QMcol7W3
"""

#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

#Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store
#their meanings as values.

#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print
#the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between

#each word-meaning pair in your output.


coding_glossary = {
    "Python": "Python is a high-level, general-purpose programming language.",
    "Variable": "A Python variable is a symbolic name that is a reference or pointer to an object.",
    "Float": "Float is a method that returns a floating-point number for a provided number or string.",
    "Program": "A program si a set of instructions that a computer uses to perform a specifc action",
    "Dictionary": "A Python dictionary is a data type that stores an unordered collection of data values.",
    }

word = "Python"
print("\n" + word.title() + ": " + coding_glossary[word])

word = "Variable"
print("\n" + word.title() + ": " + coding_glossary[word])

word = "Float"
print("\n" + word.title() + ": " + coding_glossary[word])

word = "Program"
print("\n" + word.title() + ": " + coding_glossary[word])

word = "Dictionary"
print("\n" + word.title() + ": " + coding_glossary[word])