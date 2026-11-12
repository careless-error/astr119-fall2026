# Project draft (one page, due Thu Nov 12)

**Title:**
Can stellar mass explain a MaNGA galaxy's rotation curve?

**Menu option**
MaNGA rotation curves and dark matter

**Working with**
alone

**The base version**
The template project measures how fast gas rotates at different distances from a galaxy's center. It uses a MaNGA data cube (stack of images of a galaxy at different wavelengths) and the galaxy's H-alpha velocity map (image using color to show how fast gas in different parts of the galaxy is moving relative to us). The finished notebook produces a figure showing the measured rotation speeds with an overlaid best-fit curve.

**The extension** 
I will compare two models of the galaxy's rotation curve. One will include the stellar disk (flattened part of the galaxy where most stars are) from the MaNGA catalog and the other will add a dark matter halo (cloud of unseen mass surrounding the galaxy) modeled as a pseudo-isothermal profile with free parameters central density and core radius. I will use curve_fit to adjust each model to match the data. Then I will plot the curves from both models to see if adding the halo improves the match to the measured gas rotation speeds. I will report how much the dark matter adds to the rotation speed far from the center, and how uncertain that number is.

**What could go wrong** 
I could use poor starting guesses for curve_fit and end up with a curve that doesn’t follow the measured gas speeds. I’ll check this early by trying several starting guesses and seeing whether they produce similar curves that match the measurements.
I could also pick a galaxy that is seen too face-on or edge-on, which makes the speeds hard to measure. I'll check this in the first week by looking at its velocity map and picking a different galaxy if it doesn't show clear motion toward us on one side and away on the other.

**How you will know it works**
Velocity map: check that gas is moving toward us on one side of the galaxy and away from us on the other

Base rotation curve: check that the best-fit curve follows the measured gas speeds at different distances from the center. The speeds should level off far from the center.

Disk + halo model: I will plot both model curves alongside the measured gas speeds and compare the chi-squared of each fit (how far the curve is from the measured points overall) to see which one matches better.

**Plan by week** 
Week of Nov 16: Run the starter notebooks with the example galaxy, choose a galaxy for this project, load the H-alpha velocity map, and finish the base rotation curve.

Week of Nov 23: Fit both models to the measured gas speeds, and plot the two model curves.

Week of Nov 30: Calculate the uncertainties in the halo estimates and review/fine tune the code.