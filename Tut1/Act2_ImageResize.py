# Importing the necessary libraries
from PIL import Image
import urllib.request

"""
This problem will demonstrate getting an image from an
online source using link (such as from Wikipedia, for example
"""

def getLinkFromUser():
    link = str(input("Please enter the link of the image: \n"))

    # Raise exception if the link is NOT an image:
    # TODO: DELETE THIS METHOD IF THIS CODE IS NOT WORKING
    if "jpg" or "png" or "jpeg" in link == False:
        raise TypeError("I NEED A IMAGE LINK!")

    # Otherwise, process the link from user:
    """
    This method will download the image and save as "original.png"
    """
    urllib.request.urlretrieve(link,"original.png")

    # Create an image object
    originalImage = Image.open("original.png")

    return originalImage

def testByShowImage(originalImage):
    Image.open("original.png")



