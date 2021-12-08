from math import sqrt


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def get_matrix(self):
        return self.matrix

    def transpose(self):
        return Matrix(list(map(list, zip(*self.matrix))))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = ([x * other for x in row] for row in self.matrix)
            return Matrix(result)

        elif isinstance(other, Matrix):
            m1 = self.matrix
            m2 = other.get_matrix()
            length = len(m1)
            result = [[0 for _ in range(length)] for _ in range(length)]

            for i in range(len(m1)):
                for j in range(len(m1[i])):
                    for k in range(len(m1)):
                        result[i][j] += m1[i][k] * m2[k][j]

            return Matrix(result)

    def __iter__(self):
        return iter(self.matrix)

    def __next__(self):
        return next(self.matrix)

    def __repr__(self):
        return '\n'.join(' '.join(map(str, line)) for line in self.matrix)


with open(r'in.txt') as f:
    data = f.read().split()
    length = int(sqrt(len(data)))
    m = [list(map(int, data[i:i + length])) for i in range(0, len(data), length)]

m = Matrix(m)
print('{}\n\n{}'.format(m.transpose(), m * m), file=open(r'out.txt', 'w'))
