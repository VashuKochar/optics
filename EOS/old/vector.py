# Python3 program to implement 3-D Vectors.
from cmath import sqrt

# Definition of Vector class
class Vector:

# Initialize 3D Coordinates of the Vector
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Method to calculate magnitude of a Vector
    def magnitude(self) -> float:
        return abs(sqrt(abs(self.x) ** 2 + abs(self.y) ** 2 + abs(self.z) ** 2))

    # Method to add to Vector
    def __add__(self, V):
        if isinstance(V, self.__class__):
            return Vector(self.x + V.x, self.y + V.y, self.z + V.z)
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(self.__class__, type(V)))

    # Method to subtract 2 Vectors
    def __sub__(self, V):
        if isinstance(V, self.__class__):
            return Vector(self.x - V.x, self.y - V.y, self.z - V.z)
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(self.__class__, type(V)))

    # Method to calculate the dot product of two Vectors (^)
    def __xor__(self, V):
        if isinstance(V, self.__class__):
            return self.x * V.x + self.y * V.y + self.z * V.z   
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(self.__class__, type(V)))

    # Method to calculate the cross product of 2 Vectors (*)
    def __mul__(self, V):
        if isinstance(V, self.__class__):
            return Vector(self.y * V.z - self.z * V.y,
                self.z * V.x - self.x * V.z,
                self.x * V.y - self.y * V.x)
        elif isinstance(V, (int,float,complex)):
            return Vector(self.x * V, self.y * V, self.z * V)
        # elif isinstance(V, float):
        #     return Vector(self.x * V, self.y * V, self.z * V)
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(self.__class__, type(V)))
    

    # Method to define the representation of the Vector
    def __repr__(self):
        out = str(self.x) + "x " + str(self.y) + "y " + "+ " +str(self.z) + "z"
        return out