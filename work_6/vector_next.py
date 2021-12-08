from math import sqrt


class Vector:
    def __init__(self, vector):
        self.vector = vector

    def get_vector(self):
        return self.vector

    def length(self):
        result = sqrt(sum(map(lambda x: x ** 2, self.vector)))
        return round(result, 2)

    def norm(self):
        length = self.length()
        result = map(lambda x: round(x / length, 2), self.vector)
        return Vector(result)

    def projection(self, other):
        if not isinstance(other, Vector):
            raise TypeError('Argument must be a Vector')

        v1 = Vector(self.vector)
        div = (v1 * other) / (other * other)
        result = other * div
        return result

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError('Operand must be a Vector')

        v1 = self.vector
        v2 = other.get_vector()

        result = (a + b for a, b in zip(v1, v2))

        return Vector(result)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError('Operand must be a Vector')

        v1 = self.vector
        v2 = other.get_vector()
        result = (a - b for a, b in zip(v1, v2))

        return Vector(result)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = map(lambda x: x * other, self.vector)
            return Vector(result)

        elif isinstance(other, Vector):
            v1 = self.vector
            v2 = other.get_vector()
            result = sum(a * b for a, b in zip(v1, v2))
            return result

        else:
            raise TypeError('Right operand must be a Vector or int')

    def __repr__(self):
        if isinstance(self.vector, (int, float)):
            return repr(round(self.vector, 2))
        else:
            return ' '.join(map(lambda x: str(round(x, 2)), self.vector))


with open(r'in.txt') as file:
    vec1 = list(map(int, file.readline().split()))
    vec2 = list(map(int, file.readline().split()))

vec1 = Vector(vec1)
vec2 = Vector(vec2)

out = {
    'len': vec1.length(),
    'nrm': vec1.norm(),
    'prj': vec1.projection(vec2)
}

print('{len}\n{nrm}\n{prj}'.format(**out), file=open(r'out.txt', 'w'))
