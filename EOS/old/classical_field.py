from cmath import *
from scipy import constants as constant
from vector import *

class Field:
    def __init__(self, amplitude: float, frequency: float,wavevector:Vector):
        self.E0 = amplitude
        self.w = 2* constant.pi * frequency
        self.wavevector = wavevector #k
    
    def amplitude(self, position:Vector = Vector(0,0,0)) -> float:
        expo = (self.wavevector ^ position).imag
        return self.E0 * expo
    
    def E(self,position:Vector,t: float) -> complex:
        exponent = self.w * t - self.wavevector^position
        return self.E0 * exp(1j * exponent)
    
    def PoyntingVector(self,position:Vector,t: float):
        return sqrt(constant.epsilon_0/constant.mu_0) * abs(self.E(position,t))**2
    
    def speed(self) -> float:
        # print(f"|Wavevector|: {type(self.wavevector)}")
        return self.w / self.wavevector.magnitude()
    
    def absorptionCoefficient(self) -> Vector:
        return self.wavevector * (-2)
    
    def VacccumIntensity(self):
        return (sqrt(constant.epsilon_0/constant.mu_0) * abs(self.E0)**2).real
    
    def Intensity(self, position:Vector = Vector(0,0,0)) ->float:
        return self.VacccumIntensity()*exp(-self.absorptionCoefficient()^position)

    def __repr__(self):
        tempStr = []
        tempStr.append(f"Amplitude: {self.E0} V/m")
        tempStr.append(f"Frequency: {self.w /(2* constant.pi )} Hz")
        tempStr.append(f"Wavevector: {self.wavevector} m-1")
        tempStr.append(f"Speed: {self.speed()} m/s")
        tempStr.append(f"Absorption Coefficient: {self.speed()} m/s")
        tempStr.append(f"Vaccuum Intensity: {self.VacccumIntensity()} m/s")
        return '\n'.join(tempStr)