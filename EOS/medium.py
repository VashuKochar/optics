from cmath import *
from sympy.physics.vector import dynamicsymbols
import sympy as sym
from sympy.vector import Vector
from utils import *

class Medium(Base):
    def __init__(self, x,y,z,t):
        super().__init__(x,y,z,t)
        self.mass, self.damping_constant, self.spring_constant, self.charge, self.no_density = sym.symbols('m, b, k, q, N', real=True, positive=True)
        