from cmath import *
from scipy import constants as constant
from classical_atom import Atom

class Medium(Atom):
    
    def __init__(self, damping: float, spring_constant: float, no_density: int):
        super().__init__(damping, spring_constant)
        self.no_density = no_density
        # self.dielectric_constant = dielectric_constant
        # self.susceptiblity = dielectric_constant + 1
        # self.releative_permeablity = releative_permeablity
        # self.refractive_index = sqrt(self.dielectric_constant*self.releative_permeablity)
        # self.speed_of_light = constant.c / self.refractive_index
        
    def __repr__(self):
        atom = super().__repr__()
        atom += f"\n No Density: {self.no_density} m-3"
        return atom
        
