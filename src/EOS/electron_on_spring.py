from cmath import isnan
import sympy as sym
from sympy.physics import units as constant
import numpy as np

from .classical_field import Field
from .medium import Medium

class EOS(Field, Medium):
    def __init__(self, x,y,z, t:sym.Symbol):
        
        Field.__init__(self,x,y,z, t)
        Medium.__init__(self,x,y,z,t)
                
        self.magnetic_permeablity,self.w0,self.gamma = sym.symbols('u, w0, gamma', real=True, positive=True)
        # Approx u = 1
    
    # Approximation E(x,t) = E(t) by overloading
    def E(self):
        return self.E0() * sym.exp(sym.I * self.w * self.t )
    
    def solveEOMs(self):
        F = self.charge * self.E() / self.mass
        
        # numpy array to list
        F = sym.Matrix(F)
        r = sym.Matrix(self.r())
        print("r= ",r, type(r))
        r_t = sym.diff(r,self.t)
        print("r'= ",r_t, type(r_t))
        r_tt = sym.diff(r_t,self.t)
        print("r''= ",r_tt, type(r_tt))
        
        eq_motion = sym.simplify(r_tt + self.gamma * r_t + self.w0**2 * r - F)
        
        print("EOM: ", eq_motion)
        C1 = 0
        C2 = 0
        
        self.x = sym.dsolve(eq_motion[0], self.x).subs({sym.Symbol('C1'): C1, sym.Symbol('C2'): C2}).rhs
        self.y = sym.dsolve(eq_motion[1], self.y).subs({sym.Symbol('C1'): C1, sym.Symbol('C2'): C2}).rhs
        self.z = sym.dsolve(eq_motion[2], self.z).subs({sym.Symbol('C1'): C1, sym.Symbol('C2'): C2}).rhs
        
        self.changeEMWave()
    
    def changeEMWave(self):
        # Electric field slows in the medium i.e. k -> n k
        
        refract = self.refractive_index()
        self.kx = sym.simplify(self.kx*refract[0])
        self.ky = sym.simplify(self.ky*refract[1])
        self.kz = sym.simplify(self.kz*refract[2])
    
    def p(self):
        return sym.simplify(self.charge*self.r())
    
    def P(self):
        return sym.simplify(self.no_density*self.p())
    
    def susceptiblity(self):
        p = sym.simplify(self.P())
        e = sym.simplify(self.E())
        # d = [p[0]/e[0], p[1]/e[1], p[2]/e[2]]
        
        d = sym.Matrix([[polar/electric if polar!=0 else 0 for polar in p] for electric in e])
        # d[np.isnan(d)] = 0
        suscept = sym.simplify(d.expand(complex=True)) / constant.e0
        
        return suscept
    
    def dielectric_constant(self):
        dielectric = sym.simplify(sym.diag(1,1,1)+self.susceptiblity())
        return dielectric
    
    def refractive_index(self, gaseous:bool = True):
        if gaseous:
            refract = sym.simplify(sym.ones(rows=3, cols=1)*sym.Rational(1,2) + self.dielectric_constant()/2)
        else:
            refract = sym.simplify(sym.sqrt(self.dielectric_constant()* self.magnetic_permeablity))
        return refract
    
    def eta(self):
        return sym.simplify(sym.re(self.refractive_index()))
    
    def chi(self):
        return sym.simplify(sym.im(-self.refractive_index()))
    
    def absorption_coefficient(self, truncate: int = -1):
        alpha = sym.simplify(2 * sym.im(self.k()).norm())
        
        if truncate != -1:
            alpha = sym.simplify(sym.series(alpha, self.w, self.w0, truncate).removeO())

        return alpha