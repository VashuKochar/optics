import sympy as sym
from sympy.physics.vector import *
from scipy import constants as constant
import numpy as np
import matplotlib.pyplot as plt

from optics.EOS.electron_on_spring import EOS
 
# Parameters
# spring = 1 * constant.m_e
# damp = 0.2 * constant.m_e
# no_density = 10**5

# # Hyperparameters
# NO_OF_STEPS = 10**2


t = sym.Symbol('t', real=True, positive=True)

x,y,z = sym.symbols('x,y,z', cls=sym.Function)
x = x(t)
y = y(t)
z = z(t)

eos1 = EOS(x,y,z, t)

# Define Initial system
eos1.kx = 0
eos1.ky = 0
eos1.kz = eos1.w / constant.speed_of_light
eos1.E0x = 0
eos1.E0y = 0
# eos1.E0z = eos1.w / speed_of_light

print("E(r,t) = ",eos1.E())

eos1.solveEOMs()

print("r = ",eos1.r())

P = eos1.P()
print("P = ",sym.latex(P))
dielectric = eos1.dielectric_constant()
print("Dielectric constant = ",sym.latex(dielectric))
absorb = eos1.absorption_coefficient()
print("Absorption coefficient = ",sym.latex(absorb))

# Frequency range
# f_range = np.linspace(0.1, 2*m.osciallator_frequency.real, NO_OF_STEPS)
# absorb,disperse = dispersion_relation(f_range)

# plt.plot(f_range, absorb)
# plt.plot(f_range, disperse)

# plt.show()