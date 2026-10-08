# comet.py

# IMPORTS
import numpy as np

# FUNCTIONS
def dr_per_orbit(R, albedo, rho, a_au, e):
    """
    Calculates the radius loss of a comet per orbit due to sublimation of ice.

    Args:
        R (float): Radius of the comet in meters.
        albedo (float): Albedo of the comet.
        rho (float): Density of the comet in kg/m^3.
        a_au (float): Semimajor axis of the comet's orbit in astronomical units.
        e (float): Eccentricity of the comet's orbit.

    Returns:
        float: Radius loss of the comet per orbit in meters.
    """
    #constants
    L = 3.8e26  # Luminosity of the Sun in watts (J/s)
    GM = 1.3271e20  # Gravitational constant * mass of the Sun
    h_ice = 2.5e6  # Latent heat of sublimation in J/kg
    pi = np.pi

    #convert semimajor axis from AU to meters
    a_m = a_au * 1.496e11

    #calculate energy received by the comet per orbit
    H_sol = (pi / 2) * (1 - albedo) * R**2 * L / (np.sqrt(GM * a_m * (1 - e**2)))

    #calculate mass loss rate
    dM = H_sol / h_ice

    #calculate radius loss rate
    dR = dM / (4 * pi * R**2 * rho)

    return dR

# INPUTS
radius = float(input("Enter the comet's radius in meters: "))
albedo = float(input("Enter the comet's albedo (0-1): "))
density = float(input("Enter the comet's density in kg/m^3: "))
semimajor = float(input("Enter the comet's semimajor axis in AU: "))
eccentricity = float(input("Enter the comet's eccentricity (0-1): "))

print(dr_per_orbit(radius, albedo, density, semimajor, eccentricity)) #prints based on user inputs