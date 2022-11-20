from electron_on_spring import *
from scipy import constants as constant
import numpy as np
import matplotlib.pyplot as plt
 
# Parameters
spring = 1 * constant.m_e
damp = 0.2 * constant.m_e
no_density = 10**5

# Hyperparameters
NO_OF_STEPS = 10**2

# Create a medium 
m = Medium(damp, spring, no_density)
print("------------------Medium--------------------")
print(m)
print("--------------------------------------------")


def dispersion(f:float):
    
    # Create the EM field in Vaccuum
    wavelength = constant.c / f
    kz = 2 * constant.pi /wavelength
    waveVec = Vector(0,0,kz)
    em = Field(1, f, waveVec)
    print("----------------Field in Vaccuum------------")
    print(em)
    print("--------------------------------------------")


    # Create the System
    system = EOS(m,em)
    print("----------------Net system------------------")
    print(system)
    print(system.field)
    print("--------------------------------------------")
    
    abs = system.field.absorptionCoefficient().magnitude()
    eta = system.eta()
    
    return (abs, eta)

dispersion_relation = np.vectorize(dispersion)

# Frequency range
f_range = np.linspace(0.1, 2*m.osciallator_frequency.real, NO_OF_STEPS)
absorb,disperse = dispersion_relation(f_range)

plt.plot(f_range, absorb)
plt.plot(f_range, disperse)

plt.show()