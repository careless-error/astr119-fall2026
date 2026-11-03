**Assignment: HW3 fix my pix, plzz**

**Prediction, written before I asked for anything**:
For a 100 by 200 image, I.shape is (100, 200, 3) i.e 100 rows 200 cols and 3 vlaues per pixel.
I[:, :, 0] gives the red values for each pixel. 
I[10,20] gives the RGB values for the pixel in row 10, col 20.
Based on easy_corrupt_io_small.png I think there are 5000-6000 bad pixels

**What I asked the agent for** (one line per request):
 -write code that finds pixels with red = 1 and greeen/blue = 0 then prints the number of corrupted pixels without changing the image
        python pixelfixer.py easy_corrupt_io_small.png
        Found 4840 corrupted pixels
-now lets paint all identified pixels white
        all red pixels in fixed_easy_corrupt_io_small.png are now white
-now replace the each white pixels with the average value of its verical and horizonal neighbors
    claude prompted me to write this by hand
-when I tested on the full image: python pixelfixer.py full_corrupt_io_small.png open fixed_full_corrupt_io_small.png
    returned an error: "index 698 is out of bounds for axis 1 with size 698" becasue there are no checks to make sure the neighboring pixels are inside the image
-asked claude to make sure my checks were correct
    the empt array causes a Value Error so i need to use .append
-now we need to add checks to make sure we are not including bad pixels in our average
    claude gave a very lengthy explanation that was a little hard to follow

**What I changed by hand:**
-I used np.argwhere to get the indices where "bad" is True. Then created a loop to build an array of the 4 neighbors for each bad pixel. Then take the mean of the neighbors and assign it to the corresponding pixel in Iq.
        this worked for easy_corrupt_io_small.png
-I added checks to the for loop that builds sthe array of neighboring pixels
-I rewrote the for loop and np array to use .append to skip pixels outside the image. tested and it worked!
*extra credit*
I added a check to exclude corrupted neighboring pixels from the average and a loop that keeps running until all bad pixels are fixed. if a pixel has no healthy neighbors it is skipped and try again after other pixels have been fixed.

**One "why" I asked, and the answer in my own words:**
-I asked why we are using np.argwhere. 
    np.argwhere finds and indexes where a specific boolean is True. So we can use this to create an array of the neighbors of these bad pixels.

**What the agent got wrong, and how I found out** (if nothing, say what check you ran that would have caught it): The agent didn't get anything wrong. It initially had me create the np.array with the loop inside it but then recommended I change it when I needed to add the .append

**What I still do not understand:**
I'm still not sure the loop will work i every situation or how many corrupted pixels in a specific spot will cause it to fail. but it wors for these images.