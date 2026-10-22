# pixels.py -- an image is an array (Pod 5). 
# Run from the repository folder:  python module-3/pixels.py
import numpy as np
from matplotlib.pyplot import imread, imsave

I = imread("module-3/clean_io_small.png")     # rows, columns, 3 colour channels; values 0.0 to 1.0
J = I.copy()
J[20:40, 20:40, :] = 1  # red square
J[356, :, :] = 0  # black line at bottom
imsave("module-3/pixels.png", J)  # save modified image

if __name__ == "__main__":
    print("shape:", I.shape)
    print(I.size)
    print(I[0, 0])  # first pixel, top left
    print(I[356, 349])  # last pixel, bottom right  
