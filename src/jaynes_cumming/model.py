from typing import List
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import constants as constant
import numpy as np
from qutip import Qobj, about, basis, destroy, mesolve, ptrace, qeye, tensor, wigner
from qutip.solver import Result
from optics.atom.atom import Atom
from optics.cavity.cavity import Cavity

class Model:
    
    def __init__(self, atom: Atom, cavity: Cavity, coupling: float, avg_thermal_excitation: float) -> None:
        self.atom = atom
        self.cavity = cavity
        self.coupling = coupling
        self.state = tensor(cavity.state, atom.state)
        self.avg_thermal_excitation = avg_thermal_excitation
        # operators
        self.cavity_annhilation = tensor(destroy(self.cavity.no_states), qeye(self.atom.no_states))
        self.atom_spin = tensor(qeye(self.cavity.no_states), destroy(self.atom.no_states))
        self.hamiltonian = None
        self.collapseOperators = []

    def constructCollapseOperators(self) -> List[Qobj]:

        # cavity relaxation
        rate = self.cavity.dissipation_rate * (1 + self.avg_thermal_excitation)
        if rate > 0.0:
            self.collapseOperators.append(np.sqrt(rate) * self.cavity_annhilation)

        # cavity excitation, if temperature > 0
        rate = self.cavity.dissipation_rate * self.avg_thermal_excitation
        if rate > 0.0:
            self.collapseOperators.append(np.sqrt(rate) * self.cavity_annhilation.dag())

        # qubit relaxation
        rate = self.atom.dissipation_rate
        if rate > 0.0:
            self.collapseOperators.append(np.sqrt(rate) * self.atom_spin)
            
        return self.collapseOperators

    def constructHamiltonian(self, rwa: bool = True):
        if rwa == True:
            self.hamiltonian = 1*(self.cavity.frequency * self.cavity_annhilation.dag() * self.cavity_annhilation + self.atom.frequency * self.atom_spin.dag() * self.atom_spin + self.coupling * (self.cavity_annhilation.dag() * self.atom_spin + self.cavity_annhilation * self.atom_spin.dag()))
        else:
            self.hamiltonian = 1*(self.cavity.frequency * self.cavity_annhilation.dag() * self.cavity_annhilation + self.atom.frequency * self.atom_spin.dag() * self.atom_spin + self.coupling * (self.cavity_annhilation.dag() + self.cavity_annhilation) *(self.atom_spin* self.atom_spin.dag()))
            
        return self.hamiltonian

    
    def solve(self, tlist: List[float], expectations: List[Qobj] = []) -> Result:
                
        # Evolve the system
        output = mesolve(self.hamiltonian, self.state, tlist, self.collapseOperators, expectations)
        
        if expectations == []:
            self.state = output.states[-1]
            print("State changed")
            return output.states
        else:    
            return output.expect