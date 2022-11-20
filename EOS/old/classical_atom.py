from cmath import *
from scipy import constants as constant


class Atom:
    def __init__(self, damping: float, spring_constant: float):
        self.mass = constant.m_e # m
        self.damping_constant = damping # b
        self.spring_constant = spring_constant # k
        self.osciallator_frequency = sqrt(self.spring_constant/self.mass) # w0
        self.damping = self.damping_constant/self.mass # gamma
    
    def __repr__(self):
        tempStr = []
        tempStr.append(f"Mass: {self.mass} kg")
        tempStr.append(f"Damping constant: {self.damping} kg/s")
        tempStr.append(f"Spring constant: {self.spring_constant} kg/s2")
        tempStr.append(f"Oscillator frequency: {self.osciallator_frequency/(2* constant.pi )} Hz")
        tempStr.append(f"Damping rate: {self.damping} /s")
        return '\n'.join(tempStr)