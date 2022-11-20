import sympy as sym
from sympy.vector import Vector, CoordSys3D

from classical_field import Field
from medium import Medium
from utils import *
import constants as constant

class EOS(Field, Medium):
    def __init__(self, x,y,z, t:sym.Symbol):
        
        Field.__init__(self,x,y,z, t)
        Medium.__init__(self,x,y,z,t)
                
        self.magnetic_permeablity,self.w0,self.gamma = sym.symbols('u, w0, gamma', real=True, positive=True)
        # Approx u = 1
    
    # Approximation E(x,t) = E(t)
    def E(self):
        return self.E0() * sym.exp(sym.I * self.w * self.t )
    
    def solveEOMs(self):
        F = self.charge * self.E() / self.mass
        eq_motion = sym.simplify(sym.diff(self.r(),self.t,self.t) + self.gamma * sym.diff(self.r(),self.t) + self.w0**2 * self.r() - F)
        eqns = [eq_motion & N.i,eq_motion & N.j,eq_motion & N.k]
        
        print("EOM1: ", sym.simplify(eqns[0])," = 0")
        print("EOM2: ", sym.simplify(eqns[1])," = 0")
        print("EOM3: ", sym.simplify(eqns[2])," = 0")
        
        C1 = 0
        C2 = 0
        self.x = sym.dsolve(eqns[0], self.x).subs({sym.Symbol('C1'): C1, sym.Symbol('C2'): C2}).rhs
        self.y = sym.dsolve(eqns[1], self.y).subs({sym.Symbol('C1'): C1, sym.Symbol('C2'): C2}).rhs
        self.z = sym.dsolve(eqns[2], self.z).subs({sym.Symbol('C1'): C1, sym.Symbol('C2'): C2}).rhs
    
    def changeEMWave(self):
        # Electric field slows in the medium i.e. k -> n k
        # self.field.wavevector = self.field.wavevector*self.refractive_index()
        self.kx *= self.refractive_index()
        self.ky *= self.refractive_index()
        self.kz *= self.refractive_index()
    
    def p(self):
        return sym.simplify(self.charge*self.r())
    
    def P(self):
        return sym.simplify(self.no_density*self.p())
    
    def susceptiblity(self):
        p = sym.simplify(self.P().magnitude()**2)
        e = sym.simplify(self.E().magnitude()**2)
        # print("Magnitude of P: ", sym.latex(p))
        # print("Magnitude of E: ", sym.latex(e))
        return sym.simplify( sym.sqrt(p/ e ) / constant.e_0)
    
    def dielectric_constant(self):
        dielectric = sym.simplify(1+self.susceptiblity())
        print("Dielectric: ", sym.latex(dielectric))
        return dielectric
    
    def refractive_index(self, gaseous:bool = True):
        if gaseous:
            refract = sym.simplify(sym.Rational(1,2) + self.dielectric_constant()/2)
        else:
            refract = sym.simplify(sym.sqrt(self.dielectric_constant()* self.magnetic_permeablity))
        print("Refractive index: ", sym.latex(refract))
        return refract
    
    def eta(self):
        return sym.simplify(sym.re(self.refractive_index()))
    
    def chi(self):
        return sym.simplify(sym.im(-self.refractive_index()))
    
    def absorption_coefficient(self):
        print("|k| = ", sym.latex(sym.simplify(self.k().magnitude())))
        return sym.simplify(-2 * sym.im(self.k().magnitude()))
    
    # def susceptiblity(self):
    #     c1 = self.medium.no_density* (self.charge**2)/ (constant.epsilon_0*self.medium.mass)
    #     c2 = 1/(self.medium.osciallator_frequency**2 - self.field.w**2 + 1j*self.medium.damping*self.field.w)
    #     return c1*c2
    
    # def dielectric_constant(self):
    #     return 1+self.susceptiblity()
    
    # def refractive_index(self) -> complex:
    #     return sqrt(self.dielectric_constant())
    
    # def eta(self) -> float:
    #     return self.refractive_index().real
    
    # def xi(self) -> float:
    #     return -self.refractive_index().imag
    
    # def __repr__(self):
    #     tempStr = []
    #     tempStr.append(f"Susceptiblity: {self.susceptiblity()}")
    #     tempStr.append(f"Dielectric constant: {self.dielectric_constant()}")
    #     tempStr.append(f"Refractive index: {self.refractive_index()}")
    #     tempStr.append(f"Eta: {self.eta()}")
    #     tempStr.append(f"Xi: {self.xi()}")
    #     return '\n'.join(tempStr)