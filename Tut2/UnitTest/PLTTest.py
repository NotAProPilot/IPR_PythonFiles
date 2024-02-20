import matplotlib.pyplot as p
import numpy as np

img = p.imread(r"D:\FIT\Junior Year\Official classes\SPRING 2024\Image Processing (IPR)\IPR_PythonFile\Tut2\Exercises\DeGaussianNoiseImg.jpg").astype(float)
spectrum = np.fft.fftshift(np.fft.fft2(img))

img_back=np.fft.ifft2(np.fft.ifftshift(spectrum))


p.figure(figsize=(20,6))
p.subplot(131)
p.imshow(img, cmap='gray')
p.title('input image')
p.colorbar()
p.show()

p.subplot(132)
p.imshow( np.log(np.abs(spectrum)) , cmap='gray')
p.title('Magnitude Spectrum')
p.colorbar()
p.show()

p.subplot(133)
p.imshow( np.abs(img_back),cmap='gray')
p.title('reconstructed')
p.colorbar()
p.show()