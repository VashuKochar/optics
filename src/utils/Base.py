import sympy as sym
import numpy as np

class Base:
    def __init__(self, x,y,z, t:sym.Symbol):
        self.x = x
        self.y = y
        self.z = z
        self.t = t
    

    def r(self):
        return np.array([self.x,self.y,self.z])