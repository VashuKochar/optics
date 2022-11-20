from pprint import pprint
import sympy as sym
from sympy.physics.vector import *
# from sympy.solvers import solve

from electron_on_spring import *
from utils import *
from sympy.vector import CoordSys3D

# Dimensional variables
t = sym.Symbol('t', real=True, positive=True)
# dynamicsymbols._t = t

# x,y,z = dynamicsymbols('x,y,z', real=True)
x,y,z = sym.symbols('x,y,z', cls=sym.Function)
x = x(t)
y = y(t)
z = z(t)


# dr = sym.diff(r,t)
# print(type(r), " ", r)
# print(type(t), " ", t)
# print(type(dr), " ", dr)
eos1 = EOS(x,y,z, t)

# print("k = ", eos1.k())

print("E(r,t) = ",eos1.E())
# print("|E(r,t)| = ",em1.magnitude())
# print("|E(r,t)|* = ",em1.magnitude().conjugate())
# print("|E(r,t)| X |E(r,t)|*  = ",sym.simplify(em1.magnitude() * em1.magnitude().conjugate()))
# print("|E(r,t)|* = ",sym.simplify(sym.conjugate(em1.E.magnitude())), type(sym.conjugate(em1.E.magnitude())))
# print("E*(r,t) = ",norm(em1.E))
# print("|E(r,t)| = ",em1.E.norm())

# print("|E(r,t)|2 = ",sym.simplify(em1.E.magnitude() * sym.conjugate(em1.E.magnitude()) ))
# print(type(em1.E))
# eom2 = 
# eom3 = 
# print("I(r) = ", sym.simplify(eos1.I))
# print("All eqns: ", eos1.eqns," = 0")


eos1.solveEOMs()

eos1.changeEMWave()
# print("k' = ", eos1.k())
print("x = ",eos1.x)
print("y = ",eos1.y)
print("z = ",eos1.z)

dipole = sym.simplify(eos1.p())
print("Dipole = ",sym.latex(dipole))
sus = sym.simplify(eos1.susceptiblity())
print("Susceptiblity = ",sym.latex(sus))

eta = sym.simplify(eos1.eta())
print("Eta = ",sym.latex(eta))
chi = sym.simplify(eos1.chi())
print("Chi = ",sym.latex(chi))
absorb = sym.simplify(eos1.absorption_coefficient())
print("Absorption coefficient = ",sym.latex(absorb))
