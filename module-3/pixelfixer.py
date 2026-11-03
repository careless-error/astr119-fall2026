#------------------------------------------------------------------------------
# pixelfixer.py: a command-line utility that fixes red-corrupted pixels in an
# RGB image.
#
# Run with:
#   python pixelfixer.py easy_corrupt_io_small.png
# which writes fixed_easy_corrupt_io_small.png next to the input.
#------------------------------------------------------------------------------
import sys
import numpy as np
from matplotlib.pyplot import imread, imsave


def pixelfix(I):
    """Replace bad pixels with the color averaged from their neighbors.

    Parameters
    ----------
    I : ndarray, shape (M, N, 3)
        A color image array in RGB format, values between 0 and 1.
        A bad pixel has red = 1, green = 0, blue = 0.

    Returns
    -------
    Iq : ndarray, same shape as I
        A copy of the image with the bad pixels fixed.
    """
    Iq = I.copy()

    # Stage 1: True where the pixel is pure red (R = 1, G = 0, B = 0) find bad pixels and print how many
    bad = (I[:, :, 0] == 1) & (I[:, :, 1] == 0) & (I[:, :, 2] == 0)
    print(f"Found {bad.sum()} corrupted pixels")

    # Stage 2: paint the bad pixels white in the copy
    Iq[bad] = 1

    # Stage 3: replace each bad pixel with the average of its 4 neighbors
   #find each bas pixel with np.argwhere and loop through them, for each bad pixel, find its neighbors and average their colors, then replace the bad pixel with the average color. exclude pixels outside the image.

    M, N, _ = I.shape # get the shape of the image
    remaining = bad.copy() # make a copy of the bad pixels to keep track of which ones are left to fix
    while remaining.any(): # while there are still bad pixels left to fix
        fixed = 0 # keep track of how many pixels we fix in this iteration
        for row, col in np.argwhere(remaining):
            neighbors = []
            if row > 0:
                neighbors.append(I[row - 1, col]) #check if pixel is on top edge
            if row < M - 1:
                neighbors.append(I[row + 1, col]) #check if pixel is on bottom edge
            if col > 0:
                neighbors.append(I[row, col - 1]) #check if pixel is on left edge
            if col < N - 1:
                neighbors.append(I[row, col + 1]) #check if pixel is on right edge

            if len(neighbors) == 0:
                continue #skip if no neighbors
            neighbors = np.array(neighbors) #convert the list of neighbors to a numpy array
            Iq[row, col] = neighbors.mean(axis=0)

            remaining[row, col] = False #mark the pixel as fixed
            fixed += 1 #increment the number of pixels fixed in this iteration
            
        if fixed == 0: #if no pixels were fixed in this iteration, break the loop
            break

    # Check: count pure-red pixels left in the fixed image (should be 0)
    still_bad = (Iq[:, :, 0] == 1) & (Iq[:, :, 1] == 0) & (Iq[:, :, 2] == 0)
    print(f"Bad pixels remaining: {still_bad.sum()}")

    return Iq


def _main():
    image_file = sys.argv[1]
    I = imread(image_file)
    I = pixelfix(I)
    imsave('fixed_' + image_file, I)
    print(f"Wrote fixed_{image_file}")


if __name__ == '__main__':
    _main()
