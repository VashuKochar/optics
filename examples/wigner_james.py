import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import constants as constant
import numpy as np
from qutip import about, basis, destroy, mesolve, ptrace, qeye, tensor, wigner

from optics.atom.atom import Atom
from optics.james_cumming.model import Model

from optics.cavity.cavity import Cavity

# Set no of cavity states
no_of_cavity_states = 15
print("No of cavity states: ", no_of_cavity_states)

# Discretise time
T_END = 25
T_STEPS = 101
T_DELTA = T_END/T_STEPS
tlist = np.linspace(0, T_END, T_STEPS)
print("Discretising time from t=0 to t=", T_END, " with dt = ", T_DELTA)
# Timing of interest
tinterest = [0.0, 5.0, 15.0, 25.0]
print("Timing of interest: t=", tinterest)
# find the indices of the density matrices for the times we are interested in
t_idx = np.where([tlist == t for t in tinterest])[1]
print("Timing indices of interest: ", t_idx)

# Discretise space
X_START = -3
X_END = 3
X_STEPS = 200
X_DELTA = (X_END - X_START)/X_STEPS
xlist = np.linspace(0, X_END, X_STEPS)
print("Discretising space from x=",X_START," to x=", X_END, "with dx = ", X_DELTA)

# Create atom
atom = Atom(1.0 * 2 * np.pi, 0.05, 2, 1)

# Create cavity
cavity = Cavity(1.0 * 2 * np.pi, 0.005, no_of_cavity_states,0)

# Cavity-Atom interaction
couple = 0.05 * 2 * np.pi

# External Influences
avg_thermal_excitation = 0.0


# load james_cumming_model
james =  Model(atom, cavity, couple, avg_thermal_excitation)

# Solve hamiltonian
soln = james.solve(tlist)

# print(len(soln))
print(james.state)

# get a list density matrices
rho_list = [soln[i] for i in t_idx]

# xlist = np.linspace(-3, 3, 200)

fig, axes = plt.subplots(1, len(rho_list), sharex=True,
                         figsize=(3 * len(rho_list), 3))

# loop over the list of density matrices
for idx, rho in enumerate(rho_list):

    # trace out the atom from the density matrix, to obtain
    # the reduced density matrix for the cavity
    rho_cavity = rho.ptrace(0)

    # calculate its wigner function
    W = wigner(rho_cavity, xlist, xlist)

    # plot its wigner function
    axes[idx].contourf(
        xlist,
        xlist,
        W,
        100,
        norm=mpl.colors.Normalize(-0.25, 0.25),
        cmap=plt.get_cmap("RdBu"),
    )

    axes[idx].set_title(r"$t = %.1f$" % tlist[t_idx][idx], fontsize=16)    
plt.show()