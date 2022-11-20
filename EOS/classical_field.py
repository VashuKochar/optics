from cmath import *
from sympy.vector import Vector
import sympy as sym
import constants as constant
from utils import *

class Field(Base):
    def __init__(self, x,y,z, t:sym.Symbol):
        super().__init__(x,y,z, t)
        
        self.w = sym.symbols('w', real=True, positive=True)
        self.E0x,self.E0y,self.E0z = sym.symbols('E0x,E0y,E0z', real=True)
        self.kx,self.ky,self.kz = sym.symbols('kx,ky,kz', complex=True)
    
    def k(self):
        return self.kx*N.i + self.ky*N.j + self.kz*N.k 
    
    def f(self):
        return self.w/ 2*sym.pi
    
    def wavelength(self):
        return 2 * constant.pi / self.k().magnitude()
    
    def E0(self):
        return self.E0x*N.i + self.E0y*N.j + self.E0z*N.k
    
    def E(self):
        return sym.simplify(self.E0() * sym.exp(sym.I * (self.w * self.t - (self.k() & self.r()))))
    
    def I(self):
        return sym.sqrt(constant.e_0 / constant.mu_0) * sym.simplify(self.E().magnitude() * self.E().magnitude().conjugate())
    
    # def amplitude(self, position:Vector = Vector(0,0,0)) -> float:
    #     expo = (self.wavevector ^ position).imag
    #     return self.E0 * expo
    
    # def E(self,position:Vector,t: float) -> complex:
    #     exponent = self.w * t - self.wavevector^position
    #     return self.E0 * exp(1j * exponent)
    
    # def PoyntingVector(self,position:Vector,t: float):
    #     return sqrt(constant.epsilon_0/constant.mu_0) * abs(self.E(position,t))**2
    
    # def speed(self) -> float:
    #     # print(f"|Wavevector|: {type(self.wavevector)}")
    #     return self.w / self.wavevector.magnitude()
    
    # def absorptionCoefficient(self) -> Vector:
    #     return self.wavevector * (-2)
    
    # def VacccumIntensity(self):
    #     return (sqrt(constant.epsilon_0/constant.mu_0) * abs(self.E0)**2).real
    
    # def Intensity(self, position:Vector = Vector(0,0,0)) ->float:
    #     return self.VacccumIntensity()*exp(-self.absorptionCoefficient()^position)

    # def __repr__(self):
    #     tempStr = []
    #     tempStr.append(f"Amplitude: {self.E0} V/m")
    #     tempStr.append(f"Frequency: {self.w /(2* constant.pi )} Hz")
    #     tempStr.append(f"Wavevector: {self.wavevector} m-1")
    #     tempStr.append(f"Speed: {self.speed()} m/s")
    #     tempStr.append(f"Absorption Coefficient: {self.speed()} m/s")
    #     tempStr.append(f"Vaccuum Intensity: {self.VacccumIntensity()} m/s")
    #     return '\n'.join(tempStr)