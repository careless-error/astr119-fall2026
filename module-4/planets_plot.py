# planets_plot.py -- the ten planets as arrays, ready to plot (Pod 6). 
# Run from the repository folder:  python module-4/planets_plot.py

# IMPORTS
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("dark_background")    # dark plot background with white text and axes

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
    # COMPUTE
    T = t_eq(lum * L_SUN, dist * AU)            # planet equilibrium temperatures
    d = np.linspace(0.01, 2.0, 200)              # distances for the reference curves, AU
    T_curve = t_eq(L_SUN, d * AU)                # Sun-like star
    T_curve_half = t_eq(0.5 * L_SUN, d * AU)     # star with half the Sun's luminosity
    
    # planets with L = 1 L_sun (Earth, Mars) lie on the Sun curve; brighter stars put planets above it, dimmer ones below.
    # T scales as L^(1/4), so the distance from a curve depends only on the star's luminosity, not on distance.

    # SET UP FIGURE
    plt.style.use("dark_background")
    fig, ax = plt.subplots()

    # PLOT
    for n, x, y in zip(name, dist, T):           # each planet separately so it gets its own color and legend entry
        ax.scatter(x, y, label=n)
    ax.plot(d, T_curve, color='gold', linestyle='--', label='Sun-like star Luminosity')
    ax.plot(d, T_curve_half, color='darkorange', linestyle='--', label='Half Sun luminosity')

    # LABELS AND SCALES
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Distance (AU)")
    ax.set_ylabel("Equilibrium Temperature (K)")
    ax.set_title("Ten planets: Equilibrium Temperature vs Distance")
    ax.legend(fontsize=7)

    # SAVE
    fig.savefig("module-4/planets.png", dpi=150)
    print("wrote module-4/planets.png")
