# Importing the necessary libraries:
import cv2
import matplotlib.pyplot as plt

# The function to load image
def loadColorImage():
    testColorImage = cv2.imread("histogram_demo.jpeg",0)
    cv2.imshow("Greyscale converted image",testColorImage)
    return testColorImage

def plotHistogram(testColorImage):
    # Calculate the frequency of each greyscale level
    histogram = cv2.calcHist([testColorImage], [0], None, [256], [0, 256])

    # Plot the actual data into greyscale that we can see:
    plt.plot(histogram)
    plt.show()

# Code to run the program:
plotHistogram(loadColorImage())



