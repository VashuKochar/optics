import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import constants as constant
import numpy as np
from qutip import about, basis, destroy, mesolve, ptrace, qeye, tensor, wigner

from optics.atom.atoms import test_atom
from optics.jaynes_cumming.model import Model

from optics.cavity.cavity import Cavity

# Set no of cavity states
no_of_cavity_states = 15

# Discretise time
T_END = 25
T_STEPS = 101
T_DELTA = T_END/T_STEPS
tlist = np.linspace(0, T_END, T_STEPS)

# Create atom
atom = test_atom

# Create cavity
cavity = Cavity(1.0 * 2 * np.pi, 0.005, no_of_cavity_states,0)

# Cavity-Atom interaction
couple = 0.05 * 2 * np.pi

# External Influences
avg_thermal_excitation = 0.0


# load jaynes_cumming_model
jaynes =  Model(atom, cavity, couple, avg_thermal_excitation)

# Construct collapse operators (to account for dissipation)
jaynes.constructCollapseOperators()
print("collapse operators: ", jaynes.collapseOperators)

# Construct hamiltonian with rwa approximation
jaynes.constructHamiltonian(True)
print("Hamiltonian: ", jaynes.hamiltonian)

# Expectations
expect = [jaynes.cavity_annhilation.dag() * jaynes.cavity_annhilation, jaynes.atom_spin.dag() * jaynes.atom_spin]

# Solve hamiltonian
soln = jaynes.solve(tlist, expectations = expect)

# Visualise results
n_c = soln[0]
n_a = soln[1]

fig, axes = plt.subplots(1, 1, figsize=(10, 6))

axes.plot(tlist, n_c, label="Cavity")
axes.plot(tlist, n_a, label="Atom excited state")
axes.legend(loc=0)
axes.set_xlabel("Time")
axes.set_ylabel("Occupation probability")
axes.set_title("Vacuum Rabi oscillations")

plt.show()

