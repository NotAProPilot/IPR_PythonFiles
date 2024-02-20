"""
This program displays the magnitude spectrum of an image using the Fast Fourier Transform (FFT).

The user can choose to run the FFT analysis or exit the program.
The program displays the original image, the magnitude spectrum, and the reconstructed image.

Requires the following libraries: cv2, matplotlib, numpy, urllib.request, PIL

Thanks StackOverflow for providing the syntax: https://stackoverflow.com/questions/58936938/fourier-transform-in-python-giving-blank-images
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def read_image_and_convert_to_float(image_path):
    """
    Reads an image from the specified path and converts it to a float array.

    Args:
        image_path (str): The path to the image file.

    Returns:
        tuple: A tuple containing the original image and its float array representation.
    """

    img = cv2.imread(image_path)

    # Check if image was read successfully
    if img is None:
        raise ValueError(f"Could not read image at path: {image_path}")

    # Convert to float array with values between 0 and 1
    img_float = img.astype("float32") / 255.0

    return img, img_float

def perform_fft(img_float):
    """
    Performs the Fast Fourier Transform (FFT) on a float array representing an image.

    Args:
        img_float (np.ndarray): The float array representation of the image.

    Returns:
        np.ndarray: The magnitude spectrum of the image.
    """

    fourier_array = np.fft.fft2(img_float)
    spectrum = np.fft.fftshift(fourier_array)
    magnitude_spectrum = np.abs(spectrum)

    return magnitude_spectrum

def reconstruct_image(magnitude_spectrum):
    """
    Reconstructs an image from its magnitude spectrum using the inverse Fast Fourier Transform (iFFT).

    Args:
        magnitude_spectrum (np.ndarray): The magnitude spectrum of the image.

    Returns:
        np.ndarray: The reconstructed image.
    """

    shifted_spectrum = np.fft.ifftshift(magnitude_spectrum)
    original_img = np.fft.ifft2(shifted_spectrum)

    return original_img.real  # Discard imaginary component

def display_images(img, magnitude_spectrum, reconstructed_img):
    """
    Displays the original image, the magnitude spectrum, and the reconstructed image in a subplot layout.

    Args:
        img (np.ndarray): The original image.
        magnitude_spectrum (np.ndarray): The magnitude spectrum of the image.
        reconstructed_img (np.ndarray): The reconstructed image.
    """

    plt.figure(figsize=(10, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Original image")

    plt.subplot(1, 3, 2)
    plt.imshow(magnitude_spectrum, cmap="gray")
    plt.title("Magnitude spectrum")
    plt.colorbar()

    plt.subplot(1, 3, 3)
    plt.imshow(reconstructed_img, cmap="gray")
    plt.title("Reconstructed image")

    plt.tight_layout()
    plt.show()

def main():
    """
    The main function of the program.
    """

    image_path = "processedImg.jpg"  # Replace with your image path

    try:
        img, img_float = read_image_and_convert_to_float(image_path)
        magnitude_spectrum = perform_fft(img_float)
        reconstructed_img = reconstruct_image(magnitude_spectrum)
        display_images(img, magnitude_spectrum, reconstructed_img)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
