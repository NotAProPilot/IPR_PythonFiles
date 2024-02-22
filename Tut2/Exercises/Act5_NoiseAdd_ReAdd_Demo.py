# Importing the necessary libraries:
import random

import cv2
import matplotlib.pyplot as plt
import numpy as np
from colorama import Fore


def loadImage():
    testImage = cv2.imread("histogram_demo.jpeg",0)
    cv2.imshow("Greyscale converted image",testImage)
    return testImage

# The function to add Gaussian noise to the image:
def addNoiseToImg(testImage):
    # Get image size:
    size = testImage.shape
    # Create a random Gaussian noise:
    gauss_noise = np.zeros((size), dtype=np.uint8)
    cv2.randn(gauss_noise, 128, 20)
    gauss_noise = (gauss_noise * 0.5).astype(np.uint8)

    # Add actual noise to the image
    imgafternoise = cv2.add(testImage,gauss_noise)

    # Show the image
    cv2.imshow("Image after noise", imgafternoise)
    cv2.waitKey(0)

    """
    Save the image
    """
    # Create file name:
    filepath = "GaussianNoiseImg.jpg"
    cv2.imwrite(filepath,imgafternoise)

    # Return the image:
    return imgafternoise

# The function to remove Gaussian noise to the image:
def removeNoiseFromImg(imgafternoise):
    deGaussianNoiseImg = cv2.fastNlMeansDenoising(imgafternoise)

    cv2.imshow("Image after degaussing", deGaussianNoiseImg)
    cv2.waitKey(0)

    filepath = "DeGaussianNoiseImg.jpg"
    cv2.imwrite(filepath, deGaussianNoiseImg)

    # Return the image:
    return deGaussianNoiseImg

def main():
    """
    Creating a console menu function:
    """

    # Creating a random menuOption, so first it will not exit the program:
    menuOption = random.randint(10,100)

    while(menuOption!=0):
        # Display the menu content:
        displayMenuContent()

        # Re-assign menuOption to input:
        menuOption = int(input(Fore.WHITE + "Enter your choice: "))

        # Switch case based on the menuOption inputted:
        match menuOption:
            case 1:
                addNoiseToImg(loadImage())
            case 2:
                removeNoiseFromImg(addNoiseToImg(loadImage()))

def displayMenuContent():
    print(Fore.BLUE + "1. Add noise to image")
    print(Fore.GREEN + "2. Remove noise from image")
    print(" ")
    print(Fore.RED + "0. Exit")

# The main function and display console menu
if __name__=="__main__":
    main()

