from scipy import constants as constant
from cmath import *

from classical_field import *
from classical_medium import *

class EOS:
    def __init__(self, Z: Medium, EM: Field):
        self.medium = Z
        self.field = EM
        self.charge = constant.eV
        
        # Electric field slows in the medium i.e. k -> n k
        self.field.wavevector = self.field.wavevector*self.refractive_index()
        
    def x(self,t:float):
        c1 = self.charge * self.field.E0 / self.medium.mass
        c2 = 1/(self.medium.osciallator_frequency**2 - self.field.w**2 + 1j*self.medium.damping*self.field.w)
        A = c1*c2
        exponent = self.field.w * t
        return A * exp(1j * exponent)
    
    def p(self,t:float):
        return constant.eV*self.x(t)
    
    def P(self, t:float):
        return self.medium.no_density*self.p(t)
    
    def susceptiblity(self):
        c1 = self.medium.no_density* (self.charge**2)/ (constant.epsilon_0*self.medium.mass)
        c2 = 1/(self.medium.osciallator_frequency**2 - self.field.w**2 + 1j*self.medium.damping*self.field.w)
        return c1*c2
    
    def dielectric_constant(self):
        return 1+self.susceptiblity()
    
    def refractive_index(self) -> complex:
        return sqrt(self.dielectric_constant())
    
    def eta(self) -> float:
        return self.refractive_index().real
    
    def xi(self) -> float:
        return -self.refractive_index().imag
    
    def __repr__(self):
        tempStr = []
        tempStr.append(f"Susceptiblity: {self.susceptiblity()}")
        tempStr.append(f"Dielectric constant: {self.dielectric_constant()}")
        tempStr.append(f"Refractive index: {self.refractive_index()}")
        tempStr.append(f"Eta: {self.eta()}")
        tempStr.append(f"Xi: {self.xi()}")
        return '\n'.join(tempStr)