"""
Task: Write a Python script to load an image file and display it using OpenCV or Pillow.
This exercise uses Pillow.
"""

# Importing necessary libraries
from PIL import Image

# A function to load the image
def loadImage():
    # Creating an image object:
    """
    *RARE PROBLEM*: When you load image from file, for whatever reason,
    the Python interpreter won't accept image path with this \ character.

    Solution: add r before the link.

    Thanks, StackOverflow! Source: https://stackoverflow.com/questions/1347791/unicode-error-unicodeescape-codec-cant-decode-bytes-when-writing-windows
    """
    imgToDisplay = Image.open(r"D:\Meme\x9k6z3dd7dec1.jpeg")
    return imgToDisplay
def openImage(imgToDisplay):
    # Display the image
    # Using the {ObjectName}.show() function
    imgToDisplay.show()

openImage(loadImage())


