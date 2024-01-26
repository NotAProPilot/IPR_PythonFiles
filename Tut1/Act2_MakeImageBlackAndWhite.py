from PIL import Image

def loadImage():
    imageToConvert = Image.open(r"D:\Meme\download.jpg")
    return imageToConvert
def convertToBlackAndWhite(imageToConvert):
    # Using the .convert('L') function to convert image
    blackAndWhiteImage = imageToConvert.convert('L')
    return blackAndWhiteImage

def saveNewGreyImage(blackAndWhiteImage, outputPath):
    blackAndWhiteImage.show()
    blackAndWhiteImage.save(outputPath)

# Load the image
TestImage = loadImage()

# Convert to Black and White:
ConvertedImage = convertToBlackAndWhite(TestImage)

# Save the converted image:
outputPath = r"D:\Meme\download_converted.jpg"
saveNewGreyImage(ConvertedImage, outputPath)


