# cometlife.py
# estimates the mass and radius a comet loses per orbit due to sublimation of ice
# Run with: python cometlife.py

import numpy as np

#CONSTANTS
L = float(3.8e26) #luminosity of sun in watts J/s
GM = float(1.3271e20) #gravity * mass of sun
R = float(input("Enter the comet's radius in meters: ")) #radius of comet in m
h = float(2.5e6) #latent heat sublimation J/Kg
p = float(500) #density of comet in kg/m^3
A = float(0) #albedo of comet
a = float(4.6488e11) #semimajor axis in m
e = float(0.5) #eccentricity of comet

pi = float(np.pi) #pi

V = (4/3) * pi * R**3 #volume of comet
M = p * V #mass of comet (not used in calculations)

H_sol = (pi/2) * (1-A) * R**2 * L / (np.sqrt(GM * a * (1-e**2))) # Joules

dM = H_sol / h # delta M mass loss rate of comet kg

dR = dM / (4 * pi * R**2 * p) # delta R radius loss rate of comet

percent_loss = (dR / R * 100) # percent loss of radius per second

print(f"The comet loses {dM:.3g} kg per orbit")
print (f"The comet's radius loses {dR:.3g} meters per orbit")
print (f"The radius lost per orbit is {percent_loss:.3g}%")