import cv2
import matplotlib.pyplot as plt

def read_image(filename):
    """Reads an image and displays it.

    Args:
        filename: Path to the image file.

    Returns:
        The loaded image object, or None if there's an error.
    """
    try:
        image = cv2.imread(filename)
        if image is None:
            print(f"Error reading image: {filename}")
            return None
        cv2.imshow("Original Image", image)
        cv2.waitKey(0)
        return image
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def convert_grayscale(image):
    """Converts an image to grayscale.

    Args:
        image: The input image object.

    Returns:
        The grayscale image object.
    """
    if image is not None:
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        return None

def edge_detection(grayscale_image, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=3):
    """Performs edge detection on an image using the Sobel operator.

    Args:
        grayscale_image: The grayscale image object.
        ddepth: Depth of the output image (default: cv2.CV_64F).
        dx: Derivative along the x-axis (default: 1).
        dy: Derivative along the y-axis (default: 1).
        ksize: Size of the Sobel kernel (default: 3).

    Returns:
        The edge-detected image object.
    """
    if grayscale_image is not None:
        try:
            edge_image = cv2.Sobel(grayscale_image, ddepth, dx, dy, ksize)
            cv2.imshow("Edge-Detected Image", edge_image)
            cv2.waitKey(0)
            return edge_image
        except Exception as e:
            print(f"Error during edge detection: {e}")
            return None
    else:
        return None

def save_image(image, filename="edge_detected.jpg"):
    """Saves the image to a file.

    Args:
        image: The image object to save.
        filename: The desired filename (default: "edge_detected.jpg").

    Returns:
        True if successful, False otherwise.
    """
    if image is not None:
        try:
            success = cv2.imwrite(filename, image)
            if success:
                print(f"Image saved to: {filename}")
                return True
            else:
                print(f"Error saving image: {filename}")
                return False
        except Exception as e:
            print(f"Unexpected error during saving: {e}")
            return False
    else:
        return False

# Main execution
image = read_image("singapore4k.jpg")
grayscale_image = convert_grayscale(image)
edge_image = edge_detection(grayscale_image)
save_image(edge_image)
