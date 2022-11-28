from typing import List
import numpy as np
from optics.atom.atom import Atom
from optics.cavity.cavity import Cavity
from optics.jaynes_cumming.model import Model
from qutip import wigner

import matplotlib as mpl
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def vaccumRabiOscillations(no_of_cavity_states: int,cavity_frequency:float,cavity_dissipation:float,cavity_initial_state:int,no_of_atom_states: int,atom_frequency:float,atom_dissipation:float,atom_initial_state:int, coupling:float,avg_thermal_excitation:float,rwa: bool,T_END: float, T_STEPS: float,fig:Figure):
    # Set no of cavity states
    no_of_cavity_states = 15

    # Discretise time
    tlist = np.linspace(0, T_END, T_STEPS)

    # Create atom
    atom = Atom(atom_frequency, atom_dissipation, no_of_atom_states, atom_initial_state)

    # Create cavity
    cavity = Cavity(cavity_frequency, cavity_dissipation, no_of_cavity_states,cavity_initial_state)


    # load jaynes_cumming_model
    jaynes =  Model(atom, cavity, coupling, avg_thermal_excitation)

    # Construct collapse operators (to account for dissipation)
    jaynes.constructCollapseOperators()
    print("collapse operators: ", jaynes.collapseOperators)

    # Construct hamiltonian with rwa approximation
    jaynes.constructHamiltonian(rwa)
    print("Hamiltonian: ", jaynes.hamiltonian)

    # Expectations
    expect = [jaynes.cavity_annhilation.dag() * jaynes.cavity_annhilation, jaynes.atom_spin.dag() * jaynes.atom_spin]

    # Solve hamiltonian
    soln = jaynes.solve(tlist, expectations = expect)

    # Visualise results
    n_c = soln[0]
    n_a = soln[1]

    axes = fig.add_subplot()

    plt.plot(tlist, n_c, label="Cavity")
    plt.plot(tlist, n_a, label="Atom excited state")
    plt.legend(loc=0)
    axes.set_xlabel("Time")
    axes.set_ylabel("Occupation probability")
    axes.set_title("Vacuum Rabi oscillations")

    # plt.show()
    return fig

def wignerFunctions(no_of_cavity_states: int,cavity_frequency:float,cavity_dissipation:float,cavity_initial_state:int,no_of_atom_states: int,atom_frequency:float,atom_dissipation:float,atom_initial_state:int, coupling:float,avg_thermal_excitation:float,rwa: bool,X_START:float, X_END: float, X_STEPS:float,T_END: float, T_STEPS: float,tinterest: List[float],fig:Figure):

    # Discretise time
    T_DELTA= T_END/T_STEPS
    tlist = np.linspace(0, T_END, T_STEPS)
    print("Discretising time from t=0 to t=", T_END, " with dt = ", T_DELTA)
    # Timing of interest
    print("Timing of interest: t=", tinterest)
    # find the indices of the density matrices for the times we are interested in
    t_idx = np.where([tlist == t for t in tinterest])[1]
    print("Timing indices of interest: ", t_idx)
    
    # Discretise space
    X_DELTA = (X_END - X_START)/X_STEPS
    xlist = np.linspace(X_START, X_END, X_STEPS)
    print("Discretising space from x=",X_START," to x=", X_END, "with dx = ", X_DELTA)
    
    # Create atom
    atom = Atom(atom_frequency, atom_dissipation, no_of_atom_states, atom_initial_state)

    # Create cavity
    cavity = Cavity(cavity_frequency, cavity_dissipation, no_of_cavity_states,cavity_initial_state)


    # load jaynes_cumming_model
    jaynes =  Model(atom, cavity, coupling, avg_thermal_excitation)

    # Construct collapse operators (to account for dissipation)
    jaynes.constructCollapseOperators()
    print("collapse operators: ", jaynes.collapseOperators)

    # Construct hamiltonian with rwa approximation
    jaynes.constructHamiltonian(rwa)
    print("Hamiltonian: ", jaynes.hamiltonian)
        
    # Solve hamiltonian
    soln = jaynes.solve(tlist)

    print(len(soln))
    print(jaynes.state[0][0][0])

    # get a list density matrices
    rho_list = [soln[i] for i in t_idx]

    # xlist = np.linspace(-3, 3, 200)
    
    # fig, axes = plt.subplots(1, len(rho_list), sharex=True,
    #                         figsize=(3 * len(rho_list), 3))

    # loop over the list of density matrices
    for idx, rho in enumerate(rho_list):
        axes = fig.add_subplot(2, len(rho_list), idx+1)
        # trace out the atom from the density matrix, to obtain
        # the reduced density matrix for the cavity
        rho_cavity = rho.ptrace(0)
        print(rho_cavity)
        # calculate its wigner function
        W = wigner(rho_cavity, xlist, xlist)

        # plot its wigner function
        axes.contourf(
            xlist,
            xlist,
            W,
            100,
            norm=mpl.colors.Normalize(-0.25, 0.25),
            cmap=plt.get_cmap("RdBu"),
        )

        axes.set_title(r"$t = %.1f$" % tlist[t_idx][idx], fontsize=16)    
        # plt.show()

    # plt.show()
    return fig