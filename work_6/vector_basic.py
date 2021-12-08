class Vector:
    def __init__(self, vector):
        self.vector = vector

    def get_vector(self):
        return self.vector

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
        if isinstance(other, int):
            result = map(lambda x: x * other, self.vector)

        elif isinstance(other, Vector):
            v1 = self.vector
            v2 = other.get_vector()
            result = sum(a * b for a, b in zip(v1, v2))

        else:
            raise TypeError('Right operand must be a Vector or int')

        return Vector(result)

    def __repr__(self):
        if isinstance(self.vector, (int, float)):
            return repr(round(self.vector, 2))
        else:
            return ' '.join(map(str, self.vector))


with open(r'in.txt') as file:
    vec1 = list(map(int, file.readline().split()))
    vec2 = list(map(int, file.readline().split()))
    n = int(file.readline())

vec1 = Vector(vec1)
vec2 = Vector(vec2)
out = {
    'add': vec1 + vec2,
    'sub': vec1 - vec2,
    'muln': vec1 * n,
    'mul': vec1 * vec2
}
print('{add}\n{sub}\n{muln}\n{mul}'.format(**out), file=open(r'out.txt', 'w'))
