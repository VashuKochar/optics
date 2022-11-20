import sympy as sym
from sympy.vector import CoordSys3D

N = CoordSys3D('N')

class Base:
    def __init__(self, x,y,z, t:sym.Symbol):
        self.x = x
        self.y = y
        self.z = z
        self.t = t
        
    def r(self):
        return self.x * N.i + self.y*N.j + self.z*N.k