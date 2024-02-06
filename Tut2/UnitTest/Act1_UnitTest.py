import unittest.mock
import numpy as np

# Import the functions to be tested
from Tut2.Exercises.Act1_ConvertImageToBinary import loadGrayScale, globalThreshold

# Create a sample mock image
mock_grayscale_image = np.zeros((100, 100), dtype=np.uint8)

def test_loadGrayScale():
    with unittest.mock.patch('cv2.imread') as mock_imread:
        mock_imread.return_value = mock_grayscale_image

        grayscale_img = loadGrayScale()

        assert grayscale_img is mock_grayscale_image
        assert len(grayscale_img.shape) == 2  # Check for a single channel

def test_globalThreshold():
    thresholdValue = 128
    binary_img = globalThreshold(mock_grayscale_image, thresholdValue)

    assert np.all(binary_img[mock_grayscale_image >= thresholdValue] == 255)
    assert np.all(binary_img[mock_grayscale_image < thresholdValue] == 0)