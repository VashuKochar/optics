from typing import Dict, List
import numpy as np
from optics.atom.atom import Atom
from optics.cavity.cavity import Cavity
from optics.jaynes_cumming.model import Model
from qutip import wigner

def createJaynesModel(model_config: Dict[str, str]):
    no_of_cavity_states = int(model_config["no_of_cavity_states"])
    cavity_frequency = float(model_config["cavity_frequency"])
    cavity_dissipation = float(model_config["cavity_dissipation"])
    cavity_initial_state = int(model_config["cavity_initial"])
    no_of_atom_states = int(model_config["no_of_atom_states"])
    atom_frequency = float(model_config["atomic_frequency"])
    atom_dissipation = float(model_config["atomic_dissipation"])
    atom_initial_state = int(model_config["atomic_initial"])
    coupling = float(model_config["coupling"])
    avg_thermal_excitation = float(model_config["thermal"])
    rwa = bool(model_config["rwa"])
    
    # Create atom
    atom = Atom(atom_frequency, atom_dissipation, no_of_atom_states, atom_initial_state)

    # Create cavity
    cavity = Cavity(cavity_frequency, cavity_dissipation, no_of_cavity_states,cavity_initial_state)


    # load jaynes_cumming_model
    jaynes =  Model(atom, cavity, coupling, avg_thermal_excitation)
    
    # Construct collapse operators (to account for dissipation)
    jaynes.constructCollapseOperators()

    # Construct hamiltonian with rwa approximation
    jaynes.constructHamiltonian(rwa)
    
    return jaynes

def vaccumRabiOscillations(model: Model,T_END: float, T_STEPS: float):

    # Discretise time
    tlist = np.linspace(0, T_END, T_STEPS)

    # Expectations
    expect = [model.cavity_annhilation.dag() * model.cavity_annhilation, model.atom_spin.dag() * model.atom_spin]

    # Solve hamiltonian
    soln = model.solve(tlist, expectations = expect)

    # Visualise results
    n_c = soln[0]
    n_a = soln[1]
    
    # plt.plot(tlist, n_c, label="Cavity")
    # plt.plot(tlist, n_a, label="Atom excited state")
    # plt.legend(loc=0)
    # axes.set_xlabel("Time")
    # axes.set_ylabel("Occupation probability")
    # axes.set_title("Vacuum Rabi oscillations")

    # plt.show()
    return (tlist, n_c, n_a)

def wignerFunctions(model:Model,X_START:float, X_END: float, X_STEPS:float,T_END: float, T_STEPS: float,tinterest: List[float]):

    # Discretise time
    T_DELTA= T_END/T_STEPS
    tlist = np.linspace(0.0, T_END, T_STEPS)
    print("Discretising time from t=0 to t=", T_END, " with dt = ", T_DELTA)
    # Timing of interest
    print("Timing of interest: t=", tinterest)
    # find the indices of the density matrices for the times we are interested in
    t_idx = []
    for t in tinterest:
        t_idx.append(np.argmin(tlist-t))
    print("Timing indices of interest: ", t_idx)
    
    # Discretise space
    X_DELTA = (X_END - X_START)/X_STEPS
    xlist = np.linspace(X_START, X_END, X_STEPS)
    print("Discretising space from x=",X_START," to x=", X_END, "with dx = ", X_DELTA)
        
    # Solve hamiltonian
    soln = model.solve(tlist)

    print(len(soln))
    print(model.state[0][0][0])

    # get a list density matrices
    rho_list = [soln[i] for i in t_idx]

    # xlist = np.linspace(-3, 3, 200)
    
    # fig, axes = plt.subplots(1, len(rho_list), sharex=True,
    #                         figsize=(3 * len(rho_list), 3))

    # loop over the list of density matrices
    wigners =[]
    for rho in rho_list:
        # trace out the atom from the density matrix, to obtain
        # the reduced density matrix for the cavity
        rho_cavity = rho.ptrace(0)
        # calculate its wigner function
        W = wigner(rho_cavity, xlist, xlist)
        wigners.append(W.tolist())
        
    return (tinterest, xlist, wigners)