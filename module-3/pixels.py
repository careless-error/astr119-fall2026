# pixels.py -- an image is an array (Pod 5). 
# Run from the repository folder:  python module-3/pixels.py
import numpy as np
from matplotlib.pyplot import imread, imsave, imshow, show, axis

I = imread("module-3/clean_io_small.png")     # rows, columns, 3 colour channels; values 0.0 to 1.0
J = I.copy()
J[20:40, 20:40, :] = 1  # white square
J[356, :, :] = 0  # black line at bottom
imsave("module-3/pixels.png", J)  # save modified image

N = 1-I #invert the image
imsave("module-3/pixels_inverted.png", N)  # save modified image

K = I.copy()
ny, nx = I.shape[:2]  # number of rows, number of columns
y = np.arange(ny)[:, np.newaxis]  # row numbers as a column, shape (ny, 1)
x = np.arange(nx)[np.newaxis, :]  # column numbers as a row, shape (1, nx)
dist = np.sqrt((x - nx/2)**2 + (y - ny/2)**2)  # distance from centre, shape (ny, nx)
r = 250  # radius of the bright circle, in pixels

mask = dist > r  # create a mask for pixels outside the circle dist > r returns a boolean array of shape (ny, nx) with True for pixels outside the circle and False for pixels inside the circle

K[mask, :] *= .9  # darken pixels outside the circle

imsave("module-3/pixels_vignette.png", K)  # save modified image


if __name__ == "__main__":
    print("shape:", I.shape)
    print(I.size)
    print(I[0, 0])  # first pixel, top left
    print(I[356, 349])  # last pixel, bottom right

    # ask user if they want to open an image from the this script
    files = ["module-3/clean_io_small.png", "module-3/pixels.png",
             "module-3/pixels_inverted.png", "module-3/pixels_vignette.png"]  #images this script reads or saves
    while True:
        for i, name in enumerate(files, start=1):
            print(f"{i}. {name.split('/')[-1]}")  # show only the file name, not the folder
        choice = int(input("Which image do you want to print? "))
        imshow(imread(files[choice - 1]))  # choice - 1 because lists start at 0
        axis("off")  # hide the axes and tick numbers
        print("Close the image window to continue.")
        show()  # waits here until the window is closed
        again = input("Show another image? (Y/N) ")
        if again.strip().upper() != "Y":  # anything but Y or y ends the loop
            break
