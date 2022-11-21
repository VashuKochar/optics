from sympy.physics import units as constant
import sympy as sym

from ..utils.Base import Base

class Field(Base):
    def __init__(self, x,y,z, t:sym.Symbol):
        super().__init__(x,y,z, t)
        
        self.w = sym.symbols('w', real=True, positive=True)
        self.E0x,self.E0y,self.E0z = sym.symbols('E0x,E0y,E0z', real=True)
        self.kx,self.ky,self.kz = sym.symbols('kx,ky,kz', real=True)
            
    def k(self):
        return sym.Matrix([self.kx,self.ky,self.kz])
    
    def f(self):
        return self.w/ 2*sym.pi
    
    def wavelength(self):
        return 2 * constant.pi / self.k().norm()
    
    def E0(self):
        return sym.Matrix([self.E0x,self.E0y,self.E0z])
    
    def E(self):
        return sym.simplify(self.E0() * sym.exp(sym.I * (self.w * self.t - (self.k() & self.r()))))
    
    def I(self):
        return sym.sqrt(constant.e0 / constant.mu0) * sym.simplify(self.E().magnitude() * self.E().magnitude().conjugate())