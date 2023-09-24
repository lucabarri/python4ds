import math


class Vector:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

    def __abs__(self):
        return math.sqrt(sum([ai ** 2 for ai in self.data]))

    def __add__(self, other_vector):
        if type(other_vector) is Vector:
            return Vector([ai + bi for ai, bi in zip(self, other_vector)])
        elif type(other_vector) is float or type(other_vector) is int:
            return Vector([ai + other_vector for ai in self])
        else:
            raise ValueError

    def __sub__(self, other_vector):
        if type(other_vector) is Vector:
            return Vector([ai - bi for ai, bi in zip(self, other_vector)])
        elif type(other_vector) is float or type(other_vector) is int:
            return Vector([ai - other_vector for ai in self])
        else:
            raise ValueError

    def __mul__(self, other_vector):
        if type(other_vector) is Vector:
            return sum([ai * bi for ai, bi in zip(self, other_vector)])
        elif type(other_vector) is float or type(other_vector) is int:
            return Vector([ai * other_vector for ai in self])
        else:
            raise ValueError
