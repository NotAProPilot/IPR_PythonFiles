"""
BACKGROUND KNOWLEDGE:
"""
import random

# Importing the necessary libs:
import cv2
import numpy as np
from colorama import Fore, Back, Style
from sympy import *


"""
The function to create a structuring element
Note that for practical reasons, a structuring element MUST be odd.
"""
def structuringElementGenerator():
    # Ask user about the size of the SE matrix:
    matrixSize = int(input("Enter the desired size of matrix: "))

    # Raise exception if matrixSize is even
    if simplify(matrixSize).is_even == True:
        raise Exception ("Even number matrix size will not make this program works.")

    # Taking a matrix of size matrixSize as the kernel
    kernel = np.ones((matrixSize, matrixSize), np.uint8)

    # Return the SE:
    return kernel

def erodeImage(kernel):
    # Read a binary photo:
    binarySourceImg = cv2.imread("AverageBinary.png",0)

    """
        Performs erosion and dilation on an image.

        Args:
            img (numpy.ndarray): The input grayscale image.
            kernel (numpy.ndarray): The kernel matrix used for morphological operations.
            iterations (int, optional): The number of iterations for erosion and dilation. Defaults to 1.

        Returns:
            tuple: A tuple containing two NumPy arrays, the eroded and dilated versions of the input image.

        Raises:
            TypeError: If any of the input arguments are not of the expected types.

        Notes:
            - This function performs both erosion and dilation on the same image.
            - Increasing the number of iterations increases the intensity of the morphological operation.
            - The kernel matrix defines the shape and size of the structuring element used for erosion and dilation.
    """
    # Ask user for the numbers of iterations:
    numOfIteration = int(input("How many iterations do you want? "))

    # The main code to erode the image:
    erodedImage = cv2.erode(binarySourceImg,kernel,iterations=numOfIteration)

    # Show the image:
    cv2.imshow("Eroded image with " + str(numOfIteration) + " iterations", erodedImage)

    # This code is REQUIRED to show the image:
    cv2.waitKey()

def dilateImage(kernel):
    # Read a binary photo:
    binarySourceImg = cv2.imread("AverageBinary.png", 0)

    # Ask user for the numbers of iterations:
    numOfIteration = int(input("How many iterations do you want? "))

    # The main code to erode the image:
    dilatedImage = cv2.dilate(binarySourceImg, kernel, iterations=numOfIteration)

    # Show the image:
    cv2.imshow("Dilated image with " + str(numOfIteration) + " iterations", dilatedImage)

    # This code is REQUIRED to show the image:
    cv2.waitKey()

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
                erodeImage(structuringElementGenerator())
            case 2:
                dilateImage(structuringElementGenerator())

def displayMenuContent():
    print(Fore.BLUE + "1. Erode a sample image")
    print(Fore.GREEN + "2. Dilute a sample image")
    print(" ")
    print(Fore.RED + "0. Exit")

# The main function and display console menu
if __name__=="__main__":
    main()







