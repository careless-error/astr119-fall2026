# planets_plot.py -- the ten planets as arrays, ready to plot (Pod 6). 
# Run from the repository folder:  python module-4/planets_plot.py

# IMPORTS
import numpy as np
import matplotlib.pyplot as plt

# PHYSICAL CONSTANTS (SI UNITS)
SIGMA = 5.67e-8          # Stefan-Boltzmann constant, W m^-2 K^-4
L_SUN = 3.8e26           # solar luminosity, W
AU = 1.496e11            # meters per AU

# PLANET DATA
name = np.array(["Earth", "Mars", "HD 209458 b", "51 Peg b", "TRAPPIST-1 e",
                 "Kepler-22 b", "55 Cnc e", "HD 189733 b", "Kepler-452 b", "Proxima b"])
lum = np.array([1.0, 1.0, 1.6, 1.3, 0.00055, 0.79, 0.58, 0.34, 1.2, 0.0016])        # star luminosity, solar units
dist = np.array([1.000, 1.524, 0.047, 0.052, 0.029, 0.85, 0.0154, 0.031, 1.046, 0.0485])   # distance, AU



# FUNCTIONS
def t_eq(L, d):
    """Equilibrium temperature (K) at distance d (m) from a star of luminosity L (W)."""
    return (L / (16 * np.pi * SIGMA * d**2)) ** 0.25


# MAIN: COMPUTE TEMPERATURES AND PLOT
if __name__ == "__main__":
    T = t_eq(lum * L_SUN, dist * AU)
    fig, ax = plt.subplots()

    #step 1 x axis is distance in AU, y axis is equilibrium temperature in K
    ax.set_xlabel("Distance (AU)") 
    ax.set_ylabel("Equilibrium Temperature (K)")
    plt.title("Ten planets: Equilibrium Temperature vs Distance") #Title
    ax.scatter(dist, T)
    # SUN-LIKE STAR EQUILIBRIUM TEMPERATURE CURVE
    d = np.linspace(0.01, 2.0, 200)
    T_curve = t_eq(L_SUN, d * AU)
    #the planets should not be on this temperature curve, but they should be below it. the planets with the smallest distances will be closest to the curve depending on how bright the plantet's star is.
    ax.plot(d, T_curve, color='red', linestyle='--', label='Sun-like star') # Plot the sun-like star equilibrium temperature curve
    fig.savefig("module-4/planets.png", dpi=150)
    print("wrote module-4/planets.png")
