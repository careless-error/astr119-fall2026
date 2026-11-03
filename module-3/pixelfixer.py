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

    ### YOUR WORK GOES HERE (with the agent, under the Protocol, in stages:
    ### 1. find the bad pixels and print how many;
    ### 2. paint them white and look at the result;
    ### 3. replace the white with the average of the up/down/left/right
    ###    neighbors. Then try solo_corrupt_io_small.png.)

    # Stage 1: True where the pixel is pure red (R = 1, G = 0, B = 0) find bad pixels and print how many
    bad = (I[:, :, 0] == 1) & (I[:, :, 1] == 0) & (I[:, :, 2] == 0)
    print(f"Found {bad.sum()} corrupted pixels")

    # Stage 2: paint the bad pixels white in the copy
    Iq[bad] = 1

    # Stage 3: replace each bad pixel with the average of its 4 neighbors
    #use np.argwhere to get the indices where "bad" is True. then create a loop to build an array of the 4 neighbors for each bad pixel. then take the mean of the neighbors and assign it to the corresponding pixel in Iq. axis=0 calculates 3 separate averages for the R, G, and B channels.
    for row, col in np.argwhere(bad):
        neighbors = np.array([
            I[row - 1, col],
            I[row + 1, col],
            I[row, col - 1],
            I[row, col + 1]
        ])
        Iq[row, col] = neighbors.mean(axis=0)
        

    return Iq


def _main():
    image_file = sys.argv[1]
    I = imread(image_file)
    I = pixelfix(I)
    imsave('fixed_' + image_file, I)
    print(f"Wrote fixed_{image_file}")


if __name__ == '__main__':
    _main()
